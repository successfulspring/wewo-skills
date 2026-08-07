# Test Design Document Contract

Read this guide only after the user confirms the final test design.

## Contents

- [Test plan structure](#test-plan-structure)
- [Test plan section contract](#test-plan-section-contract)
- [Test cases structure](#test-cases-structure)
- [Test case document contract](#test-case-document-contract)
- [Final quality gate](#final-quality-gate)

## Test plan structure

Use every core section in this order:

1. Test Overview
2. Test Basis
3. Test Object and Requirement Understanding
4. Test Scope
5. Quality Risk Analysis
6. Test Strategy
7. Test Design Methods
8. TDD Collaboration Strategy
9. Automation Strategy
10. Test Environment
11. Test Data Strategy
12. Test Priority
13. Test Entry Conditions
14. Test Exit Conditions
15. Test Deliverables
16. Blockers and Unresolved Questions

Localize headings and content. Keep `03-test-plan.md` in English.

## Test plan section contract

- State the test object, goals, core quality concern, and whether code already
  exists.
- List only actual requirement, design, project, and confirmed-dialogue
  sources.
- Separate current scope, regression scope, and out-of-scope behavior.
- Use a risk table with ID, description, impact, level, and test response.
- Assign each applicable test level a clear responsibility.
- Identify selected design methods and the rules they cover.
- Separate unit TDD inputs, integration-oriented inputs, and scenarios outside
  the primary TDD loop.
- Summarize automation by type, recommendation, execution stage, and method.
- Describe only verified environment and data capabilities; mark unknowns.
- Derive entry and exit conditions from the project without inventing fixed
  coverage or pass-rate targets.

Add only relevant strategy subsections for unit, component, integration, API,
frontend, E2E, authorization/security, performance/reliability, manual,
regression, compatibility, files, external systems, or data migration.

## Test cases structure

Use every core section in this order:

1. Document Notes
2. Test Case Overview
3. Requirement Coverage
4. Detailed Test Cases
5. TDD Case List
6. E2E Automation Candidate List
7. Manual Test List
8. Case Review Result
9. Unresolved Questions and Blockers

Localize headings and content. Keep `04-test-cases.md` in English.

## Test case document contract

Group detailed cases only by relevant normal flow, rules/state, negative,
boundary, authorization/security, consistency, API, frontend, integration,
E2E, regression, performance, compatibility, or exploratory areas.

Use the reusable case template. Record the Recommended Test Level and, where
business risk or observable behavior requires it, the Required Evidence Level
for each case. Build the overview counts from the actual documented cases:

```markdown
| Test level | Total | P0 | P1 | P2 | TDD inputs | Automation candidates |
|---|---:|---:|---:|---:|---:|---:|
```

Map requirement IDs when they exist, otherwise concise business rules:

```markdown
| Requirement or rule | Test cases | Coverage |
|---|---|---|
```

Summarize TDD cases:

```markdown
| Case ID | Case title | Test level | Business capability driven |
|---|---|---|---|
```

Summarize E2E candidates:

```markdown
| Case ID | User flow | Automation judgment | Blocker |
|---|---|---|---|
```

Summarize cases better suited to manual work or currently unstable for
automation. Include the internal review result and remaining gaps.

## Final quality gate

Before writing both documents, verify:

- the user confirmed the test design;
- content matches actual requirements, design, code, and test foundation;
- no page, interface, role, state, environment, account, or data is invented;
- unknown rules are not presented as expected behavior;
- steps are specific and expectations judgeable;
- priority follows risk;
- selected levels are economical and trustworthy;
- E2E is limited to useful end-to-end evidence;
- TDD and automation classifications are explicit and realistic;
- normal, negative, boundary, high-risk, security, consistency, and regression
  coverage is appropriate;
- actual counts match the documented cases;
- the internal review is complete;
- neither document contains execution results or claims;
- no executable test or production implementation is produced.
