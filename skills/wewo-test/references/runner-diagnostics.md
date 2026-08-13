# Runner Diagnostics

Diagnose a repository-native Runner before fallback or replacement. Preserve
the first failure, command, exit status, logs, code version, environment, and
relevant configuration.

## Contents

- [Command confidence](#command-confidence)
- [Bounded diagnostic sequence](#bounded-diagnostic-sequence)
- [Diagnostic command patterns](#diagnostic-command-patterns)
- [Attribution and repair](#attribution-and-repair)
- [Repository-specific workarounds](#repository-specific-workarounds)

## Command confidence

Exact commands vary by repository and tool version. Prefer repository-native
scripts and current installed-Runner help or output when uncertain:

```text
repository script
-> local Runner --help or maintained CLI documentation
-> diagnostic command
```

Use help when syntax is unfamiliar or version-sensitive, not before every
known command. Do not guess destructive, install, migration, external, or
unfamiliar commands.

## Bounded diagnostic sequence

Inspect only as far as needed to establish a cause:

1. command, arguments, working directory, and selected configuration;
2. test discovery patterns, filters, paths, and selected target;
3. test import, module loading, compilation, and configuration parsing;
4. declared and restored dependencies, lockfile, and framework version;
5. language/runtime version expected by the repository;
6. framework/runtime compatibility supported by project or official evidence;
7. worker or child-process creation and resource limits;
8. browser executable/runtime startup when applicable;
9. application/server readiness, URL, health, ports, and startup logs;
10. environment variables, services, accounts, fixtures, and test data.

Do not repeatedly rerun an unchanged failing command without a diagnostic
hypothesis. Keep attempts bounded and retain each materially distinct result.

## Diagnostic command patterns

Use the resolved repository command first. These commands are conservative
fallback patterns for the corresponding local Runner.

### Playwright Test

Check collection and selected configuration before browser startup:

```bash
npx playwright test --list
npx playwright test -c <config> --list
```

Isolate worker or concurrency startup behavior:

```bash
npx playwright test <spec> --workers=1 --reporter=list
```

### pytest

```bash
pytest --collect-only
pytest <test> -vv
```

`<test>` may be a repository-relative file or collected node ID.

### Vitest

For installed versions that support the `list` command:

```bash
npx vitest list
```

If unavailable, inspect the repository's pinned version and
`npx vitest --help` rather than substituting guessed syntax.

### Jest

```bash
npx jest --listTests
npx jest path/to/test --runInBand
```

Use serial execution only to isolate worker/process behavior.

### Go, Maven, and Gradle

Keep diagnosis close to the normal repository command and add verbosity only
when useful:

```bash
go test -json ./...
mvn -Dtest=OrderServiceTest test
./gradlew test --tests OrderServiceTest --info
```

Use `gradlew.bat` on Windows when that is the checked-in wrapper. Do not replace
a wrapper, module-specific Maven goal, or repository package selection with a
generic command.

## Attribution and repair

A timeout or startup failure does not by itself prove Product Defect,
Environment Blocker, or unsupported Runner. Determine whether evidence supports
Test Defect, test configuration defect, dependency/runtime incompatibility,
Environment Blocker, unsupported Runner, or another infrastructure issue.

Repair permitted tests, fixtures, test configuration, discovery settings, and
declared test infrastructure when the defect is in scope and the repair does
not weaken the Oracle. Rerun focused scope after repair.

Fallback to another Runner or Agent Tool Interface only when evidence shows the
current path is unsupported, unavailable, unsafe, or disproportionately broken
and the fallback preserves Required Evidence. Record the reason and any change
in native evidence. An Agent Tool Interface failure does not justify replacing
a healthy repository Runner when shell/CLI or another valid interface exists.

## Repository-specific workarounds

Keep a workaround scoped to the repository's observed framework, runtime,
version, and environment. Do not generalize project-specific environment flags,
browser paths, cache locations, executable overrides, or compatibility hacks
into universal policy. Prefer an official or repository-declared fix when
available.
