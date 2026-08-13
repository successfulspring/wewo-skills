---
name: wewo-test
description: Execute automatable test cases or verification obligations against the actual repository by resolving evidence-preserving routes, reusing or creating durable test assets, running repository-native tests, triaging failures and Flaky results, preserving native evidence, and producing a concise automated execution gate. Use when a user asks to automatically test, verify, validate, or complete execution evidence for an implemented change. Manual-only cases are recognized as out of scope rather than executed or converted into manual test artifacts. Do not use for test planning or case generation alone, manual QA execution, production implementation or repair, independent code/security review, merge, release, or deployment.
---

# Automated Test Execution Orchestrator

Execute automatable verification against the actual repository by resolving each
in-scope obligation to an evidence-preserving, repository-native route; reuse or
create durable test assets; run real tests; triage results; preserve native
evidence; and produce a concise automated execution gate. Recognize manual-only
obligations as excluded scope without executing them or duplicating them into a
manual checklist.

## Core invariants

Test cases decide what must be proven. Their Automation annotations identify
the intended evidence surface. Repository inspection determines how this
project can prove it.

Execution routing must preserve the evidence required by the already-defined
case. Optimize how evidence is collected, but never change what evidence the
case requires or rewrite its behavior, Steps, or Expected Results. A cheaper
lower-level seam must never replace explicitly required browser, API,
integration, component, contract, persistence, or other evidence.

Prefer established repository test infrastructure. Do not prescribe one
framework, create a universal runner wrapper, or require a universal HTML
report. Browser automation is one execution branch, not the whole capability.

Playwright Test has one runner-specific completion invariant. When the resolved
final Runner is Playwright Test, the final evidence execution must enable its
native HTML reporter while preserving every established repository reporter;
add HTML alongside existing reporters rather than replacing them. A diagnostic
run that overrides reporters with `--reporter=list` does not satisfy final
execution. Before declaring Playwright execution complete, verify that the
configured HTML output folder contains its actual `index.html`. Passing tests
without that file leave Playwright final evidence incomplete. Repair the
permitted reporter configuration and rerun the final Playwright target before
completion; do not classify the missing report as a Product Defect.

Keep four decisions distinct:

1. `Required Evidence`: what the unchanged case and Oracle demand;
2. `Test Route`: the semantic execution surface;
3. `Repository-native Runner`: the project framework that executes the durable
   test asset;
4. `Agent Tool Interface`: an available shell, test-agent, browser, CLI, MCP,
   or other interface that may help the agent interact with that route.

An Agent Tool Interface never silently changes the Route or Runner. Agent
tooling helps interaction; repository tooling remains authoritative for durable
execution.

Keep durable test assets and configuration portable. Do not persist
machine-specific paths, user or skill installation paths, browser-cache paths,
machine-specific browser executables, or accidental transitive dependencies.
Prefer declared dependencies, repository scripts, relative project paths, and
intentional project/runtime environment variables.

Never silently modify production logic, business rules, permissions,
migrations, production configuration, or real data to make a test pass. Do not
weaken assertions, skip failures, add backdoors, or use unlimited retries.

## Runtime contract

Write execution outputs only under one resolved requirement workspace:

```text
docs/wewo/<requirement-category>/<requirement-slug>/test-execution.md
docs/wewo/<requirement-category>/<requirement-slug>/test-artifacts/
```

Always create
`docs/wewo/<requirement-category>/<requirement-slug>/test-execution.md` when
automated execution is requested or completed. Create
`docs/wewo/<requirement-category>/<requirement-slug>/test-artifacts/` only when
native evidence needs to be retained there. Do not create a manual test checklist
or any duplicate manual-test artifact. Keep executable tests, fixtures,
mocks, helpers, page objects, data builders, and persistent test configuration
in normal project test paths, never under `docs/wewo/`.

Write reusable skill files in English. Keep stable filenames and workspace
segments in English. Write user-facing conversation and generated documents in
an explicitly requested language, otherwise the dominant interaction language,
and otherwise Chinese. Follow repository conventions for test code.

Use these execution statuses only for in-scope automated obligations:

`Passed`, `Failed`, `Blocked`, `Skipped`, `Not Run`, `Flaky`, `Not Applicable`.

Generated but unexecuted automated tests are `Not Run`. Manual-only cases are
scope exclusions, not execution statuses: do not relabel them `Not Run`,
`Blocked`, or any manual status.

Use these automated execution gate values only:

`Pass`, `Conditional Pass`, `Fail`, `Incomplete / Unable to Confirm`.

The gate evaluates only the in-scope automated execution set. Manual-only cases
must not enter automated denominators or change this gate.

## Mandatory workflow

### 1. Resolve scope and obligations

Run independently. Use a test-case artifact only when the user explicitly
supplies or references it or the current conversation already establishes it.
Never scan `docs/wewo/` or the repository to discover workflow artifacts, and
never require an earlier capability to have run.

Resolve exactly one workspace before writing:

1. use an explicit workspace;
2. otherwise reuse the workspace established for the current requirement;
3. otherwise infer one candidate from the requirement, issue, branch, or
   explicitly supplied material;
4. ask before writing when multiple candidates are plausible.

Never choose by artifact existence or modification time. Support `features`,
`bugs`, `refactors`, and `maintenance`; default to `features` only when no
evidence favors another category. Use a concise lowercase English kebab-case
slug. Never combine separate requirements without confirmation.

Read [project-and-matrix.md](references/project-and-matrix.md). Establish the
current code version, target Diff when applicable, user goal, required and
regression scope, exclusions, environment, and limitations.

When no usable test-case artifact exists, derive only the minimum execution
inventory required from the current goal, explicit requirement evidence,
actual Diff, public interfaces, affected pages, repository behavior, existing
tests, and material risk. Do not fabricate expected behavior. Ask only when an
unresolved expectation changes pass/fail.

### 2. Inspect the actual repository

Inspect repository instructions, dependency manifests, lockfiles, test
directories, existing tests, runner and browser configuration, fixtures,
mocks, helpers, page objects, package scripts, Makefiles, CI commands,
coverage/reporters, architecture, public interfaces, and required database or
service setup.

Use repository facts to discover existing test assets, safe execution commands,
concrete seams, runners, environment needs, and available native evidence. Do
not choose from language stereotypes or general framework knowledge when the
repository defines the answer.

After resolving repository infrastructure, inspect the Agent Tool Interfaces
currently available when useful for the Route. Normal shell/CLI, Playwright
Test agent tools, Playwright CLI, Playwright MCP, browser control, and other
existing interfaces are possible capabilities, not dependencies. Choose a
useful available interface without changing the Runner. A missing optional
interface must not block a valid repository-native path.

Apply operational recipes only after Route, Runner, and useful Agent Tool
Interface resolution. Prefer, in order: a repository-defined script or command;
the repository-local Runner; the relevant reference's documented minimal
recipe; then local Runner help or diagnosis when syntax remains unclear. Keep
detailed command and code syntax in references and load it only for the active
route or failure mode.

### 3. Consume test-case execution intent

Treat `Test Level` as a recommendation describing the semantic evidence level.
Treat `Automation` as the primary execution-routing input. Support:

```text
Playwright
API
Unit
Integration
Component
Contract
Auto
Manual
Conditional · <route>
Conditional · Auto
```

For `API`, `Unit`, `Integration`, `Component`, and `Contract`, preserve that
evidence surface and use the repository's established framework and runner.

For `Playwright`, preserve browser-automation evidence and resolve the durable
browser runner under the browser rules below. The annotation does not authorize
downgrading a browser-visible Oracle to a lower-level test.

For `Auto`, inspect the repository and choose the lowest-cost, stable,
maintainable concrete seam that still proves the original behavior and Oracle.
Possible routes include Unit, Component, Integration, API, Contract, Browser,
or a repository-supported specialized seam. Record the resolved Route and
Runner without rewriting the source case.

Resolve an Agent Tool Interface only after `Auto` has resolved the Route and
Runner. Never combine route resolution with interface selection.

For `Conditional · <route>`, preserve the named condition and route. If the
named route is Manual, treat it as manual-only and exclude it from automated
execution scope. For `Conditional · Auto`, preserve the condition, then resolve
`Auto` from repository facts. If an automatable condition cannot be met, record
the resulting Blocked or Not Run evidence instead of inventing another route.

For `Manual`, exclude the case from automated execution scope. Preserve its
case ID and exclusion reason when useful for scope transparency. Do not execute
it, convert it to `Not Run`, generate a manual checklist, or infer any human
result. If no in-scope automatable obligations remain after filtering, stop
before tool setup or execution, report that there is no automated execution
scope, and do not fabricate statuses or an automated execution gate.

### 4. Build a compact execution record

Keep execution decisions and results orthogonal:

- `Route`: the evidence surface and concrete execution seam;
- `Runner`: the repository-native durable test executor;
- `Agent Tool Interface`: optional agent access used for interaction,
  generation, execution assistance, or diagnosis;
- `Execution Status`: the automated execution status;
- `Failure / Blocker Attribution`: why execution failed, was blocked, remained
  unstable, or could not be verified.

Track, as useful: Scenario ID, Source, Priority, Behavior/Oracle, Planned
Automation, Resolved Route, Runner, Agent Tool Interface, Test Asset,
Environment/Data Requirement, Execution Status, Evidence, Failure/Blocker
Attribution, and Scope Exclusion when applicable.
Do not re-plan the strategy, invent level quotas, or rewrite a supplied
test-case artifact.

Apply [routing-and-automation.md](references/routing-and-automation.md).

### 5. Reuse or create durable test assets

For every automated obligation:

1. locate related existing tests;
2. determine whether current tests already prove the required behavior;
3. reuse or extend them when appropriate;
4. otherwise create the smallest maintainable missing asset;
5. keep executable assets in normal project test paths.

Permitted changes include tests, fixtures, mocks, test helpers, page objects,
test-data builders, test-only configuration, and approved runner or reporter
configuration. Do not create duplicate test files when an existing suite can
be extended cleanly.

If verification needs a production change, record a capability-neutral
Testability Change Request describing the obstacle, proposed production
change, impact, alternatives, and risk. Do not implement the production change.

### 6. Prepare tools, environment, and data

Read [framework-and-tools.md](references/framework-and-tools.md) and
[environment-and-data-safety.md](references/environment-and-data-safety.md).
Read [runner-diagnostics.md](references/runner-diagnostics.md) when a runner
cannot discover, load, start, or execute its tests reliably.

Restore and reuse declared dependencies with the repository-native package
manager and pinned versions. Do not repeatedly request confirmation merely to
restore declared dependencies unless the action is high impact.

When a persistent new framework is required, present one scoped proposal and
request confirmation once for dependency and lockfile changes, test paths and
configuration, browser installation, reporter/CI impact, and required test
services or databases.

Require explicit confirmation for system-wide installation, administrator
privileges, Docker or service provisioning, large browser downloads, system
Chrome, persistent background services, external cloud testing, source/data
upload, and production-like destructive execution.

Before write-capable or externally visible tests, verify the environment, URL,
account, data ownership, cleanup, real email/SMS/payment/callback effects,
external services, shared business data, and concurrency permission. Do not
default to production writes.

### 7. Execute focused tests and relevant regression

Read [automation-branches.md](references/automation-branches.md). For each
automated scenario:

1. verify the expected behavior and Oracle;
2. resolve Route and Runner;
3. resolve a useful available Agent Tool Interface without changing the Runner;
4. locate related existing test assets;
5. create or modify the minimal missing test asset;
6. prepare safe environment and data;
7. run the focused test;
8. preserve first-failure evidence;
9. diagnose runner startup or execution failure before fallback;
10. triage the result;
11. repair only Test Defect, fixture, locator, or test-data defects;
12. rerun the focused test;
13. run the relevant target suite;
14. run necessary affected regression;
15. collect native evidence;
16. clean up;
17. assign the final status.

Do not automatically run the entire repository suite when a smaller affected
regression gives sufficient evidence. Do not omit necessary regression merely
to save time. Generated test code alone is not execution evidence.

### 8. Resolve and execute browser automation

Read [playwright-e2e.md](references/playwright-e2e.md) for browser obligations.
Browser exploration and durable browser testing are different activities.
Discover the repository browser framework before available agent browser
capabilities. Optional Playwright Test agent tools, Playwright CLI, Playwright
MCP, or browser-control interfaces may help inspect pages, generate tests,
discover locators, execute or debug, and inspect console/network behavior.
Their absence must not block a valid Runner path or unrelated testing, and live
clicking alone cannot mark an automated case `Passed`.

A durable automated browser case must reuse or create a repository test asset,
such as a project-native `*.spec.ts` or `*.cy.ts`, and execute it through the
actual project runner.

Resolve the browser runner in this order:

1. reuse existing Playwright Test and its project commands/configuration;
2. if an established Cypress or other browser suite exists, reuse it only when
   the user did not explicitly require Playwright itself, the case needs no
   Playwright-specific behavior, and the same browser evidence is preserved;
3. when no suitable browser framework exists, propose Playwright Test as the
   default persistent addition and follow the confirmation policy.

Record the resolved Runner. Do not replace an established Cypress suite merely
for standardization or install two browser frameworks without a project reason.
The repository-native CLI is always the core fallback.

When a new durable browser test needs locators and live access is useful,
interact with the rendered page, verify material states, discover stable
locators, generate the repository asset, and then execute it with the Runner.
Do not guess speculative DOM details when reconnaissance is available. Skip
reconnaissance when clear, stable repository abstractions already suffice.

If Playwright Test is the final Runner, completion additionally requires the
native HTML reporter and verified HTML `index.html` described in the Core
invariants. A successful diagnostic run or passing final test status alone is
not sufficient.

### 9. Exclude manual-only obligations

Manual-only cases are outside this capability's execution scope. Preserve their
identifiers as excluded scope when useful, but do not create executable human
tasks, manual statuses, or duplicate manual-test artifacts. Do not count
excluded Manual cases as `Not Run`, and do not let them affect automated
execution metrics or the automated execution gate.

### 10. Triage failures and Flaky results

Read [failure-triage.md](references/failure-triage.md). Attribute each failure
or gap as `Product Defect`, `Test Defect`, `Test Data Issue`,
`Environment Blocker`, `Existing Failure`, `Flaky`, `Requirement Conflict`, or
`Unverified`.

Repair only permitted test assets for a Test Defect. Record Product Defect as
`Failed` without modifying production code. Record an Environment Blocker as
`Blocked`. Preserve first-failure evidence and bounded rerun history for
Flaky results. One successful rerun does not prove stability.

A runner timeout or startup failure is not automatically a Product Defect,
Environment Blocker, or reason to replace the Runner. Apply the bounded runner
diagnostic sequence first. Repair permitted test infrastructure defects before
fallback; keep repository-specific workarounds scoped to the observed
framework/runtime/version combination.

### 11. Preserve native evidence and produce the gate

Preserve runner-native terminal output, exit status, reports, XML/JSON events,
coverage, Trace, screenshots, video, or performance summaries when produced
and useful. Do not install a reporter solely to normalize frameworks or force
all runners into HTML. Sanitize saved evidence.

Read [metrics-and-gate.md](references/metrics-and-gate.md) and calculate only
metrics supported by actual evidence. Report code coverage only when a real
coverage tool ran. Metrics support the gate and never hide a critical failure.

Read [document-contract.md](references/document-contract.md). Generate a lean
`test-execution.md` from
[test-execution-template.md](assets/test-execution-template.md), referencing
native evidence rather than converting it unnecessarily. Do not generate a
manual checklist or any other manual-execution artifact.

When Playwright Test was used, record its native HTML report path under native
reports/evidence only after verifying that the referenced `index.html` exists.
If generation remains blocked, report Playwright final evidence as incomplete
instead of fabricating a path or declaring execution complete.

Verify that code version, automated scope, excluded Manual cases, execution
record, native evidence, counts, failure attribution, residual risks, and gate
agree. Stop before
unsafe execution or unapproved persistent/high-impact changes. Even when the
gate is incomplete, preserve partial evidence and report unfinished scope. Do
not continue into production repair, code review, merge, release, or deployment.
