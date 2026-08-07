# Slice Compliance and Quality

Apply these checks before moving to the next vertical slice.

## Completion conditions

Require applicable evidence that:

1. the focused test experienced a valid Red;
2. the implemented behavior is Green;
3. relevant existing tests pass;
4. necessary integration evidence passes;
5. type-check or compilation passes;
6. no relevant new lint error exists;
7. changes remain within plan scope;
8. global constraints are preserved;
9. business expectations were not changed to pass tests;
10. requirement compliance was checked;
11. code quality was checked;
12. the implementation record is current.

Mark non-applicable or blocked items honestly; do not silently treat them as
passed.

## Requirement compliance

Check that the slice:

- implements every required behavior for the slice;
- omits no confirmed rule;
- adds no unrequested feature;
- preserves observable outcomes;
- stays inside requirement scope;
- follows technical design;
- preserves authorization, security, and consistency requirements;
- has direct test evidence for the target behavior.

Do not proceed when requirement compliance fails.

## Code and test quality

Check for:

- test-specific hardcoding or production branches;
- duplicate logic;
- unjustified singleton or global state;
- request or user data in shared objects;
- unconfirmed dependencies;
- layer violations;
- mixed unrelated responsibilities;
- over-abstraction or long complex functions;
- weak error handling or misplaced authorization;
- excessive mocking or tests coupled to internals;
- unrelated changes;
- debug code or temporary logs.

Fix in-scope issues and rerun affected tests.

## Optional fresh perspective

When the host supports isolated agents, a bounded slice may be implemented or
checked by a fresh agent using only the task, necessary context, constraints,
actual diff, tests, and latest results. Treat this as implementation-time
quality control, not final independent review.

Without that capability, switch to a read-only self-check perspective and
reread the plan, actual diff, tests, and current outputs. Never block because
an optional host capability is unavailable, and never generate review reports.

## Verification frequency

Run focused tests, affected tests, and applicable type, compile, or lint checks
frequently enough to detect local errors. Do not run a full suite after every
line, and do not postpone the first test until all slices are complete.
