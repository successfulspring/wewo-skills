# Implementation Planning and Units

Produce an executable plan quickly from the Binding Implementation Obligations
and verified change surface.

## Choose the simplest honest shape

- **Small Atomic Change:** one coherent low-scope behavior or fix.
- **Vertical Slice:** one observable behavior across only the necessary layers;
  prefer this to separate model/service/interface/test phases.
- **Staged migration:** Expand, Migrate, Contract or another compatible sequence
  for a wide structural change that cannot honestly be independent behavior.

Do not repeatedly debate the shape. Choose the simplest one that exposes real
dependencies and verification.

## Define executable units

For each unit, colocate only:

- Goal / observable result
- `Blocked by`
- Binding obligations
- Expected scope
- Verification seam
- `TDD: Yes / No`
- Done when

Use dependency edges to order execution; never start a blocked unit. Keep a
unit small enough for one focused implementation context. Reject giant
multi-behavior units and layer-only decomposition when a behavioral unit is
practical.

Prefer a stable public seam already used by the repository. Use TDD for
behavior or rules with a stable executable seam. Mark declarative, mechanical,
or wiring work `TDD: No` when artificial Red adds little value; add a brief
reason only when it is not obvious.

Do not duplicate unit obligations in a global contract matrix or repeat unit
verification in a second strategy table. Add adaptive detail for API,
persistence, migration, dependencies, containers, CI, production environment,
compatibility, rollback, or integration only when it materially affects the
plan.

## Plan confirmation

Write `implementation-plan.md`, summarize the material scope, units,
dependencies, gaps, and verification, and explicitly ask the user to confirm.
Until confirmation, perform no implementation edits: not production code,
developer tests, migrations, implementation configuration, dependency or
lockfiles, container files, CI, or deployment files. Direct execution cannot
bypass this gate.
