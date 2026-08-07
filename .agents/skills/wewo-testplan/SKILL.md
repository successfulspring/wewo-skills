---
name: wewo-testplan
description: Design a risk-based test strategy and detailed, traceable test cases before or alongside implementation, including appropriate test levels, data and environment needs, regression scope, TDD candidates, automation candidates, and manual coverage. Use when a user asks what and how a feature, bug, refactor, or maintenance change should be tested. Do not use to implement code, generate final executable tests, execute tests, record Passed or Failed results, create execution evidence, or perform code review.
---

# Wewo Test Plan

Define what must be tested and the expected evidence without implementing or
executing tests.

## Inputs and outputs

Accept conversation context, requirement or design documents, `01-prd.md`,
`02-technical-design.md`, text and office files, PDFs, images, API documents,
issues or tasks, current project code, existing plans or cases, historical
defects, existing automated tests, and multiple related materials.

Create only:

```text
docs/wewo/<requirement-category>/<requirement-slug>/03-test-plan.md
docs/wewo/<requirement-category>/<requirement-slug>/04-test-cases.md
```

Keep filenames and path segments in English. Conduct user interaction and
write both documents in an explicitly requested language, otherwise the
dominant interaction language, and otherwise Chinese.

## Mandatory workflow

### 1. Resolve the requirement workspace

Run independently. Use `01-prd.md` and `02-technical-design.md` only when the
user explicitly selects them: an explicitly provided workspace, an explicit
reference, or an explicit request to continue an existing requirement. Never
require them, create empty replacements, scan for them, or block because
another skill has not run.

Resolve exactly one workspace before creating documents:

1. Use an explicit workspace supplied by the user.
2. Otherwise reuse the workspace established for this requirement.
3. Otherwise infer a candidate from the requirement, issue, branch, or
   available upstream documents.
4. Ask before writing if multiple workspaces are plausible.

Never select a workspace because it was modified most recently. Use
`features`, `bugs`, `refactors`, or `maintenance`; default to `features` only
when no evidence favors another category. Use a concise lowercase English
kebab-case slug. Create parent directories only after resolution is
unambiguous, and never mix different requirements without explicit
confirmation.

### 2. Establish sufficient test context

Read and apply
[context-analysis.md](references/context-analysis.md).

Combine the user's current request with the requirement, design, project, and
test materials explicitly provided, referenced, or confirmed. Do not scan
`docs/wewo/` or the repository for historical documents; a discovered
candidate requires explicit user confirmation. Do not treat one source as the
only truth. Surface critical conflicts and ask which expectation governs. Inspect relevant repository structure, public interfaces,
affected modules, test frameworks, existing tests, reusable fixtures, and
historical defects when available.

Establish the minimum necessary context when upstream documents are absent.
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
exclusions, business and quality risks, test-data needs, environment needs,
external dependencies, and blocking conditions. Cover relevant normal,
negative, boundary, authorization, security, consistency, concurrency,
migration, compatibility, performance, reliability, and regression risks.

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
Manual. Do not inspect, select, or ask about concrete tools such as Playwright,
Cypress, Selenium, pytest, Jest, or Vitest; do not inspect browser availability
or ask about browser installation. Concrete tooling belongs to the
test-execution stage.

For every risk or scenario, recommend the lowest-cost, fastest, most stable
level that provides direct and trustworthy evidence. Use complementary levels
only when each adds distinct evidence. Do not force every scenario through
unit, integration, API, and E2E, and never equate automation with browser
testing.

Define applicable black-box and white-box perspectives, unit and component
candidates, integration, API and contract coverage, E2E, security behavior,
data and migration, performance and reliability, regression, and manual
testing. Reuse existing project test infrastructure rather than introducing
tools merely for the plan.

### 5. Classify TDD, automation, and manual candidates

Read and apply
[tdd-and-automation.md](references/tdd-and-automation.md).

Classify each scenario as appropriate for:

- TDD during implementation;
- post-implementation automation;
- manual execution;
- multiple complementary levels;
- blocked or pending confirmation.

Do not label every scenario as TDD or immediately executable. Base automation
recommendations on interface stability, repeatable data, environment control,
isolation, external dependencies, real-device or captcha needs, destructive
effects, execution frequency, maintenance cost, and business risk.

### 6. Design traceable test cases

Read and apply
[test-case-quality.md](references/test-case-quality.md).

Design cases only after requirement analysis, risk analysis, and strategy
selection. Each case must state the confirmed expected business behavior
separately from the adjustable execution method and automation recommendation.
Where useful, distinguish the Recommended Test Level from the Required
Evidence Level: the former is advisory, while the latter is the weakest
evidence later execution may substitute (a specific level or "X or higher").
Set a Required Evidence Level only where business risk or observable behavior
requires it; do not require E2E for every scenario. Use stable case IDs and
trace requirements and risks to cases.

Do not mechanically convert each requirement sentence into a case. Do not
require a one-to-one mapping between a documented case and a future test
function; later stages may split, merge, parameterize, or change the test level
without changing the confirmed business expectation.

### 7. Review and confirm the design

Perform the internal case review defined in `test-case-quality.md`. Revise
duplicates, coverage gaps, unreasonable levels, weak expectations, unsupported
assumptions, and poor TDD or automation classifications before presenting the
design.

Do not generate final documents while any condition holds:

- the basic test object is unclear;
- core business rules conflict;
- a key expected result is unknown;
- result-changing roles or permissions are unconfirmed;
- test or regression scope is unclear;
- a critical environment condition changes the cases but is unknown;
- source materials contain an unresolved critical conflict;
- the user has not confirmed the final test design;
- the workspace is ambiguous.

Summarize the test object, scope, top risks, selected levels, TDD scope, E2E
candidates, environment or data constraints, and unresolved questions. Ask
the user to correct or explicitly confirm the design. Generate nothing before
confirmation.

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
docs/wewo/<requirement-category>/<requirement-slug>/03-test-plan.md
docs/wewo/<requirement-category>/<requirement-slug>/04-test-cases.md
```

If either file exists, treat an explicit update request as authorization;
otherwise ask before replacing it. Include the internal review result in
`04-test-cases.md`. Derive all overview counts from the cases actually
documented.

Do not write executable test code under `docs/wewo/...` or elsewhere. Do not
modify production code or databases, start the project, run a test suite,
create execution evidence, record actual results, assign Passed or Failed, or
generate review reports.

After both files are successfully written and verified, report:

- both exact paths;
- test scope and primary risks;
- the actual count of documented TDD candidates;
- the actual count of documented E2E automation candidates;
- blockers and unresolved questions.

Do not automatically continue into implementation, executable-test creation,
test execution, triage, manual-test tracking, gates, or code review. Claim only
the document-generation work that was actually completed.
