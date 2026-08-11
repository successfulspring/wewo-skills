---
name: wewo-prd
description: Clarify incomplete software product requirements through progressive, user-confirmed questioning and create prd.md only after confirmation. Use for product goals, users, flows, business rules, scope, exceptions, and acceptance criteria from user-provided or explicitly selected sources. Do not use for technical design, ERDs, implementation planning, coding, test creation or execution, or code review.
---

# Wewo PRD

Turn incomplete source material into a user-confirmed product requirements
document without crossing into technical design or implementation.

## Inputs and output

Accept user intent and confirmed conversation context, plus requirement
material explicitly supplied or referenced by the user: text, images, TXT or
office documents, multiple related materials, an explicitly identified issue or
task, or an existing requirement workspace.

Create only:

```text
docs/wewo/<requirement-category>/<requirement-slug>/prd.md
```

Keep the filename and path segments in English. Write the document and conduct
the conversation in the explicitly requested language, otherwise the dominant
interaction language, and otherwise Chinese.

## Mandatory workflow

```text
Requirement Intake
-> Explicit Source / Repository Fact Analysis
-> Dynamic Decision Map
-> Decision Topic Clarification
-> User Answer
-> Update Decision Map
-> Expand Material Dependent Branches
-> Repeat
-> Coverage Audit
-> Branch Expansion Audit
-> Structured Requirement Summary
-> Synthesis Provenance Audit
-> Final User Confirmation
-> Adaptive PRD Composition
-> prd.md
```

This flow creates no intermediate workflow artifact. The Decision Map and
audits are internal runtime reasoning protocols; the only owned business
artifact remains `prd.md`.

### 1. Establish context and resolve the workspace

Start from the user's current request and confirmed conversation context.
Establish the minimum requirement context here when no usable artifact exists.
Use only material explicitly supplied or referenced in this interaction.

Resolve the requirement workspace before creating any document:

1. Use a workspace path explicitly supplied by the user.
2. Otherwise reuse the workspace established for the current requirement.
3. Otherwise infer a candidate from the requirement, an explicitly identified
   issue or task, or the branch when appropriate.
4. Ask before writing if more than one workspace is plausible.

Never infer a workspace from the existence of workflow artifacts; artifact
existence is not an input-selection signal. Never choose a workspace because it
was modified most recently. Use `features`, `bugs`, `refactors`, or
`maintenance` as the category. Default to `features` only when no category was
supplied and no evidence favors another category. Use a concise lowercase
English kebab-case slug.

Do not create parent directories until resolution is unambiguous. Do not reuse
one workspace for different requirements unless the user explicitly confirms
they are the same requirement.

### 2. Select and analyze authorized sources

Apply the opt-in rules in
[source-handling.md](references/source-handling.md). Never scan `docs/wewo/`
or the repository for historical requirement documents; a document's existence
in a workspace does not by itself authorize it as input. For a new PRD request,
do not automatically read an existing `prd.md`. Never recursively read Markdown
files or treat repository documentation as business requirements. External
source documents outside `docs/wewo/...` are read-only.

Read the authorized material before asking questions. Separate:

- established facts and confirmed requirements;
- vague or missing information;
- conflicts between sources;
- discussion or proposal content;
- product decisions requiring user confirmation;
- temporary assumptions that must not become requirements.

### 3. Gather repository facts selectively

Repository reconnaissance is allowed only to understand current-state facts.
The repository may answer questions such as:

- what behavior exists today;
- which states already exist;
- which product concepts or terms already exist;
- which related capability already exists.

Repository facts must not decide desired behavior, business rules, desired
scope, acceptance policy, or any product decision. The user decides
requirements.

Obtain accessible repository facts directly rather than asking the user to
repeat them. If the current host cannot read a source format, explain the
limitation and ask for a text export, screenshots, or pasted relevant content.
Do not pretend the source was analyzed.

### 4. Clarify progressively

Read and apply
[clarification-guide.md](references/clarification-guide.md) and
[decision-map.md](references/decision-map.md).

Build a dynamic decision tree from the material. Discuss one topic per round
using this model:

```text
Requirement
-> Decision Topic
-> Decision Questions
-> Dependent Branches
```

One round means exactly one Decision Topic, not one question. A substantial
topic should normally contain around 2–5 tightly related Decision Questions;
a simple topic may contain one. This is a preference, never a maximum, minimum,
or stopping rule. Questions in the same round should normally be answerable in
parallel. Defer a question when its relevance, options, or existence depends
materially on an unanswered prerequisite.

Maintain the internal Decision Map throughout the conversation. After every
material answer, resolve the current decision, record valid provenance, update
the requirement understanding, eliminate irrelevant branches, expand newly
unlocked material dependent branches, keep those branches unresolved, and
choose the highest-value unresolved Decision Topic. Do not treat a resolved
answer as merely finished or ask a question merely because it appeared in the
initial map. Never write the map under `docs/wewo/...` or present it as a
business artifact.

Number topics `Topic 1`, `Topic 2`, and so on. Within them use stable question
IDs `Q1.1`, `Q1.2`, then `Q2.1`, and so on. Once assigned, do not reuse an ID
for a different decision. For each individual closed or semi-closed question,
label options `A`, `B`, `C`, `D` as applicable and restart at `A`; do not mix
lettered and numbered option references. Keep these identifiers stable, but
localize surrounding user-facing labels to the conversation language.

For each material decision:

- explain why it matters;
- state the current evidence-based understanding;
- where appropriate, offer 2–4 materially distinct options and an Other or
  custom route when useful;
- when evidence supports a recommendation for a single-choice question,
  recommend exactly one listed option by its actual letter and explain the
  reason, important tradeoff, or assumption;
- when evidence is insufficient, explicitly say that no option can yet be
  recommended;
- ask the user to confirm, reject, or revise it.

Recommendations are proposals, never confirmations. Surface source conflicts
and material assumptions explicitly. Do not silently decide permissions,
allowed states, result behavior, notifications, historical-data handling, or
failure behavior. Ground recommendations preferentially in confirmed user
goals, confirmed requirements, verified repository facts, explicit
constraints, and directly explainable tradeoffs. Present general patterns only
as general guidance; do not use unsupported claims such as "industry
standard," "mainstream products," or "best practice" as factual evidence.

Prefer semantically explicit business options over confusing yes/no or
negated phrasing. Be exhaustive about material requirement branches, not about
theoretical possibilities. A question is material when its answer can change
scope, visible behavior, rules, roles or permissions, lifecycle, main flow,
business or data consequences, exception behavior, compatibility, acceptance
outcomes, or material business risk. Do not expand into code, database fields,
API paths, technical architecture, test tooling, or deployment. Record
user-supplied technical details only as constraints or references.

### 5. Check the stopping conditions

Before presenting the final requirement summary, read and apply
[completeness-audit.md](references/completeness-audit.md). Run all three layers:
Coverage Audit, Branch Expansion Audit, and Synthesis Provenance Audit. Reopen
clarification when a relevant material dimension is unresolved, a confirmed
decision created an unresolved second-order product branch, or a planned
material rule lacks valid provenance.

A material branch is complete only when it is `Confirmed`, `Explicitly Out of
Scope`, `Explicitly Deferred by the User`, or `Intentionally Unresolved with
the User Accepting the Remaining Risk`. Never guess an unanswered product
decision or convert an unknown into a recommended choice. There is no maximum
number of rounds, questions, or interview duration; stop based on material
requirement completeness, not question count or elapsed conversation length.

Do not generate the PRD while any of these conditions holds:

- the core goal is unclear;
- the primary users are unclear;
- the core business flow has a material conflict;
- a business rule that changes functional outcomes is unconfirmed;
- the in-scope and out-of-scope boundaries are unclear;
- the user has not confirmed the overall requirement understanding;
- the workspace or source authorization is ambiguous.

If the user asks to stop questioning or generate the PRD early, identify the
remaining material unresolved branches, state that the skill will not decide
them automatically, and ask the user to confirm acceptance of those unresolved
or deferred items. Proceed only after that confirmation, preserving them in
the summary and PRD where appropriate.

After the audit, summarize confirmed scope, users and roles, main flows,
business rules, relevant exception behavior, out-of-scope items, and deferred
or unresolved items. Ask the user to correct omissions or explicitly confirm
that this summary accurately represents the requirement. Only that final
confirmation authorizes writing `prd.md`.

### 6. Synthesize the confirmed PRD

Clarification and synthesis are two phases. Once the user confirms the
clarified understanding, synthesis writes the PRD rather than restarting the
interview, unless genuinely new ambiguity appears that requires more
clarification.

Before writing, read
[prd-document-guide.md](references/prd-document-guide.md) and optionally consult
[prd-structure-patterns.md](references/prd-structure-patterns.md). Compose the
document adaptively from the confirmed requirement's relevant semantic
dimensions. Do not force identical headings, section counts, or ordering, and
do not create empty or low-value sections merely to satisfy a document shape.
Keep the filename `prd.md` in English while localizing headings and prose.

Keep the PRD product-semantic. Do not normally include implementation file
paths, function or class names, test file names, code snippets, internal
architecture decisions, or database implementation details, unless one of
those is itself an explicit business or technical constraint provided by the
user.

Include only content covered by the confirmed overall understanding and valid
decision provenance. Preserve material unresolved or deferred decisions where
useful, but do not create an empty unresolved section merely to say "None."
Do not present an AI recommendation, assumption, implementation convenience,
unsupported general claim, or repository current-state fact as a confirmed
future product rule. When a product outcome is confirmed but an implementation
choice is not, write only the product-semantic outcome. Record the actual
requirement sources used.

Write only to the resolved
`docs/wewo/<requirement-category>/<requirement-slug>/prd.md` path. If that
file already exists, treat an explicit request to update it as authorization;
otherwise ask before replacing it. Never modify an external source document.

After a successful write, report:

- the exact PRD path;
- the requirement's core goal;
- the requirement sources used;
- whether unresolved questions remain.

Do not automatically continue into technical design, implementation, testing,
or review. Do not create documents owned by other capabilities. Claim success
only after the file was actually written and verified.
