# Design Dialogue

Use this guide to resolve technical decisions without presenting a fixed
questionnaire.

## Build a dynamic decision sequence

Select only topics relevant to the requirement:

1. impact scope;
2. overall implementation approach;
3. module responsibilities and code location;
4. frontend pages, components, and state;
5. backend business flow;
6. interfaces and data flow;
7. data model;
8. state transitions;
9. transactions, concurrency, and idempotency;
10. authorization and sensitive data;
11. external services and failure behavior;
12. compatibility and migration;
13. code structure and implementation constraints.

Resolve higher-level choices before dependent detail. After each answer, update
which decisions are settled, which new questions emerged, what matters next,
and whether the design generation gate is satisfied.

## Ask one focused round

Discuss one topic per round and normally ask one to three tightly related
questions. Adapt this structure to the user's language:

```markdown
### Current design topic

Evidence from the requirement and project:
...

Viable choices:
...

Recommended approach:
...

Why:
...

Please confirm:
1. ...
2. ...
```

Do not present a recommendation as a final decision before confirmation.

## Apply engineering defaults without unnecessary questions

Unless a real tradeoff exists, directly preserve these constraints:

- never hardcode passwords, tokens, or secrets;
- enforce authorization on the server, not through hidden UI alone;
- keep user and request state out of process-global shared objects;
- do not swallow exceptions;
- preserve existing dependency injection and lifecycle conventions;
- do not introduce a hand-written singleton without a justified need;
- preserve existing interface compatibility unless change is confirmed;
- avoid unrelated modifications;
- reuse existing shared capabilities;
- avoid unconfirmed third-party dependencies;
- keep unrelated responsibilities separate;
- avoid overdesign.

When a shared instance is justified, specify its owner, lifecycle, mutable
state, concurrency safety, user/request isolation, and test isolation.

## Confirm the complete solution

Before document generation, summarize:

- requirement sources;
- affected and unaffected scope;
- overall implementation approach;
- modules and responsibilities;
- interface and data changes;
- security and reliability controls;
- code-structure constraints;
- unresolved questions.

Ask for explicit correction or confirmation. Do not infer confirmation from
silence or from agreement with only one design topic.
