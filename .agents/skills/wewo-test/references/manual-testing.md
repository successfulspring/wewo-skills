# Executable Manual Testing

Use manual tasks for work that requires human observation, physical context,
uncontrollable external behavior, or unjustifiably expensive automation.

## Task format

```markdown
### MT-001 {Title}

- **Source requirement or case:**
- **Priority:**
- **Environment:**
- **Preconditions:**
- **Test data:**
- **Steps:**
- **Expected result:**
- **Required evidence:**
- **Execution status:** Manual Pending
- **Actual result:**
- **Executor:**
- **Execution time:**
- **Defect ID:**
```

Use stable IDs and unambiguous, executable steps. Separate expected behavior
from actual result. Do not write “verify it works.”

## Status rules

- `Manual Pending`: not executed.
- `Manual Passed`: a human executed it, supplied sufficient evidence, and the
  observed result matched expectations.
- `Manual Failed`: a human executed it and the result differed.
- `Manual Blocked`: environment or prerequisite prevented execution.
- `Manual Skipped`: an explicit, recorded reason justified skipping.

An agent may prepare, clarify, or record a human result. It must not impersonate
the executor or infer `Manual Passed` from automation output.

## Integration with the gate

Map every manual task back to the matrix. Count required P0/P1 manual work in
completion metrics. A pending or blocked required high-risk manual task makes
the gate `Incomplete / Unable to Confirm`; an observed critical failure
contributes to `Fail`.
