---
name: wewo-test
description: Orchestrate evidence-based test execution across unit, component, integration, API, contract, Web E2E, security-behavior, database, migration, performance, reliability, and manual testing; generate or modify permitted test assets, execute real checks, triage failures and Flaky results, and produce a final test gate. Use when a user asks to execute or complete verification of an implemented change. Do not use for test planning only, production implementation, independent code/security review, automatic production fixes, merge, or deployment.
---

# Wewo Test

Route each scenario to the most direct reliable test level, execute real tests,
and combine automated and human evidence into one test gate.

## Runtime contract

Create workflow outputs only at:

```text
docs/wewo/<requirement-category>/<requirement-slug>/09-test-execution.md
docs/wewo/<requirement-category>/<requirement-slug>/10-manual-test-checklist.md
docs/wewo/<requirement-category>/<requirement-slug>/test-artifacts/
```

Keep executable tests, fixtures, mocks, helpers, page objects, data builders,
and persistent test configuration in the project's normal test paths. Never
put executable test code under `docs/wewo/...`.

Write reusable skill files in English. Keep stable filenames and workspace
segments in English. Write user-facing conversation and generated documents in
an explicitly requested language, otherwise the dominant interaction language,
and otherwise Chinese. Follow repository naming, comment, and formatting
conventions for test code.

At runtime, create or modify test assets within the confirmed test scope.
Never silently modify production code, migrations, permissions, business
logic, or production configuration to make tests pass. Do not weaken
expectations, skip failing scenarios, add a backdoor, or use unlimited retries.

## Non-negotiable result vocabulary

Use these automated statuses only:

`Passed`, `Failed`, `Blocked`, `Skipped`, `Not Run`, `Flaky`, `Not Applicable`.

Use these manual statuses only:

`Manual Pending`, `Manual Passed`, `Manual Failed`, `Manual Blocked`,
`Manual Skipped`.

Generated but unexecuted tests are `Not Run`. Manual tests without actual human
execution evidence are never `Manual Passed`.

Use these final gate values only:

`Pass`, `Conditional Pass`, `Fail`, `Incomplete / Unable to Confirm`.

## Mandatory workflow

### 1. Resolve the workspace and execution scope

Run independently. Use upstream documents only when the user explicitly
selects them: an explicitly provided workspace, an explicit reference, or an
explicit request to continue an existing requirement. Never require them,
create empty earlier-stage documents, or scan the repository for them.

Resolve exactly one requirement workspace before writing reports or artifacts:

1. Use an explicit workspace supplied by the user.
2. Otherwise reuse the workspace established for the current requirement.
3. Otherwise infer one candidate from the requirement, issue, branch, or
   available upstream documents.
4. Ask before writing when multiple candidates are plausible.

Never choose by modification time. Support `features`, `bugs`, `refactors`,
and `maintenance`; default to `features` only when no evidence favors another
category. Use a concise lowercase English kebab-case slug. Create parents only
after resolution is unambiguous. Never combine different requirements without
confirmation.

Apply [project-and-matrix.md](references/project-and-matrix.md). Establish the
current code version, branch or commit, target Diff when applicable, user
objective, feature scope, regression scope, excluded scope, environment, and
limitations. Prefer an explicit user scope, then an identified requirement or
issue, then an actual Diff and affected context. Ask about material boundaries
instead of inventing them.

### 2. Collect inputs and analyze the actual project

Use current user goals, requirements, code, Diff, public interfaces, pages,
existing tests, repository instructions, environment and account information,
and known risks.

When the user explicitly provides or confirms them, reuse `01-prd.md`,
`02-technical-design.md`, `03-test-plan.md`, `04-test-cases.md`,
`05-implementation-plan.md`, and `06-implementation-record.md`. Treat an
explicitly selected `04-test-cases.md` as the primary scenario inventory and
an explicitly selected `03-test-plan.md` as optional scope and strategy
context. Treat implementation records as claims, not current execution
evidence. Never scan `docs/wewo/` or the repository to discover these
documents.

When upstream testing documents are absent, derive the minimum matrix from the
user goal, actual Diff, interfaces, pages, existing tests, repository behavior,
and risk. Do not fabricate expected behavior. Ask when an unresolved
expectation changes the test result.

Inspect dependency manifests, lockfiles, test directories, runner
configuration, scripts, CI, installed runtimes, browsers, existing fixtures,
reporters, and repository commands before selecting tools. Do not guess
commands or replace the established test stack for consistency.

### 3. Build the unified execution matrix

Read and apply
[routing-and-automation.md](references/routing-and-automation.md).

For every scenario, record:

- stable scenario ID, source, objective, priority, and risk;
- recommended test level, required evidence level, and actual test level;
- automation-feasibility status and rationale;
- framework, test seam, environment, account, and data needs;
- execution status and actual evidence;
- defect, failure attribution, or blocker;
- manual task ID when applicable.

Choose the lowest-cost, fastest, most stable level that provides direct and
trustworthy evidence. Use unit, component, integration, API, contract, Web
E2E, security-behavior, database/migration, performance/reliability, and manual
testing only where applicable. Do not convert every scenario to E2E.

Determine the obligations from the user's current test request, explicitly
selected requirements and cases, actual code, and the selected scope; do not
depend on a build-stage statement that E2E was deferred.

For every P0/P1 scenario with a documented Required Evidence Level of E2E,
execute E2E and classify it `Passed` or `Failed`, or mark it `Blocked` with a
concrete blocker, or `Not Run` with an explicit justified reason. Never
silently replace required E2E evidence with unit, component, integration, or
API evidence. When E2E is only recommended, another level may be used when it
provides equivalent direct evidence; record the reason for the routing
decision.

Classify automation feasibility as `Direct Automation`,
`Automation with Setup`, `Change Test Level`, `Infrastructure Required`,
`Blocked`, `Manual Preferred`, `Not Applicable`, or `Needs Clarification`.

The actual method may differ from the test plan. Record the reason, but never
silently change business behavior, acceptance criteria, permissions, security,
or consistency requirements. Keep execution results out of
`03-test-plan.md` and `04-test-cases.md`.

### 4. Confirm the test implementation approach

Reuse existing relevant tests first and verify that they exercise the intended
behavior. When scenarios are missing, create or modify focused test assets in
the existing framework and project test paths.

Read [framework-and-tools.md](references/framework-and-tools.md). Before
material persistent changes, present one implementation proposal covering new
dependencies, lockfiles, runner configuration, directories, CI, Docker,
`.gitignore`, test databases, browsers, services, and external platforms.
Obtain confirmation once for that agreed scope rather than per file.

When production-code testability changes are needed, do not make them. Record a
Testability Change Request with:

- the obstacle and proposed change;
- production-behavior impact;
- alternatives and risk;
- recommended handoff to `wewo-build`.

Examples include `data-testid`, injected time or randomness, test-only setup,
test-environment captcha controls, and replaceable external adapters.

### 5. Prepare tools, environment, accounts, and data

Apply [framework-and-tools.md](references/framework-and-tools.md) and
[environment-and-data-safety.md](references/environment-and-data-safety.md).

Prefer declared project tools, versions, package manager, scripts, fixtures,
and configuration. Restore declared dependencies using the native manager
without silent upgrades or manager changes.

For one-time validation, prefer a fixed-version isolated temporary tool that
does not modify project dependencies. Obtain confirmation before persistent
framework additions or high-impact actions such as system packages,
administrator access, Docker, large browser downloads, system Chrome,
persistent services, CI changes, external cloud testing, or source/test-data
upload. Never use unsafe installers or production secrets.

Before any write-capable test, confirm the URL and environment type, account,
data ownership, cleanup, email/SMS effects, payment effects, external-service
effects, shared inventory or business data, and concurrency permission. Do not
default to production write testing.

Installation or environment failure blocks only affected scope. Continue safe
available tests, record degraded verification, and never call blocked tests
Passed.

### 6. Implement and execute each automation branch

Read [automation-branches.md](references/automation-branches.md). For each
automatable scenario:

1. confirm expected observable behavior;
2. select the test level and seam;
3. reuse the project framework, fixtures, and helpers;
4. create or modify only missing test assets;
5. prepare isolated data and environment;
6. run one focused test first;
7. diagnose the first result;
8. fix test-code, fixture, or assertion defects without weakening expectations;
9. run the target set and necessary regression;
10. collect actual command, exit status, output, and artifacts;
11. update the execution matrix.

Generated test code is not execution evidence. Use `Passed` only after the
relevant current code and environment actually produced a passing result.

When Web E2E is appropriate, additionally read
[playwright-e2e.md](references/playwright-e2e.md). Reuse an existing
Playwright installation and configuration when present. Prefer bundled
Chromium, semantic locators, web-first assertions, auto-waiting, isolated
tests, and cleanup. Do not require all browsers, all devices, full
parallelism, Page Object, or one directory layout.

A scenario whose Required Evidence Level is E2E must enter the Web E2E branch
and finish as `Passed`, `Failed`, `Blocked` with a concrete blocker, or
`Not Run` with an explicit justified reason. Missing framework or browser
tooling follows the normal approval and setup rules in
[framework-and-tools.md](references/framework-and-tools.md); it is not a
reason to silently lower the evidence level.

Browser control, MCP, and host browser tools are optional. Fall back to the
project's configured CLI runner; when no safe executable browser path exists,
route the scenario to Blocked or an executable manual task rather than
fabricating browser evidence.

### 7. Manage manual execution

Read [manual-testing.md](references/manual-testing.md). Convert visual,
usability, wording, real-device, hardware, payment, captcha, external-page,
subjective, unsafe, or low-value automation scenarios into executable manual
tasks.

Each task must include a stable ID, source, priority, environment,
preconditions, data, steps, expected result, evidence requirement, status,
actual result, executor, execution time, and defect ID.

Generate and maintain
`docs/wewo/<requirement-category>/<requirement-slug>/10-manual-test-checklist.md`.
Combine actual human results with automation evidence in the matrix. Leave
unexecuted tasks `Manual Pending`; never impersonate a human executor.

### 8. Triage failures and Flaky behavior

Read and apply
[failure-triage.md](references/failure-triage.md).

Classify each failure as `Product Defect`, `Test Defect`, `Test Data Issue`,
`Environment Blocker`, `Existing Failure`, `Flaky`, `Requirement Conflict`, or
`Unverified`. Only confirmed product behavior failures enter the formal product
defect list.

Fix in-scope test-code defects and rerun. Do not silently fix production
defects; record them and recommend `wewo-build`. For a suspected Flaky result,
preserve first-failure evidence and use limited reruns under unchanged code and
environment. Mixed outcomes are `Flaky`, never reliably Passed.

### 9. Calculate metrics and the test gate

Read and apply
[metrics-and-gate.md](references/metrics-and-gate.md).

Calculate metrics only from the current matrix and actual evidence: scenario
execution and P0/P1 completion, automation applicability/implementation/
execution/pass rates, manual counts and completion, status and attribution
counts, regression and core-flow pass rates, and data-cleanup success.
Report coverage only when a real coverage tool ran.

Use:

- `Pass` only when all P0 scenarios pass, required P1 and manual work is
  complete, core flows and critical permission/transaction/consistency checks
  pass, no required-evidence scenario was silently downgraded, and no blocking
  defect or unaccepted high-risk Blocked/Flaky remains.
- `Conditional Pass` only when core flows pass, no blocker remains, residual
  risk is low, and an actual risk owner and follow-up are recorded.
- `Fail` for a failed P0/P1 core scenario, permission, transaction,
  consistency, core E2E, or migration test; a blocking product defect;
  uncontrolled test side effect; or accidental production connection.
- `Incomplete / Unable to Confirm` for missing environments, accounts, data,
  required manual evidence, blocked high-risk scenarios, persistent Flaky
  results, unavailable external systems, or necessary tools.

Automation rate and pass rate never decide the gate alone. Base the conclusion
on the latest code, real environment, and actual execution evidence.

### 10. Write and verify outputs

Read [document-contract.md](references/document-contract.md). Generate
`09-test-execution.md` from
[test-execution-template.md](assets/test-execution-template.md) and
`10-manual-test-checklist.md` from
[manual-test-checklist-template.md](assets/manual-test-checklist-template.md).

Store sanitized HTML/JSON/JUnit reports, logs, coverage, screenshots, traces,
necessary video, performance results, and structured execution output under
`test-artifacts/`. Never expose credentials, cookies, tokens, secrets, or
production data.

Verify that the report, manual checklist, artifacts, matrix, status counts,
failure attribution, metrics, and gate agree. Mark non-applicable test types
`Not Applicable`; do not fill them with invented content.

Report to the user:

- tested code version, scope, inputs, environment, and test types;
- test assets and dependencies added or modified;
- tools, browsers, and dynamic installations;
- Passed, Failed, Blocked, Not Run, Flaky, and manual counts;
- product defects, test defects, and blockers;
- artifact locations;
- test gate and remaining risks.

Stop and request clarification before execution when expected behavior is
materially ambiguous. Stop before unsafe environment writes or unapproved
persistent/high-impact changes. Even when the gate is incomplete, preserve
actual partial evidence and report unfinished scope. Do not automatically
continue into production fixes, code review, merge, release, or deployment.
