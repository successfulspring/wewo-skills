# Adaptive Engineering Design Composition Scaffold

Use this only as an internal composition aid after final confirmation. It is
not a fixed schema. Preserve the Stable Core semantics, but combine, rename,
reorder, or omit sections when the confirmed design is clearer. Insert only
relevant adaptive detailed-design sections. Do not copy this instruction block
or empty placeholders into `technical-design.md`.

```markdown
# {Localized engineering design title}

## {Design Goal and Constraints}

{Requirement outcome, actual sources, explicit constraints, non-goals, and
design-shaping forces}

## {Existing System and Impact Scope}

{Verified existing entry points, responsibilities, boundaries, interfaces,
data/state/lifecycle, reusable capabilities, proposed changes, and explicit
non-changes. Label Existing, Proposed, Constraint, and Decision clearly.}

## {Proposed Engineering Design}

{Responsibilities, dependency direction, collaboration, control/data flow,
interfaces, state/lifecycle, persistence, failure behavior, and rationale}

{Add, combine, rename, reorder, or omit only relevant detailed sections such as
frontend, backend, interface/API, data model, ER diagram, state/lifecycle,
transactions, concurrency/idempotency, cache, queue/background work, files,
integrations, migration/backfill, compatibility, release/rollback, and
observability. Integrate each area's security, consistency, reliability, and
resource controls where that area is designed.}

## {Engineering Risk Controls and Invariants}

| {Risk and boundary} | {Design control} | {Implementation constraint} | {Engineering invariant} |
|---|---|---|---|
| ... | ... | ... | ... |

{Use only for admitted material risks and invariants. A compact summary may
point back to controls already integrated in detailed design.}

## {Verification Seams}

| {Linked invariant or behavior} | {Stable engineering seam} | {Observable property} |
|---|---|---|
| ... | ... | ... |

{Engineering boundaries only; no QA cases, test steps, tools, or TDD workflow.}

## {Engineering Decision Record}

| {Decision} | {Context / Evidence} | {Final Approach} | {Reason} | {Trade-offs / Consequences} | {Reversibility} |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

{Record only material implementation-shaping decisions. Add considered options
when they materially explain the choice.}

## {Optional: Deliberately Unresolved or Deferred Issues}

{Include only when actual non-blocking items remain and the user accepted them;
otherwise omit this section.}
```
