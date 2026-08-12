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

Automation may be `Playwright`, `API`, `Unit`, `Integration`, `Component`,
`Contract`, `Auto`, `Manual`, or a `Conditional · <value>` form. `Auto` means
automation is appropriate but the concrete route is intentionally deferred to
downstream repository analysis; it is not a Test Level or tool.

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
