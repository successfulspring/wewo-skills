---
name: wewo-erd
description: Produce a user-confirmed, implementation-guiding technical design for a feature, bug, refactor, or maintenance requirement by analyzing the existing project, resolving material engineering decisions, and designing relevant security and reliability controls. Use for architecture, module responsibilities, interfaces, data flow, data models, transactions, compatibility, and implementation constraints. Do not use for full product discovery, code implementation, implementation task breakdown, complete test planning or execution, or post-implementation code review.
---

# Wewo ERD

Transform confirmed requirement context, verified repository facts, and
resolved material engineering decisions into an Engineering Design
Specification. Treat an entity-relationship diagram as optional data-design
content, not as the skill's primary purpose.

The design must let a fresh implementation agent begin work without inventing
material engineering decisions. It explains what changes, why the design has
this shape, which existing boundaries are reused, which responsibilities are
new, how interfaces, data, state, and lifecycle change, and which constraints
and engineering invariants implementation must preserve.

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

```text
Requirement / Explicit Requirement Artifact
-> Requirement Understanding
-> Progressive Repository Discovery
-> Engineering Impact Map
-> Engineering Decision Map
-> Engineering Decision Dialogue where needed
-> Dependent Engineering Branch Expansion
-> Engineering Risk Design
-> Engineering Invariants
-> Verification Seams
-> Coherence / Enforceability / Interleaving Checks
-> Design Closure Audit
-> Final Design Summary
-> Explicit User Confirmation
-> Adaptive technical-design.md
```

These are runtime reasoning protocols, not extra workflow artifacts. The only
owned business artifact is `technical-design.md`.

### 1. Establish context and resolve the workspace

Run independently. Use `prd.md` or another requirement artifact only when the
user explicitly supplies or references it, or the current conversation already
establishes it. Never require such an artifact, ask the user to create one
first, or scan the repository to find one. Establish the minimum requirement
context within this skill when no usable artifact exists.

Resolve the requirement workspace before creating a document:

1. Use an explicit workspace supplied by the user.
2. Otherwise reuse the workspace already established for this requirement.
3. Otherwise infer a candidate from the requirement, issue, branch, or
   explicitly supplied or referenced material.
4. Ask before writing when more than one workspace is plausible.

Never infer a workspace from workflow-artifact existence or recency. Use
`features`, `bugs`, `refactors`, or `maintenance`; default to `features` only
when no evidence favors another category. Use a concise lowercase English
kebab-case slug. Create missing parents only after resolution is unambiguous,
never mix unrelated requirements, and never create another capability's
artifact.

### 2. Understand the requirement and discover the project progressively

Read and apply
[requirements-and-project-analysis.md](references/requirements-and-project-analysis.md).

Use only requirement material explicitly supplied, referenced, or established
in the current conversation. Do not scan `docs/wewo/` or the repository for
historical workflow documents. Surface material source conflicts for user
resolution.

For an existing project, use decision-driven progressive technical discovery:
identify affected entry points, trace relevant control and data flow, form the
current Engineering Impact Map, and inspect more only when a design branch
requires evidence. Stop discovery for a decision when enough verified
repository evidence supports it; do not explore the whole repository by
default or impose arbitrary tool-call or token limits.

Distinguish claims as `Existing`, `Proposed`, `Constraint`, or `Decision`.
Existing-project claims must be verified. Never present proposed design as a
verified repository fact. Proposed design may introduce justified
responsibilities, modules, interfaces, data structures, tables or fields,
components, configuration, and dependencies. Do not pretend that proposed
paths, classes, functions, or modules already exist, and avoid exact names when
the verified repository structure or confirmed design does not require them.

### 3. Establish impact and engineering decision ownership

Read and apply
[design-coverage.md](references/design-coverage.md) and
[engineering-decision-map.md](references/engineering-decision-map.md).

Identify what changes, what is added, and what is explicitly unchanged. Prefer
verified existing architecture, shared capabilities, dependency direction,
dependency injection, lifecycle management, terminology, and response or error
conventions unless a concrete reason supports change.

Classify every material engineering issue as one of:

1. `Repository Fact`;
2. `User Technical Constraint`;
3. `Engineering Default`;
4. `Material Engineering Decision`;
5. `Blocking Requirement Ambiguity`.

Discover repository facts rather than asking the user to repeat them. Preserve
explicit constraints without silently broadening them. Decide routine
Engineering Defaults from verified facts, project conventions, requirement
constraints, and minimal-complexity judgment. Ask the user only about Material
Engineering Decisions and Blocking Requirement Ambiguities.

An Engineering Default may rely on assumptions, but any assumption that
materially affects correctness, security, consistency, deployment,
availability, data safety, or scalability architecture needs valid provenance.
If it is not a verified Repository Fact, explicit User Technical Constraint, or
confirmed Material Engineering Decision, escalate it rather than silently
adopting it. Treat an unsupported numeric value as a tuning hypothesis or
unresolved non-blocking parameter, not as a confirmed Engineering Default.

Maintain the internal Engineering Decision Map throughout design. After each
material answer, update the decision and provenance, eliminate irrelevant
branches, identify newly unlocked material engineering branches, keep them
unresolved, and select the next highest-value Decision Topic. Never create a
decision-map artifact under `docs/wewo/`.

### 4. Resolve material decisions progressively

Read and apply [design-dialogue.md](references/design-dialogue.md).

Discuss exactly one Decision Topic per round. A topic may contain multiple
tightly related, normally parallel-answerable questions. Defer a question when
its relevance, options, or existence depends materially on an unanswered
prerequisite. Preserve stable topic, question, and option identifiers while
localizing surrounding labels.

For each Material Engineering Decision:

- state verified requirement and repository evidence;
- present viable options;
- recommend exactly one listed option when evidence supports it;
- explain direct trade-offs, consequences, operational burden, and
  reversibility where material;
- request explicit user confirmation.

Do not ask the user to decide routine implementation details. Do not introduce
architecture, infrastructure, patterns, dependencies, performance targets, or
SLA values because they are fashionable or unsupported.

### 5. Design risks, invariants, and verification seams

Read and apply [risk-design.md](references/risk-design.md) within the affected
design areas, not as a generic final checklist. Analyze only relevant risks
across Security, Correctness and Consistency, Architecture and Maintainability,
and Reliability and Resource Safety.

For every admitted material risk, derive the relevant parts of:

```text
Risk
-> Location / Trust or Failure Boundary
-> Design Control
-> Hard / Enforceable Invariant with a concrete mechanism
   OR Implementation / Architecture Constraint
   OR Risk-Reduction Control with Residual Risk
-> Verification Seam where useful
```

For every claimed material invariant, identify the concrete mechanism that
makes it hold. A stated `MUST` is not enough. If no credible mechanism exists,
do not describe the property as guaranteed; classify it as an implementation
constraint or risk-reduction control and record material residual risk.

When async, stateful, retried, scheduled, callback-driven, queued, or concurrent
work is relevant, examine material interleavings: what other actor can change
the resource between important steps, and what explicit guard preserves the
design property? For multi-step state-changing workflows, also determine what
happens when failure occurs after one or more side effects commit and how retry
or recovery remains safe.

For important invariants, identify stable verification seams such as an
application or use-case service, domain operation, public API contract,
repository or integration boundary, or message-consumer boundary. Record the
linked invariant or behavior and observable property where useful. Do not
generate detailed test cases, QA steps, concrete testing-tool choices, or TDD
instructions.

### 6. Run the Design Closure Audit

Read and apply
[design-closure-audit.md](references/design-closure-audit.md) before final
confirmation. Evaluate only relevant dimensions. Continue repository
investigation, engineering reasoning, or user dialogue whenever a material
dimension remains unresolved.

Do not generate the design until all of these conditions hold:

- requirement context is sufficient for engineering design;
- relevant repository evidence has been obtained;
- Material Engineering Decisions are resolved;
- Blocking Requirement Ambiguities are resolved;
- the complete proposed design has no material cross-section contradiction;
- claimed hard invariants have credible enforcement mechanisms, while
  constraints and risk-reduction controls are labeled honestly;
- relevant risks have concrete controls, constraints, residual-risk treatment,
  and invariants where justified;
- material interleavings and partial-side-effect recovery are resolved where
  relevant;
- material runtime or deployment assumptions have valid provenance;
- schema or contract evolution and data migration or backfill are separately
  resolved where relevant;
- unsupported arbitrary tuning values are not presented as confirmed design;
- material compatibility and rollback consequences are resolved;
- useful Verification Seams are identified;
- the Design Closure Audit passes;
- the output workspace is unambiguous.

Closure depends on material engineering branches, not a predefined number of
topics, questions, rounds, tool calls, or elapsed conversation length.

### 7. Present the final design summary and require confirmation

Summarize requirement sources, verified existing system and impact scope,
proposed responsibilities and data flow, interface and state changes,
engineering decisions and reasons, risk controls, implementation invariants,
constraints, residual risks, material assumptions, compatibility or migration
consequences, observability, verification seams, and any deliberately
unresolved non-blocking issue.

Ask the user to correct or explicitly confirm the complete design summary.
Never infer confirmation from silence or agreement with only one topic. Write
nothing until explicit final confirmation.

### 8. Generate the adaptive technical design

After confirmation, read
[technical-design-document.md](references/technical-design-document.md) and
use [technical-design-template.md](assets/technical-design-template.md) as an
adaptive composition scaffold.

Write only to
`docs/wewo/<requirement-category>/<requirement-slug>/technical-design.md`.
If it exists, treat an explicit update request as authorization; otherwise ask
before replacing it.

Keep the document's Stable Core semantically present and add only relevant
detailed-design sections. Combine, rename, reorder, or omit sections when that
communicates the confirmed design more clearly. Do not create empty sections or
an Unresolved Questions section merely to say `None`.

Do not modify production code or executable tests. Do not create a separate ERD
file. Include a Mermaid ER diagram inside the design only when database entities
or relationships change; use a textual schema description if rendering is
unavailable.

Do not generate ordered coding tasks, file-by-file implementation checklists,
vertical slices, implementation sequencing, Red/Green/Refactor steps,
executable tests, QA test cases, test execution instructions, or testing-tool
decisions. Proposed responsibilities, modules, interfaces, and affected areas
are allowed when they materially communicate architecture.

After a successful write, report:

- the exact document path;
- the core engineering approach;
- whether database changes and an ER diagram are involved;
- the material engineering invariants and verification seams;
- whether unresolved issues remain.

Do not automatically continue into implementation, task planning, test
planning, test execution, or review. Claim completion only after the file was
actually written and verified.
