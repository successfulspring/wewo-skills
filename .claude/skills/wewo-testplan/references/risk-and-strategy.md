# Risk-Based Test Strategy

Use this guide to identify coverage and produce the test-plan strategy.

## Risk categories

Select only applicable risks.

### Normal behavior

Cover core user paths, primary functional outcomes, valid state transitions,
and normal data processing.

### Negative and boundary behavior

Cover empty, invalid, minimum, maximum, out-of-range, missing, changed-state,
interrupted, and dependency-failure conditions.

### Authorization and security behavior

Cover unauthenticated use, roles, resource ownership, horizontal and vertical
privilege escalation, sensitive data, input validation, upload and download,
business-rule bypass, and bulk operations.

### Reliability and business correctness

Cover duplicates, concurrency, idempotency, transactions, partial success,
state conflicts, retries, duplicate messages, cache inconsistency, and
repeated scheduled work.

### Regression

Cover affected pages, interfaces, shared modules, state flows, schemas,
compatibility, old clients, old data, and related historical defects.

## Test-design methods

Apply methods intentionally:

- equivalence classes for representative valid and invalid groups;
- boundary analysis for numeric, size, count, and time limits;
- decision tables for interacting rules;
- state transitions for lifecycle behavior;
- scenarios for complete user or system flows;
- causal analysis for inputs, events, and outcomes;
- error guessing informed by project history;
- permission matrices for roles and resource ownership;
- data combinations or pairwise coverage where combinations matter;
- concurrency and idempotency analysis for state-changing operations;
- risk-driven testing for impact and likelihood;
- historical-defect regression for known failure patterns.

State which methods are used and where.

## Scope and priority

Define current scope, regression scope, and explicit exclusions. Prioritize:

- P0 for core flow, authorization, money, inventory, critical consistency,
  release blockers, and severe security risk;
- P1 for major exceptions, important boundaries, frequent actions, important
  regression, and high business impact;
- P2 for low-frequency behavior, ordinary compatibility, non-core experience,
  and issues that do not block the main flow.

Use actual risk rather than generation order. Record risk-to-test responses in
the plan.

## Environment and data strategy

Identify required services, accounts, roles, browsers or devices, databases,
external dependencies, mocks, data setup, isolation, cleanup, and destructive
side effects. Mark unknown facts as pending confirmation.

Define entry and exit conditions from the actual project and requirement. Do
not invent fixed coverage percentages, pass rates, environments, or data.
