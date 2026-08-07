@AGENTS.md

# Claude Code Notes

`skills/` is canonical. `.claude/skills/` is a synchronized mirror and must
never be edited directly.

Claude-specific subagents, tools, hooks, and other capabilities are optional
enhancements. Preserve the portable Codex/Claude core and provide a functional
fallback whenever an enhancement is unavailable.

When work matches one of the six workflow stages, use the corresponding
`wewo-prd`, `wewo-erd`, `wewo-testplan`, `wewo-build`, `wewo-review`, or
`wewo-test` skill. Do not reproduce their complete workflows in this file.

Treat these repository instructions as maintenance guidance, not as business
requirements for a runtime user requirement.
