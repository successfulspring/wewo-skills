# Requirement Authority and Repository Modes

Resolve expected-behavior authority and build the requirement model before any
implementation inspection.

## Sufficient authoritative input

Operate from a sufficiently clear current user requirement, an explicitly
supplied or established `prd.md`, a PRD plus optional `technical-design.md`, or
an explicit business/API/compatibility contract. The exact resolved current
Git branch and current requirement workspace may supply its `prd.md` and
`technical-design.md` automatically. This evidence is sufficient for normal
requirement-driven test design before product code exists. Do not discover
historical QA or workflow artifacts from sibling requirements or another
branch workspace merely because they exist.

Use this order for Expected Results:

1. current explicit user clarification;
2. authoritative current requirement or PRD;
3. authoritative technical design or external contract;
4. an explicit compatibility requirement.

Repository implementation is not a fallback requirement oracle. Keep distinct:

- **Requirement authority**: what the system must do.
- **Repository fact**: what the current implementation appears to do.
- **Test-design decision**: what evidence verifies the required behavior.

An authoritative technical design may define a testable API, transaction,
idempotency, state, data-integrity, or producer/consumer contract even before
product code exists. Distinguish that contract from incidental implementation
detail.

## Requirement-derived obligation invariant

Derive and lock requirement behaviors, rules, expected outcomes, and test
obligations before consulting implementation. Repository facts must not
redefine an oracle, suppress an obligation, replace required behavior with
current behavior, or manufacture an outcome for an ambiguous requirement.

Missing implementation is a potential test failure, not a reason to omit the
test case. Keep the case and its requirement-derived Expected Results. An
optional concise Note may state that the current implementation may not expose
the capability. Omit behavior only when authoritative evidence explicitly
marks it optional, future, out of scope, or not required for this delivery.

## Repository access modes

Use default requirement-driven mode when authoritative requirements and
optional design evidence are sufficient. Do not broadly inspect source code,
functions, classes, providers, pages, current tests, runners, or fixtures merely
to detail the case set.

Use implementation-aware mode only when:

- the user explicitly requests implementation-aware or regression design;
- source code is explicitly supplied or referenced as input;
- authoritative requirement artifacts are absent and current repository
  behavior is the requested basis; or
- a specific authoritative technical-design seam requires repository grounding.

In implementation-aware mode, use two passes:

1. derive and lock the requirement-driven scenario and oracle model;
2. inspect progressively from a specific risk or seam and enrich the locked
   model.

The second pass may add regression risk, setup, public-interface detail,
compatibility coverage, or automation-suitability evidence. It may not remove
or weaken locked obligations, reinterpret missing behavior as out of scope, or
rewrite requirement outcomes to match code.

## Material oracle ambiguity

Ask a targeted clarification when missing information changes pass/fail,
expected state, permission or ownership, a business rule, an acceptance
threshold, or an externally visible contract. State the evidence and exact
missing decision. Do not block for execution details that do not change the
oracle.

If clarification is declined or authority remains silent, generate unaffected
cases, keep the affected evidence need unresolved, optionally record only the
material rule in Unresolved Items, and never copy current behavior into Expected
Results. Never use `follow current implementation`, `follow current mock
behavior`, or equivalent language as an Expected Result. Do not add a general
assumptions or repository-facts report.
