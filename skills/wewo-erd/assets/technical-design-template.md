# Reusable Technical Design Template

Use this as an internal rendering template. Replace every brace-delimited
instruction with confirmed content in the selected output language. Localize
all headings while keeping the filename `02-technical-design.md` in English.
Do not copy this instruction block into the generated document.

```markdown
# {Localized title: Technical Design Document}

## 1. {Localized heading: Design Overview}

{Goal, functionality, systems, modules, and core problem}

## 2. {Localized heading: Requirement Sources}

{Actual source material, inspected project areas, and confirmed dialogue}

## 3. {Localized heading: Existing System Analysis}

{Verified project facts and reusable capabilities}

## 4. {Localized heading: Requirement Impact Scope}

{Additions, modifications, and explicit non-modifications}

## 5. {Localized heading: Overall Technical Approach}

{Module placement, collaboration, data flow, processing, and result}

## 6. {Localized heading: Detailed Design}

{Only applicable frontend, backend, interface, data, state, transaction,
concurrency, idempotency, cache, queue, scheduled work, file, integration,
exception, migration, compatibility, release, and rollback subsections}

{Include a Mermaid ER diagram here only for entity or relationship changes}

## 7. {Localized heading: Security and Engineering Risk Analysis}

### 7.1 {Localized heading: Application Security}

{Relevant risks, design controls, and implementation constraints}

### 7.2 {Localized heading: Reliability and Business Correctness}

{Relevant risks, design controls, and implementation constraints}

### 7.3 {Localized heading: Code Structure and Maintainability}

{Relevant risks, design controls, and implementation constraints}

## 8. {Localized heading: Implementation Constraints}

{Concrete rules later code must obey}

## 9. {Localized heading: Verification Focus}

{Important later verification directions, not full test cases}

## 10. {Localized heading: Design Decision Summary}

| {Localized: Decision} | {Localized: Final approach} | {Localized: Reason} |
|---|---|---|
| ... | ... | ... |

## 11. {Localized heading: Unresolved Questions}

{Non-blocking unresolved questions, or the localized equivalent of "None"}
```
