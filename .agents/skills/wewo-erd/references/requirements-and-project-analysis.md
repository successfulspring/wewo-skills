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

Use sources explicitly supplied or referenced in this interaction, or already
established in the current conversation. Do not scan `docs/wewo/` or the
repository for historical workflow documents.

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
