# Project Analysis and Execution Matrix

Establish the actual code version, project capabilities, and unified scenario
inventory before generating or executing tests.

## Scope resolution

Use the first applicable source:

1. explicit user scope;
2. identified feature, issue, bug, or acceptance requirement plus necessary
   regression;
3. explicit Diff and affected call paths;
4. current branch changes with confirmation of material boundaries.

Record current branch or commit, tested code version, target Diff when
applicable, environment, objective, included scope, regression scope,
excluded scope, and limitations.

## Input priority

Use current user requirements and actual project behavior first. Reuse
`test-plan.md` and `test-cases.md` only when the user explicitly supplies or
references them, or the current conversation already establishes them:

- an explicitly established `test-cases.md` as the primary scenario inventory;
- an explicitly established `test-plan.md` as optional scope and strategy
  context.

Never scan `docs/wewo/` or the repository to discover these documents. Never
treat a prior report or label as current execution evidence. Keep execution
status, logs, screenshots, and actual responses out of test-planning documents.

Without usable testing artifacts, derive the minimum matrix from the user
goal, actual Diff, public interfaces, pages, existing tests, repository
behavior, and risk. Ask when an unresolved expectation affects pass/fail.

## Project analysis

Inspect:

- repository instructions and project startup guidance;
- language, framework, architecture, and affected modules;
- dependency manifests and lockfiles;
- existing test directories, frameworks, fixtures, mocks, and helpers;
- runner, coverage, reporter, E2E, browser, and environment configuration;
- package scripts, Makefiles, CI, and documented commands;
- installed runtimes, executables, and browsers;
- database, service, account, and test-data requirements.

Do not run a detection command that may trigger a download when project files
can establish whether a tool is declared.

## Matrix contract

Use one row per independently reportable scenario:

```markdown
| Scenario ID | Source | Objective | Priority | Risk | Recommended level | Required evidence | Actual level | Automation status | Framework/seam | Environment/data | Execution status | Evidence | Defect/blocker | Manual task |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
```

Keep expected behavior separate from execution method. A level or tool may
change without changing the expected outcome.

Update the matrix after every generated asset, execution, triage decision,
manual result, or blocker. Do not reconstruct it from memory at the end.
