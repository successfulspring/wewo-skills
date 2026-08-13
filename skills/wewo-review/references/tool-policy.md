# Review Tool Policy

Use tools as evidence, never authority.

## Bundled helper execution

When a bundled review helper is needed and Node is available, execute the
bundled `.mjs` helper directly with Node. Do not alter the target package,
lockfile, configuration, or dependencies to run it.

Do not install Node solely to run a Wewo helper. When Node is unavailable,
disclose the helper limitation and use equivalent read-only Git evidence for
Diff metrics. Still attempt Semgrep through an equivalent safe approved direct
invocation when available or acquirable. Never claim a bundled helper ran when
it did not.

## Layer 1: semantic review

Each lane performs its assigned semantic reasoning from the Diff and affected
context. Tool absence never turns warnings into findings or replaces reviewer
reasoning.

## Layer 2: repository-native deterministic tools

Prefer configured compiler/type, lint, coding-rule, test, build, static,
secret, dependency, and security checks relevant to the Diff. Read commands and
versions from repository instructions and configuration. Run only safe checks;
record command, time, scope, exit status, and limitations.

## Layer 3: required Semgrep attempt

Every formal review must attempt Semgrep. Use
[run-semgrep.mjs](../scripts/run-semgrep.mjs) directly with Node when available,
with this acquisition order:

1. pre-existing usable Semgrep;
2. approved ephemeral isolation using an explicit repository, organization, or
   runtime pin when available;
3. approved unpinned ephemeral isolation resolved at execution time;
4. approved temporary isolated installation owned by this review;
5. honest `Blocked` or `Unavailable`.

A pin is preferred, not universally required. Its absence alone never blocks
approved acquisition. Record whether version resolution was `pinned`,
`runtime-resolved`, or `pre-existing`, plus the actual executed version. Binary
acquisition permission and rule-configuration permission remain separate.

Do not silently skip acquisition because Semgrep is absent. Seek required host
approval for network access or a material download. Never install into the
target repository, change its manifests or lockfiles, install globally,
disable TLS, use pipe-to-shell installers, or upload source implicitly.

### Recoverable authorization blockers

Before finalizing `Blocked`, Main asks once when a specific user authorization
is the only missing condition and an already-supported safe operation can
materially recover the Semgrep attempt. This includes approved external
registry/config access or isolated acquisition. State the exact permission,
why it is needed, the external access involved, that optional telemetry is
disabled where supported, that source is not silently uploaded, and that the
actual configuration source and tool version will be recorded.

After approval, perform the authorized resolution and report the scan's actual
outcome; approval is not scan success. After refusal, record `Blocked` and the
refused authorization. Do not ask again when the user or repository policy
already answered, the environment lacks a usable technical path, policy
prohibits the action, or the permission would be unsafe or insufficient.
Binary acquisition and rule-configuration authorization remain separate.

Prefer trusted repository-local or explicitly supplied local configuration.
Use trusted external registry rules only when outbound access is permitted;
disable optional telemetry where supported and record registry access. Do not
assume registry access means source upload.

Record acquisition mode, actual version, configuration source, scan target,
argv-equivalent invocation, outcome, raw warnings/errors, coverage completeness,
stdout/stderr limitations, and cleanup. Distinguish `Completed - findings
produced`, `Completed - no findings`, `Failed`, `Blocked`, and `Unavailable`;
command execution alone is not a Pass. Parseable raw errors require an explicit
partial-coverage limitation, even when the status says no findings.

Never uninstall or mutate a Semgrep installation that existed before review.
Remove only isolated temporary resources created and recorded by this review,
including after scan failure where safe. Do not delete shared caches.

Every warning remains a tool candidate until Finding Admission verifies its
semantics, reachability, attribution, impact, and root cause.

## Layer 4: additional specialty tools

Use configured or materially useful specialty tools when safe. Do not require
or temporarily stand up heavy platforms merely to satisfy review. Preserve
their raw outputs separately from formal findings.
