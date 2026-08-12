# Contextual Security Lane

Start from changed attack surfaces rather than a generic checklist. Analyze the
applicable chain:

```text
changed entry point -> asset -> trust boundary -> source/input -> propagation
-> controls -> sensitive operation/sink -> reachable impact
```

Begin from factual hints such as changed endpoints, authorization, persistence,
file handling, external requests, events/jobs, LLM/tool boundaries, or
sensitive state transitions. Trace across files and functions only when an
applicable attack or control path requires it; do not eagerly read the entire
changed scope. Establish concrete plausible paths or state an explicit
unverified gap.

Consider only applicable authentication, authorization/ownership/tenant
isolation, injection, command execution, SSRF, traversal, files,
deserialization, secrets and sensitive data, business authorization and state,
transactions, concurrency, idempotency, retries, caches/messages, external
systems, dependencies/configuration, and LLM/model-output or prompt-injection
trust boundaries.

Deeply inspect tests/fixtures only when security-relevant: secrets, sensitive
data, production systems/accounts, dangerous side effects, authorization
fixture semantics, or unsafe trust-boundary behavior. Keep ordinary test
quality in the Static lane.

For each path, inspect who controls the source, how data propagates, which
validation/sanitization/authorization controls apply, whether the sensitive
operation is reachable, and the concrete security or business-integrity impact.

Perform this lane independently before seeing Static or Semgrep candidates.
Do not merely repeat pattern warnings or print irrelevant checklist sections.
Return candidates with attack path, evidence, defenses, attribution, impact,
remediation, suggested security verification, and limitations.
