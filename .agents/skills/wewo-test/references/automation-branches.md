# Repository-Native Automation Branches

Apply one evidence-preserving execution sequence across the project's actual
frameworks.

## Common execution sequence

For each automated scenario:

1. verify expected behavior and Oracle;
2. resolve Route and Runner from the Automation annotation and repository;
3. discover useful available Agent Tool Interfaces without changing the Runner;
4. locate related existing tests, fixtures, and helpers;
5. create or modify the smallest durable missing asset;
6. prepare a controlled environment and isolated data;
7. execute the focused test through the repository-native Runner;
8. preserve first-failure evidence;
9. diagnose runner discovery, loading, startup, or execution failure before
   fallback;
10. triage Product, Test, Data, Environment, Existing, Flaky, Requirement, or
   Unverified causes;
11. repair only permitted test, configuration, fixture, locator, or data
    defects without weakening the Oracle;
12. rerun the focused test;
13. execute the relevant target set;
14. execute necessary affected regression;
15. collect native evidence and sanitize it;
16. clean up data and temporary resources;
17. assign the final status and update the execution record.

Do not run the full repository suite automatically when focused and affected
regression scopes provide sufficient evidence. Do not skip a necessary
regression merely to save time.

## Unit and component

Use the repository's runner and harness. Prefer public behavior, deterministic
inputs, isolated state, focused assertions, and existing rendering conventions.
Avoid unnecessary coupling to private implementation and mocks that bypass the
behavior under test.

## Integration, persistence, and services

Use real persistence, transactions, caches, messages, filesystems, adapters,
or test services when those boundaries carry the risk. Verify rollback,
partial failure, idempotency, cleanup, and isolation where required. Do not
replace material collaboration evidence with lower-fidelity mocks.

## API and contract

Use the project's established API or contract stack. Preserve public
authentication, authorization, parameters, status/error semantics, schemas,
idempotency, server-side validation, compatibility, and authoritative protocol
evidence. Do not infer undocumented business behavior.

## Browser

Use the durable browser branch in `playwright-e2e.md`. Browser exploration may
assist construction and debugging but cannot replace a repository test asset
executed by the project runner.

## Database and migration

Use a disposable or explicitly approved database. Verify forward migration,
historical data, defaults, backfills, constraints, indexes, compatibility, and
rollback where supported. Never test migrations against production by default.

## Security behavior

Run only controlled, non-destructive checks within the verification scope.
Cover relevant unauthenticated and cross-user behavior, resource permissions,
invalid input, file restrictions, expired tokens, replay, duplicate requests,
state transitions, and server-side enforcement.

## Performance and reliability

Run only when explicitly required or materially risk-justified. Define target,
environment, dataset, load shape, duration, thresholds from authoritative
requirements, and stop conditions. Formal pressure testing requires explicit
authorization and an isolated environment.

## Durable assets and production boundary

Keep unit, component, integration, API, contract, browser, performance,
fixtures, mocks, page objects, helpers, data builders, and approved test-only
configuration in normal project paths.

Do not change production code. When a production seam is required, document a
Testability Change Request instead of implementing it.
