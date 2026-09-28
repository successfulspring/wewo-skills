# Change-request record

## Source basis and bounded analysis

Resolve the requirement and TASK before reading workflow sources. Verify the
selected `task.md` belongs to the exact overview; ask on orphan, conflicting
identity or unclear document authority. Read actual PRD/design/task clauses and
the relevant mechanism or interface evidence. Source permission and source
authority are separate: an authorized CR is still only an unverified proposal.

Record the workspace, TASK/CR identity, source paths and sections, established
confirmation basis, and an identifiable snapshot for each relied-on document.
Use a recorded revision or content digest plus the observed dirty/untracked
state where appropriate; HEAD alone does not identify uncommitted content.
Record code revision and relevant local modifications, or honestly state a
non-Git/unavailable revision with a file snapshot. Hashes identify content,
not approval. Distinguish verified facts, developer reports and uncertainty.
Never invent version numbers, confirmation, measurements or inspected evidence.

Determine which confirmed obligation an ordinary fix would change. Merely
needing code changes, tests, refactoring, or more effort is not sufficient.
Explain whether preservation is disproven or still uncertain, with the missing
evidence. Record affected known TASK IDs, interfaces, frontend/backend contract
boundaries, and test/acceptance scope; label possible impacts as possible.
Use the overview and specifically relevant definitions for dependencies, not a
recursive history scan or automatic access to another repository. Unknown
external facts remain gaps; they do not authorize expanding access.

Keep options proportional to the conflict: the proposed change, what it would
preserve/change, tradeoffs and dependent decisions. All options/recommendations
are proposals pending a human decision. Keep internal reasoning and unrelated
chat/tool dumps out of the application; include concise reproducible evidence
or locators rather than claiming unexecuted verification.

## New application or specified supplement

Inventory only direct entries in the selected TASK's `change-requests/` when
it exists. New files use `CR-001.md`, `CR-002.md`, ... (minimum three digits),
with the next number equal to the highest existing numeric CR suffix plus one,
or 1 if none exist. Do not fill gaps or reuse a known previously issued ID.
If ambiguous/noncanonical filenames or known deletion make numbering unsafe,
clarify without renaming old files or creating a global registry. Different
TASKs have independent sequences. Use TASK/CR together in external references.

An explicit request to supplement `TASK-001/CR-001` targets that exact existing
file, never the latest CR or a new number. Check its embedded workspace and
identity. A missing or ambiguous requested CR requires clarification. Preserve
the original issue, original baseline, proposals and human edits; add the new
evidence/correction or requested handling outcome with its source and current
baseline. Do not silently rewrite the original claim to match later knowledge.
A bare retry after interruption is not a new independent application: inspect
the observed target and reconcile whether the previous write succeeded before
allocating another ID. Ask if the user's new-vs-supplement intent is ambiguous.

On an explicit handling-outcome request, attribute the reported TL/decision-maker
decision accurately. Verify any claimed updated PRD/design or revised task bundle
against authorized sources and its confirmation or revision basis; mark an
unverified report as such. For a task-only correction, cite the unchanged
confirmed PRD/design basis alongside the revised task definition. Retain an
initial pending proposal as historical text. A recorded decision
does not itself update or approve the PRD/design, revise tasks, validate older
tests, or lift the affected implementation stop. No approval state machine or
owner/status fields are needed.

## Persistence and sensitive originals

Preserve the developer's runtime-visible original issue wording separately
from the skill's analysis. Use a fenced block long enough for embedded Markdown,
keeping relevant line breaks; do not invent unavailable original messages.
The application may enter Git. Omit unrelated sensitive evidence and avoid
copying credentials, tokens, private data or authentication-bearing locators.
If the original issue itself contains obvious sensitive values, withhold that
payload, explain the conflict without echoing it, and request a safe replacement
or explicitly acknowledged omission/redaction. Label any altered excerpt; do
not silently sanitize and call it a complete original. No chat archive or extra
clarification-history entry is created for this handling.

Before writing, recheck the source snapshots, resolved task path, CR inventory
and target preimage. Reject unsafe IDs, traversal and symlink/junction escapes.
Preserve all unrelated edits. New files require exclusive creation (fail if the
target exists), never overwrite mode. For a supplement, use an available
exclusive handle or conditional-write facility against the inspected preimage;
if safe writer ownership cannot be established, stop and disclose the conflict.
Do not silently clobber concurrent edits, renumber a collided write, start
background writes or alter filesystem permissions to force success.

Create no directory or empty placeholder until there is a resolved application
to write. On write failure, source changes or uncertain partial persistence,
report the actual state and stop declaring success; reconcile before retrying.
Reread the persisted CR to verify its identity, complete content and proposals,
and verify that only the selected CR changed. Never repair another capability's
files as a side effect. Return the actual path and brief manual handoff, with
any material gap; do not send a message or start downstream work.
