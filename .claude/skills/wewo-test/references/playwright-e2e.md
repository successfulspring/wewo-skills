# Playwright Web E2E

Use this branch only for scenarios that require browser-level evidence. A
scenario whose Required Evidence Level is E2E must finish through this branch
as Passed or Failed, or be explicitly classified Blocked or Not Run; missing
tooling follows the approval and setup rules in framework-and-tools.md instead
of silently lowering the evidence level.

## Preparation

1. Inspect package manifests, lockfiles, E2E directories, Playwright
   configuration, scripts, and CI.
2. Reuse an existing Playwright installation and pinned version.
3. When absent, decide between confirmed persistent adoption and fixed-version
   isolated temporary use.
4. Prefer Playwright-bundled Chromium.
5. Use system Chrome, Firefox, WebKit, or device emulation only when required.
6. Confirm base URL, environment type, account, data, cleanup, and side
   effects.
7. Inspect the real page and identify stable locators.

Do not run a detection command that may download browsers before checking
project declarations.

## Test construction

Express user-observable behavior. Prefer `getByRole`, `getByLabel`,
`getByPlaceholder`, `getByText`, and justified `getByTestId`. Use CSS or XPath
only when no stable semantic locator exists.

Use web-first assertions and automatic waiting. Do not generate hardcoded
timeouts, execution-order dependencies, shared mutable business data, brittle
hierarchical selectors, internal-DOM-only assertions, or tests without
side-effect cleanup.

Follow existing Page Object conventions. Introduce a page or component object
only for repeated interactions; simple scenarios may remain directly in the
spec.

## Execution

1. Run one focused test.
2. Fix locator, setup, data, fixture, or assertion defects without weakening
   expected behavior.
3. Run the target E2E set.
4. Run necessary regression.
5. Collect configured HTML and JSON/JUnit reports, failure screenshots, Trace,
   and only necessary video.
6. Map the result and artifacts to the source scenario.

Automatic retries are diagnostic support. Preserve first-failure evidence and
mark mixed unchanged-code/environment outcomes Flaky.

If no safe browser execution path exists, mark the scenario Blocked or route
it to an executable manual task. Never fabricate screenshots, traces, or
browser results.
