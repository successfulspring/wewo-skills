# Lean Automated Test Execution Document Contract

Localize generated headings and prose while keeping stable filenames in
English. Use one resolved workspace, tested code version, automated execution
record, and evidence set.

## `test-execution.md`

Always create this document when automated execution is requested or completed.
Keep it execution-first and concise. Use this adaptive structure:

1. localized title;
2. Automated Test Conclusion;
3. Execution Scope and Environment;
4. Test Results;
5. Failures, Blockers, and Flaky Results, only when applicable;
6. Test Asset Changes, only when applicable;
7. Metrics and Residual Risks.

The conclusion includes the automated execution Gate and actual counts for
Passed, Failed, Blocked, Not Run, and Flaky when applicable.

Scope and environment record Code Version, automated Scope, Environment, Test
Basis, Key Limitations, and excluded Manual case IDs/count when useful. Refer to
an explicitly supplied test-case artifact without copying or rewriting it.

Center the result table on automated execution evidence:

```markdown
| Case | Route | Runner | Status | Evidence / Failure |
|---|---|---|---|---|
```

Keep Agent Tool Interface in the internal execution record when useful; do not
add it as a mandatory published column. The report prioritizes required
evidence and repository-runner results over agent implementation details.

Manual-only cases are outside this capability's execution scope. Do not create
`manual-test-checklist.md`, manual statuses, manual execution tasks, or duplicate
manual-test documents. Manual cases may be listed briefly as excluded scope so
the automated denominator is transparent. They are not `Not Run` and do not
change the automated execution gate.

Add details only when they help explain an actual failure, blocker, Flaky
result, asset change, Testability Change Request, native artifact, scope
exclusion, or residual risk. Omit empty test-type and inapplicable sections; do
not fill them with `Not Applicable` boilerplate.

Metrics remain lightweight and calculable. Record automated execution rate,
status counts, relevant automated counts, automated P0/P1 completion when its
denominator is known, unresolved blockers, residual risks, and native
report/artifact locations. Do not invent coverage or normalize every native
result into HTML.

## Native evidence

Reference runner-native evidence rather than converting it solely for report
uniformity. Useful examples include terminal output and exit status, existing
HTML/XML/JSON/JUnit reports, coverage produced by a configured coverage tool,
Playwright Trace or screenshots, Cypress screenshots/video, Gradle reports, Go
JSON events, and performance summaries.

Store retained sanitized evidence under `test-artifacts/` when it is not
already in a stable repository-native location. Never expose secrets,
credentials, cookies, tokens, personal data, or unnecessary production data.

Optional supporting tables:

```markdown
| Check | Command | Code Version | Environment | Status | Exit Status | Native Evidence |
|---|---|---|---|---|---|---|
```

```markdown
| File | Change | Cases | Executed Status |
|---|---|---|---|
```

```markdown
| Case | Status | Attribution | First Evidence | Rerun / Stability Evidence | Defect / Blocker |
|---|---|---|---|---|---|
```

## Final consistency checks

Verify:

- report, execution record, and artifacts use the same code version and
  automated scope;
- excluded Manual cases are not counted as automated, `Not Run`, or blockers;
- every `Passed` result has current-run evidence;
- generated but unexecuted automated assets remain `Not Run`;
- first-failure and Flaky evidence remain visible;
- only confirmed Product Defects enter the product defect list;
- counts and calculable automated metrics reconcile;
- required high-risk automated blockers affect the automated execution gate;
- environment coverage is not overstated;
- evidence is sanitized and cleanup risk is recorded;
- executable tests remain in normal project test paths;
- no production file or source test-case artifact was silently modified.
