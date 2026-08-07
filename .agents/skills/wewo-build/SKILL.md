---
name: wewo-build
description: Plan and implement a scoped software change through repository-aware vertical slices, TDD where appropriate, executable unit and integration tests, per-slice quality checks, and fresh verification evidence. Use when a user asks to modify production code, tests, configuration, migrations, or implementation assets and document the actual result. Do not use for full product discovery, design-only work, independent code or security review, final acceptance-test execution, test-gate reporting, merging, or deployment unless those external actions are explicitly requested and authorized.
---

# Wewo Build

Plan, construct, and verify a confirmed software change using the target
repository's conventions and actual command evidence.

## Runtime inputs and outputs

Accept user requirements, conversation context, issues or bugs, source
documents, project code, existing tests, Git diffs, repository conventions,
and optional `01-prd.md`, `02-technical-design.md`, `03-test-plan.md`, or
`04-test-cases.md`.

Create workflow documents only at:

```text
docs/wewo/<requirement-category>/<requirement-slug>/05-implementation-plan.md
docs/wewo/<requirement-category>/<requirement-slug>/06-implementation-record.md
```

Create or modify production code, executable unit, integration, and focused API
tests, fixtures, migrations, configuration, and other confirmed implementation
assets only in the project's normal paths. Never make `docs/wewo/...` a source
or executable-test tree.

Keep workflow filenames and workspace segments in English. Conduct user
interaction and write workflow documents in an explicitly requested language,
otherwise the dominant interaction language, and otherwise Chinese. Follow
repository conventions for code names, tests, comments, and formatting.

## Mandatory workflow

### 1. Resolve scope and workspace

Run independently. Use upstream documents only when the user explicitly
selects them: an explicitly provided workspace, an explicit reference, or an
explicit request to continue an existing requirement. Never require them,
create empty predecessors, or scan the repository for them. Establish the
minimum implementation context from the user, issue or task, current code,
affected interfaces, existing tests, and repository conventions when no
authorized documents exist.

Resolve exactly one requirement workspace before writing workflow documents:

1. Use an explicit workspace supplied by the user.
2. Otherwise reuse the workspace established for this requirement.
3. Otherwise infer a candidate from the requirement, issue, branch, or
   available upstream documents.
4. Ask before writing if multiple candidates are plausible.

Never choose the most recently modified workspace by default. Use
`features`, `bugs`, `refactors`, or `maintenance`; default to `features` only
when no evidence favors another category. Use a concise lowercase English
kebab-case slug. Create parent directories only after resolution is
unambiguous, and never combine separate requirements without confirmation.

Clarify any missing business or design decision that materially changes
observable behavior, authorization, consistency, security, scope, interface,
database, dependency, or completion criteria. Do not weaken or silently change
requirements to simplify implementation.

### 2. Analyze the repository and establish a baseline

Read and apply
[project-analysis.md](references/project-analysis.md).

Inspect repository instructions, language, framework, package manager,
architecture, modules, similar implementations, public interfaces, tests,
build/lint/type/format commands, security conventions, persistence and
transactions, dependencies, configuration, current branch, and worktree
status. Read commands from project configuration rather than guessing.

Preserve unrelated and uncommitted user work. Never overwrite, delete, revert,
or absorb it into this change. Suggest a branch or worktree for risky,
large-scope, or dirty-worktree work when useful; do not force creation when the
host cannot support it.

Summarize the implementation baseline: included and excluded behavior,
confirmed expectations, technical constraints, actual sources, and unresolved
questions. Do not invent files, classes, functions, interfaces, tables, tests,
or commands.

### 3. Create and confirm the implementation plan

Read and apply
[planning-and-slicing.md](references/planning-and-slicing.md) and
[dependency-and-tool-policy.md](references/dependency-and-tool-policy.md).

Before modifying production code:

- evaluate TDD candidates and choose real test seams;
- define global implementation constraints;
- identify affected and unaffected files or modules;
- split work into small, independently verifiable vertical slices;
- identify interface, database, migration, compatibility, dependency,
  security, and reliability implications;
- assign actual verification commands and completion conditions;
- make blockers explicit.

Generate
`docs/wewo/<requirement-category>/<requirement-slug>/05-implementation-plan.md`
using [implementation-plan-template.md](assets/implementation-plan-template.md).
Summarize it and obtain confirmation before code modification. If the user
explicitly requests direct execution and the goal is already sufficiently
clear, keep confirmation concise, but still create the plan as the execution
basis.

Do not begin broad implementation until the plan is sufficiently concrete.

### 4. Implement one vertical slice at a time

For each planned slice:

1. Select one observable behavior and one primary test seam.
2. Apply the TDD protocol in
   [tdd-protocol.md](references/tdd-protocol.md) when a valid seam exists.
3. Make only the production, test, fixture, configuration, or migration change
   required for that slice.
4. Run focused and relevant regression verification.
5. Apply the compliance and quality checks in
   [slice-quality.md](references/slice-quality.md).
6. Fix in-scope issues and rerun affected checks.
7. Update the implementation record with commands, outcomes, changes, and
   deviations.

Do not batch many unverified tests with a large implementation. Preserve the
loop of one behavior, one seam, one valid failing test, and one minimum
implementation when TDD is appropriate.

If no valid testing seam exists or another approach is more appropriate,
record the reason and use the best available verification. Never fabricate a
Red or Green result.

Browser E2E is outside Build's execution responsibility. Do not inspect
whether Playwright, Cypress, or browsers are installed; do not install or run
browser E2E; do not require it for completion. A test case classified as E2E
keeps its expected business behavior, stays outside Build execution, is never
marked Passed here, and is recorded as a handoff for independent test
execution.

### 5. Handle test-design input without changing expectations

Treat `04-test-cases.md` as design input, not an infallible executable
specification. Apply
[test-case-adjustments.md](references/test-case-adjustments.md).

The implementation may change test level, seam, splitting, merging,
parameterization, or defer broad E2E/manual scenarios. It must not change
confirmed business behavior, acceptance criteria, permissions, consistency,
security, or scope. Pause and request clarification when a case conflicts with
confirmed expectations.

Never modify `03-test-plan.md` or `04-test-cases.md`; do not fabricate them
when absent. Record test-case adjustments, plan deviations, and strategy
conflicts in `06-implementation-record.md` and surface them to the user. A
revision of an upstream document happens only through explicit user
confirmation and deliberate revision of the owning document.

### 6. Use repository-native tools and controlled dependencies

Prefer the project's declared tools, package manager, versions, scripts, and
configuration. Distinguish restoring declared dependencies from introducing
new ones. Do not silently upgrade versions, switch package managers, or make
material dependency, lockfile, CI, service, or system-level changes without
the required confirmation.

When a required tool is missing, inspect project configuration first. Record
installation or restoration failure and continue with available verification
where possible. Do not claim an unavailable command ran.

Default to no commit, merge, push, release, or deployment. Perform those
external changes only when the user explicitly requests them and the current
environment permits them.

### 7. Verify each slice and the completed implementation

Use [evidence-and-completion.md](references/evidence-and-completion.md).

After each slice, verify requirement compliance, the focused test, relevant
regression, applicable integration behavior, type or compile status, lint, and
scope/constraint adherence. An implementation-time self-check or optional
fresh-agent check is not final independent review and must not produce
`07-code-review.md` or `08-security-review.md`.

Before completion, freshly rerun the commands that prove the implementation:
new tests, affected-module tests, necessary integration and regression tests,
and applicable type-check, lint, formatting, migration, build, or runnable
suite commands. Read complete output and exit status.

Classify every check as passed, failed, not run, blocked, unavailable, or
limited to partial scope. Do not rely solely on earlier output, another
agent's claim, or code inspection.

### 8. Finalize the implementation record

Maintain
`docs/wewo/<requirement-category>/<requirement-slug>/06-implementation-record.md`
during implementation and finalize it with
[implementation-record-template.md](assets/implementation-record-template.md)
and [document-contract.md](references/document-contract.md).

Record actual changed files, slice status, Red/Green evidence, unit and
integration outcomes, quality checks, test-case adjustments, plan deviations,
known limitations, latest verification evidence, and remaining risks. Claim
"implementation complete" only when the latest evidence supports it.

After verifying the record, report:

- both workflow-document paths;
- implemented behavior and major changed files;
- actual test and quality-check results;
- test-plan and test-case adjustments recorded in the implementation record;
- unfinished work, blockers, and remaining risks.

Do not claim final independent review or a final test gate. Do not continue
automatically into review, broad E2E generation, acceptance execution,
deployment, or another workflow stage.
