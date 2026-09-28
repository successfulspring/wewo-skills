# <TASK-ID>/<CR-ID> — <Conflict summary>

Pending decision. This application is non-authoritative; all options and
recommendations below are proposals, not approved requirements or permission
to implement. Localize prose/headings and replace placeholders with evidence.

## Identity and source baseline

- Requirement workspace: <exact project-relative requirement directory>
- TASK / CR: <TASK-ID>/<CR-ID>
- Code state: <revision and relevant working-tree changes, or snapshot/limits>

| Source | Relevant clause | Observed revision/snapshot | Confirmation/provenance |
| --- | --- | --- | --- |
| prd.md | <section> | <basis> | <established confirmation> |
| technical-design.md | <section> | <basis> | <established confirmation> |
| task-breakdown.md | <membership/dependency> | <basis> | <source> |
| task.md | <scope/constraint> | <basis> | <source> |

## Developer's original issue

```text
<Relevant runtime-visible original wording; disclose any agreed omission or
redaction rather than presenting modified text as a complete original.>
```

## Conflict and evidence

<Confirmed obligation versus verified actual code/interface/constraint. Cite
paths/sections or reproducible evidence. Separate verified facts, reported
claims and gaps. Explain why an ordinary implementation adjustment is
insufficient, or exactly why preservation is still uncertain.>

## Affected scope

<Known/possible affected TASK IDs, shared interfaces, frontend/backend or
cross-repository boundaries, acceptance criteria and test/regression scope.
Identify the affected implementation that must stop; do not invent impacts.>

## Proposed options and recommendation

<For each viable proposal: change, preserved constraints, consequences,
dependencies and tradeoffs. State the recommended proposal and evidence-based
reason, or explicitly why no recommendation is supportable yet.>

## Questions for decision

<Concrete questions for TL or the appropriate business/technical decision
authority; unknown authority is a gap, not an assigned owner.>

## Handoff

<Human analysis required. If only the derived task split or definitions are wrong while confirmed
PRD/design remains valid, explicitly revise affected tasks with the required N
and stable IDs; do not edit PRD/design just to correct the split. If product
requirements or technical design must change, explicitly update and confirm
those sources through their existing workflows before revising affected tasks.
Reassess test cases and execution/review evidence against the new baseline.
This file performs none of those steps.>

<Only if explicitly supplementing this CR: add a sourced, dated supplement or
reported handling outcome with new baseline references while retaining the
original application. Recording an outcome does not approve authoritative files.>
