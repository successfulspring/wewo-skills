# Security and Reliability Review

Identify the attack surfaces actually changed, then apply relevant checks.

## Attack-surface inventory

Record:

```markdown
| Attack surface | Current change | Principal risks | Review status | Evidence |
|---|---|---|---|---|
```

Consider HTTP and public APIs, authentication, authorization, database writes,
files, callbacks, messages, external calls, dependencies, configuration,
administration, import/export, migrations, and sensitive data.

## Layered review

### L1: dangerous patterns

Check changed code for hardcoded secrets, dangerous execution, SQL or shell
concatenation, disabled TLS checks, broad CORS, plaintext passwords, and
untrusted input used as a file path. A pattern match is a candidate, not a
finding.

### L2: semantic Diff review

Trace:

```text
external input
-> validation and transformation
-> authentication and authorization
-> sensitive operation
```

Review new or changed entry points, parameters, writes, file operations,
external requests, configuration, and dependencies.

### L3: cross-file and business-flow review

Trace the applicable chain across controller, service, repository, database,
messages, caches, and external systems.

Perform L3 for login and permissions; orders, inventory, payments, and
refunds; files; callbacks; administration; batch operations; import/export;
public APIs; migrations; messaging; secrets; and configuration.

## Application security

Check authentication; role and resource authorization; IDOR; input validation;
SQL, command, template, and expression injection; XSS, CSRF, and SSRF; path
traversal and file upload/download; unsafe deserialization; secrets, tokens,
sensitive data, logs, and audit; callbacks; API abuse.

## Business security

Check state-machine bypass, duplicate financial or inventory operations,
parameter tampering, price and quantity bypass, approval bypass, replay, batch
limit bypass, client-only enforcement, and cross-user resource operations.

## Reliability and data safety

Check races, TOCTOU, duplicate submission, idempotency, transaction boundaries,
partial success, rollback, duplicate messages, retry side effects, cache and
message consistency, timeouts, migration safety, and shared-state pollution.

## Supply chain and configuration

Check dependency source and version, known vulnerabilities, CORS, debug
settings, TLS, default passwords, randomness, cryptography, container and CI
configuration, licenses when relevant, and secret exposure.

Do not mechanically reproduce this checklist in the report. Report applicable
attack surfaces, completed layers, verified evidence, gaps, and blockers.
