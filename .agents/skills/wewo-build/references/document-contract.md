# Implementation Document Contract

Use this guide to create and maintain the two workflow documents.

## Contents

- [Implementation plan](#implementation-plan)
- [Implementation record](#implementation-record)
- [Final document checks](#final-document-checks)

## Implementation plan

Use every core section in this order:

1. Implementation Goal
2. Implementation Basis
3. Current Project Analysis
4. Implementation Scope
   - In Scope
   - Out of Scope
5. Global Implementation Constraints
6. TDD Candidate Evaluation
7. Test Seams
8. Vertical Implementation Slices
9. Interface, Database, and Dependency Changes
10. Verification Plan
11. Git and Worktree Strategy
12. Risks and Unresolved Questions

Localize headings and prose. Keep the filename `05-implementation-plan.md` in
English.

Record only actual sources and verified project facts. Identify the final
capability and completion result, affected and unaffected scope, global
constraints, test framework and seams, quality commands, and Git state.

Use a TDD evaluation table:

```markdown
| Case or behavior | Evaluation | Final test level | Test seam | Notes |
|---|---|---|---|---|
```

Define every slice:

```markdown
### Slice-001 {Name}

- **Business goal:**
- **Requirement or case:**
- **Observable result:**
- **Test seam:**
- **Test level:**
- **Expected change scope:**
- **Implementation constraints:**
- **Verification commands:**
- **Completion conditions:**
- **Dependent slices:**
```

State when focused, integration, type, lint, build, migration, regression, and
broader-suite commands run. Never invent commands.

## Implementation record

Use every core section in this order:

1. Implementation Result Overview
2. Actual Changed Files
3. Vertical Slice Status
4. TDD Execution Record
5. Unit and Integration Test Results
6. Quality Check Results
7. Test Case Adjustments
8. Deviations from the Implementation Plan
9. Unfinished Work and Known Limitations
10. Final Verification Evidence
11. Final Conclusion

Localize headings and prose. Keep the filename `06-implementation-record.md`
in English.
Update the record continuously rather than reconstructing evidence from memory.

Record changed files:

```markdown
| File | Change type | Actual change |
|---|---|---|
```

Record slices:

```markdown
| Slice | Status | Test status | Quality-check status | Notes |
|---|---|---|---|---|
```

Use slice status not started, in progress, completed, blocked, or cancelled.
Do not label implementation-time quality checks as independent review.

Record each TDD behavior:

```markdown
### Slice-001 / Behavior-001

- **Test file:**
- **Red command and result:**
- **Valid failure reason:**
- **Implementation:**
- **Green command and result:**
- **Refactor:**
- **Post-refactor verification:**
```

Record checks:

```markdown
| Check | Command | Result | Evidence or notes |
|---|---|---|---|
```

For final evidence, include execution time, command, exit status, passed and
failed counts when available, unrun items, blockers, and remaining risks.

## Final document checks

Verify that:

- sources and project facts are real;
- scope and constraints match confirmed requirements;
- every command and outcome is actual;
- Red and Green claims have evidence;
- changed-file and slice tables match the repository;
- test-case adjustments are recorded in the implementation record, not
  applied to upstream documents;
- deviations and confirmations are explicit;
- unavailable checks and remaining risks are transparent;
- no independent-review or final-test-gate claim appears;
- no empty earlier or later workflow document was created.
