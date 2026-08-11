# Optional PRD Structure Patterns

These are composition patterns, not templates or schemas. Do not mechanically
copy them or force a requirement into one pattern. Combine, rename, reorder, or
omit sections according to the confirmed material product semantics.

## Small Change

- Goal / Context
- Expected Behavior
- Scope
- Acceptance

## Feature

- Problem / Goal
- Users / Scenarios
- Scope / Non-goals
- Main Behavior / Flows
- Business Rules
- Relevant Exceptions
- Acceptance

## Bug / Behavior Correction

- Problem / Current Behavior
- Expected Behavior
- Trigger Conditions
- Impact / Boundaries
- Compatibility
- Acceptance

## Integration / Capability

- Goal / Context
- User-facing Modes / Scenarios
- Behavior by Mode / Scenario
- Failure / Degradation
- Compatibility
- Constraints
- Acceptance

## Stateful / Workflow Feature

- Goal
- Actors
- Lifecycle / States
- Allowed Transitions
- Business Rules
- Exceptions
- Side Effects / Business Consequences
- Acceptance

Use only the dimensions that add value. Related dimensions may share a section;
irrelevant dimensions should disappear. Prefer an explicit acceptance section
unless combining it elsewhere makes the outcomes equally clear.
