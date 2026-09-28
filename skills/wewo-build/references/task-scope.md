# Task-scoped implementation

This mode applies only to explicit TASK work or existing split material in the
exact current requirement. With neither, retain the original input rules,
root output paths and gates; do not ask for task selection.

Select only an explicit TASK-ID, a supplied `task.md` path resolving safely to
this requirement's `tasks/<TASK-ID>/task.md`, or the single unambiguously selected
task in the current conversation. Otherwise ask. Do not infer selection from
directory recency, branch name, or the presence of only one task directory.
Reject unsafe IDs/paths using the entrypoint's containment rules.

Read the selected task definition, the requirement's confirmed PRD and technical
design, and relevant code. Use the overview to verify membership, dependencies
and shared contracts, reading only necessary linked task definitions. Missing,
orphan, inconsistent or materially ambiguous split inputs require clarification.
The task is a derived scope contract, not permission to override the PRD/design.
Resolve material conflicts before planning or implementing affected work.

Preserve task in/out scope and accepted shared interfaces. Confirm dependency
readiness from evidence, not from task order or a planned deliverable. An
unready prerequisite must be resolved without silently implementing another
task or inventing a substitute contract. Another repository remains outside
automatic access; use only authorized sources for cross-repository obligations.

Build's own implementation units are internal to the selected TASK. Plan them
according to the existing slicing and TDD rules; TASK IDs are not unit IDs and
the breakdown is not an approved implementation plan. Retain plan confirmation,
Red/Green sequencing, material-gap escalation and fresh verification unchanged.

Keep both workflow outputs in the selected task directory; production assets
and developer tests stay in normal project paths. Record TASK-ID, scope and
binding source sections in the existing goal/basis fields. Preserve all earlier
requirement-root outputs and other task artifacts. Completing all units of one
TASK does not establish completion of other tasks, integration, or the whole
requirement. Do not automatically continue into another task or capability.

## Material conflicts in task mode

An ordinary adjustment is allowed only when it preserves confirmed PRD/design
constraints and TASK boundaries. If preservation is impossible or uncertain,
stop the affected implementation and explain the cited obligation, verified
conflict or evidence gap, and impact. A developer's "continue anyway", approval
of a changed implementation plan, or a change request marked approved cannot
override those documents. Do not create a CR or invoke a change-request skill
automatically; the user may explicitly request that separate recording step.

Resume affected work only when evidence establishes an ordinary adjustment that
preserves the existing basis, or the changed source layer has been resolved:
if only derived TASK boundaries or definitions were wrong while confirmed
PRD/design remains valid, the affected tasks have been revised through task
decomposition without changing PRD/design; if product requirements or technical
design changed, the affected authoritative PRD/design has been incrementally
updated and finally confirmed through its owning workflow and the affected
tasks have been revised through task decomposition. Either revision still
requires an explicit positive integer count and preserves stable IDs and
existing evidence under the task-decomposition rules.
Read the resulting authoritative sources and task definitions, reassess the
plan and obtain any required confirmation before implementation. A CR or TL's
reported decision is pending/provenance material, not replacement authority.
Preserve earlier implementation/test evidence and reassess its applicability;
old results do not automatically validate the new baseline. This adds no
automatic workflow chain and no change to unsplit Material Gap handling.
