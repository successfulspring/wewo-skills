# Review Document Contract

Create both reports for the same resolved workspace and review scope. Localize
headings and prose while keeping both filenames in English.

## Contents

- [Code review report](#code-review-report)
- [Security review report](#security-review-report)
- [Cross-report checks](#cross-report-checks)

## Code review report

Use these sections in order:

1. Review Conclusion
2. Review Scope and Baseline
3. Review Evidence
4. Change Size and Risk Overview
5. Independent Reviewer Execution
6. Tool Installation and Verification
7. Requirement and Design Compliance
8. Repository Standards and Code Structure
9. Code Correctness
10. Test Quality
11. Impact and Compatibility
12. Confirmed Findings
13. Potential Risks and Unverified Items
14. Existing Issues
15. Quantitative Metrics
16. Merge Gate
17. Recommended Fix Order
18. Review Limitations

Use the filename `07-code-review.md`.

## Security review report

Use these sections in order:

1. Security Gate Conclusion
2. Review Scope
3. Attack-Surface Overview
4. L1 Dangerous-Pattern Checks
5. L2 Semantic Diff Review
6. L3 Cross-file and Business-flow Review
7. Authentication and Authorization
8. Input, Injection, and File Safety
9. Sensitive Data and Configuration
10. Business Security
11. Transactions, Concurrency, and Idempotency
12. External Systems and Supply Chain
13. Security Tools and Test Evidence
14. Confirmed Security Findings
15. Potential Risks and Unverified Items
16. Existing Security Issues
17. Security Metrics
18. Residual Risks and Verification Recommendations
19. Review Limitations

Use the filename `08-security-review.md`.

## Shared evidence tables

Scope:

```markdown
| Field | Value |
|---|---|
| Baseline | |
| Target | |
| Current commit | |
| Diff command or query | |
| Included commits | |
| Uncommitted changes | |
| Included files | |
| Exclusions | |
```

Commands:

```markdown
| Check | Command | Scope | Result | Evidence |
|---|---|---|---|---|
```

Use `Passed`, `Failed`, `Not run`, `Blocked`, or `Unavailable`; never convert
missing evidence to Passed.

Reviewer execution:

```markdown
| Dimension | Independent reviewer | Status | Limitations |
|---|---|---|---|
```

Candidate ledger:

```markdown
| Candidate | State | Root cause | Current-change attribution | Final disposition |
|---|---|---|---|---|
```

Metrics:

```markdown
| Metric | Value | Numerator | Denominator | Exclusions or limitation |
|---|---|---|---|---|
```

## Cross-report checks

Verify:

- identical baseline and included Diff;
- consistent evidence and command outcomes;
- consistent shared finding state and severity;
- no duplicate root-cause counts;
- historical issues excluded from current-change metrics;
- unsupported metrics marked not calculable;
- Critical and High blockers reflected in both gates;
- an incomplete or failed security gate never yields merge readiness;
- missing requirements and non-independent fallback are disclosed;
- conclusions use the latest Diff and command evidence;
- no source or test file was modified;
- no empty upstream or downstream workflow document was created.
