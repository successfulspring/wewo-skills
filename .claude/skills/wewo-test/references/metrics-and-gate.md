# Evidence-Based Automated Metrics and Gate

Calculate only metrics supported by the current automated execution record and
actual evidence. Metrics explain the automated execution gate; they never
override critical failures.

Manual-only cases are outside this capability's execution scope. Exclude them
from automated denominators, execution statuses, and gate decisions. When
useful, report their IDs or count only as scope exclusions. If the resulting
in-scope automated total is zero, do not calculate automated rates or issue an
automated execution gate; report that there is no automated execution scope.

## Lightweight metrics

Report applicable automated counts:

- total in-scope automated scenarios;
- Passed, Failed, Blocked, Not Run, Skipped, Flaky, and Not Applicable;
- executed automated scenarios and automated passes;
- Product Defect, Test Defect, Test Data Issue, Environment Blocker, Existing
  Failure, Requirement Conflict, and Unverified;
- unresolved automated blockers and residual risks.

Calculate only when denominators are known:

```text
automated execution rate =
executed automated scenarios / total in-scope automated scenarios

automated pass rate =
Passed automated scenarios / executed automated scenarios

automated P0/P1 completion rate =
completed in-scope automated P0/P1 scenarios /
all required in-scope automated P0/P1 scenarios
```

State whether `Skipped` counts as completed. Generated but unexecuted automated
tests are `Not Run`, not executed. Manual-only cases are neither executed nor
`Not Run`. Do not calculate automation applicability or implementation rates
when their denominator is not well-defined.

Report code or branch coverage only when a real configured coverage tool ran.
Do not infer coverage from scenario counts or report fictional coverage.

## Automated execution gate

Use exactly one value.

### Pass

Use only when required in-scope automated P0 behavior passes; required
in-scope automated P1 behavior is sufficiently complete; critical automated
user journeys and applicable permission, consistency, and transaction behavior
pass; no release-blocking Product Defect is exposed by automated execution; and
no required high-risk automated blocker or unresolved Flaky result remains.

### Conditional Pass

Use only when core automated evidence passes, remaining automated gaps are
explicitly low risk, and an actual follow-up and risk owner are recorded when
relevant.

### Fail

Use for critical required automated behavior failure, a release-blocking
Product Defect exposed by automated execution, core automated journey failure,
critical permission/consistency/transaction failure, unsafe production
connection, or uncontrolled automated-test side effect.

### Incomplete / Unable to Confirm

Use for environment, tool, account, or data blockers affecting required
automated scope; high-risk automated `Not Run`; unresolved required
external-system automated evidence; or unresolved Flaky evidence.

Manual-only cases do not change this gate. This gate is an automated execution
gate, not a complete manual-QA or release-approval decision.

A high pass rate never hides a critical failure. Report partial automated
execution and verified failures even when the final gate is incomplete.
