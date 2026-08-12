# Requirement, Risk, and Scenario Design

Turn authoritative requirements into semantic test obligations and scenarios
before selecting Test Level or Automation. Ask for each material behavior:

```text
What can fail?
What behavior must be verified?
What scenario provides distinct evidence?
What observable outcome means pass or fail?
```

## Requirement and behavior model

Identify applicable actors, roles, ownership, resources, actions, inputs,
outputs, defaults, states and transitions, rules and combinations,
calculations, side effects, persistence, lifecycle, asynchronous behavior,
dependencies, UI behavior, and errors. Trace each material requirement or risk
to one or more distinct evidence needs.

Do not organize generation by Unit, Integration, API, System, or E2E, and do
not seek a balanced pyramid or fixed ratios. Repository functions and classes
are not automatic obligations. An authoritative technical design or external
contract may legitimately define API, transaction, idempotency, state,
database, or producer/consumer evidence before implementation exists.

## Scenario-generation lenses

Apply each lens only where it can expose a distinct requirement or risk.

### Business flow

Cover the happy path, alternative flow, negative flow, and critical user or
business journey. Follow realistic entry, action, state/effect, and observable
outcome rather than producing a flat feature checklist.

### Input and data

Use equivalence partitions and boundary-value analysis. Consider valid,
invalid, empty, missing, minimum/maximum/just-inside/just-outside values,
special characters, types/formats, defaults, and cross-field constraints when
they change behavior or risk.

### Business logic

Use decision tables for rule combinations and conditional outcomes. Consider
calculations and rounding, repeated actions, duplicate submissions,
idempotency, defaults, and combinations that change the result. Do not test
every permutation when representative evidence is sufficient.

### Lifecycle and state

Use state-transition analysis for valid and invalid transitions, persistence,
refresh/restore, cancel, rollback, retry, recovery, terminal states, delayed
work, and stale updates where applicable.

### Access and trust

Consider role, permission, ownership, unauthenticated access, unauthorized
access, privilege bypass, cross-user isolation, and sensitive-data exposure
when the behavior crosses an access boundary.

### Reliability and technical contracts

Only when requirements, design, or an implementation-aware risk supports it,
consider dependency failure, timeout, retry, partial failure, rollback,
recovery, concurrency, idempotency, consistency, transactions, messages,
caches, external adapters, migration, performance, and compatibility. Do not
invent mechanisms or thresholds.

### Security

When relevant, model source -> trust boundary -> transformation/control ->
sensitive sink/effect. Consider malicious or malformed input, authorization,
injection, untrusted external or document content, prompt injection, and data
exposure only where a real boundary or risk exists.

### User experience

When relevant, consider visibility, feedback, navigation, form validation,
enabled state, responsive behavior, accessibility, localization, upload or
download, refresh/history, and recovery from user-visible errors.

## Semantic case design and economy

Express cases in user, business, or public-interface terms by default. For a
price-tier boundary, describe quantities immediately below, at, and above the
threshold rather than calling an incidental private function. Use a concrete
function or class only when it is itself an authoritative public contract or
the user explicitly requests implementation-level design.

Create one case per distinct evidence need. Merge near-duplicates through
parameterized partitions, boundaries, decision/state tables, representative
combinations, or pairwise coverage without merging different rules, outcomes,
risks, setup, side effects, or oracles. Prioritize by business impact,
likelihood, security/data exposure, regression value, and detectability. Case
count is not a completeness metric.
