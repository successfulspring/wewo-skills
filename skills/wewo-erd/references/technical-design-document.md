# Technical Design Document Guide

Read this guide after the user confirms the complete technical solution.

## Contents

- [Required core structure](#required-core-structure)
- [Section content](#section-content)
- [Quality gate](#quality-gate)

## Required core structure

Use every core section in this order:

1. Design Overview
2. Requirement Sources
3. Existing System Analysis
4. Requirement Impact Scope
5. Overall Technical Approach
6. Detailed Design
7. Security and Engineering Risk Analysis
8. Implementation Constraints
9. Verification Focus
10. Design Decision Summary
11. Unresolved Questions

Under section 7, always include:

- Application Security
- Reliability and Business Correctness
- Code Structure and Maintainability

Localize headings and content. Keep `02-technical-design.md` in English.

## Section content

### Design overview

State the design goal, functionality to implement or modify, involved systems
and modules, and the core problem addressed.

### Requirement sources

List the actual conversation, files, PRD when present, project areas inspected,
and decisions confirmed in this stage. When no formal requirement document
exists, say that the design is based on the user's description, verified
project implementation, and confirmed dialogue.

### Existing system analysis

Record only verified stack, directories, modules, interfaces, models,
authorization, error handling, and reusable capabilities. Never invent project
content.

### Requirement impact scope

Identify additions, modifications, and explicit non-modifications across
applicable pages, components, modules, APIs, database, cache, queues, scheduled
work, integrations, configuration, and shared modules.

### Overall technical approach

Explain module placement, whether a module is added, collaboration, data flow,
core processing steps, and result delivery. Use diagrams only when useful.

### Detailed design

Add only applicable subsections for frontend, backend, interfaces, data, ER
diagram, state, transactions, concurrency, idempotency, cache, queues,
scheduled work, files, integrations, exceptions, migration, compatibility,
release, and rollback.

Put a Mermaid ER diagram here only when database entities or relationships
change. Never create a separate ERD file.

### Security and engineering risk analysis

For each relevant risk, identify the risk, location, design control, and
mandatory implementation constraint. Avoid irrelevant checklist content.

### Implementation constraints

Convert confirmed decisions and risk controls into concrete rules later code
must follow, including reuse boundaries, authorization location, transactions,
idempotency, object lifetime, change scope, dependencies, and existing error
formats as relevant.

### Verification focus

List directions later verification must emphasize, such as normal flow,
illegal state, unauthorized access, duplicates, concurrency, rollback,
external failure, regression, sensitive data, and logs. Do not generate a full
test plan or test cases.

### Design decision summary

Use a compact table:

```markdown
| Decision | Final approach | Reason |
|---|---|---|
| ... | ... | ... |
```

Include only decisions that materially affect implementation.

### Unresolved questions

Record issues that do not block the current design. Continue clarification
instead of documenting an unresolved issue that changes the core
implementation. Write the localized equivalent of "None" when empty.

## Quality gate

Before writing, verify that:

- the user confirmed the complete design;
- the design matches the requirement and verified project facts;
- no path, interface, class, module, table, or framework is invented;
- no unconfirmed choice is presented as final;
- affected and unaffected scope are explicit;
- application security is designed proactively;
- reliability and business correctness are designed proactively;
- code structure and maintainability are designed proactively;
- each real risk produces a concrete implementation constraint;
- ER content exists only for database change;
- existing architecture and shared capabilities are preferred;
- irrelevant sections and overdesign are absent;
- no production code, detailed task plan, complete test plan, or test cases are
  produced.
