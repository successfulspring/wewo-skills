# Design Coverage by Requirement Type

Choose only coverage relevant to the requirement.

## Frontend

Cover applicable page and component changes, interaction flow, state, form and
input validation, API calls, loading/success/failure/empty states,
authorization presentation, browser storage, responsive behavior,
compatibility, component reuse, and frontend project structure.

Do not invent backend, database, or ER-diagram content for a frontend-only
change.

## Backend

Cover applicable module responsibilities, business logic, APIs,
authentication and authorization, parameter validation, error handling,
transactions, concurrency, idempotency, logging and auditing, external
services, and code structure.

## Data

Cover applicable entities, fields, relationships, primary keys, unique
constraints, indexes, nullability, defaults, state and audit fields, migration,
historical data, deletion, retention, and an ER diagram.

Create an ER diagram only when database entities or relationships change.

## Full stack

Combine only the applicable frontend, backend, interface, data, security,
reliability, and implementation-constraint content. Explain responsibility
boundaries and data flow across layers.

## Cross-cutting mechanisms

Include only when relevant:

- state transitions;
- transaction design;
- concurrency and idempotency;
- caching;
- message queues;
- scheduled jobs;
- file processing;
- third-party services;
- exception handling;
- data migration;
- compatibility;
- release and rollback.

Use Mermaid flow, architecture, sequence, state, or ER diagrams when a diagram
materially improves understanding. Provide an equivalent textual description
when diagram support is unavailable.
