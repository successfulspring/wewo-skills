# TDD and Automation Classification

Classify scenarios without assuming that every designed case is immediately
executable.

## TDD candidates

Prefer TDD when behavior is observable, expected outcomes are stable, testing
seams are accessible, dependencies are manageable, and the test provides value
during implementation.

Strong unit-level candidates include business rules, validation, state and
permission decisions, transformations, boundaries, exception handling,
duplicate-operation rules, and isolated module behavior.

Integration-oriented implementation inputs include service-repository
collaboration, database behavior, API-service integration, transactions,
multiple modules, cache, messaging, filesystem, and external adapters.

Do not put complete E2E journeys, browser compatibility, visual appearance,
animation, subjective usability, uncontrolled third-party pages, real SMS,
captcha, or hardware into the primary Red-Green-Refactor loop.

Mark non-TDD scenarios for later integration, E2E, manual, or
post-implementation testing.

## Automation feasibility

Evaluate:

- interface and selector stability;
- repeatable data setup and cleanup;
- environment control;
- test isolation;
- controllability of external dependencies;
- captcha, real-device, hardware, or human-judgment needs;
- destructive or irreversible side effects;
- expected execution frequency;
- maintenance cost;
- business risk and evidence value.

Use statuses such as:

- suitable for automation;
- not currently suitable;
- manual testing required;
- blocked by environment or data;
- pending confirmation.

Recommend the existing project framework when verified. Do not introduce a
tool merely to make the plan look complete.

## Web E2E automation judgment

Judge browser-level E2E automation with abstract criteria, not concrete tools.
Recommend Web E2E only when a stable page and user path exist, elements are
locatable, outcomes are observable, data is repeatable, production data is not
at risk, and uncontrolled authentication or hardware is absent.

Record one of:

- suitable for Web E2E automation;
- not currently suitable for Web E2E automation;
- manual testing required;
- blocked by environment or data.

Do not inspect, select, or install concrete browser automation tools
(Playwright, Cypress, Selenium, or similar); do not inspect browser
availability; do not ask whether browsers or test runners should be installed.
Concrete tooling selection, installation, script generation, and execution
belong to the test-execution stage. Leave final executable automation to that
stage.

## Execution-stage classification

For each case, distinguish:

- expected business behavior;
- recommended test level and method;
- TDD candidacy during implementation;
- later automation candidacy;
- manual candidacy;
- dependencies and blockers.

The expected behavior changes only through requirement confirmation. Future
stages may change execution method, split, merge, or parameterize cases.
