# Test Metrics and Gate

Calculate metrics from the current execution matrix and actual evidence.

## Contents

- [Scenario metrics](#scenario-metrics)
- [Automation metrics](#automation-metrics)
- [Manual metrics](#manual-metrics)
- [Quality and stability](#quality-and-stability)
- [Test gate](#test-gate)

## Scenario metrics

```text
scenario execution rate =
(executed automated scenarios + completed manual scenarios)
/ planned scenarios

P0/P1 completion rate =
executed P0/P1 scenarios / all planned P0/P1 scenarios
```

Define completed manual scenarios consistently and disclose whether explicitly
Skipped items enter the numerator.

## Automation metrics

```text
automation applicability =
automation-suitable scenarios / all scenarios

automation implementation rate =
implemented automated scenarios / automation-suitable scenarios

automation execution rate =
executed automated scenarios / implemented automated scenarios

automation pass rate =
Passed automated scenarios / executed automated scenarios
```

Generated but unexecuted tests are implemented and Not Run, not executed or
Passed. Do not equate a high automation rate with test quality.

## Manual metrics

Report total manual tests and counts of Manual Pending, Manual Passed, Manual
Failed, Manual Blocked, and Manual Skipped. Calculate overall and P0/P1 manual
completion only when the planned denominator is known.

## Quality and stability

Report Passed, Failed, Blocked, Not Run, Skipped, Flaky, and Not Applicable;
Product Defect, Test Defect, Test Data Issue, Environment Blocker, Existing
Failure, Requirement Conflict, and Unverified; regression pass rate; core-flow
pass rate; cleanup success; new automated assets; and automated scenario
coverage.

Report code or branch coverage only when the configured coverage tool actually
ran. State numerator, denominator, exclusions, and `Not calculable` when
evidence is insufficient.

## Test gate

- `Pass`: all P0 pass; required P1 and manual tests complete; core journeys and
  critical permission, transaction, and consistency tests pass; no
  required-evidence scenario was silently downgraded; no release-blocking
  defect; no unaccepted high-risk Blocked or Flaky remains.
- `Conditional Pass`: core flows pass, no blocker remains, residual risk is
  low, unfinished items are explicit, and an actual risk owner and follow-up
  are recorded.
- `Fail`: P0/P1 core, permission, transaction, consistency, core E2E, or
  migration failure; blocking Product Defect; uncontrolled automation side
  effect; or accidental production connection.
- `Incomplete / Unable to Confirm`: environment, account, data, required
  manual evidence, high-risk scenario, external system, or necessary tool is
  unavailable, or relevant results remain Flaky.

Use only these four values. Even when incomplete, report executed tests,
verified failures, and residual risk.

Pass rate and automation rate support transparency; neither can override core
flow failures, blockers, required manual work, or evidence gaps.
