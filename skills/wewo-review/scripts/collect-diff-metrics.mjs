#!/usr/bin/env node

import { spawnSync } from "node:child_process";
import { existsSync, readFileSync, realpathSync, statSync } from "node:fs";
import path from "node:path";

const HELP = `Usage: node collect-diff-metrics.mjs [options]

Calculate deterministic LOC facts from one Git diff. Exactly one scope is
required.

Options:
  --repo <path>              Git worktree (default: current directory)
  --range <revision-range>   Pass one revision/range to git diff
  --base <ref> --target <ref>
                             Diff two explicit Git revisions
  --staged                   Diff the index against HEAD
  --worktree                 Diff tracked unstaged changes
  --all                      Diff tracked staged and unstaged changes vs HEAD
  --include-untracked <path> Repeat for each applicable untracked file selected
                             by Main; no untracked files are auto-included
  --help                     Show this help

Output is one JSON object. Exit 0 means metrics were calculated or honestly
reported Not Calculable; exit 2 means invalid input or Git could not execute.
Untracked text uses physical lines: each line terminator closes one line, and
non-empty content after the final terminator counts as one line.
`;

const CODE_EXTENSIONS = new Set([
  ".c", ".cc", ".clj", ".cljs", ".cpp", ".cs", ".css", ".dart", ".ex",
  ".exs", ".fs", ".fsx", ".go", ".h", ".hpp", ".html", ".java", ".js",
  ".jsx", ".kt", ".kts", ".lua", ".m", ".mm", ".php", ".pl", ".pm",
  ".proto", ".py", ".r", ".rb", ".rs", ".scala", ".scss", ".sh",
  ".sol", ".sql", ".svelte", ".swift", ".ts", ".tsx", ".vue", ".zig",
]);

const BINARY_EXTENSIONS = new Set([
  ".7z", ".a", ".avi", ".bin", ".bmp", ".class", ".dll", ".dylib",
  ".eot", ".exe", ".gif", ".gz", ".ico", ".jar", ".jpeg", ".jpg",
  ".mov", ".mp3", ".mp4", ".o", ".otf", ".pdf", ".png", ".so",
  ".tar", ".tif", ".tiff", ".ttf", ".wav", ".webm", ".webp", ".woff",
  ".woff2", ".xz", ".zip",
]);

const LOCK_FILES = new Set([
  "bun.lock", "bun.lockb", "cargo.lock", "composer.lock", "gemfile.lock",
  "go.sum", "package-lock.json", "packages.lock.json", "pnpm-lock.yaml",
  "poetry.lock", "uv.lock", "yarn.lock",
]);

function fail(message, details = []) {
  process.stdout.write(`${JSON.stringify({
    schemaVersion: 1,
    status: "failed",
    error: message,
    details,
  }, null, 2)}\n`);
  process.exitCode = 2;
}

function parseArgs(argv) {
  const options = {
    repo: process.cwd(),
    scope: null,
    base: null,
    target: null,
    includeUntracked: [],
  };
  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === "--help" || argument === "-h") return { help: true };
    if (argument === "--include-untracked") {
      const value = argv[index + 1];
      if (!value) throw new Error(`${argument} requires a value`);
      if (!options.includeUntracked.includes(value)) options.includeUntracked.push(value);
      index += 1;
      continue;
    }
    if (argument === "--repo" || argument === "--range" ||
        argument === "--base" || argument === "--target") {
      const value = argv[index + 1];
      if (!value) throw new Error(`${argument} requires a value`);
      index += 1;
      if (argument === "--repo") options.repo = value;
      if (argument === "--range") {
        if (options.scope) throw new Error("choose exactly one diff scope");
        if (value.startsWith("-")) throw new Error("revision ranges cannot begin with '-'");
        options.scope = { kind: "range", value };
      }
      if (argument === "--base") options.base = value;
      if (argument === "--target") options.target = value;
      continue;
    }
    if (["--staged", "--worktree", "--all"].includes(argument)) {
      if (options.scope) throw new Error("choose exactly one diff scope");
      options.scope = { kind: argument.slice(2) };
      continue;
    }
    throw new Error(`unknown argument: ${argument}`);
  }

  if (options.base || options.target) {
    if (options.scope) throw new Error("--base/--target cannot be combined with another scope");
    if (!options.base || !options.target) throw new Error("--base and --target must be supplied together");
    if (options.base.startsWith("-") || options.target.startsWith("-")) {
      throw new Error("revision names cannot begin with '-'");
    }
    options.scope = { kind: "refs", base: options.base, target: options.target };
  }
  if (!options.scope) throw new Error("one diff scope is required");
  return options;
}

function normalizePath(filePath) {
  return filePath.replaceAll("\\", "/");
}

function classify(filePath, binaryFromGit) {
  const normalized = normalizePath(filePath);
  const lower = normalized.toLowerCase();
  const basename = path.posix.basename(lower);
  const extension = path.posix.extname(lower);
  const parts = lower.split("/");

  if (binaryFromGit || BINARY_EXTENSIONS.has(extension)) {
    return { category: "excluded", reason: "binary" };
  }
  if (LOCK_FILES.has(basename)) {
    return { category: "excluded", reason: "lock" };
  }
  if (/(^|\/)(vendor|vendors|node_modules|third_party|third-party)(\/|$)/.test(lower)) {
    return { category: "excluded", reason: "vendor" };
  }
  if (/(^|\/)(dist|build|out|coverage|\.next|\.nuxt)(\/|$)/.test(lower)) {
    return { category: "excluded", reason: "build" };
  }
  if (/(^|\/)(generated|gen)(\/|$)/.test(lower) ||
      /(^|[._-])(generated|autogen)([._-]|$)/.test(basename)) {
    return { category: "excluded", reason: "generated" };
  }
  if (/\.min\.(css|js|mjs|cjs)$/.test(lower) || basename.endsWith(".map")) {
    return { category: "excluded", reason: "minified" };
  }
  if (/(^|\/)(migrations?|db\/migrations?)(\/|$)/.test(lower) ||
      [".json", ".toml", ".yaml", ".yml"].includes(extension) ||
      ["dockerfile", "makefile"].includes(basename)) {
    return { category: "configurationMigration", reason: null };
  }
  if (!CODE_EXTENSIONS.has(extension)) {
    return { category: "excluded", reason: "non-semantic" };
  }
  const testLike = parts.some((part) => [
    "test", "tests", "__tests__", "spec", "specs", "fixtures",
  ].includes(part)) || /(^|[._-])(test|spec)([._-]|$)/.test(basename);
  return { category: testLike ? "test" : "production", reason: null };
}

function gitArguments(scope) {
  const common = ["diff", "--numstat", "--no-renames", "-z"];
  if (scope.kind === "range") return [...common, scope.value, "--"];
  if (scope.kind === "refs") return [...common, scope.base, scope.target, "--"];
  if (scope.kind === "staged") return [...common, "--cached", "--"];
  if (scope.kind === "worktree") return [...common, "--"];
  return [...common, "HEAD", "--"];
}

function parseNumstat(output) {
  const records = [];
  for (const entry of output.split("\0")) {
    if (!entry) continue;
    const firstTab = entry.indexOf("\t");
    const secondTab = entry.indexOf("\t", firstTab + 1);
    if (firstTab < 0 || secondTab < 0) {
      throw new Error("unexpected git numstat record");
    }
    const addedText = entry.slice(0, firstTab);
    const deletedText = entry.slice(firstTab + 1, secondTab);
    const filePath = entry.slice(secondTab + 1);
    const binary = addedText === "-" || deletedText === "-";
    records.push({
      path: normalizePath(filePath),
      additions: binary ? 0 : Number.parseInt(addedText, 10),
      deletions: binary ? 0 : Number.parseInt(deletedText, 10),
      binary,
    });
  }
  return records;
}

function countPhysicalLines(text) {
  if (text.length === 0) return 0;
  const terminators = text.match(/\r\n|\r|\n/g)?.length || 0;
  return terminators + (/\r\n$|\r$|\n$/.test(text) ? 0 : 1);
}

function excludedUntracked(requestedPath, reason, limitation = null) {
  return {
    requestedPath,
    path: normalizePath(requestedPath),
    source: "untracked",
    additions: 0,
    deletions: 0,
    changedLoc: 0,
    binary: reason === "binary",
    reason,
    limitation,
  };
}

function measureUntracked(repo, requestedPath) {
  const candidate = path.isAbsolute(requestedPath)
    ? path.resolve(requestedPath)
    : path.resolve(repo, requestedPath);
  if (!existsSync(candidate)) {
    return { excluded: excludedUntracked(requestedPath, "missing", "Explicit untracked path does not exist.") };
  }

  let resolved;
  try {
    resolved = realpathSync(candidate);
  } catch (error) {
    return { excluded: excludedUntracked(requestedPath, "unreadable", error.message) };
  }
  const relativeNative = path.relative(repo, resolved);
  if (!relativeNative || relativeNative.startsWith(`..${path.sep}`) ||
      relativeNative === ".." || path.isAbsolute(relativeNative)) {
    return { excluded: excludedUntracked(requestedPath, "outside-repository", "Path resolves outside the repository.") };
  }
  if (!statSync(resolved).isFile()) {
    return { excluded: excludedUntracked(requestedPath, "not-a-file") };
  }

  const relative = normalizePath(relativeNative);
  const tracked = spawnSync(
    "git",
    ["-C", repo, "ls-files", "--cached", "-z", "--", `:(literal)${relative}`],
    { encoding: "utf8", maxBuffer: 4 * 1024 * 1024, shell: false },
  );
  if (tracked.error || tracked.status !== 0) {
    return { excluded: excludedUntracked(requestedPath, "unverifiable", tracked.error?.message || tracked.stderr.trim()) };
  }
  if ((tracked.stdout || "").split("\0").includes(relative)) {
    return { excluded: excludedUntracked(requestedPath, "tracked-file", "Already represented by tracked Git scope when changed.") };
  }

  let buffer;
  try {
    buffer = readFileSync(resolved);
  } catch (error) {
    return { excluded: excludedUntracked(requestedPath, "unreadable", error.message) };
  }
  const pathClassification = classify(relative, false);
  if (pathClassification.reason === "binary" || buffer.includes(0)) {
    return { excluded: { ...excludedUntracked(requestedPath, "binary"), path: relative } };
  }

  let text;
  try {
    text = new TextDecoder("utf-8", { fatal: true }).decode(buffer);
  } catch (error) {
    return { excluded: { ...excludedUntracked(requestedPath, "unsafe-text", error.message), path: relative } };
  }
  const physicalLines = countPhysicalLines(text);
  const record = {
    requestedPath,
    path: relative,
    source: "untracked",
    additions: physicalLines,
    deletions: 0,
    changedLoc: physicalLines,
    physicalLines,
    binary: false,
  };
  if (pathClassification.category === "excluded") {
    return { excluded: { ...record, reason: pathClassification.reason } };
  }
  return { included: { ...record, category: pathClassification.category } };
}

function main() {
  let options;
  try {
    options = parseArgs(process.argv.slice(2));
  } catch (error) {
    fail(error.message);
    return;
  }
  if (options.help) {
    process.stdout.write(HELP);
    return;
  }
  if (!existsSync(options.repo)) {
    fail("repository path does not exist", [options.repo]);
    return;
  }

  let repo;
  try {
    repo = realpathSync(options.repo);
  } catch (error) {
    fail("repository path cannot be resolved", [String(error.message)]);
    return;
  }

  const args = gitArguments(options.scope);
  const command = spawnSync("git", ["-C", repo, ...args], {
    encoding: "utf8",
    maxBuffer: 64 * 1024 * 1024,
    shell: false,
  });
  if (command.error) {
    fail("git could not execute", [command.error.message]);
    return;
  }
  const limitations = [];
  let records = [];
  let trackedScopeStatus = "completed";
  if (command.status !== 0) {
    trackedScopeStatus = "not-calculable";
    limitations.push(
      "Git could not resolve the tracked scope; tracked Diff metrics are Not Calculable.",
      (command.stderr || "").trim(),
    );
  } else {
    try {
      records = parseNumstat(command.stdout || "");
    } catch (error) {
      fail(error.message);
      return;
    }
  }

  const includedFiles = [];
  const excludedFiles = [];
  const includedUntrackedFiles = [];
  const excludedUntrackedFiles = [];
  const totals = {
    additions: 0,
    deletions: 0,
    eligibleChangedCodeLoc: 0,
    densityEligibleChangedCodeLoc: 0,
    changedProductionLoc: 0,
    changedTestLoc: 0,
    configurationMigrationLoc: 0,
  };

  for (const record of records) {
    record.source = "tracked";
    const changedLoc = record.additions + record.deletions;
    totals.additions += record.additions;
    totals.deletions += record.deletions;
    const classification = classify(record.path, record.binary);
    if (classification.category === "excluded") {
      excludedFiles.push({ ...record, changedLoc, reason: classification.reason });
      continue;
    }
    includedFiles.push({ ...record, changedLoc, category: classification.category });
    if (classification.category === "production") {
      totals.changedProductionLoc += changedLoc;
    } else if (classification.category === "test") {
      totals.changedTestLoc += changedLoc;
    } else {
      totals.configurationMigrationLoc += changedLoc;
    }
  }

  for (const requestedPath of options.includeUntracked) {
    const measured = measureUntracked(repo, requestedPath);
    const record = measured.included || measured.excluded;
    totals.additions += record.additions;
    if (measured.excluded) {
      excludedFiles.push(record);
      excludedUntrackedFiles.push(record);
      if (record.limitation) limitations.push(`${requestedPath}: ${record.limitation}`);
      continue;
    }
    includedFiles.push(record);
    includedUntrackedFiles.push(record);
    if (record.category === "production") {
      totals.changedProductionLoc += record.changedLoc;
    } else if (record.category === "test") {
      totals.changedTestLoc += record.changedLoc;
    } else {
      totals.configurationMigrationLoc += record.changedLoc;
    }
  }

  totals.densityEligibleChangedCodeLoc =
    totals.changedProductionLoc + totals.changedTestLoc;
  totals.eligibleChangedCodeLoc = totals.densityEligibleChangedCodeLoc;

  includedFiles.sort((left, right) => left.path.localeCompare(right.path, "en"));
  excludedFiles.sort((left, right) => left.path.localeCompare(right.path, "en"));
  const status = totals.densityEligibleChangedCodeLoc === 0 ? "not-calculable" : "completed";
  limitations.push(
    "Path-based classification cannot detect generated content without a recognizable path/name.",
    "Only paths supplied with --include-untracked are measured; other untracked files are intentionally absent.",
    "Untracked physical LOC counts line terminators plus non-empty content after the final terminator.",
  );
  if (status === "not-calculable") {
    limitations.unshift("Density-eligible changed code LOC (production + test) is zero; KLOC densities are Not Calculable.");
  }

  process.stdout.write(`${JSON.stringify({
    schemaVersion: 1,
    status,
    repository: repo,
    scope: { ...options.scope, explicitUntrackedPaths: options.includeUntracked },
    gitInvocation: ["git", "-C", repo, ...args],
    trackedScopeStatus,
    trackedChangedFiles: records.length,
    includedUntrackedFiles,
    excludedUntrackedFiles,
    includedChangedFiles: includedFiles.length,
    excludedChangedFiles: excludedFiles.length,
    totals,
    includedFiles,
    excludedFiles,
    limitations,
  }, null, 2)}\n`);
}

main();
