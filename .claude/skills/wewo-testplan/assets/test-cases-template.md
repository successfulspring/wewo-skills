# Reusable Test Cases Template

Use this internal rendering template. Replace brace-delimited guidance with
supported content in the selected language. Localize headings but keep the
filename `test-cases.md` in English. Omit every optional field or section that
does not add execution value. Prefer requirement/business/interface semantics
over incidental implementation detail. Do not copy this instruction block into
output.

```markdown
# {Requirement Name} {Test Cases}

## {Test Cases}

### TC-001 — {Business-readable Test Scenario}

- **{Module}:** {Product/requirement module}
- **{Priority}:** P0 / P1 / P2
- **{Test Level}:** Unit / Component / Integration / API / Contract / System / E2E
- **{Automation}:** {Playwright / API / Unit / Integration / Component / Contract / Auto / Conditional · Playwright / Conditional · API / Conditional · Auto / Manual}
- **{Automation Condition}:** {Conditional only; name the intrinsic enabling capability}

{Preconditions — include only when meaningful}

1. {Required setup or state}

{Steps}

1. {Concrete action}
2. {Concrete action}

{Expected Results}

1. {One observable, authoritative pass/fail outcome for this material behavior}
2. {Observable state or side-effect outcome}

{Notes — include only when genuinely useful}

## {Unresolved Items — include only for material unresolved oracle issues}

- {Concise unresolved rule that affects published cases}
```

For an Automatable Browser route, render Automation as `Playwright`. For a
Conditional Browser route, render `Conditional · Playwright` and include its
condition. When automation is clear but the stable route requires repository
inspection, render `Auto` or `Conditional · Auto`. For a Manual case, keep its
real Test Level and render Automation as `Manual`. Never repeat Priority inside
Automation or publish materially different alternative Expected Results.
