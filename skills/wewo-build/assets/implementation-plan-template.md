# Reusable Implementation Plan Template

Replace brace-delimited instructions with verified content in the selected
output language. Localize headings while keeping `implementation-plan.md` in
English. Omit irrelevant optional sections and do not copy this instruction
block into the document.

```markdown
# {Localized title: Implementation Plan}

## {Goal & Binding Constraints}

{State the goal, what must be true, what must not change, material constraints,
explicit non-goals, and important verification boundary. Keep only obligations
that affect implementation.}

## {Repository Reality}

{Record only verified facts or conflicts that materially affect feasibility,
scope, sequencing, or verification.}

## {Implementation Units}

### {Unit-X: Name}

- **{Goal / observable result}:**
- **{Blocked by}:**
- **{Binding obligations}:**
- **{Expected scope}:**
- **{Verification seam}:**
- **{TDD: Yes / No}:** {Brief reason when No is not obvious}
- **{Done when}:**

## {Material Changes / Open Gaps}

{Include only when relevant. Record material conflicts, high-impact changes,
confirmation needs, and accepted resolutions. Add adaptive detail only where
it materially helps execution.}

## {Confirmation}

- **{Material plan summary}:**
- **{Confirmation requested}:**
- **{Implementation assets}:** Not modified before explicit confirmation
```
