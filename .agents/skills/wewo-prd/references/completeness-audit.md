# Three-Layer Requirement Completeness Audit

Run the Coverage and Branch Expansion audits before drafting the structured
requirement summary. Apply the Synthesis Provenance Audit to every planned rule
before presenting that summary or composing the PRD. This internal audit
creates no workflow artifact.

## A. Coverage Audit

Consider only dimensions relevant to the current requirement:

- problem and motivation;
- goal and observable success;
- users and actors;
- entry points and usage situations;
- scope and non-goals;
- main flows;
- business rules;
- permissions;
- state and lifecycle;
- business and data consequences;
- exceptions and failures;
- compatibility;
- acceptance outcomes.

For each dimension:

```text
irrelevant -> skip
relevant and resolved -> retain
relevant and materially unresolved -> reopen clarification
```

Do not mechanically ask about every dimension.

## B. Branch Expansion Audit

Review important confirmed decisions and ask internally:

> Did this decision create a new material product consequence or dependent
> decision that remains unresolved?

If yes, add it to the Decision Map and reopen clarification. Check especially
for second-order effects on roles, permissions, state, business or data
consequences, failure behavior, compatibility, acceptance outcomes, and
material risk. Do not expand theoretical implementation consequences.

## C. Synthesis Provenance Audit

Inspect every planned material product rule before the final summary and PRD:

- Where did this rule come from?
- Did the user confirm it?
- Is it only a repository current-state fact?
- Is it an AI recommendation or assumption?
- Is it actually an implementation decision?

Valid provenance is defined in [decision-map.md](decision-map.md). When a
material rule lacks valid provenance:

1. reopen clarification when the product outcome is unresolved; or
2. rewrite it at the confirmed product-semantic level when only the
   implementation detail is unsupported.

Never guess. Do not promote an AI recommendation, implementation convenience,
or unsupported general claim into a product requirement.

The structured summary is ready to present only when all relevant coverage is
resolved or deliberately dispositioned, no material expanded branch remains
unhandled, and every planned material rule has valid provenance.
