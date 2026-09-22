# KLOC Metrics and Review Gates

Calculate metrics only after Finding Admission from canonical deduplicated
findings and a recorded Diff classification. Preserve the Git calculations
below for supported attributable Diffs.

## Snapshot and comparison limits

Without a supported change baseline, additions, deletions, changed LOC, and
all current-change densities are `Not Calculable`; do not substitute snapshot
size, invented commits, or zero. Report supported inspected-file counts and
deduplicated `Confirmed snapshot findings` separately from current-change
totals. A user-supplied comparison supports only the measurements and causal
claims established by its verified before/after evidence; explicitly disclose
unsupported attribution and metrics.

Apply the same severity, evidence-completeness, three-lane, and security rules
to the named snapshot/comparison. A confirmed Critical/High defect fails its
scoped gate. A supported `Pass` describes that inspected scope only; it is not
a complete change-based review or merge approval. If requested change
attribution or high-risk evidence remains unavailable, use the corresponding
unable/incomplete conclusion. Metric unavailability alone does not turn a
complete explicitly requested snapshot review into a failed review.

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
