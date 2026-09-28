# Optional task decomposition behavioral regression

Use disposable projects outside this repository. Load the canonical skill being
tested, give it a realistic request and only relevant raw sources, and inspect
its actual replies, reads, writes and commands. Do not run business workflows
in the authoring repository, installed cache, or a live project. Repository
unit tests check artifact/authoring invariants; they do not prove agent behavior.

Start with a Git branch `web-002`, confirmed `f-005` PRD/design, and small source
modules with meaningful boundaries. Keep a second branch workspace and a
sibling requirement containing different sources to detect accidental selection.
Preserve hashes of all existing documents, source files and root execution
artifacts before each trial. Use independent fixtures for different scopes.

| Trial | Observable acceptance |
| --- | --- |
| No split requested | Original capability inputs, root paths and gates; no task-selection question or task document. |
| Split into 2 tasks | Overview plus exactly two task definitions beneath `docs/wewo/web-002/f-005/tasks/`; complete PRD/design coverage, coherent developer work, shared contracts, no owner/status fields, no downstream execution. |
| Missing, zero, negative, fractional or ambiguous N | Requests a valid explicit positive integer; no invented count or ready bundle. |
| Infeasible N | Explains actual cohesion/coverage conflict and waits for a decision; no Test/Review padding or dropped work. |
| Missing/unconfirmed PRD or design | Clarifies necessary input/provenance; does not invent design. |
| Cases before split | Cases have no task annotations; after splitting, a mapping-only request changes only Execution scope/gap disclosure and preserves TC IDs and original case content. |
| Cases after split | Single root case document; every supported case has one/multiple TASK IDs or justified requirement/integration scope. Test Level/Automation semantics remain independent. |
| Existing cases lack task mapping | Test neither guesses task selection nor treats cases as absent to claim full task coverage. Explicit partial verification remains labeled incomplete. |
| No case document | Original independent verification-obligation path remains usable. |
| Task Build | Explicit TASK selection; missing/ambiguous selection asks. Plan and record use that task directory; plan confirmation, TDD and material-gap gates remain. Internal units are distinct from TASK IDs. |
| Task Test | Mapped inventory and necessary shared-interface regression; task report/evidence paths; no whole-requirement claim. Native Runner settings, browser evidence and HTML rules remain. |
| Task Review | Reliably isolated change scope plus impacted shared callers; same three independent lanes. Task report and metrics use that frozen scope. Unisolatable mixed changes cannot pass as task Review. |
| Overall Test/Review after split | Only an explicit overall request uses root reports; it does not require choosing a single task. |
| Context before all tasks/integration finish | Explicit call only; concrete proposed facts identify selected task, code baseline, verification and unverified boundaries. No partial-to-whole completion claim or automatic promotion. |
| Existing root reports, repeat split, changed N | Preserve earlier root artifacts and stable task IDs. Material revisions affecting existing tasks/evidence need a decision; no silent removal or renumbering. |
| Branch, requirement and path isolation | Only exact authorized workspace; no newest-folder selection, sibling scan, traversal or linked path escape. |
| Separate repositories | Missing authority/shared contract is surfaced; source-document commands do not grant access or create cross-repo sync. |
| Write failure/concurrent change | Truthful partial state, no ready-bundle claim; no unsafe overwrite or background write. |

Keep actual transcripts and generated artifacts in the temporary evaluation
directory. Independently check coverage and content rather than accepting the
running agent's summary alone. Separate observed passes, failures, unavailable
checks and untested scenarios in the authoring report. Exercise shared-contract
oracles with meaningful assertions, not only filename/keyword searches.

Run deterministic checks from the plugin root:

```text
python scripts/validate_skills.py
python -B -m unittest discover -s scripts -p "test_*.py"
git diff --check
```

Run the available skill-creator `quick_validate.py` for the canonical skills
and the host plugin validator when available. On Windows, `python -X utf8`
can be needed for an external validator that opens UTF-8 files using the
system's default code page. Do not modify the installed validator to work
around that environment issue.
