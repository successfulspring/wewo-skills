# Dependency and Tool Policy

Prefer repository-native tools, versions, package manager, scripts, services,
and configuration.

## Discover before acting

Inspect manifests, lockfiles, tool-version files, task runners, CI
configuration, container definitions, repository instructions, and documented
commands. Do not guess a command that can be discovered.

## Distinguish restoration from introduction

- Restoring declared dependencies uses the existing manager and lockfile.
- Introducing a dependency changes the solution and requires justification.
- Upgrading versions, changing managers, rewriting lockfiles, changing CI,
  adding services, or installing system software may expand scope.

Obtain required confirmation before material dependency, lockfile, CI,
service, or system-level changes. Never silently upgrade or switch package
managers.

## Handle missing tools

When a command or tool is unavailable:

1. verify the project declares it;
2. identify the repository-native restoration command;
3. distinguish a missing install from a configuration or environment failure;
4. request approval where installation changes state or scope;
5. record the attempted command and actual failure;
6. continue with available verification where useful.

Do not claim success for a command that did not execute.

## External state

Default to no commit, push, merge, release, deployment, CI mutation, or remote
service change. Perform such actions only when explicitly requested,
authorized, and supported by the environment. Record the resulting evidence
without implying broader success.
