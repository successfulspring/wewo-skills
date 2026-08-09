# wewo-skills

`wewo-skills` is a portable library of six independently executable,
artifact-composable software-engineering capabilities for Codex and Claude
Code. The repository provides shared conventions, per-capability requirement
specifications, canonical runtime implementations, and portable
synchronization and validation tooling.

## Capabilities

Each capability is independently runnable. No capability requires another
`wewo-*` capability to have run.

- `wewo-prd` — requirement clarification and PRD synthesis.
- `wewo-erd` — engineering design grounded in the actual project.
- `wewo-testplan` — QA / acceptance test design.
- `wewo-build` — implementation with implementation-time TDD and verification.
- `wewo-test` — independent real test execution and evidence collection.
- `wewo-review` — independent Diff-centered code, security, and reliability
  review.

Artifacts are composable. A capability may use an artifact when it is
explicitly supplied by the user or already established in the current
conversation. Artifact existence alone does not authorize it as input.
Recommended composition below is documentation for humans, not a runtime
dependency.

### Recommended composition

Product / engineering:

```text
Requirement clarification
→ engineering design
→ implementation
```

QA design:

```text
Requirement / design
→ test design
```

Verification:

```text
Implemented code
→ test execution
```

Quality:

```text
Final Diff
→ review
```

Repository-level recommendation: when test execution creates or modifies
repository files such as executable tests, test assets, or test configuration,
the final quality review should evaluate the final resulting Diff. This is a
human workflow recommendation only. It does not mean that test execution
automatically invokes review, that review requires test execution, or that test
execution tracks review state.

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

Validate the canonical skills, local references, portability rules, V2
architecture contracts, and both mirrors with:

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
