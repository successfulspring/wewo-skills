# Implementation Planning and Vertical Slicing

Create the plan before production-code modification.

## Determine the implementation verification strategy

Derive implementation behaviors from the confirmed requirement, technical
design when available, and actual code and architecture. For each relevant
behavior, determine where useful:

- the observable behavior;
- the verification seam;
- whether TDD is appropriate;
- the implementation-time verification level;
- the reason.

Classify each verification approach as:

- adopt directly;
- change test level;
- split;
- merge;
- outside implementation verification scope, including browser-level
  acceptance;
- do not adopt;
- blocked by environment;
- pending confirmation.

Focus on inputs, caller behavior, and observable result rather than proposed
classes, methods, mock style, or internal structure. The verification strategy
is derived from implementation behavior, not from QA test-case documents.

When no formal design document exists, extract the minimum implementation
behaviors from confirmed requirements, code, and existing tests. Summarize
them for confirmation without generating a full test plan.

## Select test seams

Prefer stable public boundaries already used by the project:

- domain object public behavior;
- application service;
- HTTP API;
- repository plus test database;
- message consumer;
- command-line entry;
- public frontend component behavior.

Avoid private methods, internal call order, internal call counts, and extensive
mocks that freeze implementation. Ask only when multiple viable seams
materially change the solution.

## Slice by observable capability

Create vertical slices rather than separate model, service, controller, and
test phases. Each slice must include:

- business goal;
- observable result;
- linked requirement or behavior;
- primary test seam and level;
- expected file or module scope;
- implementation constraints;
- verification commands;
- completion conditions;
- dependencies on other slices.

Keep each slice small enough for independent testing and quality checking.

## Plan required changes and risks

Identify:

- affected and unaffected files or modules;
- interface, database, migration, and configuration changes;
- compatibility and historical-data concerns;
- dependency and tool changes;
- security and authorization controls;
- transaction, concurrency, idempotency, and failure handling;
- concrete build, test, type, lint, format, and migration commands;
- blockers and unresolved decisions.

Never invent commands or files.

## Confirmation gate

Summarize the objective, sources, project analysis, scope, global constraints,
TDD evaluation, seams, slices, structural changes, verification, risks, and
open questions. Obtain confirmation before code changes unless the user
explicitly requested direct execution and the goal is already clear; even
then, retain the written plan as the execution basis.
