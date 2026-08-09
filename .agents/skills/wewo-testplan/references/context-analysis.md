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
details that change the plan, such as covered roles, coverage conditions
(required platforms, browsers, or devices as part of the requirement), whether
test data may be created or deleted, mockability of external dependencies,
captcha or external login, regression boundaries, destructive-test permission,
and priority risks. Do not ask about test-environment readiness or installed
tooling; those belong to test execution.

If the expected behavior is too vague to judge results, clarify it instead of
creating speculative cases. Request additional requirement clarification or
requirement context only when the user wants a complete rediscovery; never
make another capability a prerequisite.

## Clarify in focused rounds

Discuss one test topic per round and normally ask one to three tightly related
questions. Select from scope, business risk, roles and permissions, coverage
conditions and test-data assumptions, external services and mocks, regression,
and verification method and evidence requirements according to current need.

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
- `prd.md` and `technical-design.md` when explicitly supplied or already
  established in the current conversation;
- Markdown, TXT, office documents, PDFs, images, prototypes, and diagrams;
- API documentation, issues, tasks, changes, and defects;
- current project code;
- historical defects;
- multiple related sources.

Do not assume one file is the only truth. Preserve provenance, distinguish
confirmed expectations from proposals, and surface conflicts for user
resolution.

## Understand product and design context

Inspect only what is needed to understand test behavior:

- affected modules and public interfaces;
- roles, business rules, and state transitions;
- existing product behavior and its observable outcomes;
- related historical defects and regression concerns.

Do not inspect concrete test tools, test frameworks, test runners, browser
installations, test directories, fixtures, test databases, or CI test stages
to decide how tests will be executed; those belong to test execution. Do not
invent infrastructure, accounts, data, interfaces, or test seams.

## Coverage conditions and test-data assumptions

Record product-scope coverage conditions and test-data assumptions as design
inputs:

- required platforms, browsers, or device categories when they are part of the
  requirement;
- roles, locales, and configurations that affect expected behavior;
- whether test data may be created or deleted;
- destructive-data constraints;
- required state or setup assumptions.

These are design inputs, not execution-infrastructure discovery.

## Separate expectations from execution choices

Treat confirmed business behavior as stable. Treat test level, method, and
evidence-level recommendations as adjustable engineering guidance. Ask the
user when business behavior, permissions, state transitions, failure outcomes,
or scope is unresolved. The skill does not decide which concrete tool executes
a scenario.
