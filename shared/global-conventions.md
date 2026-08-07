# Global Conventions

1. The complete collection is named `wewo-skills`.

2. The individual skills are independently runnable. No skill may require that
   an earlier skill has already run.

3. When useful upstream documents exist and the user has authorized their use
   (explicit reference, explicit workspace, a user-requested continuation of
   an existing requirement, or explicit confirmation of a discovered
   candidate), a skill should reuse them. A document's existence in a
   requirement workspace does not by itself authorize it as input. When no
   authorized upstream material exists, the skill must establish the minimum
   context needed for its own work.

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
     available upstream documents.
   - If multiple workspaces are plausible, ask the user before writing files.
   - Never silently select the most recently modified workspace.

8. Generated production code and executable test code must remain in the
   project's normal source and test directories.

   `docs/wewo/...` is for workflow documents, reports, execution evidence, and
   generated test artifacts. It must not become a duplicate source-code tree.

9. Stable workflow filenames remain in English regardless of document
   language:

   - `01-prd.md`
   - `02-technical-design.md`
   - `03-test-plan.md`
   - `04-test-cases.md`
   - `05-implementation-plan.md`
   - `06-implementation-record.md`
   - `07-code-review.md`
   - `08-security-review.md`
   - `09-test-execution.md`
   - `10-manual-test-checklist.md`

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

15. Host-specific capabilities such as subagents, browser control, MCP tools,
    or special metadata should be treated as optional enhancements with a
    documented fallback.

16. Skills may create missing parent directories only after the requirement
    workspace has been resolved unambiguously.

17. Skills must not create empty documents for earlier or later stages merely
    to complete the numeric sequence.

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
    review, implement, or test an existing requirement, provides or uploads
    the document in the current interaction, or explicitly confirms a
    candidate the agent discovered. Never silently select a workspace because
    a document appears similar or recently modified.

22. Each workflow document is owned by the skill that produces it:
    `01-prd.md` by wewo-prd, `02-technical-design.md` by wewo-erd,
    `03-test-plan.md` and `04-test-cases.md` by wewo-testplan,
    `05-implementation-plan.md` and `06-implementation-record.md` by
    wewo-build, `07-code-review.md` and `08-security-review.md` by
    wewo-review, and `09-test-execution.md`,
    `10-manual-test-checklist.md`, and `test-artifacts/` by wewo-test.
    A downstream skill must not normally modify an upstream skill's workflow
    document. Deviations, adjustments, and execution states belong in the
    owning stage's own documents, or are handled through explicit user
    confirmation and deliberate revision of the owning document.
