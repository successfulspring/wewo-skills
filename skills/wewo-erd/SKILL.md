---
name: wewo-erd
description: Produce a user-confirmed, implementation-guiding technical design for a feature, bug, refactor, or maintenance requirement by analyzing the existing project, resolving material engineering decisions, and designing relevant security and reliability controls. Use for architecture, module responsibilities, interfaces, data flow, data models, transactions, compatibility, and implementation constraints. Do not use for full product discovery, code implementation, implementation task breakdown, complete test planning or execution, or post-implementation code review.
---

# Wewo ERD

Turn requirement material and verified project facts into a confirmed
engineering design. Treat an entity-relationship diagram as optional data
design content, not as the skill's primary purpose.

## Inputs and output

Accept requirement context from the current conversation, text, Markdown, TXT,
office documents, PDFs, images, issues, tasks, change or bug descriptions,
current project code, and an optionally explicitly supplied or already
established `prd.md`. A `prd.md` is simply a requirement artifact; the skill
does not care which capability produced it.

Create only:

```text
docs/wewo/<requirement-category>/<requirement-slug>/technical-design.md
```

Keep the filename and path segments in English. Conduct user interaction and
write the document in an explicitly requested language, otherwise the dominant
interaction language, and otherwise Chinese.

## Mandatory workflow

### 1. Establish context and resolve the workspace

Run independently. Use `prd.md` or other requirement artifacts only when the
user explicitly supplies them, explicitly references them, or the current
conversation already establishes them. Never require them, never ask the user
to create them first, and never scan the repository to find them. Establish the
minimum requirement context within this skill when no usable artifact exists.

Resolve the requirement workspace before creating a document:

1. Use an explicit workspace supplied by the user.
2. Otherwise reuse the workspace already established for this requirement.
3. Otherwise infer a candidate from the requirement, issue, branch, or
   explicitly supplied or referenced material.
4. Ask before writing when more than one workspace is plausible.

Never infer a workspace from the existence of workflow artifacts. Never select
the most recently modified workspace by default. Use `features`, `bugs`,
`refactors`, or `maintenance`; default to `features` only when no evidence
favors another category. Use a concise lowercase English kebab-case slug.

Create missing parent directories only after resolution is unambiguous. Never
mix different requirements in one workspace without explicit confirmation. Do
not create documents owned by other capabilities.

### 2. Assess requirements and analyze the project

Read and apply
[requirements-and-project-analysis.md](references/requirements-and-project-analysis.md).

Combine the user's current request with materials explicitly supplied or
referenced in this interaction. Do not scan `docs/wewo/` or the repository for
historical requirement documents. Do not treat any single file as the only
truth. Surface material conflicts and ask which requirement governs.

Determine whether the goal, affected users or modules, core business result,
scope, and implementation-shaping rules are clear enough for design. Ask only
the missing questions needed here; request additional requirement clarification
or requirement context only when the user explicitly wants it, never as a
prerequisite.

For an existing project, analyze only the portions of the repository needed to
produce a grounded design. Inspect the relevant stack, structure, layers,
modules, interfaces, APIs, data models, permissions, authentication and
authorization implications, validation, transactions, concurrency, idempotency,
security, reliability, dependencies, migration, compatibility, observability,
similar implementations, and conventions. Obtain project facts directly instead
of asking the user to repeat them.

Do not invent paths, classes, functions, interfaces, tables, modules, or
frameworks. If a source format cannot be read with current capabilities, state
the limitation and request an accessible export or the relevant pasted content.
Do not claim it was analyzed.

### 3. Establish the impact scope and candidate design

Identify what will change, what will be added, and what is explicitly
unchanged. Prefer existing architecture, shared capabilities, dependency
injection, lifecycle management, terminology, and response or error
conventions. Avoid unnecessary modules, abstractions, patterns, and
dependencies.

Adapt the design to the actual requirement type using
[design-coverage.md](references/design-coverage.md). Include only relevant
frontend, backend, interface, data, integration, migration, compatibility, and
operational concerns.

Separate repository facts from engineering decisions. Obtain discoverable
repository facts directly; do not ask the user to decide them. Ask or confirm
material engineering decisions only when alternatives have meaningful
trade-offs or irreversible consequences. Develop an evidence-based candidate
solution, but do not record a recommendation as final until the user confirms
every choice that materially changes implementation.

### 4. Resolve decisions progressively

Read and apply
[design-dialogue.md](references/design-dialogue.md).

Discuss one technical topic per round and normally ask one to three tightly
related questions. For each material choice:

- state the requirement and project evidence;
- explain the viable choices;
- recommend the best fit for the existing project;
- explain the tradeoff;
- ask the user to confirm or adjust the decision.

Re-evaluate unresolved decisions after every answer. Do not turn universal
engineering safeguards into unnecessary questions.

### 5. Integrate proactive risk design

Read and apply
[risk-design.md](references/risk-design.md) while discussing each design topic,
not as a generic checklist added at the end.

Analyze only relevant risks across:

1. application security;
2. reliability and business correctness;
3. code structure and maintainability.

Convert each real risk into a concrete design measure and an enforceable
implementation constraint. Security here is pre-implementation design, not
post-implementation review.

### 6. Define testability and verification seams

Where useful, define focused Testability / Verification Seams: engineering
boundaries suitable for implementation verification, for example an
application-service boundary, a domain-operation boundary, an API boundary, or
an integration seam. These are engineering-design boundaries, not QA test
cases. Do not turn them into detailed test steps, test-plan content, or
execution-tool decisions. The design's Verification Focus section records the
directions later verification must emphasize, without generating a full test
plan or test cases.

### 7. Check the generation gate

Do not generate the technical design while any condition holds:

- the basic requirement goal is unclear;
- source materials contain an unresolved critical conflict;
- the core approach still has multiple unconfirmed options;
- a key authorization rule is unknown;
- consistency or failure behavior is unknown;
- permission to change an existing interface or database is unresolved;
- a material security or reliability concern lacks a design response;
- the user has not confirmed the complete technical solution;
- the destination workspace is ambiguous.

When the design is ready, summarize its sources, impact scope, overall
approach, module responsibilities, interface and data changes, key security
measures, reliability measures, code-structure constraints, testability seams,
and unresolved questions. Ask the user to correct or explicitly confirm the
summary. Generate nothing until confirmation.

### 8. Generate the confirmed technical design

Before writing, read
[technical-design-document.md](references/technical-design-document.md) and
use [technical-design-template.md](assets/technical-design-template.md).
Localize headings and prose while preserving the required structure and
English filename.

Write only to
`docs/wewo/<requirement-category>/<requirement-slug>/technical-design.md`.
If that file exists, treat an explicit update request as authorization;
otherwise ask before replacing it.

Do not modify production code or executable tests. Do not create a separate ERD
file. Include a Mermaid ER diagram inside the technical design only when
database entities or relationships change; use a clear textual schema
description if diagram rendering is unavailable. Do not add empty irrelevant
sections. Do not create QA test plans, test cases, or execution-tool decisions.

After a successful write, report:

- the exact document path;
- the core technical approach;
- whether database changes and an ER diagram are involved;
- the testability and verification seams;
- whether unresolved questions remain.

Do not continue automatically into implementation, task planning, test
planning, test execution, or review. Claim completion only after the file was
actually written and verified.
