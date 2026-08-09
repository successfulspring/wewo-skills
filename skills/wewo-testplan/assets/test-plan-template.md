# Reusable Test Plan Template

Use this as an internal rendering template. Replace every brace-delimited
instruction with confirmed content in the selected output language. Localize
headings while keeping the filename `test-plan.md` in English. Do not copy
this instruction block into the generated document.

```markdown
# {Localized title: Test Plan}

## 1. {Test Overview}
## 2. {Test Basis}
## 3. {Test Object and Requirement Understanding}
## 4. {Test Scope}

### {Current Test Scope}
### {Regression Scope}
### {Out of Scope}

## 5. {Quality Risk Analysis}

| {Risk ID} | {Risk} | {Impact} | {Level} | {Test Response} |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## 6. {Test Strategy}
## 7. {Test Design Methods}
## 8. {Verification Method and Evidence Levels}

{Recommended Test Level per scenario; Required Evidence Level where business
risk or observable behavior requires it}

## 9. {Coverage Conditions and Test-Data Assumptions}

{Product-scope coverage conditions and test-data assumptions as design inputs}

## 10. {Test-Data Strategy}
## 11. {Test Priority}
## 12. {Test Entry Conditions}
## 13. {Test Exit Conditions}
## 14. {Test Deliverables}
## 15. {Blockers and Unresolved Questions}
```
