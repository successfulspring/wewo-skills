# Reusable PRD Template

Use this as an internal rendering template. Replace every brace-delimited
instruction with confirmed content in the selected output language. Localize
all headings while keeping the filename `01-prd.md` in English. Do not copy
this instruction block into the generated document.

```markdown
# {Localized title for Product Requirements Document}

## 1. {Localized heading: Requirements Overview}

{Concise confirmed summary}

## 2. {Localized heading: Background and Problem}

{Confirmed background, affected users, and problem}

## 3. {Localized heading: Requirement Goals}

{Confirmed goals and observable success outcomes}

## 4. {Localized heading: Users and Usage Scenarios}

{Confirmed users, situations, entry points, and desired results}

## 5. {Localized heading: Requirement Scope}

### 5.1 {Localized heading: In Scope}

{Confirmed current scope}

### 5.2 {Localized heading: Out of Scope}

{Confirmed exclusions and deferred related work}

## 6. {Localized heading: Functional Requirements}

{Specific confirmed behavior}

## 7. {Localized heading: Business Rules}

{Confirmed permissions, states, limits, and other governing rules}

## 8. {Localized heading: Exceptions and Edge Cases}

{Confirmed invalid-input, duplicate, missing-data, state-change, dependency,
and other relevant behaviors}

## 9. {Localized heading: Acceptance Criteria}

{Observable and verifiable outcomes}

## 10. {Localized heading: Unresolved Questions}

{Known unresolved questions, or the localized equivalent of "None"}

{Add only confirmed, applicable dynamic sections}
```
