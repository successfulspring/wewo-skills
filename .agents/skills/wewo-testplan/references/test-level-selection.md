# Test Level Selection

Choose the lowest-cost, fastest, most stable level that directly proves the
behavior. Add a complementary level only when it supplies different evidence.

## Perspectives

- Use black-box design for externally observable behavior, contracts, and
  business outcomes without depending on internals.
- Use white-box design when verified implementation structure exposes
  meaningful branches, seams, state, error paths, or collaboration boundaries.

Use both perspectives when they cover different risks.

## Candidate levels and types

### Unit

Prefer for isolated business rules, validation, state decisions, permission
logic, transformations, boundaries, exceptions, duplicate-operation rules, and
independent module behavior.

### Component

Prefer for a UI component or bounded service component with controlled
dependencies and meaningful behavior above a single unit.

### Integration

Prefer for service-repository collaboration, database behavior, transactions,
multiple modules, cache, messaging, filesystem, or external-service adapters.

### API and contract

Prefer API testing for request validation, authorization, response behavior,
and endpoint semantics. Use contract testing when compatibility between
producers, consumers, or external integrations is the direct risk.

### E2E

Use for a small number of critical complete user journeys when the UI,
environment, selectors, data, and outcome are stable enough. Do not duplicate
every lower-level rule in E2E.

### Security behavior

Design observable tests for authentication, authorization, ownership, input
handling, sensitive-data exposure, business-rule bypass, and abuse controls.
This is test design, not code review or an executed security scan.

### Data and migration

Use for schema changes, transformations, backfills, constraints, old data,
retention, rollback, and compatibility.

### Performance and reliability

Use when latency, throughput, capacity, concurrency, retry, failover,
stability, recovery, or resource behavior matters. Do not invent thresholds;
record missing targets for confirmation.

### Regression

Select existing behavior plausibly affected by the change, shared capability,
schema, interface, or historical defect.

### Manual

Use for visual quality, subjective usability, exploratory work, unstable or
uncontrolled third parties, real-device behavior, hardware, captcha, and
experiences that automation cannot judge reliably.

## Complementary evidence

For a rule spanning layers, use a focused combination, such as unit evidence
for state rules, integration evidence for transaction consistency, and one E2E
case for the critical user journey. Explain why each level is necessary.
