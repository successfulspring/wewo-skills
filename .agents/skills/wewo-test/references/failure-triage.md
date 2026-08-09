# Failure Triage and Flaky Handling

Preserve first-failure evidence and distinguish product behavior from test and
environment problems.

## Failure attribution

- `Product Defect`: confirmed implementation behavior violates the expected
  product result.
- `Test Defect`: test code, fixture, locator, mock, setup, or assertion is
  incorrect.
- `Test Data Issue`: preparation, uniqueness, ownership, or cleanup is wrong.
- `Environment Blocker`: service, database, network, browser, tool, or account
  prevents execution.
- `Existing Failure`: evidence shows the failure predates the current change.
- `Flaky`: unchanged code and environment produce mixed outcomes.
- `Requirement Conflict`: requirements, test design, and current expectation
  conflict.
- `Unverified`: evidence cannot establish attribution.

Only confirmed Product Defect items enter the formal product defect list.

## Triage sequence

1. Capture command, code version, environment, timestamp, exit status, logs,
   screenshots, Trace, and relevant data state from the first failure.
2. Check whether the test reached and exercised the target behavior.
3. Validate setup, account, data, fixture, locator, mock, and assertion.
4. Compare with baseline evidence when classifying Existing Failure.
5. Fix only permitted test assets for a Test Defect.
6. Rerun the focused test, then relevant regression.
7. Record attribution, evidence, defect or blocker, and residual risk.

Do not weaken assertions, skip a required scenario, modify business
expectations, or change production logic to obtain Green.

## Mandatory stability-evidence protocol

When an affected test has shown mixed Pass/Fail behavior, unexplained
intermittent failure, or a failure that required changing synchronization,
waiting, timing, or harness behavior:

1. one successful rerun is not sufficient evidence of stability;
2. before making a stability or no-flaky conclusion, execute the final
   unchanged affected test scope under unchanged code and materially unchanged
   environment;
3. the default minimum repeated evidence is 3 consecutive executions of the
   affected scope (this does not require running the entire suite three times);
4. mixed Pass/Fail among those executions marks the affected test Flaky;
5. without sufficient repeated evidence, do not claim stability or "no flaky";
6. report the repeat count and observed outcomes.

Prefer evidence-scoped wording such as "No flaky behavior was observed in 3
consecutive executions of the affected scope under the recorded environment"
over unsupported categorical wording such as "There are no flaky tests."

After preserving the first failure, collect logs, screenshots, Trace, and
environment evidence. Fix test-code defects and rerun. Use a small bounded
number of reruns under unchanged code, environment, data policy, and test
configuration, and record every outcome. Do not use unlimited retries or
report a final passing retry as reliable success. Framework retry output is
diagnostic evidence, not a way to erase the initial failure.
