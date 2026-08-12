# Automation Feasibility and Deferred Routing

Apply this final annotation only after the complete semantic case set passes
coverage and deterministic-oracle audits and receives Recommended Test Levels.
Do not change why a case exists, its steps, or its Expected Results. Do not
inspect installed tools or claim automation is implemented or executed.

## Automation Feasibility

Evaluate Observable, Controllable, Deterministic, Resettable/Isolated, and
Toolable semantically. One intrinsic blocker can determine the result.

- **Automatable**: reliable programmatic setup, execution, observation, and
  cleanup are intrinsically suitable even when current runners, browsers,
  accounts, CI, scripts, or environments are unknown.
- **Conditional**: reliable automation intrinsically requires a specific named
  capability necessary for control, determinism, observation, or reset. Always
  state the concrete condition.
- **Manual**: human judgment or physical/real-world interaction is intrinsic,
  such as subjective visual or brand quality, human semantic judgment,
  exploratory work, hardware, or physical-device behavior without reliable
  automation.

Do not downgrade an intrinsically Automatable case because current automation
infrastructure is unavailable. Generic conditions such as `Requires automation
environment`, `Requires Playwright`, `Requires Chrome`, or `Requires testing
tools` are invalid. Legitimate conditions include a deterministic OTP hook,
payment sandbox/provider stub, controllable clock, failure-producing dependency
stub, or accepted task-specific evaluator and threshold.

## Concrete route or deferred route

When evidence already determines the execution seam, select one concrete
internal Automation Route:

`Browser`, `API`, `Integration`, `Component`, `Contract`, `Unit`, or `None`.

When a case is Automatable or Conditional but the best route depends on actual
repository structure, deliberately defer the route rather than guessing. Render
that deferred decision as `Auto` or `Conditional · Auto`. `Auto` is not a Test
Level, concrete tool, or synonym for Playwright; it tells downstream execution
to inspect the repository and choose the lowest-cost reliable seam.

Automation Feasibility and routing do not decide whether a semantic case
exists. Never generate a case from a desired route, remove a difficult case,
rewrite steps to fit a tool, weaken an oracle, or suppress an authoritative
requirement because implementation is missing.

Preserve the evidence required by the already-designed case when classifying
Automation. Never replace browser, API, Integration, or other explicitly
required evidence with a cheaper lower-level seam. A case whose Steps or
Expected Results require opening a page, clicking, entering input, selecting,
navigating, uploading, scrolling, or verifying rendered UI remains Browser /
Playwright; use `Auto` only when the case is implementation-neutral and its
required evidence does not depend on a specific execution surface.

## Routing decision order

Use the first applicable rule:

1. **Browser-native evidence -> Browser / Playwright.** Use when navigation,
   DOM rendering, form interaction, browser-visible validation, responsive UI,
   browser persistence, accessibility names, or a critical browser journey is
   itself the evidence.
2. **Authoritative technical seam -> explicit route.** Use API when an
   authoritative public API contract is the evidence. Use Integration,
   Contract, or Component when authoritative design or a public contract
   defines that seam. Use Unit only when isolated behavior is already the
   authoritative or unambiguous evidence seam.
3. **Implementation-dependent automation -> Auto.** Use only when all are true:
   the case should clearly be automated; the behavior is not intrinsically
   browser-specific; no authoritative API/Integration/Component/Contract seam
   uniquely determines the route; and reliable choice among Unit, Integration,
   API, or Playwright depends on repository structure.
4. **Intrinsic human judgment -> Manual.** Retain a real Test Level and
   internal route `None`.

Do not label every automatable case `Auto`. Prefer an explicit route whenever
the semantic evidence or authoritative contract already determines it. Do not
route a business-rule boundary through Browser merely because a page can show
the result or Playwright can send HTTP requests.

Typical `Auto` candidates include price or total calculations, sorting,
normalization, state mapping, order-number rules, and other deterministic
business decisions whose cheapest stable seam cannot be known without code.

## Human-facing Automation

Render one concise field without automation priority:

- Automatable + Browser -> `Playwright`.
- Automatable + explicit API/Unit/Integration/Component/Contract route -> the
  route name.
- Automatable + deferred route -> `Auto`.
- Conditional + Browser -> `Conditional · Playwright`.
- Conditional + explicit route -> `Conditional · <Route>`.
- Conditional + deferred route -> `Conditional · Auto`.
- Manual + None -> `Manual`.

Every Conditional case also includes a concise Automation Condition naming the
intrinsic enabling capability. Do not display `Browser`, `None`, feasibility
`Automatable`, a separate Playwright Yes/No field, or automation priority.

## Internal Playwright and E2E audit

Derive candidates internally:

```text
Playwright Candidate = Automation Route == Browser
AND Automation Feasibility in {Automatable, Conditional}

E2E Candidate = Recommended Test Level == E2E
AND Automation Feasibility in {Automatable, Conditional}
```

A deferred `Auto` case is not yet a Playwright candidate; downstream routing
may later choose Playwright or a non-browser seam. Keep E2E and routing
independent. `System + Auto`, `Unit + Auto`, `System + Playwright`,
`E2E + Playwright`, and `E2E + API` are valid. Do not publish candidate or route
counts by default.
