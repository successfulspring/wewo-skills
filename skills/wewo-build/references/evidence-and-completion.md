# Evidence and Completion

Record actual commands, scope, output, exit status, and repository state. Never
reconstruct or improve the history after the fact.

## Evidence truthfulness

Distinguish, where applicable:

- **TDD Red:** a focused test executed and failed for the intended behavior
  while that target production behavior was still unimplemented;
- **Debug / Implementation Failure:** implementation exists and verification
  exposed a defect in it;
- **Regression Failure:** existing behavior failed outside the focused target;
- **Environment / Infrastructure Failure:** setup or infrastructure prevented
  valid behavior evidence;
- **Passed**, **Failed**, **Blocked**, and **Not Run**.

TDD Red is not a debug failure. A post-implementation failure may be valuable
evidence, but never record it as Red. State partial command scope explicitly;
do not imply full regression from a focused test or create synthetic logs.

## Unit evidence and closure

For each unit, record its target, binding obligations, actual changes, executed
verification, failures, material gaps, confirmations, and status. For a true
TDD unit, include valid Red, Green, optional Refactor, and post-refactor
focused plus affected-regression evidence. For non-TDD or implementation-first
work, record what actually happened without fake Red/Green/Refactor fields.

Close a unit only when:

- its target result is complete;
- binding obligations are preserved;
- required verification actually ran;
- failures are visible;
- every material gap is resolved or confirmed.

A passing focused test alone is not completion.

## Fresh final verification

After all units close, rerun the relevant current commands that prove the
implementation: new and affected tests, necessary integration or regression,
and applicable type, lint, format, build, or migration checks. Read complete
output, exit status, counts when available, time, and actual scope. Do not reuse
old output as final evidence.

## Completion gate

Claim completion only when all required units close, fresh relevant
verification ran, Failed/Blocked/Not Run items are explicit, no unresolved
material gap is hidden, and `implementation-record.md` matches repository
reality. Otherwise report the honest incomplete or blocked status. Do not
claim independent review, final acceptance, deployment readiness, or a test
gate without separately authorized evidence.
