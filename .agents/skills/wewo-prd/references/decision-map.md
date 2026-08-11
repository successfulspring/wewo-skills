# Internal Decision Map Protocol

Use this protocol during clarification. It is runtime reasoning state, not a
business artifact. Never create `docs/wewo/.../decision-map.md`, and do not
print the map verbatim unless a concise decision summary helps the user.

## Conceptual model

```text
Requirement
-> Decision Topics
-> Decision Questions
-> Resolved Decisions
-> Unresolved Decisions
-> Unlocked Branches
-> Eliminated Branches
-> Decision Provenance
```

For each material decision, conceptually track:

- stable decision or question identity when available;
- Decision Topic;
- status;
- confirmed answer;
- provenance;
- newly unlocked dependent branches;
- eliminated branches;
- unresolved material consequences.

Use the existing branch completion states: `Confirmed`, `Explicitly Out of
Scope`, `Explicitly Deferred by the User`, or `Intentionally Unresolved with
the User Accepting the Remaining Risk`.

## Decision provenance

Valid provenance is:

- `User Confirmed`;
- `Explicit User Requirement`;
- `Explicit User-Supplied Source`;
- `Repository Fact`;
- `Explicitly Out of Scope`;
- `Explicitly Deferred by User`;
- `Intentionally Unresolved with Accepted Risk`.

`Repository Fact` establishes current state only. It cannot decide desired
future behavior. `AI Recommendation`, `AI Assumption`, `Implementation
Convenience`, and `Unsupported Best-Practice Claim` are not valid provenance
for a confirmed product requirement.

## Update after each material answer

1. Mark the current decision resolved with its stable identity.
2. Record the answer and valid provenance.
3. Update the current requirement understanding.
4. Eliminate branches made irrelevant by the answer.
5. Identify newly unlocked material dependent branches.
6. Add those branches to unresolved decisions.
7. Record any unresolved material consequences.
8. Select the highest-value unresolved Decision Topic.

Do not treat a resolved question as merely finished. A confirmed decision may
create second-order product decisions. For example, confirming automatic HTTP
fallback when SSE is unavailable may unlock quota behavior, audit behavior,
user-visible fallback behavior, or persisted-mode-preference questions. Keep
only branches that can materially change product requirements; do not expand
heartbeat mechanisms, storage technology, APIs, libraries, or other theoretical
implementation consequences unless the user explicitly supplies one as a
constraint.

## Materiality filter

A branch is material when its answer may meaningfully change scope,
user-visible behavior, business rules, users or permissions, state or lifecycle
behavior, the main flow, business or data consequences, exception or failure
behavior, compatibility, acceptance outcomes, or material business risk.

Normally exclude class or function names, API paths or methods, `localStorage`
versus cookie or server persistence, database locking, framework or library
choice, test-file location, logging implementation, and heartbeat mechanisms.
