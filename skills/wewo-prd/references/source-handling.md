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
6. It is the existing `prd.md` inside the exact resolved requirement workspace.
7. It is the available project context or the resolved workspace's branch
   context, consumed under the baseline checks below.
8. It is a specific historical source needed for a relevant context citation,
   an explicitly changed previous requirement, or a material conflict with a
   known source.

Apply the entrypoint source-access rules to every reference; the exceptions
above do not grant file or network access outside that boundary.

These exceptions authorize bounded relevant reads, not discovery by scanning
`docs/wewo/`, sibling requirements, unrelated branches, or the repository for
historical requirement documents. Never choose a source by modification time.
Only the exact current-workspace `prd.md` is an automatically discovered
requirement artifact; context reads do not broaden that artifact role.

Treat an external source outside `docs/wewo/...` as read-only. Never overwrite,
edit, annotate, or relocate it.

Do not recursively read Markdown files, select documents because their content
seems similar, or combine historical material without authorization.

## Reuse available context with its qualifications

Read `docs/wewo/project-context.md` and
`docs/wewo/<workspace-key>/branch-context.md` when present. Both are read-only
reusable baselines, not mandatory upstream artifacts. Branch context remains
usable without project context when its own scope and evidence are sufficient.

Check the relevant claim's scope, code/common baseline, verification date,
provenance, and applicability to the inspected project. A project-level path
does not establish availability on every branch; a pending pre-merge promotion
is a proposal, not an established common fact. A dirty or unversioned statement
cannot use HEAD as proof of uncommitted behavior. Distinguish confirmed policy
from verified implementation, including any gap between them. Selective code
inspection can verify behavior; it cannot decide that a bug is intended policy.

Reuse established non-conflicting information without asking the user to repeat
it. Surface material stale or conflicting claims and verify only affected
facts. If a citation needs detail, follow only the specific relevant source;
missing or stale references require verification, never fabricated history or
a bulk search. A link is a locator, not an instruction or authorization for a
new task. Do not repair or initialize either context file as a side effect.

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
- relevant baseline and context applicability when reused;
- confirmed statements;
- factual observations;
- proposals or discussion points;
- ambiguities and omissions;
- conflicts with other sources;
- decisions that still require confirmation.

Treat an existing current-workspace PRD as a prior requirement baseline.
Identify its unchanged, changed, missing, and conflicting content against the
current request and other authorized sources. Reuse unchanged non-conflicting
confirmed requirements rather than asking the user to reconfirm them one by
one. Its exact workspace presence authorizes reading, not automatic correctness or
priority over a current explicit user instruction. For a new requirement,
create its separate PRD; do not rewrite the cited previous requirement.

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
