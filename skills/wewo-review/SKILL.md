---
name: wewo-review
description: "Perform a formal, read-only, diff-centered software review through exactly three independent lanes: requirement consistency, static analysis and engineering rules, and contextual security. Use for unstaged or staged changes, commits, ranges, branches, PR/MR diffs, or explicitly scoped production and developer-test code where evidence-based findings, Semgrep evidence, KLOC metrics, and distinct overall/security gates are required in one unified review report. Do not use to implement fixes, design tests, execute a final test gate, merge, or deploy."
---

# Wewo Review

Review one fixed Diff through three independent reviewer contexts, admit only
verified current-change findings, and produce one concise unified report.

## Runtime contract

Accept an explicit review target or resolve one from unstaged/staged changes,
a commit or range, a branch comparison, a PR/MR Diff, or explicitly scoped
files. All changed executable production and developer-test code inside the
resolved Diff is reviewable, including executable fixtures and helpers.

Use requirement or technical-design context only when explicitly supplied,
referenced, or already established in the current conversation. Never scan for
historical workflow documents. Normal review input does not include
`test-plan.md`, `test-cases.md`, `implementation-plan.md`,
`implementation-record.md`, or `test-execution.md`.

Create only:

```text
docs/wewo/<requirement-category>/<requirement-slug>/review.md
```

Resolve one unambiguous requirement workspace before writing. Use an explicit
path, else the current requirement workspace, else one candidate inferred from
the requirement, issue, branch, or explicitly supplied material. Ask when
multiple candidates remain. Never select by artifact existence or modification
time. Use `features`, `bugs`, `refactors`, or `maintenance` and a concise
lowercase English kebab-case slug.

Operate read-only toward production and test source. Inspect code and Git, run
safe checks, use controlled temporary tools, and write only the resolved
report. Do not fix, revert, commit, merge, deploy, or modify another
capability's document. Reviewer contexts return candidate data to Main; they
create no project artifacts.

Keep two distinct conclusions in the unified report:

- Overall Review Conclusion: `Pass`, `Conditional Pass`, `Fail`, or
  `Unable to Conclude`.
- Security Gate: `Pass`, `Fail`, or `Incomplete / Unable to Confirm`.

Critical or High confirmed current-change defects block merge. Missing a
required independent lane prevents formal Pass. A Semgrep failure alone does
not automatically fail the whole review, but its attempt and coverage
limitation must be disclosed. Before finalizing a recoverable Semgrep blocker,
Main asks once when a specific user authorization can safely unlock the scan.
When missing evidence prevents a trustworthy high-risk security conclusion,
use the incomplete/unable conclusion.

## Mandatory three-lane architecture

Formal review requires exactly three primary independent reviewer contexts:

1. **Requirement Consistency** - apply
   [requirement-consistency.md](references/requirement-consistency.md).
2. **Static Analysis & Engineering Rules** - apply
   [static-analysis-and-rules.md](references/static-analysis-and-rules.md) and
   [tool-policy.md](references/tool-policy.md).
3. **Contextual Security** - apply
   [contextual-security.md](references/contextual-security.md).

Apply [independent-review.md](references/independent-review.md). The three
lanes must not see each other's candidates before they return. Main is the
orchestrator and Finding Admission judge, not a fourth reviewer; do not have
Main repeat all three reviews. If the host cannot create the required isolated
contexts, do not simulate formal independence. Disclose the limitation and
use `Unable to Conclude` and `Incomplete / Unable to Confirm` as applicable.

## Main review workflow

### 1. Resolve and freeze the Diff

Apply [diff-scope-and-context.md](references/diff-scope-and-context.md). Prefer
the user's explicit scope, then staged plus unstaged changes, then a branch
comparison against an evidenced target. Disclose a last-commit fallback when a
target branch cannot be established. Never assume `main` or `master`.

Before freezing scope, inspect read-only Git status and add only applicable
untracked files selected from factual review context. Do not stage files or
include unrelated untracked work.

Record baseline, target, current commit, exact Git query, included commits and
uncommitted changes, included files, exclusions, and limitations. For a scope
without a meaningful Git baseline, disclose limited attribution and metrics.

### 2. Prepare compact factual context

Prepare a compact lane-specific scope packet from the fixed baseline, changed
file manifests and classifications, applicable instructions, confirmed
requirement/design evidence, repository facts, changed entry points, and useful
deterministic facts. Keep it factual: do not pre-review the change, include
suspected defects, implementation defenses, unverified explanations, the full
development conversation, or prior conclusions.

### 3. Calculate deterministic Diff metrics

Run [collect-diff-metrics.mjs](scripts/collect-diff-metrics.mjs) directly with
Node when available, following the helper policy and fallback in
[tool-policy.md](references/tool-policy.md). Record
changed files, additions, deletions, production/test LOC,
configuration/migration LOC, density-eligible changed code LOC, and exclusions.
Pass each applicable untracked file explicitly with `--include-untracked`.
If the adapter or Git scope is unsupported, record exact fallback evidence and
the limitation; never fabricate adapter execution or metrics.

### 4. Dispatch the three independent lanes

Give each lane the same fixed Diff/baseline and its compact factual lane
context. Each starts narrow and progressively inspects repository code as its
evidence path requires; cross-file reasoning remains unrestricted when needed.
Each returns lane-local candidates with ID, lane, category, location, evidence,
expected versus actual behavior, trigger/path, impact, attribution,
remediation, verification, and confidence/limitation. Do not create permanent
additional lanes or share candidates across lanes before completion.

### 5. Require Static lane tool attempts

The Static lane must run safe relevant repository-native checks and attempt
Semgrep for every formal review. Use [run-semgrep.mjs](scripts/run-semgrep.mjs)
directly with Node when available, or the equivalent safe fallback in
[tool-policy.md](references/tool-policy.md). Record mode, version, config,
target, invocation, outcome, raw warning/error counts, coverage completeness,
limitations, and cleanup. Semgrep warnings are tool candidates, never
automatic findings. If one specific user permission is the only remaining
condition for a safe supported Semgrep attempt, Main asks once before recording
`Blocked`; continue after approval and record an authorization refusal honestly.

### 6. Collect candidates

Keep lane provenance. Contextual Security must reason independently from
Semgrep output. Preserve raw tool candidates separately from reviewer
candidates and formal findings.

### 7. Apply Finding Admission

Main applies [finding-admission.md](references/finding-admission.md). Verify
evidence, root cause/location, realistic trigger or explicit limitation,
impact, current-Diff attribution, and uniqueness. Merge duplicates, classify
candidate state, then assign each admitted canonical finding one `REV-*` ID and
one metric scope. Finding category and impact, not detecting lane, determine
whether it is a security finding.

Only Confirmed current-change findings enter formal counts and gates. Only
Confirmed findings attributable to density-eligible code enter density
numerators. Raw warnings, Potential/Unverified, Rejected, Existing Issue, and
duplicates do not.

### 8. Calibrate severity and gates

Use `Critical`, `High`, `Medium`, or `Low` based on concrete impact,
reachability or exploitability where relevant, affected scope, and
reversibility. Do not use mathematical severity weights or promote subjective
style preferences to material findings.

### 9. Calculate KLOC metrics

Apply [metrics-and-gates.md](references/metrics-and-gates.md) after admission.
Use production plus test changed code LOC as the density denominator and align
each numerator to that scope. Show raw numerator, denominator, ratio, and every
exclusion. Keep total and out-of-density findings visible. Report Not
Calculable when the denominator is zero or unsupported.

### 10. Produce and verify the report

Apply [document-contract.md](references/document-contract.md) and
[review-template.md](assets/review-template.md). Use one deduplicated `REV-*`
registry and reference security findings from the security assessment without
duplicating root causes.

Verify scope, lane coverage, evidence, findings, severity totals, metric scopes,
gates, Semgrep coverage, blockers, limitations, and latest command outcomes.
Report the path and both conclusions. Stop; do not continue into implementation,
test execution, merge, release, or deployment.
