# Diff Scope and Context

Establish an attributable review target before evaluating findings.

## Scope precedence

Use the first applicable scope:

1. the explicit Diff, commit, range, branch, PR, MR, file set, or directory set
   supplied by the user;
2. staged plus unstaged changes when uncommitted work exists;
3. the current branch relative to an evidenced target branch;
4. an explicitly disclosed last-commit fallback when a target branch cannot be
   established.

Ask when competing scopes would materially change attribution or conclusions.
Never infer that the target is `main` or `master` without repository evidence.

## Applicable untracked files

Before freezing scope, inspect read-only status such as `git status
--porcelain`. Formal scope is the tracked Git Diff plus untracked files Main
explicitly selects as applicable from the user's target, requirement/change
scope, affected paths, and branch context. Never assume all untracked files
belong to one change.

Review each selected untracked file as a complete new file from `/dev/null`,
include it in reviewer packets and metrics, and classify it by the same
production, test, configuration/migration, or exclusion rules. Pass selected
paths explicitly to the metrics utility. Do not run `git add`, mutate the
index, create a synthetic repository patch, or disturb unrelated untracked
work.

For a PR or MR, prefer the provider's authoritative base and head revisions
when available. When provider access is unavailable, reconstruct the range
from local refs and disclose the limitation.

For specified files or directories, determine whether the user wants current
contents, uncommitted changes, or a historical range. If no baseline exists,
review the supplied contents but mark change attribution and change metrics as
limited.

## Baseline record

Record:

- scope source and user instruction;
- current branch and commit;
- target branch or commit;
- merge base when relevant;
- exact Diff command or provider query;
- included commits;
- staged and unstaged inclusion;
- included and excluded files;
- applicable and excluded/unrelated untracked scope;
- incomplete, binary, generated, or unavailable content;
- unrelated changes present in the range.

Use read-only Git operations. Preserve uncommitted user work and never switch,
reset, clean, revert, or rewrite branches.

## Diff pre-analysis

Count or classify:

- changed files, additions, and deletions;
- production, test, configuration, and migration LOC;
- languages and frameworks;
- dependency additions or upgrades;
- public interface and serialization changes;
- database and migration changes;
- authentication or authorization changes;
- file operations and external calls;
- shared or global state changes;
- high-risk business modules.

Exclude or report separately:

- generated and vendor code;
- lockfiles;
- build artifacts;
- minified or compressed files;
- pure formatting;
- non-semantic mass movement or rearrangement.

Record how every exclusion was identified. Do not exclude a file merely to
improve a metric.

## Context expansion

Start from changed lines. Expand only as needed to:

- callers and consumers;
- interfaces and data models;
- repositories and persistence code;
- permission middleware and policy checks;
- transaction, cache, and message boundaries;
- migration and rollback behavior;
- shared utilities and similar implementations;
- affected tests and fixtures.

Whole-repository searches are appropriate for bounded questions such as
finding consumers or established patterns. They are not permission to convert
unrelated historical issues into current-change findings.

Mark a historical problem `Existing Issue`. Exclude it from current-change
counts and gates unless the current Diff introduced, amplified, or newly
exposed it; document that causal link when it does.
