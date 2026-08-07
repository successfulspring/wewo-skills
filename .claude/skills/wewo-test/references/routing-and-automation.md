# Test Routing and Automation Feasibility

Choose the lowest-cost, fastest, most stable level that gives direct evidence.

## Routing guide

- Unit: pure functions, business rules, state decisions, transformations,
  boundaries, isolated errors, and algorithms.
- Component: conditional rendering, validation, controls, dialogs, messages,
  and local UI state.
- Integration: service/repository behavior, real persistence, transactions,
  caches, messages, filesystems, and adapters.
- API: HTTP behavior, parameters, schema, errors, authentication,
  resource-level authorization, idempotency, server validation, compatibility.
- Contract: OpenAPI, frontend/backend fields, service protocols, messages,
  serialization, and third-party adapter contracts.
- Web E2E: critical user journeys, browser behavior, cross-page flows, and
  observable end-to-end outcomes.
- Database/migration: schema changes, historical compatibility, defaults,
  backfills, constraints, indexes, upgrade, rollback, and transformations.
- Security behavior: unauthenticated and unauthorized access, invalid input,
  file restrictions, expired tokens, replay, cross-user access, server-side
  enforcement, and state-machine bypass.
- Performance/reliability: response targets, bounded concurrency, retries,
  duplicate submission, timeout, data volume, long tasks, and leaks when a
  requirement or material risk justifies them.
- Manual: visual quality, usability, wording, real devices or hardware, real
  communications or payments, captcha, uncontrollable pages, subjective
  judgment, unsafe automation, or poor long-term value.

Formal load or stress testing requires an isolated environment, explicit
targets and data capacity, and user authorization.

## Automation statuses

- `Direct Automation`: stable seam and existing support.
- `Automation with Setup`: small fixture, account, or data preparation needed.
- `Change Test Level`: another level gives better evidence.
- `Infrastructure Required`: persistent framework or service required.
- `Blocked`: environment or dependency prevents execution.
- `Manual Preferred`: manual evidence is safer or more valuable.
- `Not Applicable`: confirmed scenario no longer applies.
- `Needs Clarification`: expected behavior is unresolved.

Evaluate interface stability, existing frameworks, repeatable data, isolation,
cleanup, accounts, captcha, payments, messages, external systems, destructive
effects, execution frequency, business risk, stability, and maintenance cost.

## Required evidence handling

For every P0/P1 scenario, honor the documented Required Evidence Level when
present. A required E2E level must be executed (`Passed` or `Failed`) or
explicitly classified `Blocked` with a concrete blocker or `Not Run` with a
justified reason; it cannot be silently replaced with unit, component,
integration, or API evidence. When E2E is only recommended, another level is
allowed when it provides equivalent direct evidence; record the routing
reason.

## Implementation order

1. Execute and inspect relevant existing tests.
2. Add missing scenarios to an existing framework.
3. If the test type has no framework, decide whether persistent adoption is
   justified.
4. Prefer isolated temporary execution for one-time validation.
5. Obtain confirmation before large infrastructure changes.

Do not replace pytest, Jest, Vitest, Cypress, Playwright, REST Assured, Newman,
or another established stack merely for consistency.
