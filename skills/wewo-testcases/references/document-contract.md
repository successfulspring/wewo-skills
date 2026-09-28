# Test Cases Document Contract

Produce exactly one project artifact: `test-cases.md`. Make it a lean,
execution-oriented test-case document, not a QA strategy, methodology, AI
reasoning, coverage-analysis, automation-statistics, or repository-inspection
report.

## Default structure

Start near-immediately with actual cases:

```markdown
# <Requirement Name> Test Cases

## Test Cases

### TC-001 — <Business-readable scenario>
...
```

Localize headings and content while keeping the filename in English. Do not
include Test Basis, Coverage Summary, Coverage Mapping, Automation Summary, or
Coverage Audit by default. Do not list inspected repository files. Publish
analysis or statistics only when the user explicitly requests them.

## Visible case schema

Each case contains only:

- ID and business-readable scenario in the heading;
- Module;
- business/test Priority (`P0`, `P1`, or `P2`);
- Recommended Test Level;
- human-facing Automation;
- Execution scope only for a split requirement, as defined below;
- Preconditions only when meaningful;
- concrete numbered Steps;
- concrete numbered Expected Results;
- Automation Condition only for Conditional cases;
- Notes only when genuinely useful.

Prefer user, business, or authoritative public-interface language. Avoid
incidental functions, private classes, repository paths, and source-line detail
unless an authoritative technical contract or explicit implementation-aware
request makes that seam the evidence target. Keep a requirement-derived case
when implementation is missing; later execution may fail it.

Do not expose Traceability, Objective, Technique, Coverage Lens, Risk Category,
Repository Fact, Evidence Need, automation priority, route `None`, or a separate
Playwright Yes/No field. Keep the internal test-level and automation-route
decisions distinct even though the visible representation is concise.

Automation may be `Browser`, `API`, `Unit`, `Integration`, `Component`,
`Contract`, `Auto`, `Manual`, or a `Conditional · <value>` form. `Auto` means
automation is appropriate but the concrete route is intentionally deferred to
downstream repository analysis; it is not a Test Level or tool. `Browser` names
the evidence route, not the selected test runner.

## Task execution scope

Decomposition is optional and does not change the requirement-level output
path. When splitting is established or a TASK is explicitly requested, inspect
only the exact current requirement's `task-breakdown.md` and the relevant
`tasks/<TASK-ID>/task.md` members it lists. Validate that IDs, paths, boundaries,
and dependencies agree; a missing overview, missing member, unsafe path, or
contradictory mapping needs clarification before claiming complete task
routing. Do not discover tasks in sibling requirements or another repository.
PRD/design and current explicit requirement clarifications remain the behavior
authority; task documents are derived scope/navigation, not new test oracles.

Add **Execution scope** to every case in a split requirement. Its value is one
or more applicable `TASK-ID` values, `Requirement-level`, or `Integration-level`.
Base the association on the case's unchanged behavior and the documented task
boundaries/shared contracts. A case may apply to multiple tasks. Use
Requirement-level or Integration-level only when that is the actual execution
responsibility, never as a substitute for an unknown association. Disclose an
unresolved mapping and its impact instead of guessing or claiming routing is
complete. This field supplies scope selection only; it must not change Steps,
Expected Results, Test Level, or Automation.

If cases predate decomposition, update only their Execution scope annotations
and any material mapping gap when asked to add task routing. Preserve every
existing TC ID and all original case content, including multiline steps,
oracles, classifications, conditions, and notes. Do not renumber, split, merge,
regenerate, or reclassify cases just to fit tasks. A request concerning one
task still updates the same root document, never a task-specific case copy.
If cases are first generated after decomposition, finish the existing semantic
and classification audits, then add supported scope annotations. With no split
materials and no TASK request, omit this field and retain the existing process.

## Material unresolved items

Ask before finalizing when ambiguity materially changes an oracle. If the user
declines or cannot clarify, omit the affected definitive oracle, publish
unaffected cases normally, and optionally add one compact `Unresolved Items`
section containing only issues that materially affect the published cases.
Omit the section when none remain. Do not create a general assumptions section.

## Final gate

Before saving, verify internally that requirement/risk traceability and all
applicable semantic coverage and oracle audits completed before Test Level and
Automation classification; every case has a valid level and an explicit or
deliberately deferred routing decision, concrete steps, one deterministic
authority-grounded pass/fail oracle for each material expected behavior,
cross-case oracle consistency, and correct Automation rendering; no material
`A or B`, `and/or`, current-implementation, or mock-behavior fallback remains;
Conditional dependencies are named; missing implementation suppressed no
authoritative obligation; and the document contains no invented thresholds,
execution results, executable tests, tool setup, long implementation
explanations, repository inventory, or default report sections.
For a split requirement also verify that scope annotations cover the published
cases without changing their semantics, and disclose any unresolved mapping.
