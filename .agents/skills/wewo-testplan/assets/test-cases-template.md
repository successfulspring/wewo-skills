# Reusable Test Cases Template

Use this as an internal rendering template. Replace every brace-delimited
instruction with confirmed content in the selected output language. Localize
headings while keeping the filename `test-cases.md` in English. Do not copy
this instruction block into the generated document.

```markdown
# {Localized title: Test Cases}

## 1. {Document Notes}
## 2. {Test Case Overview}
## 3. {Requirement Coverage}
## 4. {Detailed Test Cases}

### TC-001 {Case title}

- **{Requirement and risk traceability}:**
- **{Priority}:** P0 / P1 / P2
- **{Test objective}:**
- **{Test category or perspective}:**
- **{Recommended test level}:**
- **{Required evidence level}:** e.g., Unit or higher / E2E / Manual; omit when no level is required
- **{Preconditions}:**
- **{Test data}:**
- **{Dependencies and blockers}:**
- **{Steps or behavior}:**
  1.
  2.
- **{Expected result}:**
  1.
  2.
- **{Cleanup considerations}:**
- **{Notes and open questions}:**

## 5. {Manual Evidence Index}

{Cases whose Required Evidence Level is Manual; index only, not an execution
workflow}

## 6. {Case Review Result}
## 7. {Unresolved Questions and Blockers}
```
