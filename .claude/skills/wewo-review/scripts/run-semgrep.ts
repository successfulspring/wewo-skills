#!/usr/bin/env node

import { spawnSync } from "node:child_process";
import {
  existsSync,
  mkdtempSync,
  realpathSync,
  rmSync,
  statSync,
} from "node:fs";
import os from "node:os";
import path from "node:path";

const HELP = `Usage: <supported-ts-runner> run-semgrep.ts --target <path> [options]

Resolve or acquire an isolated Semgrep Community Edition executable, run one
JSON scan, and emit one normalized JSON evidence object.

Options:
  --target <path>                 File or directory to scan (required)
  --config <path-or-registry-id>  Trusted local config or explicit registry ID
  --allow-registry-config         Permit a non-local --config value
  --acquisition-mode <mode>       auto|existing|ephemeral|temporary (default: auto)
  --allow-acquisition             Permit isolated ephemeral/temporary acquisition
  --semgrep-version <version>     Preferred exact version for isolated acquisition
  --semgrep-executable <path>     Explicit pre-existing executable
  --semgrep-prefix-arg <arg>      Repeatable argv before Semgrep args (test/wrapper use)
  --python-executable <path>      Python used for a temporary virtual environment
  --help                          Show this help

Exit 0: completed scan. Exit 2: blocked/unavailable, including unavailable
acquisition paths. Exit 3: attempted scan/internal tool failure. This script
never installs globally, modifies target dependencies, autofixes, or decides
whether a warning is a vulnerability.
`;

const LOCAL_CONFIG_NAMES = [
  ".semgrep.yml",
  ".semgrep.yaml",
  "semgrep.yml",
  "semgrep.yaml",
  path.join(".semgrep", "config.yml"),
  path.join(".semgrep", "config.yaml"),
];
const CAPTURE_LIMIT = 8_000;

function parseArgs(argv) {
  const options = {
    acquisitionMode: "auto",
    allowAcquisition: false,
    allowRegistryConfig: false,
    semgrepPrefixArgs: [],
  };
  const valueOptions = new Map([
    ["--target", "target"],
    ["--config", "config"],
    ["--acquisition-mode", "acquisitionMode"],
    ["--semgrep-version", "semgrepVersion"],
    ["--semgrep-executable", "semgrepExecutable"],
    ["--python-executable", "pythonExecutable"],
  ]);
  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === "--help" || argument === "-h") return { help: true };
    if (argument === "--allow-acquisition") {
      options.allowAcquisition = true;
      continue;
    }
    if (argument === "--allow-registry-config") {
      options.allowRegistryConfig = true;
      continue;
    }
    if (argument === "--semgrep-prefix-arg") {
      const value = argv[index + 1];
      if (value === undefined) throw new Error(`${argument} requires a value`);
      options.semgrepPrefixArgs.push(value);
      index += 1;
      continue;
    }
    if (valueOptions.has(argument)) {
      const value = argv[index + 1];
      if (!value) throw new Error(`${argument} requires a value`);
      options[valueOptions.get(argument)] = value;
      index += 1;
      continue;
    }
    throw new Error(`unknown argument: ${argument}`);
  }
  if (!options.target) throw new Error("--target is required");
  if (!["auto", "existing", "ephemeral", "temporary"].includes(options.acquisitionMode)) {
    throw new Error("--acquisition-mode must be auto, existing, ephemeral, or temporary");
  }
  if (options.semgrepExecutable && !["auto", "existing"].includes(options.acquisitionMode)) {
    throw new Error("--semgrep-executable is compatible only with auto/existing mode");
  }
  return options;
}

function execute(executable, args, cwd = undefined) {
  const result = spawnSync(executable, args, {
    cwd,
    encoding: "utf8",
    maxBuffer: 64 * 1024 * 1024,
    shell: false,
    windowsHide: true,
  });
  return {
    executable,
    args,
    exitCode: result.status,
    signal: result.signal,
    stdout: result.stdout || "",
    stderr: result.stderr || "",
    error: result.error ? result.error.message : null,
  };
}

function excerpt(value) {
  if (value.length <= CAPTURE_LIMIT) return { text: value, truncated: false };
  return { text: value.slice(0, CAPTURE_LIMIT), truncated: true };
}

function versionCheck(command) {
  const result = execute(command.executable, [...command.prefixArgs, "--version"]);
  const version = (result.stdout || result.stderr).trim().split(/\r?\n/, 1)[0] || null;
  return { usable: !result.error && result.exitCode === 0, version, result };
}

function resolveConfig(options, target) {
  if (options.config) {
    if (existsSync(options.config)) {
      return { value: realpathSync(options.config), source: "explicit-local", externalRegistry: false };
    }
    if (!options.allowRegistryConfig) {
      return { error: "non-local Semgrep configuration requires --allow-registry-config" };
    }
    return { value: options.config, source: "explicit-registry", externalRegistry: true };
  }
  const root = statSync(target).isDirectory() ? target : path.dirname(target);
  for (const name of LOCAL_CONFIG_NAMES) {
    const candidate = path.join(root, name);
    if (existsSync(candidate)) {
      return { value: realpathSync(candidate), source: "repository-local", externalRegistry: false };
    }
  }
  return { error: "no trusted local Semgrep configuration was found or explicitly supplied" };
}

function commandFromExisting(options, attempts) {
  const executable = options.semgrepExecutable || "semgrep";
  const command = { executable, prefixArgs: options.semgrepPrefixArgs };
  const check = versionCheck(command);
  attempts.push({ mode: "existing", executable, ...check.result });
  if (!check.usable) return null;
  return { ...command, mode: "existing", origin: options.semgrepExecutable ? "explicit-pre-existing" : "path-pre-existing", version: check.version, versionResolution: "pre-existing" };
}

function commandFromEphemeral(version, attempts) {
  const packageSpec = version ? `semgrep==${version}` : "semgrep";
  const versionResolution = version ? "pinned" : "runtime-resolved";
  const candidates = [
    { executable: "uvx", prefixArgs: ["--from", packageSpec, "semgrep"] },
    { executable: "uv", prefixArgs: ["tool", "run", "--from", packageSpec, "semgrep"] },
  ];
  for (const command of candidates) {
    const check = versionCheck(command);
    attempts.push({ mode: "ephemeral", versionResolution, executable: command.executable, args: check.result.args, exitCode: check.result.exitCode, error: check.result.error, stderr: excerpt(check.result.stderr) });
    if (check.usable) return { ...command, mode: "ephemeral", origin: "ephemeral-isolated", version: check.version, versionResolution };
  }
  return null;
}

function safeCleanup(ownedRoot) {
  if (!ownedRoot) return { attempted: false, outcome: "not-applicable", ownedPath: null };
  const tempRoot = realpathSync(os.tmpdir());
  const resolvedParent = realpathSync(path.dirname(ownedRoot));
  const ownedName = path.basename(ownedRoot);
  if (resolvedParent !== tempRoot || !ownedName.startsWith("wewo-review-semgrep-")) {
    return { attempted: false, outcome: "refused-unsafe-path", ownedPath: ownedRoot };
  }
  try {
    rmSync(ownedRoot, { recursive: true, force: true });
    return { attempted: true, outcome: existsSync(ownedRoot) ? "failed" : "removed", ownedPath: ownedRoot };
  } catch (error) {
    return { attempted: true, outcome: "failed", ownedPath: ownedRoot, error: error.message };
  }
}

function commandFromTemporary(options, attempts, ownership) {
  ownership.root = mkdtempSync(path.join(os.tmpdir(), "wewo-review-semgrep-"));
  const pythonCandidates = options.pythonExecutable
    ? [{ executable: options.pythonExecutable, prefixArgs: [] }]
    : [
        { executable: "python3", prefixArgs: [] },
        { executable: "python", prefixArgs: [] },
        { executable: "py", prefixArgs: ["-3"] },
      ];
  const venv = path.join(ownership.root, "venv");
  let python = null;
  for (const candidate of pythonCandidates) {
    const probe = execute(candidate.executable, [...candidate.prefixArgs, "--version"]);
    attempts.push({ mode: "temporary-python-probe", executable: candidate.executable, args: probe.args, exitCode: probe.exitCode, error: probe.error });
    if (!probe.error && probe.exitCode === 0) {
      python = candidate;
      break;
    }
  }
  if (!python) return null;

  const create = execute(python.executable, [...python.prefixArgs, "-m", "venv", venv]);
  attempts.push({ mode: "temporary-venv", executable: python.executable, args: create.args, exitCode: create.exitCode, error: create.error, stderr: excerpt(create.stderr) });
  if (create.error || create.exitCode !== 0) return null;

  const venvPython = process.platform === "win32"
    ? path.join(venv, "Scripts", "python.exe")
    : path.join(venv, "bin", "python");
  const install = execute(venvPython, [
    "-m", "pip", "install", "--disable-pip-version-check",
    options.semgrepVersion ? `semgrep==${options.semgrepVersion}` : "semgrep",
  ]);
  attempts.push({ mode: "temporary-install", executable: venvPython, args: install.args, exitCode: install.exitCode, error: install.error, stderr: excerpt(install.stderr) });
  if (install.error || install.exitCode !== 0) return null;

  const semgrep = process.platform === "win32"
    ? path.join(venv, "Scripts", "semgrep.exe")
    : path.join(venv, "bin", "semgrep");
  const command = { executable: semgrep, prefixArgs: [] };
  const check = versionCheck(command);
  attempts.push({ mode: "temporary-version", executable: semgrep, args: check.result.args, exitCode: check.result.exitCode, error: check.result.error, stderr: excerpt(check.result.stderr) });
  if (!check.usable) return null;
  return { ...command, mode: "temporary", origin: "temporary-isolated", version: check.version, versionResolution: options.semgrepVersion ? "pinned" : "runtime-resolved" };
}

function emit(result, exitCode) {
  process.stdout.write(`${JSON.stringify({ schemaVersion: 1, ...result }, null, 2)}\n`);
  process.exitCode = exitCode;
}

function main() {
  let options;
  try {
    options = parseArgs(process.argv.slice(2));
  } catch (error) {
    emit({ status: "Blocked", limitation: error.message, cleanup: { attempted: false, outcome: "not-applicable", ownedPath: null } }, 2);
    return;
  }
  if (options.help) {
    process.stdout.write(HELP);
    return;
  }
  if (!existsSync(options.target)) {
    emit({ status: "Unavailable", limitation: "scan target does not exist", target: options.target, cleanup: { attempted: false, outcome: "not-applicable", ownedPath: null } }, 2);
    return;
  }

  const target = realpathSync(options.target);
  let config;
  try {
    config = resolveConfig(options, target);
  } catch (error) {
    emit({ status: "Blocked", target, limitation: `configuration resolution failed: ${error.message}`, cleanup: { attempted: false, outcome: "not-applicable", ownedPath: null } }, 2);
    return;
  }
  if (config.error) {
    emit({ status: "Blocked", target, limitation: config.error, cleanup: { attempted: false, outcome: "not-applicable", ownedPath: null } }, 2);
    return;
  }

  const attempts = [];
  const ownership = { root: null };
  let command = null;
  let cleanup = { attempted: false, outcome: "not-applicable", ownedPath: null };
  try {
    if (["auto", "existing"].includes(options.acquisitionMode)) {
      command = commandFromExisting(options, attempts);
    }
    const acquisitionRequested = ["ephemeral", "temporary"].includes(options.acquisitionMode) ||
      (options.acquisitionMode === "auto" && !command);
    if (!command && acquisitionRequested && !options.allowAcquisition) {
      emit({
        status: "Blocked",
        target,
        configSource: config.source,
        externalRegistryAccess: config.externalRegistry,
        acquisitionMode: options.acquisitionMode,
        attempts,
        limitation: "isolated acquisition requires --allow-acquisition",
        cleanup,
      }, 2);
      return;
    }
    if (!command && ["auto", "ephemeral"].includes(options.acquisitionMode)) {
      command = commandFromEphemeral(options.semgrepVersion, attempts);
    }
    if (!command && ["auto", "temporary"].includes(options.acquisitionMode)) {
      command = commandFromTemporary(options, attempts, ownership);
    }
    if (!command) {
      cleanup = safeCleanup(ownership.root);
      emit({
        status: "Unavailable",
        target,
        configSource: config.source,
        externalRegistryAccess: config.externalRegistry,
        acquisitionMode: options.acquisitionMode,
        attempts,
        limitation: "no usable Semgrep execution path could be resolved",
        cleanup,
      }, 2);
      return;
    }

    const scanArgs = [
      ...command.prefixArgs,
      "scan",
      "--json",
      "--metrics=off",
      "--config",
      config.value,
      target,
    ];
    const scan = execute(command.executable, scanArgs);
    let parsed = null;
    let parseError = null;
    try {
      parsed = JSON.parse(scan.stdout);
    } catch (error) {
      parseError = error.message;
    }
    const rawFindings = Array.isArray(parsed?.results) ? parsed.results : [];
    const rawErrors = Array.isArray(parsed?.errors) ? parsed.errors : [];
    cleanup = safeCleanup(ownership.root);
    const completed = !scan.error && scan.exitCode === 0 && !parseError;
    const coverageComplete = completed && rawErrors.length === 0;
    const limitation = rawErrors.length > 0
      ? `Semgrep returned ${rawErrors.length} parse/scan error(s); absence of findings does not establish complete coverage.`
      : (completed ? null : "Semgrep did not complete with parseable JSON evidence");
    const status = completed
      ? (rawFindings.length > 0 ? "Completed - findings produced" : "Completed - no findings")
      : "Failed";
    emit({
      status,
      toolOrigin: command.origin,
      acquisitionMode: command.mode,
      version: command.version,
      versionResolution: command.versionResolution,
      configSource: config.source,
      config: config.value,
      externalRegistryAccess: config.externalRegistry,
      target,
      invocation: { executable: command.executable, args: scanArgs },
      exitCode: scan.exitCode,
      signal: scan.signal,
      executionError: scan.error,
      parseError,
      rawWarningCount: rawFindings.length,
      rawErrorCount: rawErrors.length,
      coverageComplete,
      rawFindings,
      rawErrors,
      stdout: excerpt(scan.stdout),
      stderr: excerpt(scan.stderr),
      attempts,
      limitation,
      cleanup,
    }, completed ? 0 : 3);
  } catch (error) {
    cleanup = safeCleanup(ownership.root);
    emit({
      status: "Failed",
      target,
      configSource: config.source,
      attempts,
      limitation: error.message,
      cleanup,
    }, 3);
  }
}

main();
