# Proactive Risk Design

Integrate risk analysis into every relevant design topic. Select risks based on
the requirement; do not emit a generic checklist.

## Application security

Consider when relevant:

- authentication and role or resource-level authorization;
- horizontal and vertical privilege escalation;
- input and parameter validation;
- SQL, command, and cross-site scripting injection;
- upload and download authorization, validation, storage, and lifecycle;
- sensitive-data access, display, browser storage, and logging;
- password, key, and token handling;
- third-party callback verification;
- business-rule bypass;
- bulk-operation abuse, resource exhaustion, and rate limits.

For frontend work, treat server results as authoritative, use frontend
authorization only for presentation, define failure display, avoid sensitive
browser storage, and prevent accidental duplicate requests.

## Reliability and business correctness

Consider when relevant:

- duplicate submission and idempotency;
- concurrent modification and state conflicts;
- transaction boundaries and partial success;
- timeouts, retries, and duplicate effects;
- duplicate message consumption;
- cache and database consistency;
- compensation after failure;
- resource release;
- historical-data compatibility;
- repeated scheduled execution;
- multiple instances processing the same work.

For state-changing operations, specify legal states, concurrency control,
transaction boundaries, idempotency keys or equivalent safeguards, rollback or
compensation behavior, and audit evidence as applicable.

## Code structure and maintainability

Consider when relevant:

- unjustified singleton or global state;
- user or request data in shared objects;
- bypassing existing layers;
- excessive responsibilities in one module;
- duplicate shared capability;
- unnecessary dependencies;
- hardcoded configuration;
- unrelated edits;
- unclear test boundaries;
- tight coupling;
- over-abstraction or overdesign;
- interface breakage;
- designs that are difficult to mock or isolate.

Prefer the project's existing dependency injection and lifecycle management.
A singleton is not automatically wrong; when shared lifetime is necessary,
document ownership, lifetime, mutable state, concurrency, tenant/request
isolation, and test isolation.

## Convert risk into design constraints

For every admitted risk, record:

1. the concrete risk;
2. where it can occur;
3. the design control;
4. the implementation constraint that later code must obey;
5. the verification focus.

Avoid vague statements such as "consider security." Use enforceable constraints
such as server-side resource authorization, transactional state and inventory
updates, idempotent duplicate handling, no user state in process-wide objects,
and redaction of tokens and sensitive data in logs.

Analyze risks alongside the affected feature:

- For uploads, cover type, size, filename, storage, permissions, malicious
  content, duplicates, failure, and lifecycle as relevant.
- For state changes, cover permission, legal state, duplicates, concurrency,
  repeated side effects, transactions, idempotency, conflicts, and audit.
- For external services, cover authentication, timeout, retry, duplicate
  effects, partial success, compensation, and user-visible failure.
