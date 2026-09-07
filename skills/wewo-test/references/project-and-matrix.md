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
limitations.

## Input rules

Use an explicitly supplied or conversation-established test-case artifact, or
the exact resolved current Git branch and current requirement workspace's
`test-cases.md`, as the primary inventory. Never scan sibling requirements or
another branch workspace to discover a workflow artifact. Never treat an
earlier report or label as current execution evidence, and never write
execution results back into a source test-case artifact.

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
