# Unified Review Document Contract

Create exactly one `review.md` for one fixed scope and workspace. Localize
prose while keeping the filename and canonical `REV-*` IDs in English. Omit
irrelevant adaptive subsections and empty checklists.

## Stable core

1. Review Conclusion & Gates
2. Scope & Baseline
3. Independent Review Coverage
4. Requirement / Design Consistency
5. Static Analysis & Engineering Rules
6. Contextual Security Assessment
7. Confirmed Findings
8. Potential / Unverified / Existing Issues
9. Verification & Tool Evidence
10. Quantitative Metrics
11. Limitations & Residual Risk

Show Overall Review Conclusion and Security Gate separately. Record the fixed
Diff/baseline, tracked scope, applicable untracked files, material excluded or
unrelated untracked scope, exclusions, all three lane statuses, and Requirement
or Design Compliance as `Not Evaluated` when explicit evidence is absent.

## Unified findings and evidence

Keep candidate IDs lane-local. After admission and deduplication, assign
sequential `REV-001`, `REV-002`, and later IDs. One root cause is one canonical
finding even when multiple lanes detected it or it has correctness and security
impact. Security classification follows category and impact, not detecting
lane; reference security findings from Contextual Security without duplication.

Record only useful ID, state, severity, category, detected-by lanes, metric
scope, location, evidence, expected/actual behavior, trigger/path, impact,
attribution, remediation, verification, and limitation.

Record deterministic commands/outcomes, Semgrep acquisition/status, raw
warning/error counts, coverage completeness and limitation, cleanup, and other
material evidence. Keep raw tool candidates separate from admitted findings.

Show each density with numerator, denominator, result, and exclusions. Show
deduplicated absolute counts by metric scope, severity, and security
classification. Label detected-by counts overlapping/non-additive.

Disclose missing lanes, unavailable requirement/design evidence, partial
Semgrep coverage, and residual risk. Do not claim merge readiness when the
Security Gate fails or is incomplete. Do not modify source/test code or another
capability's documents.
