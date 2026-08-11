# Implementation Document Contract

Create only the Build-owned workflow artifacts:

- `implementation-plan.md`
- `implementation-record.md`

Do not create or modify product, design, QA planning/case, independent-review,
security-review, acceptance-execution, or other capability-owned documents.
Keep production assets and developer tests in normal project paths.

Localize headings and prose while keeping stable filenames in English. Use
verified facts and actual evidence. Omit irrelevant sections; never add empty
sections or fake evidence to satisfy a template.

## Implementation plan

Keep the plan lean:

1. **Goal & Binding Constraints** - minimum Binding Implementation Obligations,
   including explicit non-goals.
2. **Repository Reality** - only facts or conflicts material to implementation.
3. **Implementation Units** - colocate Goal, `Blocked by`, Binding obligations,
   Expected scope, Verification seam, `TDD: Yes / No`, and Done when.
4. **Material Changes / Open Gaps** - include only when relevant.
5. **Confirmation** - show that no implementation asset changes before the
   user's explicit confirmation.

Do not duplicate unit content in a global contract matrix or separate
verification-strategy table. Add adaptive detail only when it materially helps
execution.

## Implementation record

Create or update the record only after actual implementation evidence exists;
do not create an empty skeleton before confirmation. Keep:

- actual result and changed-file summary;
- Binding Obligation traceability;
- unit-level execution evidence;
- fresh final verification;
- deviations and confirmations;
- remaining blockers and risks;
- honest final status.

For a TDD unit, record TDD Red only when the target behavior was still
unimplemented, the focused test executed and failed, and the failure matched
the intended missing or incorrect behavior. Then record Green, Refactor if
performed, and post-refactor focused plus affected-regression verification.

If implementation came first, do not fabricate Red/Green/Refactor history.
Classify later failures as Debug / Implementation Failure, Regression Failure,
Environment / Infrastructure Failure, or another truthful status. Record
non-TDD implementation and sufficient verification directly.

For final evidence, distinguish Passed, Failed, Blocked, and Not Run; include
actual command or direct-check scope, exit status, counts, time, and limitations.

## Final document check

Verify that sources, changed files, obligations, commands, and results match
repository reality; material conflicts and confirmations are explicit; no
passing focused test is presented as completion by itself; no unresolved gap
is hidden; and no other capability's document was created or modified.
