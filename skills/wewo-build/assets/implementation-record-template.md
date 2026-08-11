# Reusable Implementation Record Template

Use this template only after actual implementation evidence exists; do not
create an empty skeleton before plan confirmation. Replace brace-delimited
instructions with actual evidence in the selected output language. Localize
headings while keeping `implementation-record.md` in English. Omit irrelevant
fields and never invent a test-first history.

```markdown
# {Localized title: Implementation Record}

## {Implementation Result}

{State the actual result and evidence-supported completion status.}

## {Actual Changes}

| {File / area} | {Change type} | {Actual change} |
|---|---|---|

## {Binding Obligation Traceability}

| {Binding obligation} | {Implemented in} | {Verification evidence} | {Actual result / confirmed gap} |
|---|---|---|---|

## {Implementation Unit Evidence}

### {TDD unit: Target behavior}

- **{Valid TDD Red}:** {Command, executed failure, intended reason, and confirmation target behavior was not yet implemented}
- **{Green}:** {Production implementation and executed result}
- **{Refactor, if performed}:**
- **{Post-refactor focused and affected-regression verification}:**
- **{Unit status}:**

### {Non-TDD or non-test-first unit: Target result}

- **{Actual implementation sequence}:**
- **{Evidence classification}:** {Debug / Implementation Failure, Regression Failure, Environment / Infrastructure Failure, or other truthful result}
- **{Sufficient verification}:**
- **{Unit status}:**

## {Final Fresh Verification}

| {Scope} | {Command / direct check} | {Status: Passed / Failed / Blocked / Not Run} | {Exit status, counts, time, and evidence classification} |
|---|---|---|---|

## {Deviations & Confirmations}

{Record meaningful ordinary adjustments, material conflicts, confirmations,
and resulting plan changes.}

## {Remaining Blockers / Risks}

{Record failures, blockers, unrun checks, partial scope, and remaining risks.}

## {Final Status}

{State whether all required units and obligations are closed and whether fresh
evidence supports completion.}
```
