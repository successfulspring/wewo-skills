# Automation Branches

Apply one evidence-preserving process across the project's actual frameworks.

## Common process

For every automatable scenario:

1. confirm observable behavior and expected result;
2. choose the level and test seam;
3. find related existing tests, fixtures, and helpers;
4. add the smallest maintainable missing asset;
5. prepare controlled environment and isolated data;
6. run the focused test;
7. preserve first-failure evidence;
8. repair test-code defects without changing expectations;
9. run the target set and relevant regression;
10. capture command, exit status, output, artifacts, and cleanup result;
11. update the matrix.

## Unit and component

Use the repository's runner. Prefer public behavior, focused assertions,
deterministic inputs, isolated state, and existing rendering or component
harnesses. Avoid tests coupled to private implementation and mocks that bypass
the behavior under test.

## Integration

Use real persistence, transactions, caches, messages, filesystems, or adapters
when those boundaries carry the risk. Verify rollback, partial failure,
idempotency, cleanup, and isolation. Do not replace material collaboration
evidence with mocks.

## API and contract

Use the project's API framework. Verify authentication, authorization,
parameters, status and error codes, schema, idempotency, server-side
validation, and compatibility. For contracts, validate only authoritative
schemas and protocols; do not infer undocumented business behavior.

## Database and migration

Use a disposable or explicitly approved database. Verify forward migration,
historical data, defaults, backfills, constraints, indexes, compatibility, and
rollback where supported. Never run migration tests against production by
default.

## Security behavior

Execute only feature-related, controlled, non-destructive checks. Verify
unauthenticated and cross-user behavior, resource permissions, invalid input,
file restrictions, expired tokens, replay, duplicate requests, state
transitions, and server-side enforcement where applicable.

## Performance and reliability

Run only when required or risk-justified. Define the target, environment,
dataset, load shape, duration, and stop conditions. Keep exploratory
concurrency bounded. Formal pressure testing requires explicit authorization
and an isolated environment.

## Test assets

Permitted assets include unit, component, integration, API, contract, E2E,
fixtures, mocks, page objects, helpers, data builders, and reporter
configuration. Keep them in normal project test paths.

Do not change production code. When a production seam is needed, document a
Testability Change Request rather than implementing it.
