@AGENTS.md

# Claude Code Notes

`skills/` is the single canonical runtime source. The repository root is the
plugin root, and `.claude-plugin/plugin.json` packages that same tree. Never
create or maintain a host-specific copy of the Skills.

Claude-specific subagents, tools, hooks, and other capabilities are optional
enhancements. Preserve the portable Codex/Claude core and provide a functional
fallback whenever an enhancement is unavailable.

When work matches one of the six capabilities, use the corresponding
`wewo-prd`, `wewo-erd`, `wewo-testcases`, `wewo-build`, `wewo-review`, or
`wewo-test` skill. Do not reproduce their complete workflows in this file.

Treat these repository instructions as maintenance guidance, not as business
requirements for a runtime user requirement.

This root `CLAUDE.md` is project-maintenance context. Installed plugin runtime
behavior belongs in the six canonical Skills, not in this file.
