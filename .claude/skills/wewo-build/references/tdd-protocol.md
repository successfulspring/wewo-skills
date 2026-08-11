# Hard TDD Sequence

Use TDD only for a unit marked `TDD: Yes`.

## Gate

Follow exactly:

```text
Test -> Execute -> Valid TDD Red -> Production implementation -> Green -> Refactor -> Verify
```

Do not modify or partially implement the target production behavior before a
valid TDD Red has been observed.

## Valid TDD Red

Record TDD Red only when all are true:

- the target production behavior is still unimplemented;
- the focused test actually ran;
- it failed;
- the failure matches the intended missing or incorrect behavior.

Environment setup, unrelated dependencies, fixture defects, unrelated
syntax/import failures, pre-existing defects, regressions elsewhere, and bugs
found after production implementation are not automatically TDD Red. Label
them truthfully; never retrofit a test-first history.

## Test seam and implementation

Use a stable public or repository-established seam. Test observable behavior,
not private methods, internal call order, or collaborator call counts. Mock
uncontrolled external boundaries rather than internal implementation.

After valid Red, implement the minimum production behavior that preserves the
unit's binding obligations and run to Green. Refactor only if useful, keeping it
unit-local, behavior-preserving, and obligation-preserving. Then rerun the
focused test and relevant affected regression.
