@AGENTS.md

# Claude Code Notes

`skills/` is the single canonical runtime source. The repository root is the
plugin root, and `.claude-plugin/plugin.json` packages that same tree. Never
create or maintain a host-specific copy of the Skills.

Claude-specific subagents, tools, hooks, and other capabilities are optional
enhancements. Preserve the portable Codex/Claude core and provide a functional
fallback whenever an enhancement is unavailable.

When a request satisfies one of the nine capabilities' invocation rules, use
the corresponding
`wewo-prd`, `wewo-erd`, `wewo-task`, `wewo-change`, `wewo-testcases`, `wewo-build`, `wewo-review`,
`wewo-test`, or `wewo-context` skill. Do not reproduce their complete workflows
in this file. The context capability alone writes project/branch snapshots;
the other eight read applicable context without changing its source authority.
Use the workspace and selective-read rules in `AGENTS.md`, including non-Git
`local` workspaces and the two context paths outside requirement directories.
Optional task decomposition requires confirmed requirement/design artifacts
and an explicit N; selected task execution uses nested task directories while
case design remains requirement-level. Existing unsplit gates and paths stay
unchanged. Follow the canonical Skills for the detailed routing contract.
The change-request capability is explicit-only and writes solely within a
selected TASK's `change-requests/`; its applications never approve or replace
requirements/design/tasks, and it never writes clarification history.

Treat these repository instructions as maintenance guidance, not as business
requirements for a runtime user requirement.

This root `CLAUDE.md` is project-maintenance context. Installed plugin runtime
behavior belongs in the nine canonical Skills, not in this file.
