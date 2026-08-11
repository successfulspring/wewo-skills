# Dependency and Tool Policy

Prefer repository-native tools, versions, package managers, scripts, services,
and configuration. Do not add generic Build wrappers for tests, lint, TDD, or
implementation verification.

## Discover before acting

Inspect only relevant manifests, lockfiles, tool-version files, task runners,
CI configuration, Docker or container definitions, repository instructions,
and documented commands. Do not guess a discoverable command.

Ordinary repository-native test, lint, type, format, build, and read-only
inspection commands do not require a material-change confirmation merely
because they are implementation tools.

## Distinguish restoration from material introduction

- Restore declared dependencies with the existing manager and lockfile.
- Treat introducing, removing, or upgrading a material dependency as a
  solution change requiring justification and confirmation unless it was
  already explicitly included in the confirmed implementation plan.
- Treat lockfile-wide changes caused by a dependency decision as part of that
  material decision.
- Never silently switch package managers or dependency strategies.

## High-impact change gate

When implementation discovers an unplanned need to introduce or materially
modify any of the following, stop and obtain explicit confirmation before
performing it:

- dependencies or broad lockfile state;
- persistent schema or migration strategy;
- public APIs;
- CI configuration;
- Dockerfile, compose, or other Docker/container configuration;
- production-environment configuration;
- service, process, or system configuration;
- deployment behavior or topology;
- infrastructure-affecting behavior;
- authentication, authorization, or security boundaries.

Explain the discovered need, invalidated assumption, impact, recommended
resolution, and relevant alternatives. Update the implementation plan after
confirmation. Do not over-gate ordinary commands or private implementation
details that preserve the confirmed contract.

## Handle missing tools

When a command or tool is unavailable:

1. verify whether the project declares it;
2. identify the repository-native restoration command;
3. distinguish a missing install from configuration or environment failure;
4. request approval where installation changes state or scope;
5. record the attempted command and actual failure;
6. continue with available verification where useful.

Never claim success for a command that did not execute.

## External state

Default to no commit, push, merge, release, deployment, CI mutation, remote
service change, or system-wide installation. Perform external actions only
when explicitly requested, authorized, and supported. Record the exact result
without implying broader success.
