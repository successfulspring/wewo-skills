# Adaptive Engineering Design Coverage

Cover every relevant engineering dimension and omit irrelevant or ceremonial
content. This model supports different requirement shapes without forcing a
fixed architecture style or document structure.

## Frontend concerns

When relevant, cover page and component responsibilities, interaction and data
flow, state ownership and lifecycle, validation, API boundaries,
loading/success/failure/empty behavior, authorization presentation, browser
storage, compatibility, reuse, and project structure.

Do not create backend, database, or ER-diagram design for a frontend-only
change unless an actual cross-boundary impact exists.

## Backend concerns

When relevant, cover module and use-case responsibilities, domain behavior,
interfaces, authentication and authorization, validation, errors, transactions,
concurrency, idempotency, auditing, integrations, lifecycle, dependencies, and
responsibility boundaries.

## Data and state concerns

When relevant, cover entities, fields, relationships, keys and constraints,
indexes, nullability and defaults, state transitions, ownership, audit fields,
retention and deletion, migration, historical data, and reconciliation.

Include a Mermaid ER diagram only when database entities or relationships
change. Never create a separate ERD artifact.

## Integration and asynchronous concerns

When relevant, cover external contracts, trust boundaries, authentication,
timeouts, retry and duplicate safety, degradation, resource lifecycle,
background jobs, queue behavior, accumulation, poison work, correlation,
observability, and user-visible failure.

## Stateful workflow concerns

When relevant, cover legal states and transitions, actor permissions,
transaction ownership, concurrency conflict behavior, idempotency, side
effects, partial success, compensation, recovery, and audit evidence.

## Migration, refactor, and compatibility concerns

When an existing system evolves materially, cover affected historical data and
clients, compatibility during rollout, backfill, reconciliation, rollout and
rollback, irreversible changes, dependency direction, and preservation or
deliberate replacement of existing boundaries. Use expand/contract or
temporary dual behavior only when justified.

## Cross-cutting risk and operational concerns

Apply relevant Security, Correctness and Consistency, Architecture and
Maintainability, and Reliability and Resource Safety controls inside the
affected design areas. Define material engineering invariants and useful
Verification Seams. Add observability only where a material workflow,
integration, asynchronous process, or failure boundary needs diagnosis.

## Adaptive coverage rule

The Engineering Impact Map and Decision Map determine coverage. Relevant
dimensions must be addressed. Related dimensions may be combined. Irrelevant
dimensions must not create empty sections, speculative components, or
fashion-driven architecture.

Use Mermaid flow, architecture, sequence, state, or ER diagrams only when they
materially improve understanding. Provide an equivalent textual description
when diagram support is unavailable.
