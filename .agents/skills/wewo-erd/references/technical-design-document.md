# Engineering Design Specification Guide

Read this guide only after the Design Closure Audit passes and the user
explicitly confirms the complete final design summary.

## Document model: Stable Core + Adaptive Detailed Design

The document must provide stable semantic navigation without forcing every
requirement into an identical 11-section rendering. Represent this Stable Core:

- Design Goal and Constraints;
- Existing System and Impact Scope;
- Proposed Engineering Design;
- Engineering Risk Controls and Invariants;
- Verification Seams;
- Engineering Decision Record.

These are semantic responsibilities, not mandatory literal headings or a fixed
section order. Related responsibilities may be combined, and headings may be
renamed or reordered when the confirmed design is clearer that way. Do not
create empty or low-value sections.

Add adaptive detailed-design sections only when relevant, including frontend,
backend, interfaces or APIs, data model, ER diagram, state or lifecycle,
transactions, concurrency or idempotency, cache, queue or background work,
files, external integrations, migration or backfill, compatibility, release or
rollback, and observability.

Keep the filename `technical-design.md` in English while localizing headings
and prose.

## Stable Core semantic coverage

### Design Goal and Constraints

Explain the requirement outcome, design goal, actual requirement sources,
explicit user technical constraints, important non-goals, and the forces that
shape the design. Expose material runtime or deployment assumptions and their
provenance. Do not invent performance targets, costs, SLOs, or SLAs, and do not
present an unsupported tuning value as confirmed architecture.

### Existing System and Impact Scope

Record only verified current stack, entry points, responsibilities, boundaries,
interfaces, data, state, lifecycle, security mechanisms, and reusable
capabilities. Identify proposed additions, modifications, and explicit
non-modifications.

Clearly distinguish `Existing`, `Proposed`, `Constraint`, and `Decision`.
Never present proposed design as verified repository fact. Proposed modules,
interfaces, components, tables, fields, configuration, or dependencies are
allowed when justified and must be labeled as proposed. Avoid exact file,
class, or function names unless verified structure or the design requires that
precision.

### Proposed Engineering Design

Explain responsibility boundaries, dependency direction, collaboration,
interfaces, control and data flow, state and lifecycle, persistence, result
delivery, failure behavior, and operational consequences as applicable. State
why existing boundaries are reused or why change is justified.

Keep those descriptions coherent across the complete design. For material
async or stateful flows, show the guards for relevant operation interleavings.
For multi-step state changes, explain the important side-effect boundaries and
how partial execution, recovery, and retry remain safe.

Integrate relevant security, consistency, reliability, and resource controls
inside the affected design sections. Do not design a workflow first and append
generic security considerations later.

Put a Mermaid ER diagram inside this document only when database entities or
relationships change. Never create a separate ERD file.

### Engineering Risk Controls and Invariants

For each admitted material risk, preserve the relationship:

```text
Risk
-> Location / Trust or Failure Boundary
-> Design Control
-> Hard / Enforceable Invariant with a concrete mechanism
   OR Implementation / Architecture Constraint
   OR Risk-Reduction Control with Residual Risk
-> Verification Seam where useful
```

Relevant controls should already appear in the affected design areas. A compact
cross-cutting summary may make the resulting properties easier to find. A hard
invariant must identify the mechanism that enforces it; a written `MUST` is not
enough. Label mandatory implementation constraints separately from controls
that only reduce risk, and record material residual risk rather than overstating
a guarantee. Do not add every category ceremonially.

### Verification Seams

For important invariants or behaviors, identify a stable engineering boundary
and observable property. Prefer application or use-case services, domain
operations, public API contracts, repository or integration boundaries, and
message-consumer boundaries over private helpers.

Verification Seams communicate where design properties can later be verified.
They are not QA test cases. Do not include detailed test steps, a test plan,
testing-tool decisions, executable tests, or TDD instructions.

### Engineering Decision Record

Record only decisions that materially shape implementation. Preserve why, not
only what. Include material assumptions and provenance when they affect the
decision's validity. A compact record may contain:

```markdown
| Decision | Context / Evidence | Considered Options | Final Approach | Reason | Trade-offs / Consequences | Reversibility |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |
```

Omit columns that add no value. Do not turn routine Engineering Defaults or
every implementation detail into an ADR.

## Evolution and operations

When persistent schemas or external contracts change materially, distinguish
`Schema / Contract Evolution`—deployment ordering, compatibility, and
rollback—from `Data Migration / Backfill`—historical conversion, reindexing,
recomputation, and reconciliation. Backfill alone does not explain how the
schema is deployed. Use the simplest safe evolution strategy justified by the
project; do not mechanically require expand/contract, dual reads, or every
migration pattern.

When a material workflow, asynchronous process, integration, or failure-prone
boundary needs diagnosis, describe relevant stable error states, structured
logging, correlation identifiers, metrics, audit evidence, tracing, and
user-impacting failure signals. Do not invent SLOs or add monitoring
infrastructure without demonstrated need.

## Deliberately unresolved issues

Continue clarification when an unresolved issue materially changes the core
design. Include a non-blocking unresolved or deferred section only when actual
items remain and the user accepted them. Do not create an `Unresolved
Questions` section merely to write `None`.

## Quality gate

Before writing, verify that:

- the Design Closure Audit passed and the user explicitly confirmed the full
  design summary;
- requirement behavior maps to the proposed engineering design;
- existing-project claims are verified and proposed design is labeled;
- material decisions have valid evidence, ownership, and confirmation;
- the complete design contains no unresolved material cross-section
  contradiction;
- affected and unaffected scope are clear;
- relevant risk controls live inside affected design areas;
- every claimed hard invariant identifies a credible enforcement mechanism;
- implementation constraints and risk-reduction controls are distinguished,
  with material residual risk recorded;
- relevant async or stateful interleavings and partial-side-effect recovery are
  resolved;
- material runtime or deployment assumptions have valid provenance;
- shared state has explicit ownership, lifecycle, concurrency, isolation, and
  testability properties where relevant;
- schema or contract evolution is distinct from data migration or backfill;
- unsupported arbitrary tuning values are not represented as confirmed design;
- compatibility, rollback, dependency, reliability, and observability
  consequences are resolved where relevant;
- material invariants and useful Verification Seams are easy to find;
- ER content appears only for database entity or relationship change;
- every included section has relevant content;
- no production code, implementation task decomposition or sequencing, TDD
  workflow, full test plan, QA test cases, or test execution instructions are
  produced.
