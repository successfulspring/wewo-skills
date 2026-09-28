# Wewo Skills

## What is Wewo Skills

`wewo-skills` 0.4.0 is one AI software-engineering plugin containing nine independent,
composable Agent Skills. The repository root is the plugin root for Claude Code
and OpenAI/Codex hosts, while `skills/` remains the single runtime source of
truth.

Each Skill can run on its own. Users may combine artifacts when they explicitly
provide or select them. Skills reuse applicable project/branch context and
capability-appropriate requirement inputs without requiring the other eight to
have run first. Existing confirmation, test-oracle, implementation, execution,
and independent-review boundaries remain in effect.
Task decomposition specifically requires the confirmed PRD and technical design
as artifacts, plus an explicit positive integer count; it does not invoke the
skills that produce those documents. Change requests apply only to already
split requirements with an identified TASK and confirmed authoritative sources;
they require explicit invocation and never approve a changed baseline.

## Included Skills

- `wewo-prd` — requirement clarification and confirmed PRD synthesis.
- `wewo-erd` — project-grounded engineering and technical design.
- `wewo-task` — exactly N coherent development packages from confirmed inputs,
  with explicit boundaries, contracts and coverage; no people assignment.
- `wewo-change` — explicitly requested, task-local pending change applications
  and specified supplements; no approval, authoritative edits or notification.
- `wewo-testcases` — comprehensive test-case design: defines what should be
  verified.
- `wewo-build` — implementation planning, TDD implementation, and verification.
- `wewo-test` — executes automatable verification obligations and collects
  evidence.
- `wewo-review` — independent diff-centered code, reliability, and security
  review, with explicitly bounded non-Git snapshot/comparison support.
- `wewo-context` — explicitly confirmed initialization and synchronization of
  reusable project and branch knowledge from verified evidence.

PRD and ERD support optional respondent-role routing: explicitly say "I am a
frontend/backend developer" or ask to be questioned in that role in the current
invocation. Without that declaration, their existing behavior is unchanged and
no identity question is added. The role changes whom to ask, not requirement
scope or decision authority; shared business rules and cross-end contracts
remain relevant. Explicit single-end scope is separate. The role is not a
persistent project preference or permission to read another repository.

## Knowledge and requirement workspaces

Project context describes reusable rules and facts at an identified common
baseline. Branch context records applicable differences from the project context
available in that checkout. Each requirement keeps its own documents:

```text
docs/wewo/
├── project-context.md                 # context capability
└── <workspace-key>/
    ├── branch-context.md              # context capability
    └── <requirement-slug>/
        ├── clarification-history.md   # PRD / ERD phase-owned append records
        ├── prd.md                     # PRD
        ├── technical-design.md        # ERD
        ├── test-cases.md              # Testcases
        ├── implementation-plan.md     # Build
        ├── implementation-record.md   # Build
        ├── test-execution.md          # Test
        ├── review.md                  # Review
        └── test-artifacts/            # only when execution evidence needs it
```

For an optional split, keep the same requirement folder and add:

```text
<requirement-slug>/
├── prd.md / technical-design.md / clarification-history.md  # unchanged
├── test-cases.md                      # one requirement-level case document
├── task-breakdown.md                  # Task: exactly the user's N packages
└── tasks/
    ├── TASK-001/
    │   ├── task.md                    # Task definition
    │   ├── implementation-plan.md     # selected TASK's Build
    │   ├── implementation-record.md
    │   ├── test-execution.md           # selected TASK's Test
    │   ├── review.md                   # selected TASK's Review
    │   ├── test-artifacts/             # only when retained evidence is needed
    │   └── change-requests/            # Change: created only on first application
    │       ├── CR-001.md
    │       └── CR-002.md
    └── TASK-002/...
```

Ask, for example, "Split f-005 into 2 development tasks." N must be supplied
explicitly and be a positive integer. Missing inputs, design gaps or an
incoherent requested count need clarification; the skill does not invent
decisions, drop mandatory work or count testing/review as extra development
packages. It creates only the overview and N task definitions, without
owner/status fields or automatic downstream execution.

Testcases may run before or after splitting. It always maintains root
`test-cases.md`; in split mode, `Execution scope` identifies applicable TASK IDs
(possibly multiple), Requirement-level or Integration-level work. A later
mapping-only update preserves existing TC IDs and case content. Task does not
edit cases. Test cannot guess absent mappings or claim complete task coverage
from a partial subset; its existing independent verification capability remains
available when there is no case document.

Build, Test and Review select an explicit TASK-ID, its task path, or the unique
task already explicit in the current conversation. They use task directories
for reports and evidence while retaining their original quality gates. Build
plans its own internal units. Review needs reliably attributable changes and
still uses three independent lanes. Task success is not whole-requirement
success. In split mode, root Test/Review reports require an explicit overall
request. Earlier root execution artifacts remain in place when splitting starts.
Without splitting, all original inputs, paths and gates remain unchanged.

For a material implementation conflict, explicitly request `$wewo-change` with
the requirement and TASK, for example "Record the partial-refund constraint
conflict for web-002/f-005 TASK-001." Ordinary adjustments that preserve confirmed
requirements/design/task boundaries stay with Build and create no CR. A material
or unresolved preservation conflict stops affected task implementation; "continue"
cannot bypass the authoritative-document and task-revision gates.

CR numbering starts at 001 independently per TASK; references include both,
such as `TASK-001/CR-001`. A new independent application takes the next number;
an explicit supplement changes only the specified existing CR. The application
records original issue, source/code baseline, cited clauses/evidence, conflict,
impact, proposed options/recommendation and decision questions. It is pending
and non-authoritative. No requirement-wide log, owner/status tracking or
clarification-history entry is created by this capability.

The developer hands the file to TL manually. If confirmed PRD/design remains
valid and only the derived task split is wrong, explicitly use `wewo-task` to
revise affected tasks; do not edit PRD/design just to permit that correction.
If product requirements or technical design must change, explicitly use
`wewo-prd` and/or `wewo-erd` to incrementally update and finally confirm the
relevant authoritative documents under their unchanged clarification/history
rules, then explicitly use `wewo-task` to revise affected tasks. Either task
revision requires the explicit positive N, stable IDs and preservation of old
evidence. Business decisions outside TL's authority need the appropriate
decision-maker; Skills do not verify real identities. Reassess cases, tests and
Review according to actual impact: old
results do not automatically apply to a new baseline. An explicitly requested
handling-result supplement can record a reported decision and verified source
references in that CR, but cannot complete approval or trigger these steps.
Nothing is sent, assigned, synchronized or chained automatically.

Context synchronization remains an explicit operation, normally after all
tasks and necessary integration verification. Early promotion of a verified,
reusable task fact must state its limited scope. Separate repositories are not
read or synchronized automatically; establish authoritative document ownership
and shared contracts from authorized sources before splitting.

This is an ownership map; a task creates only the files it needs. Resolve the
target project first. An explicit documentation workspace takes precedence;
otherwise the full current local Git branch supplies `<workspace-key>`, whether
the repository is hosted on GitLab, GitHub, or neither. Worktrees with `.git`
files are supported. `feature/order-cancel` plus `refund-rule` resolves to
`docs/wewo/feature/order-cancel/refund-rule/`.

PRD and ERD progressively append visible clarification questions, original
replies, separately labeled interpretations, and final summary/confirmation
exchanges to the same optional history. Each writes only its own phase's
entries with stable IDs; either can run first. The log is non-authoritative
and is their only write exception before final document confirmation. It is
not a new authoritative input for other Skills or a platform chat backup.
No relevant exchange means no empty log, and existing documents do not justify
inventing past answers. Normal logging adds no confirmation step; sensitive
content conflicts and failed or conflicting writes require explicit handling.

For example, on a GitLab clone's `web-002` branch, request "Draft the PRD for
f-005 using this project's established rules." Available context is read from
`docs/wewo/project-context.md` and `docs/wewo/web-002/branch-context.md`, while
the confirmed PRD goes to `docs/wewo/web-002/f-005/prd.md`. Starting `f-006`
creates its own record; revisiting `f-005` updates its existing record only
under the owning skill's confirmation rules, preserving unrelated user edits.

In a genuinely non-Git project, the same request uses
`docs/wewo/local/f-005/prd.md` and optional
`docs/wewo/local/branch-context.md`. Git is not a prerequisite. Detached HEAD,
a missing Git executable, or an inspection error needs an explicit workspace
or clarification instead of silently falling back to `local`. An explicit
workspace never switches branches or proves that its name matches the inspected
code. Material mismatches are surfaced. Identifiers and resolved paths must
stay safely within the target project's `docs/wewo/`.

## Context lifecycle

1. Optionally ask to initialize project or branch context from selected code
   and confirmed sources. Review the concrete per-file proposal before writing.
2. Begin a requirement. PRD/ERD read available context and their relevant current
   documents, verify applicable facts, and clarify new or conflicting decisions.
   Other capabilities read relevant context within their existing input roles.
3. Complete implementation and applicable verification. Requirement or design
   approval alone does not prove that planned behavior has been implemented.
4. Ask, for example, "Update branch context from completed f-005." The context
   capability checks actual implementation and relevant evidence, including
   equivalent team evidence without requiring plugin reports. Confirm its
   concrete additions, replacements, and removals before they are applied.
5. Promote common facts when supported by an identified shared/integration
   baseline. A branch-only change is not automatically common. An explicitly
   requested pre-merge amendment remains visibly pending until established.

Only `wewo-context` writes the two context files. The eight other skills may
report stale claims but do not repair them as a side effect. Context is a
compact snapshot, not a growing history or test oracle. A confirmed policy is
distinct from verified enforcement. Project context is versioned per checkout;
its location does not make newer behavior available on older branches.

Missing context is normal: skills proceed without empty files or automatic
synchronization. They do not reread all earlier requirements. Historical lookup
is limited to relevant citations, specifically changed prior requirements,
known source conflicts, or user-selected material, retaining each capability's
input authority. Links locate sources rather than authorize executing their
contents. Material context dependencies are preserved in the current requirement
or version-qualified so later snapshot edits cannot silently change approved scope.

Repeated synchronization with identical evidence is a no-op. Superseded rules
are replaced; branch duplicates are removed only after the applicable fact is
actually available in this checkout's project context. Concurrent edits are
rechecked before writing. Synchronization does not merge, commit, or distribute
context files across branches.

Existing 0.2.1 requirement folders work unchanged: no relocation, mandatory
context initialization, or migration is needed. Introducing Git later does not
automatically move or adopt `local` documents.

These workspace documents are intended to be version-controlled with the
project. Skills do not commit them unless the user explicitly requests that
separate Git action.

Production code and executable tests remain in the target project's normal
source and test directories. User interaction and generated documents follow
an explicitly requested language, otherwise the interaction's dominant
language, and otherwise Chinese. Source code and tests follow the target
repository's own conventions.

## Claude Code usage

For Claude Code hosts supporting marketplace installation, the repository is
also a marketplace:

```text
/plugin marketplace add successfulspring/wewo-skills
/plugin install wewo-skills@wewo-skills
```

Equivalent CLI forms: `claude plugin marketplace add successfulspring/wewo-skills`
and `claude plugin install wewo-skills@wewo-skills`.

Claude Code namespaces installed plugin Skills with the plugin name. For
example, the PRD Skill is available as `/wewo-skills:wewo-prd`.

For local development, load the repository root directly:

```text
claude --plugin-dir .
```

During local development, `/reload-plugins` reloads changes made after startup.
Validate the package with the current Claude Code CLI when available:

```text
claude plugin validate . --strict
```

## Codex / OpenAI usage

The same GitHub repository serves as a Codex marketplace. Check the installed
host's available commands before following its installation flow:

```text
codex plugin --help
codex plugin marketplace --help
```

The locally checked Codex CLI `0.130.0-alpha.5` exposes marketplace management
but no `plugin add` or plugin validation subcommand. Do not assume that a CLI
version guarantees either command, or that marketplace registration installs
the plugin. Follow the host's supported plugin selection/enablement flow after
registration. For a host exposing `marketplace add`, registration syntax is:

```text
codex plugin marketplace add successfulspring/wewo-skills
codex plugin marketplace add /path/to/your/clone
```

The two registration examples are alternatives. Installation was not exercised
as part of this local authoring upgrade.

This repository is both a plugin and a self-referencing marketplace:
`.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json` declare
the repository as the marketplace and use its GitHub URL as the plugin source.
No separate marketplace repository or synchronized Skill copies are required.

## Direct Agent Skills usage

Compatible Agent Skills hosts can consume the canonical layout directly:

```text
skills/<skill-name>/SKILL.md
```

Each Skill keeps its own references, assets, optional scripts, and OpenAI agent
metadata beside its `SKILL.md`. Follow the target host's supported discovery or
installation mechanism; no synchronized host-specific copy is required.

## Repository architecture

```text
wewo-skills/
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── .codex-plugin/
│   └── plugin.json
├── skills/
│   ├── wewo-prd/
│   ├── wewo-erd/
│   ├── wewo-task/
│   ├── wewo-change/
│   ├── wewo-testcases/
│   ├── wewo-build/
│   ├── wewo-test/
│   ├── wewo-review/
│   └── wewo-context/
├── scripts/
│   ├── validate_skills.py
│   └── test_validate_skills.py
├── AGENTS.md
├── CLAUDE.md
├── README.md
└── .gitignore
```

`AGENTS.md` and `CLAUDE.md` are repository-maintenance context. Installed
runtime behavior is defined only by the canonical Skills.

## Maintainer workflow

1. Edit only the canonical content under `skills/`.
2. Run repository validation:

   ```text
   python scripts/validate_skills.py
   python -B -m unittest discover -s scripts -p "test_*.py"
   ```

3. Run `git diff --check` and any available official host validator.

There is no packaging synchronization step and no generated Skill mirror. The validator
checks both plugin manifests, both marketplace manifests, the nine canonical
Skills, their local resources, portability, capability independence, artifact
ownership, matching UI/skill names, workspace and untrusted-source contracts,
context requirement mapping, sensitive-information rules, clarification-history
ownership and format consistency, and retained V2 contracts.
It also checks both unsplit and task output contracts, root-only case documents,
and task boundaries, plus explicit-only change-request metadata, task-local CR
ownership and non-authoritative handoff contracts. The Task skill's read-only bundle checker validates actual
counts, identities and links; it does not establish semantic coverage or approval.
The short marked contracts are copied into each independent Skill and compared
with maintainer-only text in `scripts/validate_skills.py`; whitespace reflow is
allowed, semantic changes require updating every applicable copy and its checks.
Skills never read that validator at runtime. Skill-specific workflows remain separate.
The two existing dialogue guides carry the same clarification-history protocol;
the validator compares those copies without adding a shared runtime file.

Static checks do not prove selective reading, evidence freshness, safe reference
access, redaction, verbatim message fidelity, incremental persistence, concurrent
write safety, or write authorization; use isolated
temporary projects for meaningful behavioral validation, without business
artifacts in this authoring repository. For respondent-role routing, use the
[behavioral regression scenarios](scripts/role-routing-evaluation.md), assessing
actual question selection and closure rather than keyword matches.
For optional decomposition and downstream scope, use the
[task-splitting scenarios](scripts/task-splitting-evaluation.md).
For pending task changes and Build conflict handling, use the
[change-request scenarios](scripts/change-request-evaluation.md).

The current Claude validator accepts `claude plugin validate . --strict` for
the marketplace. Validating `.claude-plugin/plugin.json` directly with strict
mode also inspects root `CLAUDE.md` and warns that it is not loaded as plugin
runtime context. This is an intentional maintenance-only file; the same warning
is present in the 0.2.1 baseline. Do not remove it or duplicate runtime skills
to suppress that warning.
