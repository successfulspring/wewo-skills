---
name: wewo-build
description: Plan and implement a scoped software change through repository-aware vertical slices, TDD where appropriate, executable unit and integration tests, per-slice quality checks, and fresh verification evidence. Use when a user asks to modify production code, tests, configuration, migrations, or implementation assets and document the actual result. Do not use for full product discovery, design-only work, independent code or security review, final acceptance-test execution, test-gate reporting, merging, or deployment unless those external actions are explicitly requested and authorized.
---

# Wewo Build

Plan, construct, and verify a confirmed software change using the target
repository's conventions and actual command evidence.

## Runtime inputs and outputs

Accept a clear implementation intent or requirement, conversation context,
issues or bugs, source documents, project code, existing tests, Git diffs, and
repository conventions. High-value context when available: confirmed
technical-design decisions already established in the conversation, an
explicitly supplied `prd.md`, and an explicitly supplied `technical-design.md`.
A formal technical-design artifact is not a prerequisite.

Create workflow documents only at:

```text
docs/wewo/<requirement-category>/<requirement-slug>/implementation-plan.md
docs/wewo/<requirement-category>/<requirement-slug>/implementation-record.md
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

Run independently. Use `prd.md` and `technical-design.md` only when the user
explicitly supplies or references them, or the current conversation already
establishes them. Never require them, create empty predecessors, or scan the
repository for them. Establish the minimum implementation context from the
user, issue or task, current code, affected interfaces, existing tests, and
repository conventions when no usable artifact exists.

Resolve exactly one requirement workspace before writing workflow documents:

1. Use an explicit workspace supplied by the user.
2. Otherwise reuse the workspace established for this requirement.
3. Otherwise infer a candidate from the requirement, issue, branch, or
   explicitly supplied or referenced material.
4. Ask before writing if multiple candidates are plausible.

Never infer a workspace from the existence of workflow artifacts. Never choose
the most recently modified workspace by default. Use `features`, `bugs`,
`refactors`, or `maintenance`; default to `features` only when no evidence
favors another category. Use a concise lowercase English kebab-case slug.
Create parent directories only after resolution is unambiguous, and never
combine separate requirements without confirmation.

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

- derive implementation behaviors from the requirement, technical design when
  available, and actual code;
- determine the implementation verification strategy: for each relevant
  behavior, identify the observable behavior, the verification seam, whether
  TDD is appropriate, the implementation-time verification level, and the
  reason;
- define global implementation constraints;
- identify affected and unaffected files or modules;
- split work into small, independently verifiable vertical slices;
- identify interface, database, migration, compatibility, dependency,
  security, and reliability implications;
- assign actual verification commands and completion conditions;
- make blockers explicit.

Generate
`docs/wewo/<requirement-category>/<requirement-slug>/implementation-plan.md`
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

Browser-level acceptance testing is outside this capability's implementation
verification scope. Do not inspect, install, configure, generate, or execute
browser acceptance tests, and do not reason about concrete browser-test tools.
Do not track browser acceptance as deferred workflow state or create a handoff
to another capability. Record the actual scope of implementation verification
performed in the implementation record.

### 5. Use repository-native tools and controlled dependencies

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

### 6. Verify each slice and the completed implementation

Use [evidence-and-completion.md](references/evidence-and-completion.md).

After each slice, verify requirement compliance, the focused test, relevant
regression, applicable integration behavior, type or compile status, lint, and
scope/constraint adherence. An implementation-time self-check is not an
independent code or security review and does not create those reports.

Before completion, freshly rerun the commands that prove the implementation:
new tests, affected-module tests, necessary integration and regression tests,
and applicable type-check, lint, formatting, migration, build, or runnable
suite commands. Read complete output and exit status.

Classify every check as passed, failed, not run, blocked, unavailable, or
limited to partial scope. Do not rely solely on earlier output, another
agent's claim, or code inspection.

### 7. Finalize the implementation record

Maintain
`docs/wewo/<requirement-category>/<requirement-slug>/implementation-record.md`
during implementation and finalize it with
[implementation-record-template.md](assets/implementation-record-template.md)
and [document-contract.md](references/document-contract.md).

Record actual changed files, slice status, Red/Green evidence, unit and
integration outcomes, quality checks, plan deviations, known limitations,
latest verification evidence, and remaining risks. Claim "implementation
complete" only when the latest evidence supports it.

After verifying the record, report:

- both workflow-document paths;
- implemented behavior and major changed files;
- actual test and quality-check results;
- unfinished work, blockers, and remaining risks.

Do not claim final independent review or a final test gate. Do not continue
automatically into browser acceptance execution, deployment, or another
capability's work.
