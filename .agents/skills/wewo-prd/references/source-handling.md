# Source Handling

Use this guide whenever requirement context may come from files, images,
repository content, or linked work items.

## Authorize business-requirement sources

Read or incorporate an external requirement document only when at least one
condition holds:

1. The user explicitly references the document.
2. The user explicitly provides a requirement workspace for the current
   requirement, authorizing the documents of that requirement.
3. The user explicitly asks to continue, revise, or update an existing
   requirement.
4. The user uploads or pastes it in the current interaction.
5. The user explicitly identifies an issue, task, merge request, or document
   as a source for this requirement.

Never scan `docs/wewo/` or the repository for historical requirement
documents. A document's presence in a workspace does not by itself authorize
it as input. For a new PRD request, do not automatically read an existing
`prd.md`.

Treat an external source outside `docs/wewo/...` as read-only. Never overwrite,
edit, annotate, or relocate it.

Do not recursively read Markdown files, select documents because their content
seems similar, or combine historical material without authorization.

## Separate repository instructions from requirements

Read `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, and relevant `README.md`
files when needed to understand repository conventions. Do not treat their
content as a business requirement unless the user explicitly authorizes that
use.

## Gather repository facts selectively

Repository reconnaissance is allowed only to understand current-state facts
such as what behavior exists today, which states exist, which product concepts
or terms exist, and which related capability already exists.

Repository facts must not decide desired behavior, business rules, desired
scope, acceptance policy, or any product decision. The user decides
requirements. Do not infer requirement intent from implementation convenience.

## Analyze authorized material

Maintain a working source inventory with:

- source identity and authorization basis;
- confirmed statements;
- factual observations;
- proposals or discussion points;
- ambiguities and omissions;
- conflicts with other sources;
- decisions that still require confirmation.

Do not ask the user to repeat information already available in an authorized
source. When sources conflict, describe the conflicting claims and ask which
one governs; do not silently rank them.

### Text and conversation

Extract explicit needs, key terms, user roles, business actions, constraints,
vague expressions, possible contradictions, and implied decisions.

### Images

Inspect relevant page structure, labels, entry points, visible states, marked
change locations, and state changes. Identify interaction details that the
image cannot establish. Never infer a complete requirement from a screenshot
alone.

### TXT, office documents, PDFs, and other documents

Use a source-capable reader available in the current host. Extract requirement
information, merge duplicate statements, mark conflicts, and distinguish
settled content from discussion. If the format cannot be read, ask for an
accessible export or the relevant pasted content.

### Multiple sources

Analyze authorized sources together without losing provenance. Deduplicate
equivalent statements, but do not merge materially different requirements.
Ask the user whether apparently separate requirements belong in one workspace
before combining them.

## Facts versus decisions

Obtain verifiable facts from authorized files, images, source code, or project
content when possible, including existing framework, screens, domain terms,
states, and functionality.

Require user confirmation for decisions such as:

- who can use the capability;
- which states permit an action;
- success and failure behavior;
- scope boundaries;
- notification behavior;
- historical-data compatibility;
- the desired user-visible result.

Offer recommendations to help the user decide, but never record an unaccepted
recommendation as a requirement.
