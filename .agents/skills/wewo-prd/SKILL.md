---
name: wewo-prd
description: Clarify incomplete software product requirements through progressive, user-confirmed questioning and create 01-prd.md only after confirmation. Use for product goals, users, flows, business rules, scope, exceptions, and acceptance criteria from user-provided or explicitly selected sources. Do not use for technical design, ERDs, implementation planning, coding, test creation or execution, or code review.
---

# Wewo PRD

Turn incomplete source material into a user-confirmed product requirements
document without crossing into technical design or implementation.

## Inputs and output

Accept an idea from the conversation, text, images, TXT or office documents,
multiple related materials, an explicitly identified issue or task, or an
existing requirement workspace.

Create only:

```text
docs/wewo/<requirement-category>/<requirement-slug>/01-prd.md
```

Keep the filename and path segments in English. Write the document and conduct
the conversation in the explicitly requested language, otherwise the dominant
interaction language, and otherwise Chinese.

## Mandatory workflow

### 1. Establish context and resolve the workspace

Identify the current project and requirement without requiring an earlier Wewo
stage. Start from the user's current request. Use only material explicitly
provided in this interaction, explicitly referenced sources, and explicitly
confirmed candidate sources. Establish the minimum context needed here when no
authorized upstream material exists.

Resolve the requirement workspace before creating any document:

1. Use a workspace path explicitly supplied by the user.
2. Otherwise reuse the workspace established for the current requirement.
3. Otherwise infer a candidate from the requirement, an explicitly identified
   issue or task, the branch, or authorized upstream material.
4. Ask before writing if more than one workspace is plausible.

Never choose a workspace because it was modified most recently. Use
`features`, `bugs`, `refactors`, or `maintenance` as the category. Default to
`features` only when no category was supplied and no evidence favors another
category. Use a concise lowercase English kebab-case slug.

Do not create parent directories until resolution is unambiguous. Do not reuse
one workspace for different requirements unless the user explicitly confirms
they are the same requirement.

### 2. Select and analyze authorized sources

Apply the opt-in rules in
[source-handling.md](references/source-handling.md). Never scan `docs/wewo/`
or the repository for historical requirement documents; a document's
existence in a workspace does not by itself authorize it as input. For a new
PRD request, do not automatically read an existing `01-prd.md`. Never
recursively read Markdown files or treat repository documentation as business
requirements. External source documents outside `docs/wewo/...` are read-only.

Read the authorized material before asking questions. Separate:

- established facts and confirmed requirements;
- vague or missing information;
- conflicts between sources;
- discussion or proposal content;
- product decisions requiring user confirmation;
- temporary assumptions that must not become requirements.

Obtain accessible repository facts directly rather than asking the user to
repeat them. If the current host cannot read a source format, explain the
limitation and ask for a text export, screenshots, or pasted relevant content.
Do not pretend the source was analyzed.

### 3. Clarify progressively

Read and apply
[clarification-guide.md](references/clarification-guide.md).

Build a dynamic decision tree from the material. Discuss one topic per round
and normally ask one to three tightly related questions. Start with
high-impact, upstream decisions and revisit the tree after each answer.

For each material decision:

- explain why it matters;
- state the current evidence-based understanding;
- offer a recommended option when useful;
- ask the user to confirm, reject, or revise it.

Recommendations are proposals, never confirmations. Surface source conflicts
and material assumptions explicitly. Do not silently decide permissions,
allowed states, result behavior, notifications, historical-data handling, or
failure behavior.

Avoid exhaustive questioning. Gather enough product detail to support later
design and development, but do not design code, database fields, API paths,
technical architecture, test tooling, or deployment. Record user-supplied
technical details only as constraints or references.

### 4. Check the stopping conditions

Do not generate the PRD while any of these conditions holds:

- the core goal is unclear;
- the primary users are unclear;
- the core business flow has a material conflict;
- a business rule that changes functional outcomes is unconfirmed;
- the in-scope and out-of-scope boundaries are unclear;
- the user has not confirmed the overall requirement understanding;
- the workspace or source authorization is ambiguous.

When the main questions are resolved, summarize the problem, target users,
core capability, key rules, main exceptions, in-scope work, and explicitly
out-of-scope work. Ask the user to correct omissions or confirm that this
summary accurately represents the requirement. Generate nothing until the
user confirms it.

### 5. Generate the confirmed PRD

Before writing, read
[prd-document-guide.md](references/prd-document-guide.md) and use
[prd-template.md](assets/prd-template.md). Localize headings and prose to the
output language while preserving the required structure and the English
filename.

Include only content covered by the confirmed overall understanding. Preserve
remaining known open questions in the final section; write the localized
equivalent of "None" when there are none. Do not present an AI guess as a
confirmed requirement.

Write only to the resolved
`docs/wewo/<requirement-category>/<requirement-slug>/01-prd.md` path. If that
file already exists, treat an explicit request to update it as authorization;
otherwise ask before replacing it. Never modify an external source document.

After a successful write, report:

- the exact PRD path;
- the requirement's core goal;
- whether unresolved questions remain.

Do not automatically continue into technical design, implementation, testing,
or review. Do not create empty documents for other workflow stages. Claim
success only after the file was actually written and verified.
