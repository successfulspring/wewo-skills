# Reusable Implementation Plan Template

Use this internal template after the baseline is established. Replace every
brace-delimited instruction with verified content in the selected output
language. Localize headings while keeping `implementation-plan.md` in
English. Do not copy this instruction block into the generated document.

```markdown
# {Localized title: Implementation Plan}

## 1. {Implementation Goal}
## 2. {Implementation Basis}
## 3. {Current Project Analysis}
## 4. {Implementation Scope}

### 4.1 {In Scope}
### 4.2 {Out of Scope}

## 5. {Global Implementation Constraints}
## 6. {TDD and Implementation Verification Strategy}
## 7. {Test Seams}
## 8. {Vertical Implementation Slices}

### Slice-001 {Slice name}

- **{Business goal}:**
- **{Requirement or behavior}:**
- **{Observable result}:**
- **{Test seam}:**
- **{Test level}:**
- **{Expected change scope}:**
- **{Implementation constraints}:**
- **{Verification commands}:**
- **{Completion conditions}:**
- **{Dependent slices}:**

## 9. {Interface, Database, and Dependency Changes}
## 10. {Verification Plan}
## 11. {Git and Worktree Strategy}
## 12. {Risks and Unresolved Questions}
```
