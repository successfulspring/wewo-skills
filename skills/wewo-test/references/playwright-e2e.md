# Durable Browser Automation

Use this branch when the case requires browser-visible evidence. Preserve that
evidence surface even when a lower-level implementation seam exists.

## Contents

- [Browser execution architecture](#browser-execution-architecture)
- [Resolve the Runner](#resolve-the-runner)
- [Resolve Agent Tool Interfaces](#resolve-agent-tool-interfaces)
- [Playwright Test operational recipes](#playwright-test-operational-recipes)
- [Reconnaissance versus durable execution](#reconnaissance-versus-durable-execution)
- [Generator-style workflow](#generator-style-workflow)
- [Construct durable tests](#construct-durable-tests)
- [Execute and preserve evidence](#execute-and-preserve-evidence)

## Browser execution architecture

Use this order:

```text
Required Browser Evidence
-> Repository Browser Framework Discovery
-> Agent Browser Capability Discovery
-> Live Browser Reconnaissance when useful
-> Durable Test Generation
-> Repository-native Browser Runner
-> Native Evidence
-> Failure Triage
```

Do not let an Agent Tool Interface alter required evidence or the selected
repository framework.

## Resolve the Runner

1. Inspect browser test paths, manifests, lockfiles, configuration, fixtures,
   page objects, scripts, CI, installed runtimes, and browser availability.
2. Reuse project-local Playwright Test, its pinned version, configuration, and
   repository commands when present.
3. If an established Cypress or other durable browser suite exists, it may
   satisfy an Automation annotation of `Playwright` only when the user did not
   explicitly require Playwright itself, no Playwright-specific behavior is
   involved, and the same browser evidence is preserved. Record the Runner.
4. When no suitable browser framework exists, propose Playwright Test as the
   default persistent addition and obtain confirmation under the framework and
   tool policy.

Do not replace an established Cypress suite merely for standardization or
install Cypress and Playwright together without a concrete project reason. Do
not run a detection command that may download a browser before inspecting
project declarations.

Inspect `package.json`, the lockfile, `playwright.config.*`, existing
`*.spec.*` files, fixtures, authentication setup, and package scripts first.
When npm is the repository package manager and no script is more authoritative,
this checks for an already available local CLI without installing it:

```bash
npx --no-install playwright --version
```

Use the equivalent repository-local invocation for pnpm, Yarn, Bun, or another
established package manager. A failed detection command is setup evidence, not
permission to download or replace the Runner.

The repository-native Runner remains authoritative. Available Playwright tools
do not justify replacing Cypress. A Playwright repository continues to use
Playwright Test even when optional Playwright-specific agent interfaces are
unavailable.

## Resolve Agent Tool Interfaces

Treat these capabilities separately:

- `Playwright Test`: durable repository browser test Runner.
- `Playwright Test agent tools`: optional interfaces for test generation,
  execution assistance, debugging, and browser interaction.
- `Playwright CLI`: optional coding-agent interface for reconnaissance,
  locator discovery, debugging, and console/network inspection.
- `Playwright MCP`: optional browser interaction and reconnaissance interface.
- normal shell/CLI: valid fallback for repository commands.

Do not require an agent interface or confuse interface success with Runner
success. Playwright MCP may perform reconnaissance against an application whose
durable suite uses Cypress, but the case passes only when Cypress executes its
repository asset successfully.

## Playwright Test operational recipes

Prefer the repository's script, configuration, package manager, and local
Runner. Use these minimal npm-style recipes only when the repository does not
define a more specific command.

### Test discovery

Use listing as the first Playwright diagnostic when collection or configuration
selection is unclear:

```bash
npx playwright test --list
npx playwright test -c <config> --list
```

### Focused execution

```bash
npx playwright test <spec>
npx playwright test <spec> -g "<pattern>"
```

Paths and title patterns must come from repository discovery or the source
case. Do not guess them.

### Single-worker diagnostic execution

Use this to isolate worker, concurrency, or reporter noise; it is not the
default project command:

```bash
npx playwright test <spec> --workers=1 --reporter=list
```

### Native HTML report

Preserve existing reporter configuration. When HTML is intentionally selected:

```bash
npx playwright test --reporter=html
npx playwright show-report
```

Do not force HTML when the repository uses another native reporter. Reporter
overrides may change evidence behavior, so record them when used.

## Reconnaissance versus durable execution

Live browser reconnaissance is optional agent assistance. When available and
useful, the interfaces above may help discover page structure, accessible
names, stable locators, navigation, rendered states, console/network activity,
and debugging context.

Reconnaissance alone is not durable execution. Do not treat “the agent clicked
through successfully” as a passing automated regression case. A durable case
must reuse or create a normal repository browser test asset, such as a
project-native `*.spec.ts`, `*.cy.ts`, or equivalent file, and execute it with
the repository-native Runner.

Absence of Playwright Test agent tools, Playwright CLI, or Playwright MCP does
not block a configured browser suite or unrelated routes. The repository-native
CLI remains the fallback.

When Playwright CLI is already available and useful for reconnaissance, a
minimal interaction may use:

```bash
playwright-cli open <url>
playwright-cli snapshot
playwright-cli click <ref>
playwright-cli fill <ref> "<value>"
playwright-cli console
playwright-cli requests
```

Use snapshot refs from the current rendered page and re-snapshot after material
state changes. Playwright Test agent tools may perform equivalent generation,
execution assistance, or interaction through their available interface.
Playwright MCP may inspect and interact through its exposed browser operations.
Do not require or emulate an unavailable interface.

## Generator-style workflow

When generating a new durable browser test and live access is available and
useful, prefer:

```text
scenario
-> interact with the real rendered page
-> verify every material interaction and state
-> discover stable locators
-> generate the durable repository test asset
-> execute it with the repository Runner
```

Do not guess DOM structure or locators solely from requirements when the real
page can safely provide better evidence. Reconnaissance is not mandatory when
existing fixtures, page objects, locators, or test abstractions are clear,
stable, and sufficient.

## Construct durable tests

Express user-observable behavior. With Playwright, prefer `getByRole`,
`getByLabel`, `getByPlaceholder`, `getByText`, and justified `getByTestId`.
Use CSS or XPath only when no stable semantic locator exists.

Minimal TypeScript examples:

```ts
await page.getByRole('button', { name: '提交' }).click();
await page.getByLabel('邮箱').fill('user@example.com');
await page.getByPlaceholder('搜索').fill('keyword');
await expect(page.getByText('提交成功')).toBeVisible();
await expect(page).toHaveURL(/success/);
```

Use locator priority: role, label, placeholder, visible text, justified test ID,
then justified CSS. Avoid brittle DOM hierarchy and XPath unless genuinely
necessary.

Use web-first assertions and automatic waiting. Do not use hardcoded sleeps,
arbitrary fixed waits, brittle hierarchy selectors, hidden shared mutable
state, execution-order dependencies, internal-DOM-only assertions, or tests
without side-effect cleanup.

Follow established fixture and Page Object conventions. Introduce an
abstraction only when repeated interactions justify it.

A new Playwright Test asset normally starts with the repository's established
imports and fixture shape, for example:

```ts
import { expect, test } from '@playwright/test';

test('observable behavior', async ({ page }) => {
  // Arrange and act through public browser behavior.
  // Assert the requirement-defined observable result.
});
```

Replace comments with concrete repository-aware actions and assertions. Do not
publish a speculative test as complete.

## Execute and preserve evidence

1. ensure the application can run safely in the recorded environment;
2. optionally perform live browser reconnaissance;
3. reuse or create the durable spec;
4. run the focused spec with the repository-native Runner;
5. preserve the first failure and diagnose Runner, configuration, dependency,
   runtime, browser, server, test, fixture, locator, and data causes;
6. repair permitted test infrastructure defects before justified fallback;
7. rerun after permitted test-asset or infrastructure repairs;
8. run the relevant browser target and affected regression;
9. collect configured native evidence such as terminal output, HTML report,
   JSON/JUnit, Trace, screenshots, or necessary video;
10. sanitize artifacts, clean data, and map evidence to the source case.

HTML, Trace, screenshots, and video are native evidence when configured and
useful, not mandatory universal formats. Automatic retries are diagnostic;
they do not erase the initial failure. Apply bounded stability evidence when
unchanged runs produce mixed results.

If no safe durable browser path exists, use `Blocked` or justified `Not Run`
with the concrete reason. Manual execution is outside this capability and
cannot replace required automated browser evidence.

Completion requires all three:

```text
durable repository test asset
+ repository-native Runner execution
+ native evidence
```

Live MCP, CLI, test-agent, or browser interaction alone is not durable
automated test completion.
