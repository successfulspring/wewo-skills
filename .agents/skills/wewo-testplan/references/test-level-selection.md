# Post-Generation Test Level Classification

Apply this classification only after semantic scenarios and executable cases
exist and pass coverage and oracle audits. Test Level answers where an
already-designed behavior can be proven most economically and reliably. It
does not answer what cases should exist.

Keep Objective, Technique, Recommended Test Level, Automation Feasibility, and
Automation Route distinct. Objectives and techniques remain internal; do not
expose a mixed generic Test Type field.

## Recommended Test Level

Assign one primary level without changing the case's behavior, steps, or
Expected Results:

- **Unit**: deterministic calculations, transformations, validation, or
  isolated decisions.
- **Component**: bounded UI or service-component behavior with controlled
  dependencies.
- **Integration**: database, transaction, adapter, messaging, cache,
  filesystem, or multi-module collaboration.
- **API**: request validation, authorization, response semantics, or endpoint
  behavior.
- **Contract**: producer/consumer or external-interface compatibility.
- **System**: complete running-application behavior whose distinct evidence is
  local to one feature.
- **E2E**: a realistic user-observable journey across meaningful boundaries,
  from entry/interface through business behavior and persistence/external
  effect to an observable outcome.

Levels are not a hierarchy or generation quota. Do not produce cases by level,
seek a balanced pyramid, use `Unit or higher`, or force every requirement
through multiple levels. Manual is Automation Feasibility, not a level.

## Classification rule

Choose the lowest reliable and economical level that directly proves the
already-designed evidence need. Consider observability, controllability,
isolation, determinism, fidelity, diagnostic value, and maintenance cost. Add
another semantic case or level only when it supplies genuinely distinct
evidence, not to satisfy a ratio.

Do not force a case into Unit merely because source code exposes a convenient
function. Repository functions/classes do not create obligations. Conversely,
an authoritative technical design may legitimately make an API, transaction,
integration, database, state, idempotency, or producer/consumer contract the
direct evidence target before code exists.

Generate E2E candidacy from critical user or business journeys whose complete
path supplies evidence isolated cases cannot provide. Do not create E2E to
meet a count or percentage, and do not turn every Browser/System case into E2E.

## Test Level versus Automation Route

Test Level describes where the behavior is proven. Automation Route describes
which downstream execution path implements the case: `Browser`, `API`, `Unit`,
`Integration`, `Component`, `Contract`, or `None`. Select both only after case
design; neither may determine whether the case exists.

Browser route means Playwright within wewo-skills but does not imply E2E.
`System + Playwright`, `E2E + Playwright`, and `E2E + API` are valid. Exact
non-browser tools and detailed implementation-level construction belong to the
downstream execution capability.

Test Level remains independent when the Automation route is deferred. `Auto`
is a human-facing deferred-routing signal, not a Test Level or tool. Valid
combinations include `Unit + Auto`, `System + Auto`, `System + Playwright`,
`E2E + Playwright`, and `API + API`. A recommended level may express the best
semantic evidence location even when downstream repository inspection must
choose the actual concrete seam.
