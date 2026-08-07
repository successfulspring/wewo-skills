# TDD and Test Quality Protocol

Use TDD for behavior with a valid, valuable testing seam.

## Red

For one observable behavior:

1. Use the project's existing test framework.
2. Add or identify one focused test through the selected seam.
3. Run the exact test.
4. Confirm that it fails.
5. Confirm failure is caused by missing or incorrect target behavior.

Syntax errors, import failures, missing fixtures, missing dependencies,
database connection failure, startup failure, framework misconfiguration, and
pre-existing project errors are not valid Red evidence. Fix or resolve the
environment problem before implementation, or record TDD as blocked.

Do not write production behavior without valid Red evidence when TDD is
applicable.

## Green

Implement the minimum production change that:

- satisfies the current behavior;
- fits existing architecture;
- follows global constraints;
- remains evolvable;
- preserves existing behavior.

Never hardcode test inputs, add test-environment branches, remove or weaken
assertions, change business expectations, implement later slices early,
change unrelated code, introduce premature abstraction, duplicate reusable
logic, swallow exceptions, or add an unconfirmed dependency.

Run the focused test and record actual Green evidence.

## Refactor

After Green, make only small in-scope improvements such as naming, obvious
deduplication, splitting a newly long function, extracting a small helper,
simplifying conditions, or matching surrounding style. Avoid broad
architecture changes, unrelated cleanup, mass renames, complex abstraction,
and behavior outside the slice.

Rerun relevant tests after every refactor.

## Unit and integration balance

Use unit or application-service tests for fast rules, validation, state,
authorization, transformations, boundaries, exceptions, idempotency, and
isolated behavior.

Use integration evidence for persistence, transactions, API-service
collaboration, cache, messaging, filesystem, external adapters, and
multi-module behavior. Mocks cannot replace real integration evidence when the
risk is collaboration or transaction correctness.

Prefer input, public behavior, and observable result. Mock uncontrolled system
boundaries such as external payment, email, SMS, time, randomness, HTTP,
filesystem, or messaging. Avoid mocking internal collaborators merely to
assert calls.

## E2E boundary

Browser E2E is outside Build's execution responsibility. Do not make browser
E2E part of the implementation loop, do not inspect whether E2E tooling or
browsers are installed, and do not install or run browser E2E. When a planned
or documented scenario is classified as E2E, preserve its expected business
behavior, keep it outside Build execution, never mark it Passed, and record
the handoff for independent test execution in the implementation record.
Leave browser scripts, compatibility, visual checks, exploration, full
acceptance, large performance tests, and uncontrolled third-party pages to
the test-execution stage.
