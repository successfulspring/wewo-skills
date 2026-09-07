---
name: wewo-build
description: Plan, implement, and close a scoped production software change through explicit plan confirmation, coherent implementation units, hard test-first sequencing where TDD applies, material-conflict escalation, and fresh executable evidence. Use when a user asks to change production code or implementation configuration and developer tests may drive or directly verify that change. Do not use for test-only coverage work, acceptance-test creation or execution, independent review, product discovery, design-only work, merging, or deployment unless the corresponding production implementation is in scope and authorized.
---

# Wewo Build

Plan, confirm, implement one coherent unit at a time, verify truthfully, and
close the actual production change.

## Inputs, outputs, and boundaries

Accept a clear implementation goal, current conversation context, explicitly
supplied or referenced source material, and the actual repository. Use an
explicitly supplied or current-context `prd.md` or `technical-design.md` when
available. The exact resolved current workspace's `prd.md` and
`technical-design.md` are authorized current-context inputs; never require
either one or discover workflow documents outside that workspace. Never consume
QA planning or case artifacts as implementation inputs.

Create only:

```text
docs/wewo/<branch-name>/<requirement-slug>/implementation-plan.md
docs/wewo/<branch-name>/<requirement-slug>/implementation-record.md
```

Keep production code, implementation configuration, migrations, and developer
tests in normal project paths. Developer tests belong in this workflow only
when they drive or directly verify the production implementation in scope.
Browser-level acceptance work, independent review, deployment, and unrelated
test-only work are outside the runtime workflow.

Resolve one requirement workspace before reading workflow artifacts or writing:
determine the target repository's full current Git branch name, preserve its
slash-separated components below `docs/wewo/`, and combine it with an explicit,
established, or uniquely inferred concise lowercase English kebab-case
requirement slug. Ask when the branch is unavailable or detached without an
explicit branch/workspace, the slug is ambiguous, or multiple requirements
remain. Never scan sibling requirements, another branch workspace, or select
documents by existence or modification time outside the exact workspace. Keep
workflow filenames in English; use the requested or dominant language for
documents and conversation.

## Binding Implementation Obligations

From the requirement, available design, confirmed context, and relevant code,
extract only:

1. What must be true?
2. What must not change?
3. What material constraints bind implementation?
4. Where can the important behavior be verified?

Preserve source labels when useful, but do not restate or classify the whole
design. Never reinterpret a confirmed requirement, constraint, or non-goal to
make implementation easier.

## Gate 1: Plan

Read [project-analysis.md](references/project-analysis.md),
[planning-and-slicing.md](references/planning-and-slicing.md), and
[dependency-and-tool-policy.md](references/dependency-and-tool-policy.md).

Before confirmation, perform only read-only discovery, non-mutating feasibility
checks, and creation of `implementation-plan.md`. Inspect enough repository
reality to identify the change surface, important entry points, likely seams,
material conflicts, unrelated user work, and credible repository-native
commands.

Choose the simplest honest implementation shape: one Small Atomic Change,
Vertical Slices for behavioral work, or a staged Expand-Migrate-Contract style
migration when needed. Define coherent units with:

- goal or observable result;
- `Blocked by` dependencies;
- binding obligations;
- expected scope;
- verification seam;
- `TDD: Yes / No`;
- done conditions.

Write
`docs/wewo/<branch-name>/<requirement-slug>/implementation-plan.md`
from [implementation-plan-template.md](assets/implementation-plan-template.md),
summarize material scope and gaps, and explicitly ask the user to confirm.

Before explicit confirmation, do not modify any implementation asset,
including production source, developer tests, migrations, implementation
configuration, Docker/container files, dependency manifests or lockfiles, CI,
or deployment files. A direct-execution request may shorten confirmation but
cannot bypass this gate. Do not create an empty record skeleton merely because
the plan exists.

## Gate 2: TDD / Implementation Unit

Execute only a confirmed, dependency-ready unit. Before it, inspect the exact
files and mechanisms it needs. If a binding obligation relies on an existing
helper, wrapper, persistence operation, transaction, lock, cache, index,
retry, delete method, library behavior, or service, inspect its actual relevant
semantics; never infer behavior from a name, comment, or design prose alone.

For `TDD: Yes`, keep Red -> Green -> Refactor -> Verify and follow this sequence
without exception:

1. Write the smallest focused test for the target behavior.
2. Run it.
3. Observe a valid **TDD Red**.
4. Only then modify the target production behavior.
5. Run to Green.
6. Refactor if useful.
7. Rerun the focused test and relevant affected regression.

Do not partially implement the target production behavior before valid Red.
A failure is TDD Red only when the target behavior is still unimplemented, the
focused test actually ran and failed, and the failure matches the intended
missing or incorrect behavior. Environment, fixture, unrelated dependency,
syntax/import, pre-existing, regression, and post-implementation failures are
not automatically TDD Red. Never relabel a debug failure found after production
implementation as Red.

For `TDD: No`, implement the unit and run sufficient repository-native
verification. Use TDD for behavior or rules with a stable executable seam; do
not manufacture Red for declarative, mechanical, or wiring work.

Keep Refactor unit-local, behavior-preserving, and preserving binding
obligations. Apply [tdd-protocol.md](references/tdd-protocol.md) and close the
unit against [slice-quality.md](references/slice-quality.md). Create or update
the implementation record only when actual implementation evidence exists; it
may begin after the first unit closes or at the end.

## Gate 3: Material Gap

Ask one question when repository reality conflicts with the plan:

Can the issue be solved while preserving confirmed behavior, public contracts,
material architecture and persistence decisions, security boundaries, binding
invariants, and explicit non-goals?

- If yes, make the ordinary implementation adjustment and record it when
  meaningful.
- If no or uncertain, stop, explain the conflict and its impact, recommend a
  resolution, and ask the user to confirm before continuing.

Do not reason away a confirmed boundary as something the user "probably" did
not mean. When a shared component serves both in-scope and explicitly excluded
behavior, check whether the change affects the excluded behavior; if yes or
uncertain, stop at this gate.

Unplanned material dependency, schema or migration strategy, public API,
Docker/container, production-environment, CI/CD, infrastructure,
authentication/authorization, security-boundary, or deployment-topology
changes normally trigger this gate. Use the existing repository-native tool
and approval rules in
[dependency-and-tool-policy.md](references/dependency-and-tool-policy.md).

## Gate 4: Completion

Use [evidence-and-completion.md](references/evidence-and-completion.md) and
[document-contract.md](references/document-contract.md).

Close a unit only when its target result is complete, binding obligations are
preserved, required verification actually ran, failures are visible, and every
material gap is resolved or confirmed. A passing focused test alone is not
enough.

After all required units close, run fresh relevant verification and finalize
`docs/wewo/<branch-name>/<requirement-slug>/implementation-record.md`
from [implementation-record-template.md](assets/implementation-record-template.md).
Record actual changes, obligation traceability, unit evidence, TDD Red versus
debug/regression/environment failures, Passed/Failed/Blocked/Not Run checks,
confirmations, remaining risks, and honest final status.

Claim completion only when the record matches repository reality and no
failure, blocker, unrun requirement, or unresolved material gap is hidden.
Report the two document paths, changed behavior and files, executed evidence,
open risks, and incomplete work. Do not claim independent review, final
acceptance, deployment readiness, or a test gate, and do not continue
automatically into another capability.
