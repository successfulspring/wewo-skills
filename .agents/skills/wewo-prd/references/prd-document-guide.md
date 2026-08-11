# PRD Document Guide

Read this guide only after the user confirms the overall requirement summary.

## Semantic contract

Write clear, precise business language in the selected output language.
Include only current-state facts and product decisions supported by valid
provenance and covered by the user's confirmation. Do not state an AI
inference, unaccepted recommendation, implementation convenience, or
unsupported general claim as a product requirement.

Keep the PRD product-semantic. Make functional requirements specific enough
for design, business rules understandable to developers, and acceptance
criteria observable by later testing. Do not include code-level implementation,
perform technical design, or normally include implementation file paths,
function or class names, test file names, code snippets, internal architecture
decisions, or database implementation details, unless one of those is itself
an explicit business or technical constraint provided by the user.

## Required Semantic Coverage

Represent every material product-semantic dimension relevant to the confirmed
requirement. Candidate dimensions include:

- Problem / Motivation
- Goal / Observable Outcome
- Users / Actors
- Scope / Non-goals
- Observable Behavior
- Main Flow
- Business Rules
- Permissions
- State / Lifecycle
- Business/Data Consequences
- Exceptions / Failure Behavior
- Compatibility
- Acceptance Outcomes
- Unresolved / Deferred Decisions

Relevant dimensions must be represented. Irrelevant dimensions must not be
added merely to satisfy a document shape. Related dimensions may be combined;
section names and order should reflect the actual requirement. Do not create
empty or low-value sections, and do not create an unresolved section merely to
say “None” unless it materially improves clarity.

Use [prd-structure-patterns.md](prd-structure-patterns.md) only as optional
composition guidance. The patterns are not templates or schemas. Keep the
filename `prd.md` in English and localize document headings and prose.

## Acceptance criteria

Describe verifiable results rather than aspirations. Cover the confirmed normal
result and the material rejection, duplicate, or failure behaviors. Use a
structured format only when it improves clarity; do not force one syntax on
every requirement. Acceptance outcomes should normally remain explicit even
when other semantic dimensions are combined.

## Synthesis provenance

Apply the Synthesis Provenance Audit before and during composition. Every
material product rule must trace conceptually to a valid source. A repository
fact may describe current state but cannot choose desired future behavior. If a
rule is only an AI recommendation, AI assumption, implementation convenience,
or unsupported best-practice claim, omit it and reopen clarification when the
product outcome itself is unresolved.

When the product outcome is confirmed but the implementation choice is not,
rewrite at the product-semantic level. For example, write “The system remembers
the user's previous output-mode preference” rather than requiring
`localStorage` or another unconfirmed storage mechanism.

## Final quality check

Before writing, verify that:

- the user confirmed the overall understanding;
- all relevant material semantic dimensions are represented;
- source conflicts affecting behavior are resolved or explicitly retained as
  unresolved;
- every material product rule has valid provenance;
- no AI recommendation, temporary assumption, repository fact, or
  implementation convenience appears as an unconfirmed future rule;
- technical implementation has not replaced product behavior;
- each acceptance criterion is observable;
- every included section has relevant content;
- the destination is the resolved isolated workspace;
- no unrelated requirement is combined into this document.
