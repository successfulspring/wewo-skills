# Repository Maintenance Instructions

## Repository purpose

This repository maintains `wewo-skills`, a portable collection of six
independently runnable software-engineering skills for Codex and Claude Code:
`wewo-prd`, `wewo-erd`, `wewo-testplan`, `wewo-build`, `wewo-review`, and
`wewo-test`.

These instructions govern repository maintenance. They do not define business
requirements for a runtime user request and do not replace any skill's detailed
workflow.

## Source-of-truth model

- `shared/global-conventions.md` is the source for collection-wide behavior.
- `specs/<skill-name>-requirements.md` is the authoritative requirement source
  for that skill.
- `skills/<skill-name>/` contains the canonical reusable implementation,
  including `SKILL.md`, references, assets, and any justified scripts.
- `.agents/skills/` is the generated Codex mirror.
- `.claude/skills/` is the generated Claude Code mirror.

Never edit either mirror directly. Change canonical files under `skills/`,
validate the canonical change, synchronize, and then verify equality.

## Conflict handling

Before making a material change, compare:

- the user's current explicit instruction;
- `shared/global-conventions.md`;
- the affected skill specification;
- the affected canonical implementation;
- these repository-maintenance instructions.

Do not apply a simplistic precedence rule or silently choose one side when
these sources materially disagree. Stop before the conflicting modification
and report the exact statements, file paths and line locations, practical
impact, and a recommended resolution. Repository guidance must not silently
override an authoritative skill specification.

## Change boundaries

- Modify only the requested skill or repository-level file.
- Do not modify another skill merely to make implementations look consistent.
- Do not change `shared/global-conventions.md` or a file under `specs/` unless
  the user explicitly requests that authoritative change.
- Preserve unrelated, uncommitted, or pre-existing user work.
- While authoring a reusable skill, do not run its runtime workflow or create
  real workflow documents, reports, evidence, production code, or executable
  project tests.
- Do not create empty documents owned by other capabilities.
- Do not combine separate requirements in one
  `docs/wewo/<requirement-category>/<requirement-slug>/` workspace without
  explicit confirmation.

## Skill-authoring workflow

Before changing a skill:

1. Read `shared/global-conventions.md` completely.
2. Read the affected `specs/<skill-name>-requirements.md` completely.
3. Inspect the complete canonical implementation under
   `skills/<skill-name>/`.
4. Identify material conflicts, missing decisions, and unresolved ambiguity.
5. Modify only the canonical skill.
6. Validate the canonical skill with the available skill-authoring validator
   before synchronization. Do not invent a validator command if none is
   available in the current host.
7. Synchronize only after canonical validation passes.
8. Run repository validation and verify that canonical, Codex, and Claude Code
   copies are equal.
9. Report omissions, partial implementation, assumptions, and unresolved
   ambiguity.

The repository validator compares complete mirror trees, so it is expected to
be the final validation after synchronization.

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
- Do not require subagents, MCP servers, browser-control tools, proprietary
  APIs, hooks, or host-specific metadata for the core workflow.
- Treat host-specific capabilities as optional enhancements and document a
  functional fallback.
- Write reusable implementation files in English.
- Adapt user-facing interaction and generated documents to an explicitly
  requested language, otherwise the interaction's dominant language, and
  otherwise Chinese.
- Follow the target business repository's conventions for source-code and test
  naming, comments, and formatting.

## Workflow workspace

Store workflow documents, reports, execution evidence, and generated test
artifacts only under:

```text
docs/wewo/<requirement-category>/<requirement-slug>/
```

Resolve one unambiguous workspace before writing. Production code and
executable tests belong in the business project's normal source and test
directories, never in the requirement workspace.

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
- Never edit mirrors directly or overwrite unrelated user work.
- Do not use unsafe installers, unknown binaries, disabled TLS verification,
  production secrets, or uncontrolled source uploads.
- Obtain required confirmation before material dependency, lockfile, CI,
  Docker, administrator, system-wide, persistent-service, external-service, or
  production-environment changes.
- Resolve exact targets before destructive or recursive filesystem actions.

## Repository commands

Run commands from the repository root.

Synchronize the complete canonical skill tree to both mirrors:

```text
python scripts/sync_skills.py
```

The synchronization script also accepts `--repo-root PATH`. It replaces both
complete mirror trees from `skills/`; inspect canonical and unrelated user
changes before running it.

Validate required files, canonical skill structure and frontmatter, distinct
skill descriptions, portability, local references, and both mirrors:

```text
python scripts/validate_skills.py
```

There is no separate repository mirror-equality command. Successful execution
of `scripts/validate_skills.py` includes exact canonical/Codex/Claude tree and
file-digest equality checks.

## Scope restraint

Keep repository-wide guidance concise and durable. Leave detailed runtime
behavior in the relevant specification, canonical `SKILL.md`, references, and
assets.

Do not introduce universal slogans such as always removing backward
compatibility, always avoiding migrations, always choosing the smallest
possible implementation, or never introducing abstractions. Those decisions
depend on the affected skill specification and the current requirement.
