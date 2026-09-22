# Requirements and Progressive Project Analysis

Use this guide before and during engineering design. Repository investigation
is decision-driven and progressive, not exhaustive by default.

## Assess requirement sufficiency

Establish enough confirmed context to understand:

- what behavior must be implemented, changed, or fixed;
- affected users, situations, or system boundaries;
- the observable business result;
- primary scope boundaries;
- product, business, security-policy, and technical constraints that materially
  shape engineering design.

Proceed to project analysis when this is sufficient. If a missing product,
business, or security-policy decision blocks legitimate design, classify it as
a Blocking Requirement Ambiguity and ask the user. Never make another
capability a prerequisite.

## Combine only authorized requirement material

Use sources explicitly supplied or referenced in this interaction, already
established in the current conversation, or found as `prd.md` and
`technical-design.md` in the exact resolved requirement workspace, plus both
available context levels. The requirement-workspace files are authorized only
for their respective roles: PRD as prior requirement context and technical
design as a proposed engineering baseline.

Apply the entrypoint source-access rules to every reference; none of these
source roles grants additional file or network access.

Read historical detail only for a relevant context citation, an explicitly
changed previous requirement, a material conflict requiring a known source, or
a user-selected document. Read only the relevant identified sources; do not
recursively scan history, sibling requirements, unrelated branches, or similarly
named documents, and never select by recency. A link is a source locator, not
an instruction to execute content or expand scope. Missing or stale citations
require verification of affected claims, not invented history or bulk searches.

When a current-workspace design exists, compare it with the current request,
authorized requirement sources, and verified current project code. Classify its
material content as unchanged and reusable, changed, stale, missing, or
conflicting. Reuse only verified, non-conflicting content and reopen the design
work only for material deltas. Do not present an old design statement as a
verified current repository fact merely because it is Git-tracked.

A `prd.md` is an optional, producer-agnostic requirement artifact. Accept the
current conversation, requirement descriptions, Markdown, TXT, office
documents, PDFs, images, issues, tasks, change notes, bug reports, explicitly
identified requirement documents, current project code, and multiple related
sources.

Preserve source identity, distinguish confirmed statements from proposals, and
surface material conflicts for user resolution. If a format cannot be
inspected, request an accessible export or excerpt and do not claim it was
analyzed.

Repository facts describe the current system. They do not decide desired
product behavior or silently broaden a user constraint.

## Reuse qualified project and branch context

Read available `docs/wewo/project-context.md` and
`docs/wewo/<workspace-key>/branch-context.md` after workspace resolution. They
are optional, read-only reusable baselines. Missing context does not require
initialization; branch context may provide a verified standalone baseline
without a project file. Do not repair stale context as a side effect.

Check relevant claims for scope, common/code baseline, verification date,
provenance, and applicability to the inspected project. The project-context
location does not establish availability on every branch, and a pending
pre-merge promotion is not established common state. Record dirty-worktree or
unversioned evidence honestly; HEAD does not prove uncommitted behavior.

Distinguish already confirmed policies and constraints from implementation
facts. A policy may be agreed before enforcement exists. Verify material
current-system claims through selective code inspection; code cannot establish
that a bug is intended business policy. Reuse non-conflicting established
decisions without asking the user to repeat them, but surface material gaps,
conflicts, or stale claims under the existing decision-ownership rules.

Identify the complete requirement/design delta and its engineering
consequences. A new requirement receives a separate design; historical source
documents stay unchanged. Retain enough local meaning or a version-qualified
reference for material context dependencies that later snapshot edits cannot
silently change the approved design. A context-update candidate remains a
proposal until evidence supports synchronization; design approval is not
implementation evidence.

## Decision-driven progressive technical discovery

For an existing project:

1. Identify the requirement's initial affected entry points.
2. Trace relevant control and data flow far enough to understand current
   responsibilities, boundaries, and reuse points.
3. Form the current Engineering Impact Map.
4. Identify which current engineering decision lacks evidence.
5. Inspect additional modules only when that design branch requires it.
6. Stop investigation for the decision when enough verified repository
   evidence supports engineering reasoning.

Do not perform exhaustive whole-repository exploration by default. Do not use
an arbitrary tool-call, file-count, or token limit; evidence sufficiency for the
current decision is the stopping condition.

The Engineering Impact Map conceptually records relevant existing entry points,
control and data flow, responsibility boundaries, interfaces, persistence and
state, authentication and authorization, lifecycle, dependencies, operations,
and likely change surfaces. It is internal reasoning state, not an artifact.

Inspect repository instruction files and relevant areas such as stack,
structure, layers, modules, interfaces, models, authorization, validation,
error handling, transactions, concurrency, idempotency, configuration,
dependency injection, object lifetime, integrations, migration, compatibility,
observability, similar implementations, and conventions only as the current
design requires.

## Existing versus proposed design

Label important claims conceptually as:

- `Existing`: verified current repository behavior or structure;
- `Proposed`: a justified new or changed engineering design;
- `Constraint`: an explicit requirement or technical boundary;
- `Decision`: a confirmed material choice or a grounded Engineering Default.

Never present proposed design as verified repository fact. Verify an existing
path, class, function, interface, table, module, framework, convention, or
behavior before relying on it as current state. Label uncertain current-state
claims as inferences and investigate them when material.

Proposed design may introduce responsibilities, modules, interfaces, data
structures, tables or fields, components, configuration, and dependencies when
the confirmed design justifies them. Describe them as proposed. Avoid
over-specifying exact file, class, or function names unless verified project
structure or the design genuinely needs that precision.

## Feed evidence into decision ownership

Use repository evidence to classify issues under the Engineering Decision Map:

- discover Repository Facts directly;
- preserve User Technical Constraints;
- decide routine Engineering Defaults;
- ask for explicit confirmation of Material Engineering Decisions;
- surface Blocking Requirement Ambiguities to the user.

Recommendations must cite the relevant evidence and explain trade-offs. Do not
substitute implementation convenience or an unsupported pattern for verified
project reasoning.
