# Engineering Risk Design

Integrate risk controls into the affected design areas. Analyze only risks
material to the current requirement; do not emit a generic checklist or append
security, consistency, and reliability after the workflow is already designed.

Use four relevant risk families.

## 1. Security

Consider when relevant:

- authentication and server-side role or resource authorization;
- horizontal or vertical privilege escalation;
- untrusted input and injection;
- malicious upload or download behavior;
- sensitive data, secrets, logs, and audit evidence;
- third-party callbacks and external-model data exposure;
- business-rule bypass;
- rate, quota, and resource abuse;
- prompt injection, knowledge poisoning, unauthorized retrieval, and data
  exfiltration for AI or RAG systems.

Universal security hygiene normally becomes an Engineering Default rather than
a user question: derive authorization from server-side identity and resource
context, do not trust client identity, validate untrusted input, do not hardcode
secrets, redact sensitive logs, and use least privilege.

Ask the user only when a Material Security Policy decision exists, such as who
may cross a department boundary, which data may be sent to an external model,
or whether a compatibility promise permits weaker legacy behavior.

Place controls inside the affected design. A document-processing flow, for
example, should define its trust boundary, authorization, validation,
idempotency, resource boundary, and failure behavior where that flow is
described. A compact cross-cutting summary may supplement this but cannot
replace it.

## 2. Correctness and Consistency

Consider when relevant:

- legal states and transitions;
- duplicate submission and idempotency;
- concurrent modification and race conditions;
- transaction boundaries and partial success;
- repeated side effects;
- cache and database consistency;
- message redelivery and compensation;
- historical-data consistency;
- auditability and reconciliation.

Translate each admitted risk into concrete behavior. Specify legal transitions,
transaction ownership, conflict detection, idempotency identity and retention,
at-most-once business effects where required, compensation, and reconciliation
only when the project needs them. Do not use vague phrases such as “pay
attention to concurrency.”

## 3. Architecture and Maintainability

Consider when relevant:

- unjustified singleton or process-global mutable state;
- request, user, or tenant data retained in shared objects;
- unclear object ownership or lifetime;
- bypassing existing layers or dependency direction;
- excessive module responsibilities or God services/classes;
- duplicate shared capability;
- tight coupling or cyclic dependencies;
- unnecessary abstractions or dependencies;
- hardcoded configuration;
- difficult test isolation;
- public-interface breakage;
- unrelated edits.

A singleton is not automatically wrong. Never use a numeric singleton limit.
When shared lifetime is justified, define its owner, creation and disposal
lifecycle, mutable-state behavior, concurrency safety, request/user/tenant
isolation, resource ownership, and test isolation.

Prefer existing dependency injection, lifecycle management, responsibility
boundaries, and dependency direction unless a concrete design reason supports
change. Every new abstraction, component, or dependency must justify its
complexity.

## 4. Reliability and Resource Safety

Consider when relevant:

- timeout semantics;
- retries, backoff, and retry safety;
- partial failure and graceful degradation;
- dependency isolation;
- resource exhaustion;
- queue or job accumulation and poison messages;
- duplicate processing;
- connection, stream, file, and resource lifecycle;
- failure recovery;
- backup and recovery;
- user-visible failure.

For every material new external call or dependency, define as relevant:

- timeout behavior;
- retry policy and backoff;
- duplicate-effect safety or idempotency;
- failure, fallback, or degradation behavior;
- resource cleanup and dependency lifecycle;
- diagnostic observability.

Do not mechanically require circuit breakers, dead-letter queues, caches,
queues, or new monitoring infrastructure. Add them only when the failure model
and verified project context justify their burden.

## Derive controls, property classes, and seams

For every admitted material risk, record:

```text
Risk
-> Location / Trust or Failure Boundary
-> Design Control
-> Hard / Enforceable Invariant with an enforcement mechanism
   OR Implementation / Architecture Constraint
   OR Risk-Reduction Control with Residual Risk
-> Verification Seam where useful
```

Avoid “consider security,” “use best practices,” or similar non-design. State
the actual boundary, mechanism, and property implementation must preserve.

Classify the resulting property honestly:

- A `Hard / Enforceable Invariant` has a concrete system mechanism that makes
  the property hold.
- An `Implementation / Architecture Constraint` is mandatory for later coding,
  but correct implementation still requires verification.
- A `Risk-Reduction Control` lowers likelihood or impact without establishing
  an absolute guarantee; record material residual risk.

Do not promote a written `MUST`, prompt instruction, logging rule, monitoring
signal, or developer convention into a hard guarantee without a credible
enforcement mechanism.

Example:

```text
Risk:
Cross-document graph traversal can expose evidence from unauthorized documents.

Location / Trust Boundary:
Candidate evidence selection before context assembly.

Design Control:
Every retrievable graph fact retains source-document provenance, and candidate
evidence is authorization-filtered before entering context assembly.

Enforcement Mechanism:
The application retrieval boundary is authoritative for final evidence
selection and applies the resource-authorization filter to every candidate path
using immutable source provenance.

Implementation Constraint:
The traversal result cannot bypass the established resource-authorization
filter, including during fallback or retry.

Security Invariant:
Cross-document traversal MUST NOT widen the caller's authorized evidence set.

Verification Seam:
The application retrieval boundary exposes the authorized candidate set and
assembled evidence as observable outputs.
```

## Engineering invariants

Document only categories that materially constrain correct implementation:

- `Behavioral Invariant`;
- `Data Invariant`;
- `Security Invariant`;
- `Consistency Invariant`;
- `Reliability Invariant`;
- `Architecture Constraint`.

Examples include:

- Authorization derives from server-side identity and resource context, never
  client-supplied ownership identifiers.
- A successful business operation produces its state-changing side effect at
  most once.
- Retrying the same job does not create additional business effects.
- Request-scoped state is never retained in process-global mutable objects.

For every claimed material invariant, ask what concrete mechanism makes it
hold. Depending on the design, the simplest justified mechanism may be a
database or unique constraint, transaction boundary, conditional update,
compare-and-set, version or generation token, deterministic identity,
idempotency key, atomic replacement, state guard, authorization boundary,
immutable ownership or provenance, lock, compensation, reconciliation, or
authoritative filtering boundary. This list is illustrative, not mandatory.

If no credible mechanism exists, do not call the property guaranteed. Recast it
as an Implementation or Architecture Constraint, or as a Risk-Reduction
Control with explicit residual risk. These design properties are not
executable tests.

## Material interleaving analysis

For relevant background tasks, asynchronous processing, queues, retries, state
machines, scheduled jobs, callbacks, webhooks, multiple workers, or concurrent
mutation, ask what other actor can change the resource between important steps.

Analyze only material races: delete versus completion, update versus stale
completion, two workers handling one logical job, retry versus earlier partial
execution, timeout versus a remote effect that may have succeeded, lifecycle
transition versus delayed callback, and rollback versus still-running work.

When an interleaving can violate a material property, add the simplest explicit
guard justified by the project, such as a conditional state transition,
compare-and-set, generation token, task ownership, cancellation marker,
idempotent replacement, or authoritative final-state check. Do not require one
universal concurrency pattern.

## Partial side effects and retry safety

For each material multi-step state-changing workflow, identify what happens if
failure occurs after database, external API, file, index, event, message
acknowledgement, audit, or downstream side effects have committed.

Resolve recovery through the simplest credible design, which may use
transactional atomicity, idempotent replay, delete-and-replace, versioned
rebuild, compensation, reconciliation, staging and publish, or authoritative
projection filtering. Do not claim at-most-once business effects unless the
design explains partial execution, ambiguous outcomes, redelivery, and retry.

## Verification seams

For material invariants, prefer a stable application or use-case service,
domain operation, public API contract, repository or integration boundary, or
message-consumer boundary. Record the linked invariant or behavior, the seam,
and the observable property when useful.

Avoid private helper methods unless no stable higher-level boundary exists. Do
not generate detailed test cases, QA steps, testing-tool decisions, or TDD
Red/Green/Refactor instructions.

## Schema evolution, data migration, and observability

When persistent schemas or external contracts change, separately design:

- `Schema / Contract Evolution`: new tables, columns, indexes, constraints,
  API or message schemas, deployment ordering, rollout compatibility, and
  rollback implications.
- `Data Migration / Backfill`: historical conversion, state conversion,
  reindexing, recomputation, reconciliation, and historical projections.

Historical backfill does not explain schema deployment. If the repository has
no verified migration mechanism and persistent schema changes, explicitly
resolve how the schema is introduced safely. Use only the simplest safe
evolution strategy justified by the project; do not require every migration
pattern.

For a material new workflow, asynchronous process, integration, or
failure-prone boundary, explain how failure can be diagnosed. Consider stable
error or failure states, structured logging, request/job/document correlation,
meaningful metrics, audit evidence, tracing across material boundaries, and
user-impacting failure signals. Do not invent SLO or SLA values or add
monitoring infrastructure without demonstrated need.
