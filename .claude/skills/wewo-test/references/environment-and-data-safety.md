# Environment and Test-Data Safety

Confirm safety before tests can write or trigger external effects.

## Pre-execution confirmation

Record:

- URL and environment type: local, test, staging, or production;
- code version and deployment identity;
- test account and authorization scope;
- data ownership and deletion capability;
- real email, SMS, payment, callback, or external-service effects;
- shared inventory, financial, or business data;
- batch, concurrency, and performance permission;
- cleanup method and residual risk.

Do not default to production writes. Stop before destructive, financial,
external, shared-data, or production behavior without explicit safe
authorization.

## Production-like evidence

Do not invent a production-like environment. Production-like evidence becomes
relevant only when established by project deployment or start conventions, an
acceptance environment, project requirements, or the user's explicit test goal.

When production-like evidence is relevant:

- record the environment or mode actually tested;
- development-mode evidence proves only development-mode behavior;
- development success does not prove production-like coverage, production
  readiness, or deployment-mode correctness.

If production-like execution is attempted but blocked, record the
production-like environment evidence as Blocked with the concrete blocker. If
production-like verification is relevant but intentionally not attempted,
record it as Not Run with the reason. A development-mode fallback may provide
supplementary evidence but does not replace the missing production-like
evidence. Keep scenario execution status and environment coverage distinct.

## Data lifecycle

Prefer:

```text
create uniquely identifiable data
-> execute independently
-> verify observable outcomes
-> clean up created data
-> verify cleanup
```

Avoid execution-order dependencies. When shared accounts or data cannot be
isolated, reduce parallelism, serialize affected tests, use unique identifiers,
record cleanup, and disclose residual risk.

Authentication state, cookies, tokens, and credentials must use test accounts,
remain outside version control and public artifacts, and be cleaned according
to repository policy.

## Artifact sanitation

Before saving logs, HTML, JSON/JUnit, screenshots, traces, video, coverage, or
performance output:

- redact credentials, tokens, cookies, secrets, and sensitive headers;
- remove or mask production and personal data;
- avoid copying entire environment dumps;
- retain only evidence necessary to support the result;
- document material redaction without exposing the removed value.

Record cleanup as Passed, Failed, Blocked, Not Run, or Not Applicable. A failed
cleanup is a test risk and may affect the gate.
