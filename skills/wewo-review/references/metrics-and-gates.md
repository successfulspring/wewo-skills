# Metrics and Review Gates

Calculate metrics only from an evidenced, recorded Diff classification.

## Contents

- [LOC model](#loc-model)
- [Candidate and issue metrics](#candidate-and-issue-metrics)
- [Effectiveness and security metrics](#effectiveness-and-security-metrics)
- [Small Diff interpretation](#small-diff-interpretation)
- [Code-review conclusion](#code-review-conclusion)
- [Security gate](#security-gate)

## LOC model

Record additions plus deletions separately for:

- production code;
- test code;
- configuration and migrations;
- eligible reviewable code;
- actually reviewed code.

Exclude generated, vendor, lock, build, minified, compressed, and
pure-formatting changes. Document classifications and exclusions.

```text
review coverage = reviewed eligible LOC / total eligible LOC
```

Do not claim full coverage merely because every changed filename was opened.

## Candidate and issue metrics

Record:

- raw candidate count;
- Confirmed, Potential, Unverified, Rejected, and Existing Issue counts;
- root-cause-deduplicated finding count;
- unresolved blocker count.

```text
confirmation rate = Confirmed candidates / all candidates

confirmed issue density =
Confirmed current-change issues / reviewed production KLOC

serious issue density =
(Critical + High current-change issues) / reviewed production KLOC

security issue density =
Confirmed current-change security issues / reviewed production KLOC

weighted issue density =
sum(issue count * severity weight) / reviewed production KLOC
```

Use Critical 8, High 5, Medium 2, and Low 1. Use reviewed test KLOC as the
denominator for test-quality issue density.

Do not calculate a ratio when the denominator is zero, uncertain, or not
classified. Mark it `Not calculable` and explain why.

## Effectiveness and security metrics

Calculate when evidence exists:

- requirement implementation mapping;
- requirement test mapping;
- high-risk scenario test coverage;
- tool verification coverage;
- changed attack-surface count;
- reviewed attack-surface count and coverage;
- security severity distribution;
- high-risk flow test coverage;
- tool-warning manual-verification rate;
- unresolved security blockers.

```text
requirement implementation mapping =
requirements with verified code evidence / confirmed applicable requirements

requirement test mapping =
requirements with verified test evidence / confirmed applicable requirements

attack-surface review coverage =
reviewed changed attack surfaces / identified changed attack surfaces

high-risk flow test coverage =
high-risk flows with actual test evidence / identified high-risk flows

tool-warning manual-verification rate =
manually verified warnings / total tool warnings
```

The target for a merge-ready security gate is zero unresolved Critical, zero
unresolved High, and 100% review coverage for identified high-risk attack
surfaces. An identified high-risk entry point omitted from review fails the
gate. If semantic review was completed but essential environment-dependent
verification remains unavailable, use `Incomplete / Unable to Confirm`.

## Small Diff interpretation

For fewer than roughly 200 eligible changed lines, emphasize absolute findings,
severity, and blockers. Show KLOC ratios only with a volatility warning.
Evaluate long-term density using comparable project periods and at least about
1,000 cumulative lines. Never use one small Diff to rate a team or project.

Metrics support transparency and trends; they do not decide the gate alone.

## Code-review conclusion

- `Pass`: no Critical or High, no known core-requirement omission, relevant
  tests and applicable build/quality checks passed, and no unresolved blocker.
- `Conditional Pass`: no Critical or High; only explicitly accepted Medium or
  Low items remain. Record conditions, residual risk, follow-up, and risk
  owner.
- `Fail`: any unresolved Critical or High, core requirement omission, material
  business error, authorization or consistency risk, relevant test/build
  failure, or severe compatibility break.
- `Unable to Conclude`: incomplete Diff, missing critical code or environment,
  unverifiable permission/transaction/external behavior, missing necessary
  independent review, or unverified high-risk security flow.

Even when unable to conclude, report completed review and verified findings.
Use only the four conclusion values above; express individual checks as
blocked or unavailable without replacing the final conclusion label.

## Security gate

- `Pass`: applicable high-risk attack surfaces are reviewed, no unresolved
  Critical or High exists, critical security checks support the conclusion,
  and no security blocker remains.
- `Fail`: unresolved Critical or High, valid-secret exposure, unprotected
  resource authorization, missing transaction or idempotency in a core
  transaction, unreviewed high-risk entry point, or failed critical security
  test.
- `Incomplete / Unable to Confirm`: critical evidence or high-risk
  verification is unavailable.

Security gate failure or incompleteness prevents a merge-ready result
regardless of the ordinary code-review conclusion.

Use only the three security-gate values above. Do not convert missing
independent review or critical high-risk evidence into a Pass through an
invented exception. Risk acceptance may support `Conditional Pass` only for
Medium or Low findings and only when the actual accepting owner, conditions,
and follow-up are recorded.
