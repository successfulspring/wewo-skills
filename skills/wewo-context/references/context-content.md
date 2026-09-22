# Context content and provenance

Both files are compact current-state snapshots, not accumulating execution
logs. Requirement history stays in its owning documents and, when available,
Git history. Include only information that changes a later requirement's
understanding or decisions; omit empty sections and arbitrary size quotas.

## Project context

Use `docs/wewo/project-context.md` for applicable reusable knowledge:

- project purpose, domain vocabulary, core entities, and stable user roles;
- shared business rules, permission principles, and product constraints;
- system and module boundaries, important contracts, and relevant data flows;
- compatibility, consistency, security, and reliability constraints;
- short source references sufficient to revisit a material conclusion.

Identify the common code baseline and applicability. This file is versioned in
each checkout: its path does not prove that every branch has the described
capabilities. A branch-only implementation cannot become a common fact just
because it was copied here. A pending pre-merge amendment must be visibly
separated from established facts, with its proposed integration baseline and
pending status, so readers cannot consume it as current common behavior.

## Branch context

Use `docs/wewo/<workspace-key>/branch-context.md` for reusable additions or
differences relative to the project context actually available in this checkout:
implemented capabilities, branch-specific rules, interfaces or model changes,
architectural constraints, deviations, and superseding rules. Link to relevant
requirement and implementation evidence without copying whole documents.

Identify the branch/local workspace, actual inspected code scope, and the
project-context version or baseline used when material. If project context is
absent, retain the minimum standalone verified baseline; do not create an empty
project file as a prerequisite. The `local` workspace uses this same filename.

## Evidence and meaning

Keep metadata small and meaningful: scope, relevant revision or baseline when
available, last verification date, and evidence/source references. Do not label
uncommitted changes as proved by HEAD. Describe dirty-worktree or unversioned
limitations and tie evidence to the actual inspected files when no commit
represents them. Record unavailable revisions honestly.

Distinguish these kinds of knowledge:

- **Verified implementation fact:** observed in the relevant current code and
  supported by applicable evidence; describe what is actually implemented.
- **Confirmed policy:** explicitly agreed behavior or constraint. Identify its
  source and any enforcement gap; agreement does not make a missing mechanism
  exist. Observed code, including a bug, does not establish intended policy.
- **Proposal or unresolved requirement decision:** keep it in the owning
  requirement document, not among current context facts. The explicitly
  requested pending project amendment is the qualified exception above.

Use short locators to existing sources; do not invent inaccessible history or
flatten conflicting evidence. A missing source requires verifying the affected
claim or omitting/qualifying it, not treating every other supported fact as blocked.

## Sensitive information

<!-- wewo:sensitive-information:start -->
Never include real passwords, tokens, cookies, private keys, database connection
credentials, authentication-bearing URLs, production user data, or personal
private data in either context file. This also applies to evidence excerpts,
metadata, citations, and proposed patches or summaries. A confirmed source or
patch does not make sensitive values suitable for version-controlled context.

Before presenting a patch and before writing, omit or redact sensitive values
while preserving the reusable meaning. Record configuration names or abstractions,
such as credentials supplied through `DATABASE_PASSWORD` or authentication
through `API_TOKEN`, without assignments or real values. Remove authentication
query parameters, userinfo, and sensitive fragments from source locators; retain
a non-sensitive locator or describe the evidence gap. Verify the resulting files
contain no copied sensitive values. Do not automatically read secret files to
perform this check or alter the source evidence.
<!-- wewo:sensitive-information:end -->

## Reconciliation

Replace superseded rules rather than appending mutually contradictory versions.
Merge duplicates while retaining meaningful qualifications and provenance.
Remove obsolete conclusions and keep only reusable conclusions plus necessary
detail links. Do not remove unrelated manually maintained content under the
label of cleanup.

Keep branch differences relative to the project context in this checkout.
Remove a branch duplicate only once the corresponding applicable fact is
actually available in that project context, not merely in another branch or a
proposed promotion. If a common fact has changed, preserve a still-applicable
branch deviation instead of silently adopting the newer behavior.

Do not store full PRDs or designs, exhaustive requirement indexes, test-case
inventories, execution logs, full reviews, speculative future designs, or
generic engineering advice. Do not introduce domain sharding, search indexes,
databases, scheduled compaction, or automatic background synchronization.
