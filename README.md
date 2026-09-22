# Wewo Skills

## What is Wewo Skills

`wewo-skills` 0.3.0 is one AI software-engineering plugin containing seven independent,
composable Agent Skills. The repository root is the plugin root for Claude Code
and OpenAI/Codex hosts, while `skills/` remains the single runtime source of
truth.

Each Skill can run on its own. Users may combine artifacts when they explicitly
provide or select them. Skills reuse applicable project/branch context and
capability-appropriate requirement inputs without requiring the other six to
have run first. Existing confirmation, test-oracle, implementation, execution,
and independent-review boundaries remain in effect.

## Included Skills

- `wewo-prd` — requirement clarification and confirmed PRD synthesis.
- `wewo-erd` — project-grounded engineering and technical design.
- `wewo-testcases` — comprehensive test-case design: defines what should be
  verified.
- `wewo-build` — implementation planning, TDD implementation, and verification.
- `wewo-test` — executes automatable verification obligations and collects
  evidence.
- `wewo-review` — independent diff-centered code, reliability, and security
  review, with explicitly bounded non-Git snapshot/comparison support.
- `wewo-context` — explicitly confirmed initialization and synchronization of
  reusable project and branch knowledge from verified evidence.

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
        ├── prd.md                     # PRD
        ├── technical-design.md        # ERD
        ├── test-cases.md              # Testcases
        ├── implementation-plan.md     # Build
        ├── implementation-record.md   # Build
        ├── test-execution.md          # Test
        ├── review.md                  # Review
        └── test-artifacts/            # only when execution evidence needs it
```

This is an ownership map; a task creates only the files it needs. Resolve the
target project first. An explicit documentation workspace takes precedence;
otherwise the full current local Git branch supplies `<workspace-key>`, whether
the repository is hosted on GitLab, GitHub, or neither. Worktrees with `.git`
files are supported. `feature/order-cancel` plus `refund-rule` resolves to
`docs/wewo/feature/order-cancel/refund-rule/`.

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

Only `wewo-context` writes the two context files. The six other skills may
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
checks both plugin manifests, both marketplace manifests, the seven canonical
Skills, their local resources, portability, capability independence, artifact
ownership, matching UI/skill names, workspace and untrusted-source contracts,
context requirement mapping, sensitive-information rules, and retained V2 contracts.
The short marked contracts are copied into each independent Skill and compared
with maintainer-only text in `scripts/validate_skills.py`; whitespace reflow is
allowed, semantic changes require updating every applicable copy and its checks.
Skills never read that validator at runtime. Skill-specific workflows remain separate.

Static checks do not prove selective reading, evidence freshness, safe reference
access, redaction, or write authorization; use isolated
temporary projects for meaningful behavioral validation, without business
artifacts in this authoring repository.

The current Claude validator accepts `claude plugin validate . --strict` for
the marketplace. Validating `.claude-plugin/plugin.json` directly with strict
mode also inspects root `CLAUDE.md` and warns that it is not loaded as plugin
runtime context. This is an intentional maintenance-only file; the same warning
is present in the 0.2.1 baseline. Do not remove it or duplicate runtime skills
to suppress that warning.
