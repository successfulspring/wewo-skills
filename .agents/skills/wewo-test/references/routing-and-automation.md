# Evidence-Preserving Routing

Resolve how the actual repository can prove each obligation without changing
what must be proven.

## Core rule

Execution routing must preserve the evidence required by the already-defined
case. A cheaper lower-level seam must never replace browser, API, integration,
component, contract, persistence, or other evidence explicitly required by the
case. Never rewrite Steps or Expected Results to fit a runner.

Treat Test Level as semantic guidance. Treat Automation as the primary routing
input.

Keep these concepts separate:

```text
Required Evidence -> Test Route -> Repository-native Runner
                                      |
                                      +-> Agent Tool Interface
```

Required Evidence defines what must be shown. Route defines the semantic
surface. Runner is the project framework that executes the durable asset. Agent
Tool Interface is optional access the agent can use to interact, generate,
execute, or debug. Interface availability never redefines evidence, Route, or
Runner.

## Explicit Automation values

- `Unit`: preserve isolated behavior evidence and use the repository's unit
  runner.
- `Component`: preserve bounded component/rendering evidence and use the
  established component harness.
- `Integration`: preserve collaboration, persistence, transaction, messaging,
  filesystem, cache, or adapter evidence.
- `API`: preserve public request/response, authentication, authorization,
  validation, idempotency, or API compatibility evidence.
- `Contract`: preserve authoritative producer/consumer, schema, protocol, or
  serialization evidence.
- `Playwright`: preserve durable browser-automation evidence; resolve the
  concrete browser runner under the browser policy.
- `Manual`: exclude from automated execution scope. Preserve the case ID and
  exclusion reason when useful, but do not execute it, generate a manual
  checklist, or convert it to `Not Run`.
- `Conditional · <route>`: preserve both the enabling condition and route. If
  the named route is Manual, exclude it as manual-only scope.

Do not impose a global mapping from route to framework. Unit may use pytest,
unittest, Vitest, Jest, JUnit, `go test`, or another established runner; API,
integration, component, and contract routes likewise use the repository's
actual stack.

## Auto

`Auto` is repository-aware deferred routing. Inspect the repository and choose
the lowest-cost, stable, maintainable seam that directly proves the original
behavior and Oracle.

Possible resolved routes include Unit, Component, Integration, API, Contract,
Browser, or a repository-supported specialized test seam. Base the decision on
existing tests, test paths, configuration, scripts, fixtures, helpers,
architecture, public interfaces, and the implementation seam. Record the
resolved Route and Runner.

Do not choose from language stereotypes. Do not label `Auto` as a runner,
status, or test level. For `Conditional · Auto`, preserve the condition and
perform deferred routing only when the condition can be met.

Keep `Auto` unchanged: resolve its Route and Runner from repository facts
first. Only afterward select a useful available Agent Tool Interface. The
presence of Playwright, MCP, or another agent tool must not bias an otherwise
non-browser `Auto` obligation toward Browser.

## Route examples

A deterministic price-tier rule with a pure domain seam and an existing unit
suite may resolve to Unit. An idempotency rule with stable HTTP fixtures may
resolve to API. A case that opens a product page, selects a filter, and verifies
the rendered list remains Browser even when an internal filtering function is
easy to unit test.

## Decision factors

Use observability, controllability, isolation, determinism, fidelity,
diagnostic value, maintenance cost, existing infrastructure, data lifecycle,
accounts, external effects, and material risk. Formal load or stress execution
also requires an isolated environment, explicit targets and capacity, and
authorization.

Do not invent quotas by route, add redundant levels for completeness, or
replace an established framework merely for consistency.
