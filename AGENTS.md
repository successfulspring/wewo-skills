# Repository Maintenance Instructions

## Repository purpose

This repository maintains `wewo-skills`, a portable collection of six
independently runnable software-engineering skills for Codex and Claude Code:
`wewo-prd`, `wewo-erd`, `wewo-testcases`, `wewo-build`, `wewo-review`, and
`wewo-test`.

These instructions govern repository maintenance. They do not define business
requirements for a runtime user request and do not replace any skill's detailed
workflow.

## Source-of-truth model

- `AGENTS.md` and `CLAUDE.md` define repository-maintenance behavior. They are
  project context, not installed-plugin runtime instructions.
- `skills/<skill-name>/` is the canonical runtime source for that capability,
  including `SKILL.md`, local references, assets when needed, and any justified
  scripts.
- The repository root is the plugin root. `.claude-plugin/plugin.json` and
  `.codex-plugin/plugin.json` package the same canonical `skills/` tree for
  their respective hosts.
- `scripts/validate_skills.py` checks repository structure, plugin packaging,
  and runtime invariants. It does not define or require a separate
  specification layer.

There is one runtime Skill source: `skills/`. Never create or maintain
host-specific Skill copies.

## Conflict handling

Before making a material change, compare:

- the user's current explicit instruction;
- the affected canonical implementation;
- these repository-maintenance instructions.

Do not apply a simplistic precedence rule or silently choose one side when
these sources materially disagree. Stop before the conflicting modification
and report the exact statements, file paths and line locations, practical
impact, and a recommended resolution.

## Change boundaries

- Modify only the requested skill or repository-level file.
- Do not modify another skill merely to make implementations look consistent.
- Preserve unrelated, uncommitted, or pre-existing user work.
- While authoring a reusable skill, do not run its runtime workflow or create
  real workflow documents, reports, evidence, production code, or executable
  project tests.
- Do not create empty documents owned by other capabilities.
- Do not combine separate requirements in one
  `docs/wewo/<branch-name>/<requirement-slug>/` workspace without
  explicit confirmation.

## Skill-authoring workflow

Before changing a skill:

1. Inspect the complete canonical implementation under
   `skills/<skill-name>/`.
2. Identify material conflicts, missing decisions, and unresolved ambiguity.
3. Modify only the canonical skill.
4. Validate the canonical skill with the available skill-authoring validator.
   Do not invent a validator command if none is available in the current host.
5. Run repository validation from the plugin root.
6. Report omissions, partial implementation, assumptions, and unresolved
   ambiguity.

The repository validator checks the canonical tree and both plugin manifests;
it is the final repository-level static validation.

## Skill structure

- Keep `SKILL.md` focused on triggers, exclusions, orchestration, mandatory
  decisions, confirmation gates, permissions, outputs, stopping conditions,
  and completion rules.
- Put detailed domain guidance, quality criteria, examples, and decision
  frameworks in `references/`.
- Put reusable output-document structures and templates in `assets/`.
- Add scripts only for deterministic, repetitive, transformation, or
  validation-oriented behavior.
- Test every added script using representative inputs.
- Do not add empty, decorative, placeholder, or process-history files.
- Keep local references direct and valid; avoid unnecessary reference nesting.

## Portability and language

- Preserve a portable core that works in both Codex and Claude Code.
- Do not require MCP servers, browser-control tools, proprietary APIs, hooks,
  or host-specific metadata for the core workflow. Subagents remain optional
  unless a capability explicitly makes isolated contexts part of correctness
  under the narrow exception below.
- Treat host-specific capabilities as optional enhancements and document a
  functional fallback.
- Write reusable implementation files in English.
- Adapt user-facing interaction and generated documents to an explicitly
  requested language, otherwise the interaction's dominant language, and
  otherwise Chinese.
- Follow the target business repository's conventions for source-code and test
  naming, comments, and formatting.

## Focused Subagent Execution

Subagents and fresh contexts are optional host/runtime execution strategies by
default, not ordinary capability contracts. A capability defines what correct
work requires; the host normally decides whether to use the current context, a
fresh context, or a subagent. A capability may explicitly require isolated
reviewer contexts only when independence itself is part of correctness. If the
host cannot provide those contexts, report the capability as unavailable or
unable to conclude; never simulate independence in one shared context. This is
a narrow exception and does not make subagents mandatory for other skills or
tasks.

Use a fresh subagent only after work is decomposed into a coherent unit with a
clear goal and completion condition, and when a focused context would reduce
unnecessary context load or drift without weakening plan or confirmation
gates. Keep small or already-focused work in the current context.

Delegate sequentially by default: execute one ready unit, return its changes
and evidence, let the parent check closure, then select the next unit. The
parent retains the overall plan, user-confirmation gates, dependency ordering,
confirmed requirements and material constraints, material-conflict
escalation, cross-unit integration, final fresh verification, and completion
reporting. Never delegate a material decision that requires user confirmation.

Give the subagent only the unit goal, relevant completed dependency outcomes,
binding constraints, expected scope, verification seam, applicable TDD rule,
and repository context needed to inspect and execute the unit. The subagent
must stay within that unit, run focused verification, return actual changes and
evidence, and report failures, blockers, or material conflicts to the parent
without expanding scope or choosing a material resolution.

Use parallel delegation only for clearly independent units. Treat shared source
files, interfaces or contracts, mutable runtime or database state, test
infrastructure, generated artifacts, dependency ordering, or verification
baselines as reasons to avoid parallel work. When independence is uncertain,
execute sequentially.

## Workflow workspace

Store workflow documents, reports, execution evidence, and generated test
artifacts only under:

```text
docs/wewo/<branch-name>/<requirement-slug>/
```

Resolve the current full Git branch name and one concise lowercase English
kebab-case requirement slug before writing. Preserve slash-separated branch
components below `docs/wewo/`; for example, branch `feature/order-cancel` and
requirement `refund-rule` resolve to
`docs/wewo/feature/order-cancel/refund-rule/`. If no branch can be resolved,
ask for an explicit branch name or workspace. Never infer a requirement from
the existence or recency of another workspace, scan another branch workspace,
or combine separate requirements without confirmation.

Documents in the exact resolved current-branch/current-requirement workspace
may be read as capability-appropriate context. Their presence authorizes
reading, not treating every statement as current or authoritative. Preserve
source ownership, surface conflicts with the current request or repository,
and keep each capability's input boundaries. Production code and executable
tests belong in the business project's normal source and test directories,
never in the requirement workspace.

## Evidence and honesty

- Never claim that a command, test, scan, review, build, synchronization, or
  validation passed unless it was actually executed and produced supporting
  evidence.
- When applicable, distinguish Passed, Failed, Blocked, Not Run, and
  unavailable checks.
- Preserve actual command output, exit status, scope, and limitations needed
  to support a claim.
- Report assumptions, omissions, partial implementation, blockers, and
  unresolved ambiguity.

## Dependency and safety boundaries

- Prefer repository-native tools, declared versions, and existing package
  managers.
- Do not silently add or upgrade dependencies, switch package managers, or
  rewrite lockfiles.
- Never create host-specific Skill mirrors or overwrite unrelated user work.
- Do not use unsafe installers, unknown binaries, disabled TLS verification,
  production secrets, or uncontrolled source uploads.
- Obtain required confirmation before material dependency, lockfile, CI,
  Docker, administrator, system-wide, persistent-service, external-service, or
  production-environment changes.
- Resolve exact targets before destructive or recursive filesystem actions.

## Repository commands

Run commands from the repository root.

Validate required files, plugin manifests, canonical Skill structure and
frontmatter, distinct Skill descriptions, portability, local references, and
the retained V2 runtime contracts:

```text
python scripts/validate_skills.py
```

For Claude Code packaging, when the installed CLI supports it, also run:

```text
claude plugin validate . --strict
```

No synchronization step exists. Edit `skills/`, then validate.

## Scope restraint

Keep repository-wide guidance concise and durable. Leave detailed runtime
behavior in the canonical `SKILL.md`, references, and assets.

Do not introduce universal slogans such as always removing backward
compatibility, always avoiding migrations, always choosing the smallest
possible implementation, or never introducing abstractions. Those decisions
depend on the affected runtime contract and the current requirement.
