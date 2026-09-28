# Development package contract

## Cohesion and complete coverage

A package is a developer-sized outcome with explicit deliverables and acceptance
conditions. Prefer boundaries grounded in the actual modules, behavior and
contracts; do not assume equal size or split by a fixed frontend/backend/layer
recipe. A task may depend on another; separately understandable does not mean
all tasks can execute concurrently. Include migrations, compatibility, security,
configuration and developer verification required by the approved design.

Build a coverage relation from every mandatory PRD acceptance criterion and
design obligation to one or more TASK IDs. Retain source section references
when no stable source IDs exist; never invent approved criteria. Explain shared
responsibility without duplicating implementation. Assign each shared interface
change to a task, state its consumers, field/authentication/state/error semantics
and prerequisite delivery. Development of a shared contract belongs in a real
package, not an extra coordination or review task. Detect circular dependencies
and resolve their actual contract/order before calling the split executable.

N is a hard constraint on developer packages, not on implementation units,
test cases, commits or people. For example, a genuinely indivisible change
cannot become three meaningful tasks merely by naming coding, testing and
review. Explain which obligation/boundary prevents the requested count and ask
for a decision. Recommendations remain proposals until the user resolves any
required scope or design change. Do not write a misleading partial bundle.

## Document content

The overview must contain all N task links, boundaries, deliverables,
dependencies, shared contracts, and complete acceptance/design coverage.
Each task must state its objective, in/out scope, deliverables, acceptance,
dependencies and contracts with other tasks. Distinguish confirmed constraints
from repository observations. The bundle refines the confirmed PRD/design;
it cannot authorize new behavior, replace either input, or claim completion.

Use the templates as content guides; localize headings and substantive prose.
Keep each task's first heading `# TASK-001 — <meaningful title>` (with its actual
ID) and give the overview a relative Markdown link `tasks/TASK-001/task.md`
for every task. These identities and links support the read-only checker;
there is no separate task registry, counter, owner or status metadata.
Dependencies use TASK IDs or explicitly sourced external prerequisites,
never presumed cross-repository synchronization. Avoid secrets and personal
data in this version-controlled bundle; reference configuration names instead.

## Existing documents and writes

Inspect only the exact current requirement's overview and direct task directory
entries, then its relevant task definitions. This bounded inventory is needed
to count all existing tasks; it does not permit scanning sibling requirements.
An overview without its task definitions, orphan tasks, or conflicting IDs is
an incomplete bundle, not authorization to fall back to an unsplit workflow.

On repeated requests, preserve stable IDs, existing manual edits and downstream
artifacts. If N or boundaries would require removing/renumbering tasks, reusing
an ID for different work, or invalidating existing execution evidence, show
the concrete impact and obtain a decision before that rewrite. Do not leave
extra old task definitions while claiming exactly N. Do not automatically
delete, relocate, or adopt previous requirement-root execution documents.
Fresh bundles use sequential IDs; an explicitly resolved revision may leave
gaps in retained IDs. Do not renumber surviving tasks just to close those gaps.

Before writing, recheck the observed source/bundle versions and safe resolved
paths, including symlinks/junctions. Stop on concurrent changes, ambiguous path
ownership or access failure. After writing, reread the bundle and verify the
actual count, task identities, all overview links and required content. A
partially written set is not ready; report its exact state and resolve the
failure before downstream use. Do not use background writes.

Structural validation is deliberately limited: the helper never follows
document citations, checks confirmation, judges scope, or performs workflow
routing. Its input directory must already be resolved and authorized under
the entrypoint's workspace contract. Downstream capabilities resolve their
own scope and require no runtime call to this skill or its helper.
