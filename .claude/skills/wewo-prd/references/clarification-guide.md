# Clarification Guide

Use this guide to choose the next clarification topic and judge when the
requirement is ready for confirmation.

## Build a dynamic decision tree

Start from the evidence already available. Track:

```text
Goal
├── Target users
├── Usage situations and entry points
├── Core operation
│   ├── Preconditions
│   ├── Normal flow
│   └── Result
├── Business rules
├── Exceptions and boundaries
├── Scope
└── Acceptance outcomes
```

Ask higher-level questions before dependent questions. After every answer, mark
resolved decisions, add newly exposed decisions, and choose the highest-impact
unresolved topic for the next round.

## Ask one focused round

Discuss one topic per round and normally ask one to three tightly related
questions. Do not begin with a comprehensive questionnaire covering screens,
permissions, data, performance, notifications, and failures at once.

Adapt this pattern to the user's language:

```markdown
❓ Decision to confirm

Why this matters:
...

Based on the current material, my understanding is:
...

My recommendation is:
...

Please confirm this understanding or describe what should change.
```

Omit a recommendation when evidence is insufficient to make one responsibly.
Never interpret silence as acceptance.

## Select relevant clarification topics

Do not ask every question mechanically. Cover a topic only when it affects this
requirement.

### Background and problem

- Why is the change needed?
- What current problem exists, who experiences it, and what outcome should
  improve?

### Goal and success

- What must the requirement achieve?
- What observable outcome demonstrates success?
- Is the requested feature the real need or a proposed solution to a deeper
  problem?

### Users and situations

- Who uses it, under what circumstances, and from which entry point?
- What result does the user expect?

### Core flow

- What preconditions apply?
- What does the user do and how does the system respond?
- What changes after success?

### Business rules

- When is the action allowed or prohibited?
- Which states, roles, permissions, counts, quantities, or time limits apply?

### Exceptions and boundaries

- What happens for empty or invalid input, duplicate actions, missing data,
  changed state, or external-service failure?
- Which easily missed special cases materially change the result?

### Scope

- What is included now?
- What is explicitly excluded?
- What related work is deferred?

### Acceptance outcomes

Express observable, verifiable results. Replace vague qualities such as
“friendly,” “stable,” or “easy to use” with behavior that a later test can
observe, including success, rejection with a reason, and duplicate-action
handling where relevant.

## Avoid implicit assumptions

Surface any temporary assumption that materially affects the final behavior
and require confirmation. Pay particular attention to permissions, permitted
states, result data, notifications, historical data, and whether failures block
or allow continuation.

## Stop at product requirements

Do not expand into code structure, classes or functions, database fields,
specific API paths, detailed architecture, test-tool selection, or deployment.
If the user supplies technical details, preserve them as constraints or
references without turning clarification into technical design.

Stop questioning when the product decisions are sufficiently clear for later
design and development. Do not pursue every theoretical edge case.
