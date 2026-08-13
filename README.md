# Wewo Skills

## What is Wewo Skills

`wewo-skills` is one AI software-engineering plugin containing six independent,
composable Agent Skills. The repository root is the plugin root for Claude Code
and OpenAI/Codex hosts, while `skills/` remains the single runtime source of
truth.

Each Skill can run on its own. Users may combine artifacts when they explicitly
provide or select them, but no Skill requires the other five to have run first.

## Included Skills

- `wewo-prd` — requirement clarification and confirmed PRD synthesis.
- `wewo-erd` — project-grounded engineering and technical design.
- `wewo-testcases` — comprehensive test-case design: defines what should be
  verified.
- `wewo-build` — implementation planning, TDD implementation, and verification.
- `wewo-test` — executes automatable verification obligations and collects
  evidence.
- `wewo-review` — independent diff-centered code, reliability, and security
  review.

Workflow documents, reports, and execution evidence use isolated requirement
workspaces under:

```text
docs/wewo/<requirement-category>/<requirement-slug>/
```

Production code and executable tests remain in the target project's normal
source and test directories. User interaction and generated documents follow
an explicitly requested language, otherwise the interaction's dominant
language, and otherwise Chinese. Source code and tests follow the target
repository's own conventions.

## Claude Code usage

Anyone can install `wewo-skills` directly from this GitHub repository as a
marketplace:

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

The same GitHub repository serves as a Codex marketplace, so anyone can
install `wewo-skills` in two commands:

```text
codex plugin marketplace add successfulspring/wewo-skills
codex plugin add wewo-skills@wewo-skills
```

Requires Codex CLI v0.122 or later. Start a new Codex session after
installation so the Skills are discovered. Local clones work too:

```text
codex plugin marketplace add /path/to/your/clone
codex plugin add wewo-skills@wewo-skills
```

This repository is both a plugin and a self-referencing marketplace:
`.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json` declare
the repository root as the marketplace and list `wewo-skills` as its own plugin.
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
│   └── wewo-review/
├── scripts/
│   └── validate_skills.py
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
   ```

3. Run `git diff --check` and any available official host validator.

There is no synchronization step and no generated Skill mirror. The validator
checks both plugin manifests, both marketplace manifests, the six canonical
Skills, their local resources, portability, capability independence, artifact
ownership, and retained V2 contracts.
