# Context Analysis

Use this guide before risk analysis or case design.

## Determine sufficiency

Establish at least:

- the test object;
- core users or roles;
- core business flow;
- key business rules;
- permitted and prohibited states;
- main exceptions and boundaries;
- current and regression scope;
- expected business outcomes.

Proceed directly when the information is sufficient. Ask only for missing
details that change the plan, such as covered roles, test environment,
data-creation and cleanup permission, mockability, captcha or external login,
browser or device support, regression boundaries, test database availability,
destructive-test permission, and priority risks.

If the expected behavior is too vague to judge results, clarify it instead of
creating speculative cases. Suggest product clarification only when the user
wants a complete rediscovery; never make another skill a prerequisite.

## Clarify in focused rounds

Discuss one test topic per round and normally ask one to three tightly related
questions. Select from scope, business risk, roles and permissions,
environment, data, external services and mocks, browsers or devices,
regression, automation conditions, and TDD scope according to current need.

For each material question:

- state what the current material establishes;
- identify the test risk;
- recommend a testing approach;
- explain why it is appropriate;
- ask the user to confirm the missing condition or expectation.

After every answer, re-evaluate which conditions are settled, which new risks
emerged, which uncertainties still change cases, and whether final generation
is ready. Do not present a long fixed questionnaire.

## Combine available material

Use relevant:

- user instructions and conversation context;
- requirement and design documents;
- `01-prd.md` and `02-technical-design.md` when present;
- Markdown, TXT, office documents, PDFs, images, prototypes, and diagrams;
- API documentation, issues, tasks, changes, and defects;
- current project code;
- existing plans, cases, historical defects, and automated tests;
- multiple related sources.

Do not assume one file is the only truth. Preserve provenance, distinguish
confirmed expectations from proposals, and surface conflicts for user
resolution.

## Inspect the project's test foundation

Inspect only relevant project areas:

- affected modules and public interfaces;
- existing test frameworks and configuration;
- test directory and naming conventions;
- existing unit, component, integration, API, contract, and E2E tests;
- fixtures, factories, mocks, stubs, helpers, and test data;
- test databases, containers, services, and environment configuration;
- authentication helpers and reusable user roles;
- existing CI test stages when they inform feasibility;
- related historical defects and regression tests.

Do not invent infrastructure, accounts, data, interfaces, or test seams. Reuse
verified project capabilities in recommendations.

## Separate expectations from execution choices

Treat confirmed business behavior as stable. Treat test level, framework,
automation, fixtures, parameterization, and execution timing as adjustable
engineering recommendations.

Ask the user when business behavior, permissions, state transitions, failure
outcomes, or scope is unresolved. Recommend execution methods based on verified
project facts without turning them into business requirements.
