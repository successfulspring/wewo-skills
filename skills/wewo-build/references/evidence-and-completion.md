# Verification Evidence and Completion

Use actual command output, exit status, and current repository state.

## Per-slice evidence

Record:

- focused Red command and valid failure reason;
- focused Green command and result;
- post-refactor verification;
- relevant existing and integration tests;
- type, compile, lint, or format result;
- requirement and code-quality self-check result;
- changed files and scope;
- blockers or unavailable checks.

## Final fresh verification

After all slices, identify commands that prove the current implementation and
rerun applicable:

- all new tests;
- affected-module tests;
- necessary integration tests;
- relevant regression tests;
- type-check;
- lint and formatting verification;
- build and migrations;
- currently executable broader suite.

Read complete output, exit status, failure count, and current timestamp. Do not
reuse an earlier result as final evidence, and do not trust another agent's
summary without main-flow verification.

## Result vocabulary

Classify each check explicitly:

- passed: executed successfully with supporting output;
- failed: executed and returned failure;
- not run: intentionally omitted;
- blocked: prevented by a known external condition;
- unavailable: command or required capability does not exist;
- partial: only a stated subset ran.

Never equate code inspection with a passing test. State when the full suite was
not run.

## Completion decision

Before claiming completion, verify:

- confirmed behavior and scope are implemented;
- every slice has current evidence or a transparent blocker;
- failures are resolved or reported;
- latest quality commands support the conclusion;
- plan deviations are documented;
- the actual scope of implementation verification performed is recorded,
  including the browser-acceptance boundary;
- known limitations and remaining risks are explicit;
- implementation record matches actual files and commands.

Do not claim independent review, final acceptance, deployment readiness, or a
test gate unless that work was separately performed and authorized.
