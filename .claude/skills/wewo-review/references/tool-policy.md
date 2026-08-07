# Review Tool Policy

Use tools in three layers and preserve evidence integrity.

## Layer 1: semantic review

Always perform Diff inspection, file reading, code search, call-path tracing,
requirements comparison, and permission, transaction, and test semantics.
Missing specialty tools never stop this layer.

## Layer 2: repository-native tools

Prefer configured unit and integration tests, type checking, lint, formatting
checks, compilation, build, coverage, migration checks, and security rules.
Read commands from repository instructions, CI, README files, Makefiles,
manifests, or scripts. Do not guess.

Run only checks safe for the current environment. Avoid commands that mutate
production data, require production credentials, or create uncontrolled
external side effects. Record command, time, scope, exit status, and relevant
output. Classify unavailable or blocked checks honestly.

## Layer 3: optional specialty tools

Select SAST, secret, dependency, configuration, container, IaC, complexity,
contract, or license tools only when the stack and attack surface justify
them. Their output strengthens evidence but is not a prerequisite for review.

## Controlled temporary installation

Automatic temporary installation requires all of:

- an approved allowlist and trusted source;
- a fixed version;
- an isolated temporary environment;
- no project dependency or lockfile modification;
- no administrator rights or global-environment pollution;
- no persistent service;
- no source upload;
- complete installation and cleanup records.

Obtain user confirmation before Docker use, large downloads, system or
administrator installation, background services, project-environment or
lockfile changes, source upload, production access, or any unclear source or
version.

Never use pipe-to-shell installers, unknown binaries, disabled TLS
verification, production secrets, automatic company-source upload, or system
security-policy changes.

If installation fails, continue semantic review and record the unverified
scope. Cleanup only paths created for the temporary tool after resolving and
checking their exact locations.

## Warning verification

For every warning:

1. locate the relevant code;
2. establish whether the path is reachable;
3. determine whether input is controllable;
4. inspect existing defenses;
5. attribute it to the current change;
6. deduplicate the root cause;
7. classify it as Confirmed, Potential, Unverified, Rejected, or Existing
   Issue.

Never use a raw warning count as a formal finding count.
