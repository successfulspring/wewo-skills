# Repository Analysis and Execution Record

Establish the tested code version, actual repository capabilities, and minimum
verification inventory before changing or executing tests.

## Scope resolution

Use the first applicable source:

1. explicit user scope;
2. identified feature, issue, bug, or verification obligation plus necessary
   regression;
3. explicit Diff and affected call paths;
4. current branch changes with confirmation of material boundaries.

Record branch or commit, tested code version, target Diff when applicable,
environment, objective, included scope, regression scope, excluded scope, and
limitations. For non-Git projects record the inspected file snapshot, execution
time, and unavailable revision honestly; Git is not an execution prerequisite.
Do not cite a commit as evidence of uncommitted files.

## Optional task scope

When the exact current requirement has neither `task-breakdown.md` nor `tasks/`
and no TASK is requested, retain ordinary scope resolution and root outputs.
Presence of either split material or an explicit TASK request activates task
resolution. Partial, unsafe, or inconsistent materials require clarification;
never silently revert to the ordinary root scope.

An explicit whole-requirement test request keeps requirement-wide selection
and does not require choosing a TASK. The following task-selection rules apply
when the requested execution is task-scoped.

Select a task only from an explicit TASK-ID, a path resolving to the current
requirement's `tasks/<TASK-ID>/task.md`, or the current conversation's unique
clearly established task. A sole directory, the newest directory, or a previous
report is not selection. Apply the existing path and source-access protections.
If selection is ambiguous, ask before executing or writing a task report.

Read the current `task-breakdown.md` as a bounded membership/dependency index,
the selected `task.md`, and root `prd.md` and `technical-design.md`. Check that
the selected member, safe path, scope, and dependencies agree. Task scope is
derived from the confirmed requirement/design; it cannot override them or turn
implementation-process reports into requirements. Read other task members only
when their named dependency or shared contract is necessary for this scope.
Cross-repository citations still require existing explicit source authorization;
do not scan a second repository or assume its task documents are synchronized.

Use `tasks/<TASK-ID>/test-execution.md` and `tasks/<TASK-ID>/test-artifacts/`
under this requirement for the task report and retained evidence. Only an
explicit whole-requirement execution request uses the original root report in
split mode. Preserve earlier root artifacts when selecting a task; do not move
or overwrite them. Native Runner output/configuration stays repository-native.
Record the task ID, boundaries, necessary regression, dependencies, and any
unverified requirement-level or integration-level obligations. A task gate
assesses only this scope, not completion of the entire requirement.

## Input rules

Use an explicitly supplied or conversation-established test-case artifact, or
the exact resolved requirement workspace's `test-cases.md`, as the primary
inventory. Relevant optional project/branch context supplies background and
constraints under existing authority; it cannot change case oracles, required
evidence, or routes. Apply the entrypoint's bounded historical lookup rules
without adding implementation-process or review artifacts as execution inputs.
Do not bulk-scan sibling requirements or another workspace. Never treat an
earlier report or label as current execution evidence, and never write
execution results back into a source test-case artifact.

In task mode, consume **Execution scope** from the single root `test-cases.md`:
select cases naming the chosen TASK-ID, including multi-task cases, and add
necessary regression based on affected interfaces/call paths with its basis
recorded. Requirement-level and Integration-level labels are distinct scopes;
do not silently treat them as completed by one task's execution. Include such a
case as necessary affected regression only when its scope and Oracle are
established and execution is authorized; disclose remaining broader obligations.
Scope selection never changes Steps, Expected Results, Test Level, Automation,
Route, or Runner, and never writes mapping or results back into the case file.

When an existing case document lacks, contradicts, or incompletely specifies
task mapping, ask for the missing associations or a targeted case-document
update. Do not infer missing task labels from case titles, treat the document
as absent, or claim complete task coverage. Explicitly established partial
obligations may still run with the mapping gap recorded and task completeness
unconfirmed. Do not manufacture a Pass for the full task from that subset.

Without usable cases, derive only the minimum execution inventory from the
current goal, explicit requirement evidence, actual Diff, public interfaces,
affected pages, existing executable tests, repository behavior, and material
risk. Do not fabricate an Oracle. Ask only when unresolved behavior changes
pass/fail.

## Mandatory repository inspection

Inspect as relevant:

- repository instructions and startup guidance;
- language, architecture, public interfaces, and affected modules;
- manifests, lockfiles, installed runtimes, and package-manager state;
- test directories, existing tests, fixtures, mocks, helpers, and page objects;
- runner, browser, coverage, reporter, and environment configuration;
- package scripts, Makefiles, CI commands, and documented test commands;
- databases, services, accounts, test data, and cleanup requirements;
- native result and artifact formats.

Do not run a detection command that may download software when files can show
whether it is declared. Use repository facts, not language stereotypes, to
resolve the execution seam and runner.

## Compact execution record

Track one row per independently reportable scenario. Keep this record internal
unless publishing it adds execution value.

```markdown
| Scenario ID | Source | Priority | Behavior / Oracle | Planned Automation | Resolved Route | Runner | Agent Tool Interface | Test Asset | Environment / Data | Status | Evidence | Failure / Blocker | Scope Exclusion |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Route, Status, and Failure/Blocker are orthogonal. For example:

```text
Route: Browser
Runner: Playwright Test
Agent Tool Interface: Playwright CLI
Status: Blocked
Blocker: browser runtime unavailable
```

Required Evidence, Route, Runner, and Agent Tool Interface are separate. An
interface may help inspect or execute without redefining the project Runner.
Do not add a second feasibility classification. Manual-only cases may be retained
only as scope exclusions and must not receive an execution status. Update the
record after asset changes, execution, triage, or blocker discovery. Preserve the
source behavior and Oracle throughout.
