# KLOC Metrics and Review Gates

Calculate metrics only after Finding Admission from canonical deduplicated
findings and a recorded Diff classification.

## Density scope

```text
Density-Eligible Changed Code LOC =
Changed Production Code LOC + Changed Test Code LOC
```

These totals include physical lines from applicable untracked files explicitly
selected into scope and measured as new files.

Exclude configuration/migration, documentation, generated, vendor, build,
minified, lock, binary, and other non-semantic LOC. Report production, test,
configuration/migration, every exclusion, and the denominator.

Out-of-density findings remain real, appear in absolute totals, and affect
both gates when warranted. Exclude them only from density numerators so each
numerator and denominator describe the same scope. If the denominator is zero
or unsupported, report `Not Calculable`; never substitute another denominator.
For a very small Diff, report the ratio and a volatility warning without a
numeric threshold.

## Required metrics

```text
Confirmed Finding Density =
Density-Eligible Confirmed Current-Change Findings
/ Density-Eligible Changed Code LOC * 1000

Serious Finding Density =
Density-Eligible Critical + High Confirmed Current-Change Findings
/ Density-Eligible Changed Code LOC * 1000

Security Finding Density =
Density-Eligible Confirmed Current-Change Security Findings
/ Density-Eligible Changed Code LOC * 1000
```

Display numerator, denominator, density, and exclusions. Exclude Potential /
Unverified, Rejected, Existing Issue, raw warnings, out-of-density findings,
and duplicates from density numerators.

Report deduplicated absolute counts for total Confirmed, density-eligible,
Production Code, Test Code, Out of Density, each severity, security findings,
and raw Semgrep/tool candidates. Severity totals must equal the canonical
confirmed total. Label optional detected-by lane counts overlapping/non-additive.

`Tool Candidate Confirmation Rate` may be reported as a diagnostic but never
controls a gate. Do not use severity weights or weighted density without an
explicit organizational policy.

## Overall Review Conclusion

- `Pass`: no Critical/High current-change finding or known core requirement
  omission, evidence supports the Diff, and all three lanes ran.
- `Conditional Pass`: no Critical/High; only disclosed Medium/Low conditions.
- `Fail`: a Critical/High, core omission, material correctness failure, or
  failed critical verification blocks the change.
- `Unable to Conclude`: incomplete Diff, critical evidence, or independent
  execution prevents a trustworthy conclusion.

## Security Gate

- `Pass`: high-risk surfaces were reviewed, no Critical/High security finding
  remains, and evidence supports the conclusion.
- `Fail`: a confirmed Critical/High security finding or failed critical
  security control blocks the change.
- `Incomplete / Unable to Confirm`: missing independent or high-risk evidence
  prevents a trustworthy conclusion.

Semgrep failure or partial coverage does not automatically fail either gate
when other evidence remains meaningful, but disclose its limitation. An
incomplete or failed Security Gate prevents merge readiness.
