# Repository-Native Framework and Tool Policy

Reuse established repository test infrastructure before adding a framework.
The repository-native CLI is the universal fallback.

## Contents

- [Operational recipe priority](#operational-recipe-priority)
- [Discover before selecting](#discover-before-selecting)
- [Declared dependencies](#declared-dependencies)
- [Tool Capability Resolution](#tool-capability-resolution)
- [Quick Runner Recipes](#quick-runner-recipes)
- [Minimal durable asset shapes](#minimal-durable-asset-shapes)
- [Persistent framework addition](#persistent-framework-addition)
- [High-impact actions](#high-impact-actions)
- [Optional interfaces](#optional-interfaces)
- [Durable portability](#durable-portability)

## Operational recipe priority

Use this order after resolving the Route and repository-native Runner:

```text
repository-defined script or command
-> repository-local Runner
-> documented minimal tool recipe
-> local Runner help or diagnosis when still unclear
```

For example, prefer an authoritative `npm run test:e2e` script over manually
reconstructing a Playwright command. Minimal recipes below are fallbacks, not
replacements for repository configuration.

## Discover before selecting

Inspect manifests, lockfiles, test directories, runner configurations,
fixtures, mocks, helpers, page objects, package scripts, Makefiles, CI
commands, browser configuration, coverage, reporters, and database/test-service
setup. Reuse repository commands and configuration rather than hardcoding
global commands.

Representative stacks such as pytest, unittest, Vitest, Jest, Maven/Gradle,
`go test`, Playwright, Cypress, Pact, k6, Locust, or JMeter are examples only.
Never encode them as universal language-to-runner mappings.

## Declared dependencies

When the project already declares the required dependency:

- restore it with the repository-native package manager;
- reuse the pinned version and existing lockfile;
- reuse existing configuration and scripts;
- avoid repeated confirmation unless the restore is high impact.

Do not silently upgrade versions, switch package managers, or rewrite a
lockfile.

## Tool Capability Resolution

After discovering the repository-native Runner, inspect available agent
capabilities when useful for the resolved Route. Candidates may include normal
shell/CLI execution, Playwright Test agent tools, Playwright CLI, Playwright
MCP, browser control, or other already available test interfaces.

Record the selected Agent Tool Interface internally when it affects execution
or diagnosis. Do not require preconfiguration of any particular interface. A
specific capability being absent does not make the skill unavailable when the
repository Runner has another valid path. MCP, Playwright CLI, and Playwright
Test agent tools remain optional; shell execution of repository commands
remains valid.

Do not force Playwright because Playwright-oriented tools happen to be
available. Resolve repository tooling before agent tooling. For non-browser
Unit, API, Integration, Component, and Contract routes, prefer the native CLI
and avoid adding MCP concepts without a concrete need.

## Quick Runner Recipes

Use only the section matching the resolved Runner. Respect the repository's
package manager, wrapper, configuration, paths, and scripts.

### pytest

Do not assume pytest merely because the project is Python.

```bash
pytest
pytest tests/test_order.py -q
pytest tests/test_order.py::test_create_order -q
pytest --junit-xml=test-results/pytest.xml
```

### Vitest

```bash
npx vitest run
npx vitest run src/order.test.ts
```

### Jest

```bash
npx jest
npx jest path/to/test
```

### Go

```bash
go test ./...
go test -json ./...
```

### Maven

```bash
mvn test
mvn -Dtest=OrderServiceTest test
```

### Gradle

Prefer the checked-in wrapper over a global Gradle installation.

```bash
./gradlew test
./gradlew test --tests OrderServiceTest
```

On Windows, use the corresponding repository wrapper:

```powershell
.\gradlew.bat test
```

### Cypress

```bash
npx cypress run
npx cypress run --spec "cypress/e2e/order.cy.ts"
```

### API, contract, and performance

Reuse the repository-native API, contract, or performance runner and its
existing collections, schemas, thresholds, scripts, and service setup. Do not
introduce a universal tool mapping for these routes.

## Minimal durable asset shapes

Follow existing repository conventions first. When a missing asset must be
created, use the smallest recognizable shape and add real setup and assertions
for the unchanged Oracle.

pytest:

```python
def test_price_rule():
    result = ...
    assert result == ...
```

Vitest:

```ts
import { describe, expect, it } from 'vitest';

describe('price rule', () => {
  it('applies the expected tier', () => {
    expect(actual).toBe(expected);
  });
});
```

These intentionally incomplete snippets show structure only. Replace
placeholders with repository-established calls and requirement-defined
expected results; do not invent names, values, imports, or Oracles.

## Persistent framework addition

When no suitable framework exists and persistent adoption is necessary,
present one scoped proposal covering applicable:

- dependency and lockfile changes;
- test directory, runner, reporter, and configuration changes;
- browser installation;
- package scripts, CI, and `.gitignore` impact;
- Docker services, test databases, or external platforms.

Obtain confirmation once for the agreed scope. Do not ask once per file.

## High-impact actions

Require explicit confirmation for system-wide package installation,
administrator privileges, Docker or service provisioning, large browser
downloads, system Chrome, persistent background services, external cloud
testing, source/test-data upload, or production-like destructive execution.

Never use pipe-to-shell installers, unknown binaries, disabled TLS checks,
production secrets, global-environment pollution, automatic company-source
upload, or uncontrolled production tests.

Do not install a new language/runtime solely to use an optional Agent Tool
Interface.

Before a destructive, install, migration, external, or unfamiliar command, do
not guess. For version-sensitive syntax, prefer the repository script, then the
local Runner's `--help` or maintained documentation, then execute. Examples
include `pytest --help`, `npx vitest --help`, and
`npx playwright test --help`. Use help only when needed, not before every known
command.

If setup fails, retain the command and failure evidence, mark only affected
tests `Blocked` or `Not Run`, continue remaining safe tests, report degraded
evidence, and clean only exact temporary paths created for the task. Tool
installation is not a test result.

## Optional interfaces

Browser control, Playwright CLI, Playwright MCP, other MCP interfaces, and
subagents are optional execution aids. Their absence must not block unrelated
testing or a project whose normal suite runs through its configured CLI.

Do not add a universal runner wrapper or an HTML aggregation layer. Execute
real repository runners directly and retain their native evidence.

## Durable portability

Keep durable tests and test configuration independent of a particular user or
machine. Do not persist user-specific absolute paths, local skill installation
paths, hardcoded browser-cache directories, machine-specific Chromium
executables, or accidental transitive dependencies.

Prefer repository-declared dependencies and scripts, official framework
discovery/install behavior, relative project paths, and environment variables
only when they represent intentional project/runtime configuration.
