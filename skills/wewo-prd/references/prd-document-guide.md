# PRD Document Guide

Read this guide only after the user confirms the overall requirement summary.

## Content contract

Write clear, precise business language in the selected output language.
Include only facts and product decisions covered by the user's confirmation.
Do not state an AI inference or unaccepted recommendation as a requirement.

Make functional requirements specific enough for design, business rules
understandable to developers, and acceptance criteria observable by later
testing. Do not include code-level implementation or perform technical design.

Preserve unresolved issues in the final section. Write the localized equivalent
of “None” when no unresolved issues remain.

## Required core structure

Use every core section in this order:

1. Requirements Overview
2. Background and Problem
3. Requirement Goals
4. Users and Usage Scenarios
5. Requirement Scope
   - In Scope
   - Out of Scope
6. Functional Requirements
7. Business Rules
8. Exceptions and Edge Cases
9. Acceptance Criteria
10. Unresolved Questions

Localize the headings; do not translate the filename `01-prd.md`.

## Optional dynamic sections

Add only sections supported by the confirmed requirement:

- Page and interaction requirements
- User roles and permissions
- Data requirements
- Import and export
- Messages and notifications
- Third-party system interactions
- Historical-data handling
- Compatibility
- Performance
- Privacy or compliance
- Glossary
- References

Do not add empty optional sections. Insert applicable sections without removing
or changing the order of the required core sections.

## Acceptance criteria

Describe verifiable results rather than aspirations. Cover the confirmed normal
result and the material rejection, duplicate, or failure behaviors. Use a
structured format only when it improves clarity; do not force one syntax on
every requirement.

## Final quality check

Before writing, verify that:

- the user confirmed the overall understanding;
- goal, primary users, core flow, outcome-changing rules, and scope are clear;
- source conflicts affecting behavior are resolved or explicitly retained as
  unresolved;
- no temporary assumption appears as a confirmed requirement;
- technical implementation has not replaced product behavior;
- each acceptance criterion is observable;
- every optional section has relevant content;
- the destination is the resolved isolated workspace;
- no unrelated requirement is combined into this document.
