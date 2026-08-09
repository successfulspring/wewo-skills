---
name: wewo-review
description: Perform an independent, diff-centered, evidence-based, read-only code review and security/reliability review of actual code changes, producing separate code-review and security-gate reports. Use for unstaged or staged changes, commits, commit ranges, branch or PR/MR diffs, or explicitly scoped files and directories. Do not use to implement or automatically fix code, replace implementation self-checks, design tests, execute the final testing gate, merge, or deploy.
---

# Wewo Review

Review actual code changes independently, verify every admitted finding, and
report code quality and security conclusions separately.

## Runtime contract

Accept a user-specified review target or determine one from unstaged changes,
staged changes, a commit, a commit range, a branch comparison, a PR or MR Diff,
or specified files or directories.

Create only:

```text
docs/wewo/<requirement-category>/<requirement-slug>/code-review.md
docs/wewo/<requirement-category>/<requirement-slug>/security-review.md
```

Resolve exactly one requirement workspace before writing either report. Keep
stable filenames and workspace segments in English. Write user-facing
conversation and reports in an explicitly requested language, otherwise the
dominant interaction language, and otherwise Chinese.

Operate read-only by default. Read code and documents, inspect Git, search
context, run safe checks, use approved temporary tools, and write the two
reports. Do not modify production or test code, apply fixes, revert changes,
commit, merge, deploy, alter requirements or expected behavior, or modify a
workflow document owned by another capability. If the user requests fixes, stop
after review and obtain explicit authorization for a separate implementation
task.

## Non-negotiable conclusion vocabulary

Use only these final values:

- Code review: `Pass`, `Conditional Pass`, `Fail`, `Unable to Conclude`.
- Security gate: `Pass`, `Fail`, `Incomplete / Unable to Confirm`.

`Blocked`, `Pending`, `Unverified`, and candidate states are not final
conclusions. When a high-risk change lacks necessary independent review or
critical environment-dependent verification, report:

```text
Code review: Unable to Conclude
Security gate: Incomplete / Unable to Confirm
Merge readiness: Not ready
```

Do not invent an exception path for missing critical evidence. Risk acceptance
can support `Conditional Pass` only for Medium or Low findings and only with an
actual authorized owner, recorded conditions, and follow-up.

## Mandatory workflow

### 1. Resolve the workspace and review target

Run independently. Use `prd.md` and `technical-design.md` only when the user
explicitly supplies or references them, or the current conversation already
establishes them. Never require or create empty earlier-stage documents, and
never scan `docs/wewo/` or the repository for historical requirement documents.
Normal review input does not include `test-plan.md`, `test-cases.md`,
`implementation-plan.md`, `implementation-record.md`, or `test-execution.md`.
A user may explicitly request additional review context through ordinary user
instructions, but that does not make an artifact part of the standard input
contract.

Resolve the requirement workspace in this order:

1. Use an explicit workspace supplied by the user.
2. Otherwise reuse the workspace established for this requirement.
3. Otherwise infer one candidate from the requirement, issue, branch, or
   explicitly supplied or referenced material.
4. Ask before writing if multiple candidates are plausible.

Never infer a workspace from the existence of workflow artifacts. Never select
a workspace by modification time. Support `features`, `bugs`, `refactors`,
and `maintenance`; default to `features` only when no evidence favors another
category. Use a concise lowercase English kebab-case slug. Create missing
parents only after resolution is unambiguous. Never mix different requirements
without confirmation.

Apply the scope precedence in
[diff-scope-and-context.md](references/diff-scope-and-context.md). Prefer an
explicit user scope. Otherwise review staged and unstaged changes when they
exist; otherwise establish the current branch Diff against an evidenced target
branch. Ask or clearly disclose a last-commit fallback when the target branch
cannot be established. Never assume `main` or `master`.

Before formal review, record:

- review baseline, target branch or commit, and current commit;
- the exact Diff command or equivalent query;
- included uncommitted changes and commit list;
- included files and explicitly excluded generated or unrelated changes;
- scope limitations and whether the target is complete.

For specified files without a meaningful Git baseline, record the equivalent
scope and state that current-change attribution may be limited.

### 2. Collect evidence and pre-analyze the Diff

Use direct code evidence first: the actual Diff, affected context, production
and test code, repository rules, and actual command output. An implementer's
process narrative is not proof that the implementation is correct. Actual test
code may be reviewed because it is part of the repository or Diff. Actual
directly available execution evidence may be considered when relevant, but the
review does not depend on another capability's workflow report.

When the user explicitly supplies or references them, or the current
conversation already establishes them, use requirement context (`prd.md`) and
design context (`technical-design.md`), plus an identified issue or MR
description. Never scan `docs/wewo/` or the repository to discover these
documents.

Read and apply
[diff-scope-and-context.md](references/diff-scope-and-context.md). Inspect
changed lines and only the affected callers, consumers, models, permissions,
transactions, caches, messages, migrations, tests, and similar
implementations needed to reason about them. Do not start with a whole-repository
issue hunt.

Pre-analyze changed files, added and deleted lines, production/test/configuration
or migration LOC, languages, frameworks, dependencies, interfaces, database,
permissions, files, external calls, global state, and high-risk modules.
Exclude or separately classify generated, vendor, lock, build, minified,
compressed, pure-formatting, and non-semantic rearrangement changes.

### 3. Establish risk and independent review dimensions

Read and apply
[independent-review.md](references/independent-review.md) and
[review-dimensions.md](references/review-dimensions.md).

The orchestrator must establish scope, collect factual requirements and
standards, prepare the Diff and necessary context, run shared safe commands,
dispatch review dimensions, consolidate candidates, verify evidence,
deduplicate root causes, calibrate severity, calculate supportable metrics, and
write the reports.

When fresh reviewer agents are available, use clean factual context for these
independent dimensions:

1. requirement and design compliance;
2. repository standards and code structure;
3. correctness and test quality;
4. impact and compatibility;
5. security and reliability.

Do not send implementation defenses, unproven explanations, the complete
development conversation, or another reviewer's initial conclusions.

When independent agents are unavailable, perform separate semantic and
tool-assisted passes yourself, label the result `Non-independent preliminary
review`, and disclose the lack of context isolation. Never claim formal
independence. For high-risk changes, use `Unable to Conclude` when the missing
independent review prevents a trustworthy merge conclusion.

### 4. Perform code, security, and reliability review

Apply [review-dimensions.md](references/review-dimensions.md) to requirement,
standards, correctness, test, and compatibility analysis.

**Requirement Compliance** — when requirement context exists, evaluate missing
requirements, partial implementation, wrong observable behavior, acceptance
mismatch, and scope creep. When requirement context is absent, mark
`Requirement Compliance: Not Evaluated` and explain why. Do not invent missing
requirements.

**Design Compliance** — when technical-design context exists, evaluate
architecture deviation, module/interface/API deviation, data-model deviation,
transaction/concurrency deviation, permission/security deviation, reliability
constraint deviation, and other material design deviations. When design context
is absent, mark `Design Compliance: Not Evaluated` and explain why. Do not
invent missing design expectations.

Apply
[security-and-reliability.md](references/security-and-reliability.md).
Identify only attack surfaces actually added or changed, then perform:

- L1 dangerous-pattern checks;
- L2 semantic Diff review;
- L3 cross-file and business-flow analysis for applicable high-risk areas.

Trace affected authentication, authorization, validation, injection, files,
sensitive data, business-state transitions, transactions, concurrency,
idempotency, retries, caches, messages, migrations, dependencies, and
configuration. Dynamically select applicable checks instead of printing an
irrelevant full checklist.

Keep existing issues separate. Do not attribute an existing issue to the
current change unless the Diff introduced it, expanded its impact, or made it
newly reachable.

### 5. Use tools as evidence, not authority

Read and apply [tool-policy.md](references/tool-policy.md).

Always perform baseline semantic review. Prefer repository-native commands and
versions found in repository instructions, CI, manifests, Makefiles, or
scripts. Run only safe and relevant tests, lint, type-check, build, coverage,
migration, or security checks. Do not invent commands or claim an unexecuted
command passed.

Use specialty tools only when they add material evidence. A missing tool never
blocks semantic review. Install dynamically only under the controlled policy:
fixed trusted version, isolated temporary environment, no project dependency
or lockfile change, no administrator rights, no source upload, no persistent
service, and recorded installation and cleanup. Obtain confirmation for every
high-impact case.

Treat every tool warning as a candidate. Locate the code, establish
reachability and controllability, inspect defenses, attribute it to the
current change, and deduplicate its root cause before classification.

### 6. Verify and admit findings

Read and apply
[finding-admission.md](references/finding-admission.md).

Classify every candidate as `Confirmed`, `Potential`, `Unverified`,
`Rejected`, or `Existing Issue`. Admit a formal current-change finding only
when it has:

- actual evidence and current-change attribution;
- a file and precise location or code range;
- a trigger condition and concrete impact;
- actionable remediation and suggested verification;
- one unique root cause;
- a calibrated `Critical`, `High`, `Medium`, or `Low` severity;
- an evidence level supported by the actual review.

Only Confirmed current-change findings enter formal issue totals, density
metrics, and merge gates. Report Potential and Unverified items separately.
Exclude generic advice, unsupported speculation, style preference, raw
unverified warnings, duplicate symptoms, and unrelated historical issues.

### 7. Calculate supported metrics and conclusions

Read and apply
[metrics-and-gates.md](references/metrics-and-gates.md).

Calculate only metrics with evidenced numerators and denominators. Separate
production, test, configuration, and migration LOC. Record eligible and
reviewed LOC, review coverage, candidate-state counts, confirmation rate,
confirmed and serious issue density, weighted density, requirement
implementation and test mapping, high-risk attack-surface coverage, tool
verification, and unresolved blockers when applicable.

Mark a metric `Not calculable` with its missing evidence instead of inventing
it. For small Diffs, emphasize absolute counts, severity, and blockers rather
than unstable KLOC ratios. Metrics support transparency and trends; they never
replace gate rules.

Issue separate conclusions:

- Code review: `Pass`, `Conditional Pass`, `Fail`, or `Unable to Conclude`.
- Security gate: `Pass`, `Fail`, or `Incomplete / Unable to Confirm`.

Use exactly these conclusion values; do not substitute `Blocked`, `Pending`,
or informal labels. Represent blockers inside the report while keeping the
canonical conclusion.

Unresolved Critical or High findings block merge. An unresolved security gate
prevents a merge-ready conclusion even if ordinary code quality passes.
Critical high-risk verification gaps keep the security gate unresolved.
Use `Unable to Conclude` for code review and `Incomplete / Unable to Confirm`
for security when absent independent review or critical environment evidence
prevents a high-risk conclusion. Do not invent an exception or risk-acceptance
process to turn missing critical evidence into a pass. Risk acceptance applies
only to remaining Medium or Low findings under `Conditional Pass` and must
identify the actual authorized owner.

### 8. Write and verify both reports

Read [document-contract.md](references/document-contract.md). Generate
`code-review.md` from
[code-review-template.md](assets/code-review-template.md) and
`security-review.md` from
[security-review-template.md](assets/security-review-template.md).

Include the real scope, baseline, evidence sources, independent-review status,
commands and outcomes, tool installations, all candidate classifications,
deduplicated findings, supported metrics, limitations, blockers, and separate
gate conclusions. Include the Requirement Compliance and Design Compliance
disposition, including `Not Evaluated` with the reason when context is absent.
Never present implementation self-check as independent review.

Before finishing, verify that both reports agree on scope, evidence, shared
findings, severity, blockers, and whether merge is allowed. Base conclusions
on the latest Diff and latest actual command evidence.

Report to the user:

- scope, baseline, included uncommitted changes, and materials used;
- independent reviewer dimensions completed;
- executed and dynamically installed tools;
- incomplete verification;
- Confirmed counts and severity distribution;
- supported density and coverage metrics;
- security issues and blockers;
- code-review and security-gate conclusions;
- both report paths.

Stop without pretending success when the Diff is unavailable, the review
target is materially ambiguous, critical context is missing, or safe
verification cannot be completed. Still preserve verified partial findings and
clearly label the resulting limitation. Do not automatically continue into
implementation, test execution, merge, release, or deployment.
