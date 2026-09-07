# Progressive Implementation Discovery

Discover repository facts only when they support a credible plan or the next
implementation unit.

## Before the plan

Inspect enough to establish:

- the requested production outcome and explicit non-goals;
- Binding Implementation Obligations;
- important entry points and likely affected paths;
- likely stable verification seams and repository-native commands;
- material feasibility conflicts, overlapping user work, and dirty-worktree
  risk.

Read applicable repository instructions and current configuration. Do not
broadly scan unrelated files or invent repository facts and commands. Read only
the capability-appropriate `prd.md` and `technical-design.md` automatically
from the exact resolved current Git branch and current requirement workspace;
do not discover workflow documents from sibling requirements or another branch
workspace.

## Before each unit

Inspect the exact affected files, tests, seams, dependencies, and runtime
mechanisms more deeply. Preserve unrelated user changes and stop when safe
isolation is impossible.

If a binding obligation depends on an existing mechanism's semantics, inspect
that mechanism before relying on it. This includes helpers, wrappers,
persistence operations, transactions, locks, caches, indexes, retries, delete
methods, libraries, and services. Do not infer behavior from its name, comments,
or design prose alone.

When the mechanism does not behave as the plan assumed, apply the Material Gap
Gate: proceed with an ordinary adjustment only if all binding obligations and
explicit non-goals remain preserved; otherwise stop for confirmation.

## Record only material reality

Keep the plan and record focused on verified facts that change scope,
sequencing, verification, or feasibility. Do not create a broad repository
inventory.
