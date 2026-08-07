# wewo-skills

`wewo-skills` is a portable collection of six software-engineering skills for
Codex and Claude Code. The repository currently provides the collection
structure, shared conventions, skill metadata, requirement placeholders, and
portable synchronization and validation tooling. `wewo-prd`, `wewo-erd`,
`wewo-testplan`, `wewo-build`, `wewo-review`, and `wewo-test` are implemented.

## Six-stage workflow

The collection is organized around six independently runnable stages:

1. `wewo-prd` — establish product requirements.
2. `wewo-erd` — establish the technical design.
3. `wewo-testplan` — plan coverage and test cases.
4. `wewo-build` — implement the requirement.
5. `wewo-review` — review code quality and security.
6. `wewo-test` — execute verification and record evidence.

The stages form a useful end-to-end sequence, but they are not prerequisites for
one another. Each skill must be able to establish the minimum context it needs
when useful upstream documents are unavailable.

## Requirement workspaces

Workflow documents, reports, execution evidence, and generated test artifacts
belong in an isolated workspace:

```text
docs/wewo/<requirement-category>/<requirement-slug>/
```

For example:

```text
docs/wewo/features/homepage-english-localization/
```

Supported categories include `features`, `bugs`, `refactors`, and
`maintenance`. Slugs use concise lowercase English kebab-case. Production code
and executable tests remain in the project's normal source and test
directories; the requirement workspace is not a duplicate source tree.

See [shared/global-conventions.md](shared/global-conventions.md) for the complete
workspace-resolution and output rules.

## Language adaptation

Skill implementation files are written in English so the collection remains
portable and maintainable. User-facing conversation and generated workflow
documents follow an explicitly requested language, otherwise the dominant
language of the interaction, and finally Chinese when the language cannot be
determined. Source code and tests continue to follow the target repository's
own conventions.

## Synchronize and validate

The canonical source of every skill is under `skills/`. Generate the Codex and
Claude Code mirrors with:

```text
python scripts/sync_skills.py
```

Validate the canonical skills, local references, portability rules, and both
mirrors with:

```text
python scripts/validate_skills.py
```

Both scripts use only the Python standard library and work on Windows, macOS,
and Linux. Synchronization copies files rather than creating symbolic links.
Run synchronization after every canonical skill change, then run validation.

## Use with Codex

Open the repository as the working project. Codex discovers the generated
copies under `.agents/skills/`. Invoke a skill explicitly by name, such as
`$wewo-prd`.

## Use with Claude Code

Open the repository as the working project. Claude Code discovers the generated
copies under `.claude/skills/`. Invoke the corresponding skill by name according
to the host's supported skill-invocation interface.

## Current implementation status

The reviewed requirements and implementations for `wewo-prd`, `wewo-erd`,
`wewo-testplan`, `wewo-build`, `wewo-review`, and `wewo-test` are complete.
