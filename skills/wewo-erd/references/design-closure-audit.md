# Internal Design Closure Audit

Run this audit before presenting the final design summary. It is a runtime
reasoning protocol and creates no workflow artifact. The checks below are not
mandatory headings or a checklist section for `technical-design.md`.

## Relevant dimensions

Evaluate only dimensions material to the current design:

- Requirement Mapping;
- Impact Scope;
- Architecture and Responsibilities;
- Interface and Data Flow;
- State and Lifecycle;
- Security;
- Correctness and Consistency;
- Architecture and Maintainability;
- Reliability and Resource Safety;
- Compatibility;
- Schema and Contract Evolution;
- Data Migration and Backfill;
- Dependencies;
- Observability;
- Engineering Invariants;
- Verification Seams;
- Cross-Section Coherence;
- Invariant Enforceability;
- Material Interleavings;
- Partial Side Effects;
- Material Assumption Provenance;
- Arbitrary Tuning Values.

For each dimension:

```text
irrelevant -> skip
relevant and resolved -> closed
relevant and materially unresolved
  -> continue repository investigation, engineering reasoning, or user dialogue
```

Do not mechanically create questions or document sections for every dimension.
Use the Engineering Decision Map to check that confirmed decisions did not
unlock material branches that remain unresolved.

## Cross-section design coherence

Reason across the complete proposed design rather than validating sections in
isolation. Trace material end-to-end flows and compare their claims about
ordering, state, persistence, visibility, authorization, failure, recovery,
migration, and rollback.

Look for concrete contradictions such as:

- a flow described as parallel even though one branch consumes another's
  output;
- lifecycle transitions that conflict with background completion behavior;
- API results that conflict with persistence or visibility semantics;
- retry behavior that invalidates an idempotency or at-most-once claim;
- failure behavior that conflicts with availability or user-visible state;
- migration mechanics that make the claimed rollback impossible;
- one access path applying authoritative security filtering while another
  bypasses it;
- one design statement contradicting a claimed invariant.

Do not close this check with generic language such as “ensure consistency.”
Resolve a material contradiction through engineering reasoning, targeted
repository investigation, or user confirmation according to decision
ownership. Generation remains blocked while it is unresolved.

## Invariant enforceability

For every claimed material invariant, ask:

> What concrete mechanism makes this property hold?

Accept a Hard or Enforceable Invariant only when the design identifies a
credible mechanism at the relevant boundary. Depending on the project, that
may be a database or unique constraint, transaction boundary, conditional
update, compare-and-set, generation token, deterministic identity, idempotency
key, atomic replacement, state guard, authorization boundary, immutable
ownership or provenance, concurrency primitive, compensation, reconciliation,
or authoritative filtering boundary. This list is illustrative, not required.
Choose the simplest mechanism justified by the project.

A written `MUST` does not make a property enforceable. If no credible mechanism
exists, classify it honestly as either:

- an Implementation or Architecture Constraint whose implementation requires
  later verification; or
- a Risk-Reduction Control that lowers likelihood or impact but retains
  material Residual Risk.

Do not claim an absolute guarantee from prompt wording, developer discipline,
logging, monitoring, or another probabilistic control.

## Material interleavings

When background tasks, asynchronous processing, queues, retries, state
machines, scheduled jobs, callbacks, webhooks, multiple workers, or concurrent
mutation are relevant, ask:

> What other actor can change this resource between the important steps?

Analyze only material interleavings, such as delete versus background
completion, update versus stale task completion, duplicate workers, retry
versus earlier partial execution, timeout versus a remote side effect that may
have succeeded, lifecycle transition versus delayed callback, or rollback
versus still-running work.

If an interleaving can violate a material property, design an explicit guard at
the right boundary. A conditional transition, version or generation token,
task ownership, cancellation marker, idempotent replacement, or authoritative
final-state check may be suitable, but no one pattern is mandatory.

## Partial side effects and retry safety

For each material multi-step state-changing workflow, ask:

> What happens if failure occurs after one or more side effects have committed?

Identify relevant commit boundaries such as database writes, external calls,
files, indexes, event publication, message acknowledgement, audit records, and
downstream mutations. Determine how recovery works through the simplest
credible combination of transactional atomicity, idempotent replay,
delete-and-replace, versioned rebuild, compensation, reconciliation, staging
and publish, or authoritative projection filtering.

Do not accept “business side effects occur at most once” unless the design
explains how partial execution, ambiguous remote outcomes, redelivery, and
retry preserve that property. Otherwise narrow the guarantee and record the
remaining risk.

## Material assumptions and arbitrary values

Inspect every Engineering Default that materially affects correctness,
security, consistency, deployment, availability, data safety, or scalability
architecture. Its required assumption must trace to a verified Repository Fact,
explicit User Technical Constraint, or confirmed Material Engineering
Decision. Otherwise escalate it to a Material Engineering Decision or Blocking
Requirement Ambiguity when design validity depends on it.

Inspect material numeric or default parameters. Values supported by repository
configuration, protocols, measured evidence, capacity data, acceptance
criteria, explicit requirements, or verified external constraints may be
confirmed. Unsupported values must remain suggested starting values, tuning
hypotheses, evaluation-dependent values, or unresolved non-blocking parameters.
Do not invent SLA or SLO values, and do not ask the user about immaterial tuning.

## Schema evolution and data migration

When persistent schemas or external contracts change, evaluate two separate
concerns:

1. `Schema / Contract Evolution`: tables, columns, indexes, constraints, API or
   message schemas, rollout compatibility, deployment ordering, and rollback.
2. `Data Migration / Backfill`: historical conversion, state conversion,
   reindexing, recomputation, reconciliation, and historical projection
   generation.

A backfill does not explain how a schema is deployed safely. If the repository
has no verified migration mechanism and the design changes persistent schema,
resolve how the schema change is introduced before closure.

## Closure conditions

The audit passes only when:

- requirement behavior maps to a concrete engineering response;
- existing-system and impact claims have sufficient verified evidence;
- responsibility, interface, data, state, and lifecycle boundaries are clear
  where relevant;
- Material Engineering Decisions and Blocking Requirement Ambiguities are
  resolved;
- cross-section claims are coherent and no material contradiction remains;
- every claimed hard invariant has a credible enforcement mechanism;
- implementation constraints, risk-reduction controls, and residual risks are
  labeled without overstating guarantees;
- material interleavings and partial-side-effect recovery are safe or their
  accepted limits are explicit;
- material runtime and deployment assumptions have valid provenance;
- schema or contract evolution and data migration or backfill are separately
  closed where relevant;
- unsupported tuning values are not presented as confirmed architecture;
- migration, compatibility, dependency, operational, and failure consequences
  are closed where relevant;
- useful stable Verification Seams identify observable design properties;
- no proposed design is presented as an existing repository fact;
- the final summary can explain what changes, why, and which properties are
  guaranteed versus merely constrained or risk-reduced.

Do not allow generation because a queue is empty or a predefined number of
topics was discussed. All material engineering branches must be closed, and
the user must explicitly confirm the complete final design summary before
`technical-design.md` is written.
