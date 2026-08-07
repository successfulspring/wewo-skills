# Code Review Dimensions

Apply repository rules before generic best practices. Report only issues tied
to the actual Diff or its affected context.

## Requirement and design compliance

Check:

- complete versus partial behavior;
- missing state, error, and permission branches;
- scope creep or changed observable outcomes;
- design and explicit constraint violations;
- requirement-to-code evidence;
- requirement-to-test evidence.

When requirements are absent, do not reconstruct them from code. State that
business completeness is not confirmable and continue the other dimensions.

## Repository standards and structure

Check:

- explicit repository instructions and architecture boundaries;
- reuse versus duplicated capability;
- unnecessary abstraction or mixed responsibilities;
- unjustified singleton, global, or shared mutable state;
- request or user state retained in shared objects;
- hardcoded configuration;
- unrelated modifications;
- consistency with existing exception, dependency, and lifecycle patterns.

Do not admit personal style preference as a defect.

## Correctness and test quality

Check:

- logic, nulls, boundaries, and state transitions;
- exception paths, recovery, resource cleanup, and partial failure;
- data transformation and precision;
- public or externally observable assertions;
- weak assertions and false-positive tests;
- over-mocking and tests coupled to private details;
- missing high-risk behavior and regression tests;
- test ordering, isolation, and deterministic setup.

Distinguish test existence from test effectiveness. Never infer a passing
result from source inspection.

## Impact and compatibility

Check:

- API and caller compatibility;
- database schema, data, migration, and rollback compatibility;
- configuration and default changes;
- serialization and protocol changes;
- cache and message compatibility;
- lifecycle and shared-state effects;
- historical data handling;
- downstream consumers;
- regression scope.

Trace both direct and indirect consumers when a public contract changes.
