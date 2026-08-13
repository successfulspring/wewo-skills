# Semantic Test Case Quality and Oracle Audit

Generate complete semantic scenarios and executable cases before assigning Test
Level or Automation.

## Internal design model

Retain stable IDs, Requirement/Rule/Risk -> Case traceability, evidence needs,
objectives, techniques, coverage-lens decisions, and oracle provenance
internally. These decide what cases exist. Test Level and Automation are later
annotations and must not generate, remove, split, weaken, or rewrite cases.

## Executable semantic case

Each case first contains:

- ID and business-readable scenario;
- Module using requirement/product language;
- business/test Priority (`P0`, `P1`, or `P2`);
- Preconditions only when meaningful;
- concrete numbered Steps in user, business, or public-interface terms;
- concrete numbered Expected Results grounded in authority;
- Notes only when genuinely useful.

After the semantic audits pass, add Recommended Test Level, human-facing
Automation, and Automation Condition for Conditional cases. Keep Traceability,
Objective, Technique, Coverage Lens, Risk Category, Repository Fact, and
Evidence Need internal. Do not publish a Coverage Mapping by default.

Avoid unnecessary function names, private classes, provider methods,
repository paths, and source-line details. Use implementation language only
when an authoritative technical contract or explicit implementation-aware
request makes the seam itself the evidence target. Missing implementation does
not invalidate or remove a requirement-derived case; later execution may fail.

## Expected-result and oracle quality

Every published case must have one authoritative and executable pass/fail
oracle for each material expected behavior. Ground each oracle in current
explicit clarification, authoritative requirement/PRD, authoritative technical
design or external contract, or an explicit compatibility requirement. Current
implementation and mock behavior are not fallback requirement oracles.

Reject a material alternative such as `A or B`, `A and/or B`, `either A or B`,
`follow current implementation`, or `follow current mock behavior` when the
alternatives change the product contract or pass/fail meaning. Do not use
ambiguity to avoid clarification or publish an assertion that allows mutually
different outcomes.

Flexible wording is acceptable when it preserves one business outcome. For
example, `show a clear error message` is deterministic when exact copy is not
contractual, and `provide an actionable way back to product browsing` is
deterministic when the specific link is not required. Different implementation
wording is not material ambiguity; different required behavior is.

Prefer numbered outcomes for multiple effects, such as response semantics,
visible state, persistence, restored inventory, or absence of a side effect.
Reject `works normally`, `response is correct`, `no abnormal behavior`, and
unmeasurable performance or reliability claims. Do not mix implementation
explanation into the result unless it is part of the authoritative contract.

Require an authoritative measurable oracle for performance, capacity,
availability, latency, throughput, resource use, or reliability acceptance.
Never invent thresholds. If a material oracle remains undefined after targeted
clarification, keep the evidence need unresolved rather than copying current
behavior.

## Pre-classification audit order

Audit the semantic case set before Test Level or Automation classification:

1. Requirement Coverage: every required behavior/rule has evidence; only
   authoritatively optional, future, or out-of-scope behavior is omitted.
2. Happy Path and Critical Journey: core business flows and representative
   complete journeys have distinct evidence.
3. Negative and Alternative Flow: invalid, rejected, alternate, and error
   outcomes are covered where meaningful.
4. Boundary and Equivalence: partitions and just-below/at/just-above boundaries
   are covered where they change outcomes.
5. Business Rules: conditions, combinations, calculations, repeated actions,
   and duplicates are covered economically.
6. State Transition: valid/invalid transitions, persistence, rollback, retry,
   refresh, and recovery are covered where applicable.
7. Permission and Ownership: roles, authorization, ownership, isolation, and
   bypass risks are covered where applicable.
8. Failure and Recovery: timeout, partial failure, concurrency, idempotency,
   and consistency are covered only when authoritative evidence or real risk
   supports them.
9. Security and Trust Boundaries: relevant input, authorization, injection,
   untrusted-content, and sensitive-data risks have evidence.
10. Oracle Authority and Determinism: every Expected Result has authoritative
    support and one executable pass/fail meaning; no material alternative or
    implementation/mock fallback remains.
11. Cross-case Oracle Consistency: cases sharing a boundary, rule, state,
    permission, contract, error, calculation, side effect, or lifecycle agree.
    A user clarification overrides earlier assumptions and is propagated to
    every affected case; one case must not allow what another forbids.
12. Duplicate/Low-value Compression: every remaining case provides distinct
    evidence.

Fix gaps, contradictions, vague results, and duplicates before classification.
If materially different outcomes remain possible, first resolve them from
authority, then ask a targeted question when pass/fail changes. If clarification
is explicitly declined or unavailable, do not invent a winner or publish a
falsely deterministic Expected Result; publish unaffected cases and preserve
the affected requirement only as a compact Unresolved Item. Keep passing audit
details and statistics internal.
