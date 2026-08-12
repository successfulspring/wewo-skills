# Global Conventions

1. The complete collection is named `wewo-skills`.

2. The individual skills are independently runnable. No skill may require that
   another `wewo-*` skill has already run.

3. Skills are artifact-composable, not workflow-state-coupled. A skill may
   consume an artifact established in the current conversation context or
   explicitly supplied or referenced by the user. A skill must never select an
   artifact because the agent discovered its existence in the repository or a
   requirement workspace; artifact existence is not an input-selection signal.
   When no usable artifact exists, the skill must establish the minimum context
   needed for its own work.

4. Every generated workflow document, review report, execution report, and
   related evidence must be stored under an isolated requirement workspace:

   ```text
   docs/wewo/<requirement-category>/<requirement-slug>/
   ```

   Example:

   ```text
   docs/wewo/features/homepage-english-localization/
   ```

5. Supported requirement categories should include:

   - `features`
   - `bugs`
   - `refactors`
   - `maintenance`

   Default to `features` only when the category is not supplied and there is no
   evidence that another category is more appropriate.

6. Requirement slugs must use concise lowercase English kebab-case.

7. Workspace resolution order:

   - Use an explicit workspace path supplied by the user.
   - Otherwise reuse the workspace established in the current requirement
     context.
   - Otherwise infer a candidate from the requirement, issue, branch, or
     explicitly supplied or referenced material.
   - If multiple workspaces are plausible, ask the user before writing files.
   - Never silently select the most recently modified workspace.

8. Generated production code and executable test code must remain in the
   project's normal source and test directories.

   `docs/wewo/...` is for workflow documents, reports, execution evidence, and
   generated test artifacts. It must not become a duplicate source-code tree.

9. Stable workflow filenames remain in English regardless of document
   language:

   - `prd.md`
   - `technical-design.md`
   - `test-cases.md`
   - `implementation-plan.md`
   - `implementation-record.md`
   - `test-execution.md`
   - `manual-test-checklist.md`
   - `review.md`

10. Skill implementation files must be written in English, including:

    - `SKILL.md`
    - references
    - internal instructions
    - templates and template instructions
    - script documentation

11. User-facing conversations and generated workflow documents must adapt to
    the user's language:

    - Follow an explicitly requested language.
    - Otherwise follow the dominant language of the current interaction.
    - Default to Chinese when the language cannot be determined.

12. Source-code naming, test naming, comments, and formatting must follow the
    existing repository conventions instead of forcing Chinese or English.

13. Core `SKILL.md` files must support both Codex and Claude Code.

14. Do not make the core workflow depend on platform-specific slash commands,
    proprietary frontmatter, or capabilities that may be unavailable in the
    other agent.

15. Host-specific capabilities such as browser control, MCP tools, or special
    metadata should be treated as optional enhancements with a documented
    fallback. Subagents are also optional by default. A capability may require
    isolated reviewer contexts only when independence is explicitly part of
    correctness; if unavailable, report unable to conclude rather than
    simulating independence in one shared context. This exception does not
    apply to other capabilities implicitly.

16. Skills may create missing parent directories only after the requirement
    workspace has been resolved unambiguously.

17. Skills must not create empty documents owned by other capabilities.

18. Documents from different requirements must never be written into the same
    workspace unless the user explicitly confirms they belong to the same
    requirement.

19. Do not claim that a command, test, scan, review, or validation passed unless
    it was actually executed and produced supporting evidence.

20. Prefer progressive disclosure:

    - Keep `SKILL.md` focused on orchestration and mandatory behavior.
    - Put detailed domain guidance in references.
    - Use scripts only for deterministic or repetitive operations.
    - Use assets for reusable document templates.

21. Workflow documents are opt-in input sources. A skill must not scan
    `docs/wewo/` or the repository for historical workflow documents (PRDs,
    designs, plans, reports, or test documents). A workflow document may be
    used as input only when the user explicitly references it, explicitly
    provides its requirement workspace, explicitly asks to continue, revise,
    review, implement, or test an existing requirement, or provides or uploads
    the document in the current interaction. Never silently select a workspace
    because a document appears similar or recently modified.

22. Each workflow document is owned by the capability that produces it:
    `prd.md` by wewo-prd, `technical-design.md` by wewo-erd,
    `test-cases.md` by wewo-testplan,
    `implementation-plan.md` and `implementation-record.md` by wewo-build,
    `test-execution.md`, `manual-test-checklist.md`, and `test-artifacts/` by
    wewo-test, and `review.md` by wewo-review.
    A skill must not normally modify a workflow document owned by another
    capability. Deviations, adjustments, and execution states belong in the
    owning capability's own documents, or are handled through explicit user
    confirmation and deliberate revision of the owning document.
