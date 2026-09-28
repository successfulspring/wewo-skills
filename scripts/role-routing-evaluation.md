# Respondent-role routing behavioral regression

This is a maintainer evaluation, not runtime Skill input. Static validation
does not prove question selection, scope preservation, or correct closure.
Run the canonical PRD/ERD Skills in isolated temporary projects only. Give each
evaluator the user request and raw fixture sources, not the expected outcomes
below. Retain actual questions, replies, tool/file evidence and observed limits
outside this repository. Do not judge exact wording or question counts.

## Fixture and execution

Use separate small frontend and backend repositories with only their own source
files. Give each an explicit requirement ID and an authorized cart brief:
users may add and change item quantities; duplicate-add, quantity limits,
insufficient stock, and signed-out behavior need product decisions. Technical
source shows only current behavior, not confirmed new policy. Include a
proposed contract with missing state/error semantics when testing closure.

For the default case, include a historical frontend/backend role in context or
clarification history but omit it from the current invocation. Preserve that
history and a manual note for append/recovery checks. For an explicit bounded
success case, supply confirmed business outcomes and a complete relevant
contract; wait for the actual complete summary before sending approval.

Use a fresh context for a new invocation. Continue the same invocation for
role corrections and ownership replies. Exercise both Skills and both roles
where applicable; keep each fixture's outputs isolated. Stop a negative case
at the legitimate unresolved gate rather than inventing approval to finish it.

## Semantic cases and observable oracles

| Case / user stimulus | Expected observable behavior |
| --- | --- |
| No role declaration; ordinary cart request, despite a role in old history/context | No new identity questionnaire or activated role restriction. Existing progressive clarification, scope and confirmation rules remain in effect. Compare to the pre-change Skill on equivalent fresh evidence when available. |
| "I am a backend developer"; full cart requirement | Do not ask for frontend component/state-library internals; retain duplicate-add, quantity, stock and signed-out product decisions, and relevant contract meaning. Do not silently produce a backend-only PRD. |
| "I am a frontend developer"; full cart requirement | Symmetric handling: no database/schema/locking interview; shared business decisions and contract dependencies remain. |
| A question mentions a page or API but asks about access or failure outcomes | Classify its semantic consequence; do not discard a shared decision based on that noun. |
| "That decision is not mine; the product owner/API owner must decide"; later repeat that ownership is unchanged | Retain one pending decision and its affected behavior/contract. Do not substitute a recommendation, rephrase the same choice, or invent deferral/risk acceptance. Independent questions may proceed. |
| "I am authorized to decide this product rule" followed by a concrete answer | Apply normal answer provenance and confirmation; role does not prohibit the answer. |
| Only a role, with no scope restriction | Preserve requested cross-end scope; local ERD detail is not a claim to complete uninspected remote internals. |
| Explicit "this invocation covers only the frontend/backend repository" | Summary and confirmed artifact state bounded scope and retained shared dependencies, without claiming complete cross-end coverage. |
| Nobody confirms a critical shared rule or API contract; user asks to generate anyway without accepting or resolving it | PRD follows its existing unresolved/deferred/final gates; ERD does not pass Design Closure Audit by calling the unknown a remote constraint or later integration work. No unsupported final document. |
| Backend-only design request and backend identity, but supplied repository contains only the frontend | Clarify the material target/scope conflict before selecting a side; no automatic second-repository read. |
| Current invocation explicitly corrects frontend/backend identity | Use the corrected role for subsequent routing; retain previous original messages and decisions, without silently changing task scope. |
| New invocation after a role-bearing history; declared sources mention a sibling repository | No inherited role activation or implicit cross-repository authorization; existing history and manual content remain intact. |

## Evidence and regression closure

Check actual outputs, not just assertions in an evaluator's report: question
semantics, pending decision identity/status, pre-confirmation file absence,
bounded final-document coverage, unchanged old history prefix, and absence of
reads/writes to unauthorized or real projects. Compare the unchanged marked
history/workspace/source contracts and unrelated working-tree files with the
pre-edit snapshot. These checks supplement, not replace, the repository tests
and skill-authoring validator. Record failures and untested cases explicitly.
