# Test Execution Document Contract

Create both documents for the same resolved workspace, code version, matrix,
and evidence set. Localize headings and prose while keeping filenames in
English.

## Contents

- [Test execution report](#test-execution-report)
- [Manual checklist](#manual-checklist)
- [Evidence tables](#evidence-tables)
- [Final consistency checks](#final-consistency-checks)

## Test execution report

Use these sections in order:

1. Test Conclusion
2. Test Objective, Scope, and Code Version
3. Test Basis
4. Existing Project Test Foundation
5. Environment and Data-Safety Confirmation
6. Test Scenario Execution Matrix
7. Automation Feasibility
8. Tool Discovery, Installation, and Execution
9. Unit Test Results
10. Component Test Results
11. Integration Test Results
12. API and Contract Test Results
13. E2E Test Results
14. Security-Behavior Test Results
15. Database and Migration Test Results
16. Performance and Reliability Test Results
17. Manual Test Status
18. Failure Attribution and Defect List
19. Flaky Tests
20. Automated Test-Asset Changes
21. Testability Change Requests
22. Quantitative Metrics
23. Test Gate
24. Environment Limitations and Residual Risks

Use the filename `test-execution.md`. Mark inapplicable test-type sections
`Not Applicable` without fabricated detail.

## Manual checklist

Use these sections in order:

1. Manual Test Instructions
2. Test Environment and Account
3. Manual Test Summary
4. P0 Manual Tests
5. P1 Manual Tests
6. P2/P3 Manual Tests
7. Manual Failures and Defects
8. Manual Blockers
9. Missing Evidence
10. Manual Test Conclusion

Use the filename `manual-test-checklist.md`.

## Evidence tables

Execution commands:

```markdown
| Check | Command | Code version | Environment | Status | Exit status | Evidence/artifacts |
|---|---|---|---|---|---|---|
```

Test assets:

```markdown
| File | Change | Scenarios | Executed status |
|---|---|---|---|
```

Failure ledger:

```markdown
| Scenario | Status | Attribution | Evidence | Defect/blocker | Rerun result |
|---|---|---|---|---|---|
```

Metrics:

```markdown
| Metric | Value | Numerator | Denominator | Limitation |
|---|---|---|---|---|
```

Testability request:

```markdown
### TCR-001 {Title}

- **Obstacle:**
- **Proposed production change:**
- **Production impact:**
- **Alternative:**
- **Risk:**
- **Recommended production-code change:**
```

## Final consistency checks

Verify:

- report, checklist, matrix, and artifacts use the same code version;
- every Passed result has actual current-run evidence;
- generated-only assets remain Not Run;
- manual Passed entries identify human execution evidence;
- first-failure and Flaky evidence are preserved;
- formal Product Defects have confirmed attribution;
- command and status counts reconcile with metrics;
- required P0/P1 and manual gaps affect the gate;
- secrets and production data are absent from reports and artifacts;
- executable tests remain in project test paths;
- no production file or planning document was silently modified;
- no document owned by another capability was created.
