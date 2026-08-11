# Engineering Decision Dialogue

Use this guide only for Material Engineering Decisions and Blocking Requirement
Ambiguities. Apply Engineering Defaults directly without turning routine design
details into user questions.

## Build a dynamic decision sequence

Use the internal
[engineering-decision-map.md](engineering-decision-map.md). Select only topics
relevant to the requirement, such as impact boundaries, responsibilities,
interfaces, data and state, security policy, consistency, external dependencies,
compatibility, migration, operational burden, and difficult-to-reverse choices.

Resolve higher-level decisions before dependent detail. After each material
answer, update provenance and the selected approach, eliminate irrelevant
branches, expand newly unlocked material engineering branches, and choose the
next highest-value unresolved Decision Topic. Do not ask a question merely
because it appeared in the initial map.

## Ask one focused round

Discuss exactly one Decision Topic per round. One topic does not mean one
question: a substantial topic may contain multiple tightly related Decision
Questions, normally around 2–5 when useful; a simple topic may contain one.
This is a preference, not a minimum, maximum, or stopping rule.

Questions in one round should normally be answerable in parallel. Defer a
question when its relevance, viable options, or existence depends materially
on an unanswered prerequisite.

Use stable identifiers:

- number topics `Topic 1`, `Topic 2`, and so on;
- number questions `Q1.1`, `Q1.2`, then `Q2.1`, `Q2.2`, and so on;
- never reuse an assigned identifier for a different decision;
- label each question's options `A`, `B`, `C`, `D` as applicable, restarting at
  `A` for every question;
- reference a recommendation by the actual listed option letter.

Keep `Qx.y` and `A/B/C/D` stable, but localize surrounding user-facing labels
to the conversation language. In a Chinese conversation, prefer labels such as
`决策主题`, `为什么需要确认`, `选项`, `推荐`, `推荐理由`, and `主要权衡`.

## Recommendation contract

For a closed or semi-closed Material Engineering Decision, offer 2–4 materially
distinct viable options and a custom route when useful. When evidence supports
a recommendation for a single-choice question:

- recommend exactly one listed option by its actual letter;
- ground it in explicit requirements or constraints, verified repository
  facts, and existing architecture or conventions;
- explain the direct engineering trade-off and operational burden;
- explain consequences and reversibility where material.

If evidence does not justify one option, say so explicitly. Never recommend an
unlisted option, recommend multiple options for a single-choice question, mix
option numbering systems, or treat the recommendation as confirmed.

Prefer simplicity, minimal change, justified complexity, and reversible
choices. Do not cite unsupported best practices, architecture fashion, or
invented performance or SLA numbers.

## Canonical format

Adapt this format to the user's language:

```markdown
### Decision Topic 1 — Persistence Boundary

Why this requires confirmation:
The requirement needs graph traversal, while the verified project currently
operates one PostgreSQL persistence boundary. A separate graph database would
materially change infrastructure and operations.

#### Q1.1 Which persistence direction should the design use?

Evidence:
- Existing: PostgreSQL is the verified system of record.
- Constraint: no additional infrastructure restriction has been supplied.

A. Model the required relations in the existing PostgreSQL boundary
B. Introduce a separate graph database
C. Keep PostgreSQL authoritative and add a derived graph projection
D. Other / custom constraint

Recommended: A

Reason:
It preserves the current operational boundary and is the least complex option
while the required traversal remains supportable there.

Main trade-off:
This avoids synchronization and recovery complexity, but may be less suitable
if later evidence proves that traversal scale or query shape exceeds the
existing database's practical limits.
```

## Apply Engineering Defaults without unnecessary questions

Use verified project conventions and engineering judgment for routine choices,
including reusing existing dependency injection and layering, preserving error
formats and lifecycle management, keeping responsibilities cohesive, avoiding
unrelated changes, and not adding unsupported third-party dependencies.

Universal security hygiene is also normally an Engineering Default: enforce
authorization server-side, do not trust client-supplied identity, validate
untrusted input, avoid hardcoded secrets, use least privilege, and redact
sensitive logs. Ask only when a material security-policy choice exists.

When a shared instance is justified, specify owner, lifecycle, mutable-state
behavior, concurrency safety, request/user/tenant isolation, and test isolation.
A singleton is not automatically wrong, and no numeric singleton limit applies.

## Complete based on engineering closure

There is no arbitrary maximum number of topics, questions, rounds, or interview
duration. Stop dialogue when material engineering branches meet the Design
Closure Audit, not because a question count was reached.

Before document generation, present the complete final design summary and ask
for explicit correction or confirmation. Do not infer confirmation from
silence or from agreement with only one Decision Topic.
