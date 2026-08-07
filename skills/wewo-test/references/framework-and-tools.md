# Framework Discovery and Tool Policy

Prefer project-native tools and control every persistent or high-impact change.

## Declared tools

Read manifests, lockfiles, configuration, test directories, scripts, CI, and
runtime/browser versions. Restore declared dependencies through the existing
package manager and pinned versions. Do not silently upgrade versions, switch
package managers, or rewrite lockfiles.

Reuse existing commands and configurations. Do not invent commands from
general framework knowledge when repository sources define them.

## Persistent framework changes

Before adding a framework or runner that should remain in the project, present
one proposal identifying effects on:

- dependency declarations and lockfiles;
- runner and reporter configuration;
- test directories and scripts;
- CI and `.gitignore`;
- Docker services or test databases;
- browsers, services, or cloud platforms.

Obtain confirmation before executing the agreed material changes. A confirmed
proposal covers its listed files; do not repeatedly ask per file.

## Isolated temporary use

For one-time validation, prefer a temporary directory or isolated environment,
a fixed trusted version, no project dependency changes, and cleanup after
execution.

Obtain confirmation before system packages, administrator privileges, Docker,
large browser downloads, system Chrome, persistent services, lockfile or CI
changes, external cloud testing, or source/test-data upload.

Never use pipe-to-shell installers, unknown binaries, disabled TLS checks,
production secrets, global-environment pollution, automatic company-source
upload, or destructive production tests.

If installation fails:

- record the command and failure;
- mark affected tests Blocked or Not Run;
- execute remaining safe tests;
- document degraded evidence and residual risk;
- clean only exact temporary paths created for this task.

Tool installation is not a test result.

## Optional host capabilities

Use browser control, MCP, or subagents only when they improve the supported
workflow. The core fallback is the repository-native CLI, direct file and
configuration inspection, and executable manual tasks. Do not block unrelated
test levels because an optional host capability is absent.
