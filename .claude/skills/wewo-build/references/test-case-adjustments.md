# Test Case Input and Adjustment Records

Treat an existing `04-test-cases.md` as test-design input, not a fixed mapping
to executable functions. Never modify `03-test-plan.md` or `04-test-cases.md`;
do not create them when absent.

## Candidate evaluation

Record for each relevant case in the implementation record:

- build evaluation result;
- final test level;
- actual test seam;
- actual test file;
- TDD adoption status;
- split, merge, parameterization, or deferral;
- automation approach;
- reason for adjustment or non-adoption.

Use statuses such as adopt, change level, split, merge, defer, do not adopt,
environment blocked, and pending confirmation.

## Allowed adjustments

Implementation may adjust test level, seam, splitting, merging,
parameterization, and deferral of E2E or manual scenarios, without changing
confirmed business behavior, observable outcomes, authorization, consistency,
security, acceptance criteria, or scope.

Record every adjustment in `06-implementation-record.md`; do not write it back
into `04-test-cases.md` or `03-test-plan.md`.

If a case conflicts with confirmed requirements, pause and surface the
conflict. Never weaken an expected result to match implementation.

## Conflicts and upstream revisions

If an upstream test document must be corrected (for example, the overall
strategy is proven infeasible), do not edit it directly. Propose the
correction and obtain explicit user confirmation for a deliberate revision of
the owning document.

## Plan deviations

Allow implementation-derived changes to test seam, level, file split, internal
class or function structure, case grouping, and implementation detail.

For every plan deviation, record the original plan, actual solution, reason,
business impact, confirmation when required, and affected files and tests.
Never silently depart from technical or test expectations.
