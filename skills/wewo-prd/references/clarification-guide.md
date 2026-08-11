# Clarification Guide

Use this guide to choose the next clarification topic and judge when the
requirement is ready for confirmation.

## Build a dynamic decision map

Apply [decision-map.md](decision-map.md). Start from the evidence already
available. Track:

```text
Requirement
-> Decision Topic
-> Decision Questions
-> Dependent Branches
```

Internally map relevant goals, users, usage situations and entry points, core
flows, business rules, states, permissions, consequences, exceptions, scope,
compatibility, and acceptance outcomes into this structure. Ask higher-level
questions before dependent questions.

After every answer:

1. mark resolved decisions;
2. record decision provenance;
3. update the current understanding;
4. identify newly unlocked material dependent branches;
5. remove branches that are no longer relevant;
6. choose the highest-value unresolved Decision Topic.

Do not ask a question merely because it was identified at the beginning.

## Ask one focused round

Discuss exactly one Decision Topic per round. One topic per round does not mean
one question per round: a substantial topic should normally contain around
2–5 tightly related Decision Questions, while a simple topic may contain one.
This is a preference, not a hard maximum, minimum, or stopping rule. Do not
begin with a comprehensive questionnaire spanning unrelated topics.

Questions grouped in one round should normally be answerable in parallel. Ask
a dependent question in a later round when its relevance, available options,
or existence changes materially based on another unanswered question. For
example, first decide whether paid orders may be cancelled; only if they may,
ask how their refunds should behave.

Use stable identifiers:

- number topics `Topic 1`, `Topic 2`, and so on;
- number their questions `Q1.1`, `Q1.2`, then `Q2.1`, `Q2.2`, and so on;
- keep an assigned ID attached to the same decision and never reuse a retired
  ID for a different question;
- label each question's options `A`, `B`, `C`, `D` as applicable, restarting
  from `A` for every question;
- reference recommendations by the actual listed option letter only.

Users may reply with forms such as `1.1 B`, `1.2 A`, `1.3 use the
recommendation`, `use all recommendations`, or free-form business rules.

## Recommendation contract

For a closed or semi-closed Decision Question, provide 2–4 materially distinct
options where appropriate and an Other or custom route when useful. When the
available evidence supports a recommendation for a single-choice question:

- recommend exactly one listed option;
- cite its actual option letter;
- explain the reason;
- explain the important tradeoff or assumption.

Never recommend an option that is not listed, mix option numbering systems, or
recommend multiple options for a single-choice question. If the evidence does
not justify one recommendation, say so explicitly. Prefer options that state
the business meaning directly instead of yes/no answers to a negated question.

Ground a recommendation preferentially in:

1. confirmed user goals;
2. confirmed requirements;
3. verified repository facts;
4. explicit constraints;
5. directly explainable tradeoffs;
6. general patterns only when clearly identified as general guidance.

Use direct reasoning. Do not present "industry standard," "mainstream
products," "standard behavior," or "best practice" as factual justification
without actual evidence.

## Canonical interaction example

### Decision Topic 1 — Cancellation Eligibility

#### Q1.1 Which order states may be cancelled?

Known fact:
The current repository contains `PENDING_PAYMENT`, `PAID`, `SHIPPED`,
`DELIVERED`, and `CANCELLED`.

A. `PENDING_PAYMENT` only
B. `PENDING_PAYMENT` and `PAID`
C. Any order not yet shipped
D. Other / custom rule

Recommended: B

Reason:
This covers orders that have not entered fulfillment while avoiding
post-shipment rollback complexity. The assumption is that payment reversal is
an accepted business consequence for eligible paid orders.

#### Q1.2 Who may initiate cancellation?

A. Order owner only
B. Order owner and administrator
C. Any authenticated user
D. Other / custom rule

Recommended: B

Reason:
This preserves owner control while allowing administrators to resolve support
cases. The tradeoff is that administrator actions require clear authorization
and accountability requirements.

Reply example:

```text
1.1 B
1.2 A
```

or:

```text
Use all recommendations.
```

Both questions belong to one topic and are normally answerable in parallel.
The user may always replace an option with a custom business rule.

## Ask with context

Keep `Q1.1`, `Q1.2`, and `A/B/C/D` stable, but adapt every surrounding label to
the user's language. In a Chinese conversation, prefer labels such as
`决策主题`, `为什么需要确认`, `选项`, `推荐`, `推荐理由`, and `主要权衡` instead of
unnecessary English labels.

Adapt this pattern to the user's language:

```markdown
❓ Decision to confirm

Why this matters:
...

Based on the current material, my understanding is:
...

Options:
A. ...
B. ...
C. ...
D. Other / custom

Recommended: B

Reason and material tradeoff:
...

Reply with the question ID and option letter, accept the recommendation, or
describe a custom business rule.
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

## Audit requirement completeness

Be exhaustive about material requirement branches, not about theoretical
possibilities. A question is material when its answer can meaningfully change
scope, user-visible behavior, business rules, users or permissions, state or
lifecycle transitions, the main flow, business or data consequences, exception
or failure behavior, compatibility, acceptance outcomes, or material business
risk. Do not ask implementation or theoretical edge-case questions merely to
make the interview appear comprehensive.

Before presenting the final summary, apply all three layers in
[completeness-audit.md](completeness-audit.md). An empty question queue does
not authorize synthesis when the Coverage Audit, Branch Expansion Audit, or
Synthesis Provenance Audit reveals a material gap.

A material branch is complete only when it is:

- `Confirmed`;
- `Explicitly Out of Scope`;
- `Explicitly Deferred by the User`; or
- `Intentionally Unresolved with the User Accepting the Remaining Risk`.

Never guess an unanswered product decision or turn an unknown into a default.
There is no arbitrary limit on rounds, questions, or interview duration.
Completeness of material branches—not question count—controls readiness.

If the user asks to stop questioning or generate the PRD now, list the
remaining material unresolved branches, state that they will not be decided
automatically, and request confirmation that the user accepts them as deferred
or unresolved. After confirmation, preserve them in the final summary and PRD.

After the audit, present a concise structured summary of confirmed scope,
users and roles, main flows, business rules, relevant exception behavior,
out-of-scope items, and deferred or unresolved items. Require explicit final
confirmation before writing `prd.md`. Do not restart clarification after final
confirmation unless the user adds new information, a direct contradiction is
discovered, or a material gap becomes newly apparent.

## Stop at product requirements

Do not expand into code structure, classes or functions, database fields,
specific API paths, detailed architecture, test-tool selection, or deployment.
If the user supplies technical details, preserve them as constraints or
references without turning clarification into technical design.

Stop only when relevant material branches meet the completion states above and
the user has confirmed the final requirement summary. Do not pursue a
theoretical edge case that cannot materially affect the product requirement.
