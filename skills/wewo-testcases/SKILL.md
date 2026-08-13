---
name: wewo-testcases
description: Design comprehensive, executable test cases from authoritative requirements and risks, then classify the already-designed cases by test level and downstream automation route. Use when a user asks what behaviors and failure scenarios should be verified for a feature, bug, refactor, or maintenance change. Do not use to implement or execute tests, modify product code, record test results, or perform code review.
---

# Wewo Test Cases

Design semantic test scenarios and executable cases from authoritative
requirements and risks first. Only after the case set passes coverage and
oracle audits, annotate it with Test Level and Automation. The only owned
project artifact is `test-cases.md`.

## Inputs and output

Work from a sufficiently clear current user requirement, an explicitly
supplied or established `prd.md`, or both. An optional `technical-design.md` or
explicit external contract may define authoritative technical behavior.
Requirement and design evidence are sufficient; implementation code and other
capabilities are not prerequisites.

Do not discover historical QA documents, workflow artifacts, or old case
libraries unless explicitly supplied or authorized. Write only:

```text
docs/wewo/<requirement-category>/<requirement-slug>/test-cases.md
```

Do not create a test plan or intermediate risk, coverage, automation, or audit
artifact. Keep the filename and workspace path in English. Use the requested
language, otherwise the interaction's dominant language, and otherwise Chinese
for the document.

## Runtime workflow

### 1. Resolve the requirement workspace

Use an explicit workspace, then one established in the current requirement
context, then one unambiguous candidate inferred from the requirement, issue,
branch, or explicitly referenced material. Ask before writing when multiple
candidates are plausible. Never select by discovered artifact or modification
time. Use `features`, `bugs`, `refactors`, or `maintenance`; default to
`features` only when no evidence favors another category. Never mix different
requirements without confirmation.

### 2. Establish authoritative requirements and repository mode

Read [context-analysis.md](references/context-analysis.md). Requirement defines
expected behavior; repository implementation reveals implemented behavior.
Resolve material oracle ambiguity without using current implementation as a
fallback requirement oracle.

In default requirement-driven mode, do not broadly inspect implementation
source, functions, classes, providers, pages, current tests, runners, or
fixtures. Use implementation-aware mode only when the user requests it, source
code is explicitly supplied or referenced, current behavior is the requested
basis because authoritative requirements are absent, or an authoritative
technical-design seam requires repository grounding.

### 3. Model requirements, behavior, risks, and scenarios

Read [risk-and-strategy.md](references/risk-and-strategy.md). Before any
implementation inspection, derive and trace the authoritative behaviors,
rules, outcomes, risks, and material test obligations. Ask what can fail, what
must be verified, what scenarios provide distinct evidence, and what exact
observable outcome means pass or fail.

Apply applicable business-flow, input/data, business-rule, lifecycle, access,
reliability, security, user-experience, and critical-journey lenses. Create
semantic scenarios from distinct evidence needs, not from test levels,
repository functions, requirement sentences, fixed ratios, or test-pyramid
quotas.

Lock requirement-derived obligations before implementation-aware enrichment.
Missing implementation is a potential test failure, not a reason to omit the
test case. Only authoritative evidence may mark behavior optional, future,
out-of-scope, or not required for this delivery.

### 4. Optionally enrich from implementation

When implementation-aware mode applies, inspect progressively only after the
requirement-derived scenario and oracle model is locked. Repository facts may
add regression risks, technical seams, compatibility cases, executable setup,
public interfaces, or automation-suitability evidence. They must not remove or
weaken a requirement-derived case, redefine its oracle, turn missing behavior
into out-of-scope work, or rewrite expected behavior to match implementation.

Do not create Unit cases merely because code exposes functions or classes.
Prefer user, business, or public-interface semantics unless an authoritative
technical contract or explicit implementation-aware request makes a concrete
seam itself the evidence target.

### 5. Generate executable semantic cases

Read [test-case-quality.md](references/test-case-quality.md). Create the full
semantic case set before selecting Test Level or Automation. Use stable IDs,
business-readable scenarios, adaptive Preconditions and Notes, concrete Steps,
and authority-grounded Expected Results. Keep Traceability, Objective,
Technique, Coverage Lens, Risk Category, Repository Fact, and Evidence Need
internal.

Compress equivalent or low-value duplicates with partitions, boundaries,
decision tables, state matrices, parameterization, representative combinations,
or pairwise coverage. Never rewrite a difficult or missing-implementation case
to fit a tool.

### 6. Audit semantic coverage and oracles

Before classification, run the requirement, happy-path, negative/alternative,
boundary, business-rule, state-transition, permission/ownership,
failure/recovery, security, critical-journey, oracle-authority, duplicate-value,
and Cross-case Oracle Consistency audits in `test-case-quality.md`, applying
each where relevant. Fix missing cases, vague or unsupported oracles,
contradictions, and unnecessary duplicates. Do not invent thresholds.

Every published case must have one authoritative and executable pass/fail
oracle for each material expected behavior. Reject materially different
`A or B`, `A and/or B`, current-implementation, or mock-behavior fallbacks.
Different wording is acceptable only when it preserves the same required
business outcome. Propagate confirmed clarifications consistently across every
case that shares the rule.

If material ambiguity remains after clarification is declined or unavailable,
publish unaffected cases and optionally disclose only the material unresolved
item; do not publish a definitive oracle for the affected evidence need.

### 7. Classify the completed cases

Only after the semantic case set passes audit, read
[test-level-selection.md](references/test-level-selection.md) and assign one
Recommended Test Level to each case. Test Level describes where an
already-designed case is best proven; it never decides whether the case exists.

Then read [automation-classification.md](references/automation-classification.md),
classify Automation Feasibility, select a concrete Automation Route when
semantics determine it, otherwise deliberately defer the route and render
`Auto`. Automation is a final annotation: it must not generate or remove a
case, rewrite steps, weaken an oracle, or suppress unimplemented required
behavior.

Use Playwright only when browser behavior itself supplies the evidence. Use an
explicit API, Integration, Component, or Contract route when authoritative
technical evidence defines that seam. Use `Auto` when automation is clearly
appropriate but choosing the cheapest stable route requires downstream
repository inspection. `Auto` is neither a Test Level nor a concrete tool. Keep
Manual narrow to intrinsic human judgment and preserve named conditions in
`Conditional · Auto` or other Conditional values.

Except for the fixed Browser-to-Playwright convention, the skill does not
inspect, select, configure, or reason about concrete test tools, test runners,
browser installations, or execution infrastructure. Concrete non-browser tools
belong downstream. Do not implement or run automation.

### 8. Finalize the lean artifact

Read [document-contract.md](references/document-contract.md) and use
[test-cases-template.md](assets/test-cases-template.md). If the file exists,
treat an explicit update request as authorization; otherwise ask before
overwriting it. Start near-immediately with cases. Do not publish passing audit
narratives, coverage mappings, automation statistics, repository inventories,
or internal methodology by default. Add only a compact Unresolved Items
section when material oracle issues remain.

Do not create executable tests, start services, install tools, modify product
code or databases, record actual results, or continue into execution or review.
Report the exact path and any material unresolved oracle issues. Claim only
completed work.
