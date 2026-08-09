---
name: wewo-testplan
description: Design a risk-based test strategy and detailed, traceable test cases before or alongside implementation, including appropriate test levels, coverage conditions and test-data assumptions, regression scope, and manual coverage. Use when a user asks what and how a feature, bug, refactor, or maintenance change should be tested. Do not use to implement code, generate final executable tests, execute tests, record Passed or Failed results, create execution evidence, or perform code review.
---

# Wewo Test Plan

Define what must be tested and the expected evidence without implementing or
executing tests.

## Inputs and outputs

Accept requirement context, an optionally explicitly supplied or already
established `prd.md` and `technical-design.md`, text and office files, PDFs,
images, API documents, issues or tasks, current project code, historical
defects, and multiple related materials.

Create only:

```text
docs/wewo/<requirement-category>/<requirement-slug>/test-plan.md
docs/wewo/<requirement-category>/<requirement-slug>/test-cases.md
```

Keep filenames and path segments in English. Conduct user interaction and
write both documents in an explicitly requested language, otherwise the
dominant interaction language, and otherwise Chinese.

## Mandatory workflow

### 1. Resolve the requirement workspace

Run independently. Use `prd.md` and `technical-design.md` only when the user
explicitly supplies them, explicitly references them, or the current
conversation already establishes them. Never require them, create empty
replacements, scan for them, or block because another capability has not run.

Resolve exactly one workspace before creating documents:

1. Use an explicit workspace supplied by the user.
2. Otherwise reuse the workspace established for this requirement.
3. Otherwise infer a candidate from the requirement, issue, branch, or
   explicitly supplied or referenced material.
4. Ask before writing if multiple workspaces are plausible.

Never infer a workspace from the existence of workflow artifacts. Never select
a workspace because it was modified most recently. Use `features`, `bugs`,
`refactors`, or `maintenance`; default to `features` only when no evidence
favors another category. Use a concise lowercase English kebab-case slug.
Create parent directories only after resolution is unambiguous, and never mix
different requirements without explicit confirmation.

### 2. Establish sufficient test context

Read and apply
[context-analysis.md](references/context-analysis.md).

Combine the user's current request with the requirement, design, and project
materials explicitly provided, referenced, or confirmed. Do not scan
`docs/wewo/` or the repository for historical documents. Do not treat one
source as the only truth. Surface critical conflicts and ask which expectation
governs. Inspect requirement, product, and design context needed to understand
test behavior: affected modules, public interfaces, roles, business rules, and
historical defects when available. Do not inspect concrete test tools, test
frameworks, test runners, browsers, or execution-environment readiness; those
belong to test execution.

Establish the minimum necessary context when usable artifacts are absent.
Do not fabricate pages, interfaces, roles, states, environments, data, or
business rules. Ask when an unresolved expected behavior materially changes
test design. If a source format cannot be read with current capabilities,
state the limitation and request an accessible export or pasted content.

Clarify progressively rather than presenting a comprehensive questionnaire.
Discuss one test topic per round and normally ask one to three tightly related
questions. State the evidence, risk, recommendation, reason, and exact
confirmation needed. After each answer, re-evaluate resolved conditions, new
risks, remaining case-changing uncertainties, and readiness to generate.

### 3. Analyze risk and define scope

Read and apply
[risk-and-strategy.md](references/risk-and-strategy.md).

Identify the test object, in-scope behavior, regression scope, explicit
exclusions, business and quality risks, coverage conditions, test-data
assumptions, external dependencies, and blocking conditions. Cover relevant
normal, negative, boundary, authorization, security, consistency, concurrency,
migration, compatibility, performance, reliability, and regression risks.

Coverage conditions describe product scope only, such as required platforms,
required browser or device categories, roles, locales, and configurations.
Test-data assumptions include whether data may be created or deleted,
destructive-data constraints, and required state or setup assumptions. These
are design inputs, not execution-infrastructure discovery.

Select test-design methods that fit the rules, such as equivalence classes,
boundaries, decision tables, state transitions, scenarios, causal analysis,
permission matrices, combinations, concurrency analysis, risk-driven testing,
and historical-defect regression.

Prioritize by business risk rather than document order. Do not invent fixed
coverage targets, pass rates, environments, accounts, or test data.

### 4. Select the testing strategy and levels

Read and apply
[test-level-selection.md](references/test-level-selection.md).

Use abstract test-level labels only: Unit, Component, Integration, API,
Contract, E2E, Security Behavior, Migration/Data, Performance/Reliability, and
Manual. The skill does not inspect, select, configure, or reason about concrete
test tools, test runners, browser installations, or execution infrastructure,
unless the user explicitly requests a tool-specific test-design task.

For every risk or scenario, recommend the lowest-cost, fastest, most stable
level that provides direct and trustworthy evidence. Use complementary levels
only when each adds distinct evidence. Do not force every scenario through
unit, integration, API, and E2E, and never equate verification with browser
testing.

Define applicable black-box and white-box perspectives, unit and component
candidates, integration, API and contract coverage, E2E, security behavior,
data and migration, performance and reliability, regression, and manual
testing.

### 5. Classify the recommended and required evidence levels

Classify each scenario using:

- **Recommended Test Level**: advisory guidance for later verification.
- **Required Evidence Level**: the minimum evidence level considered sufficient
  to verify the scenario (a specific level, or "X or higher"). It defines only
  the evidence requirement; it does not define who executes it, which capability
  consumes it, or which concrete tool executes it.

Recommended Test Level and Required Evidence Level may both be, for example,
E2E, without deciding whether or how the scenario will be automated. A Manual
Required Evidence Level is appropriate for scenarios requiring subjective
human judgment, such as visual or UX quality.

### 6. Design traceable test cases

Read and apply
[test-case-quality.md](references/test-case-quality.md).

Design cases only after requirement analysis, risk analysis, and strategy
selection. Each case must state the confirmed expected business behavior
separately from the adjustable execution method. Where useful, distinguish the
Recommended Test Level from the Required Evidence Level. Set a Required
Evidence Level only where business risk or observable behavior requires it; do
not require E2E for every scenario. Use stable case IDs and trace requirements
and risks to cases.

Do not mechanically convert each requirement sentence into a case. Do not
require a one-to-one mapping between a documented case and a future test
function; later verification may split, merge, parameterize, or change the test
level without changing the confirmed business expectation.

### 7. Review and confirm the design

Perform the internal case review defined in `test-case-quality.md`. Revise
duplicates, coverage gaps, unreasonable levels, weak expectations, unsupported
assumptions, and poor evidence-level classifications before presenting the
design.

Do not generate final documents while any condition holds:

- the basic test object is unclear;
- core business rules conflict;
- a key expected result is unknown;
- result-changing roles or permissions are unconfirmed;
- test or regression scope is unclear;
- a critical coverage condition or test-data assumption changes the cases but
  is unknown;
- source materials contain an unresolved critical conflict;
- the user has not confirmed the final test design;
- the workspace is ambiguous.

Summarize the test object, scope, top risks, selected levels, coverage
conditions and test-data assumptions, and unresolved questions. Ask the user to
correct or explicitly confirm the design. Generate nothing before confirmation.

### 8. Generate the two confirmed documents

Before writing, read
[document-contract.md](references/document-contract.md) and use
[test-plan-template.md](assets/test-plan-template.md) and
[test-cases-template.md](assets/test-cases-template.md). Include the
Recommended Test Level and, where required, the Required Evidence Level for
each case. Localize headings and prose while preserving the fixed English
filenames.

Write only to:

```text
docs/wewo/<requirement-category>/<requirement-slug>/test-plan.md
docs/wewo/<requirement-category>/<requirement-slug>/test-cases.md
```

If either file exists, treat an explicit update request as authorization;
otherwise ask before replacing it. Include the internal review result in
`test-cases.md`. Derive all overview counts from the cases actually
documented.

Keep a Manual Test List only as an index of scenarios whose Required Evidence
Level is Manual.

Do not write executable test code under `docs/wewo/...` or elsewhere. Do not
modify production code or databases, start the project, run a test suite,
create execution evidence, record actual results, assign Passed or Failed, or
generate review reports.

After both files are successfully written and verified, report:

- both exact paths;
- test scope and primary risks;
- the actual count of cases by Recommended Test Level;
- the actual count of cases with a Manual Required Evidence Level;
- blockers and unresolved questions.

Do not automatically continue into implementation, executable-test creation,
test execution, triage, manual-test tracking, gates, or code review. Claim only
the document-generation work that was actually completed.
