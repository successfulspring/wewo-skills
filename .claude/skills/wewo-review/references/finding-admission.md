# Finding Admission

A reviewer or tool candidate is not automatically a formal finding. Main owns
admission and the compact candidate ledger.

## IDs and states

Reviewer candidates keep lane-local `REQ-*`, `STATIC-*`, or `SEC-*` IDs. After
admission and root-cause deduplication, Main assigns one sequential canonical
`REV-*` ID and records every detecting lane as non-additive provenance.

- `Confirmed`: evidence establishes a current-change defect.
- `Potential / Unverified`: a plausible issue lacks decisive evidence.
- `Rejected`: evidence disproves, duplicates, or makes it irrelevant.
- `Existing Issue`: it predates the Diff and is not materially expanded or
  newly reachable because of it.

Only Confirmed current-change findings enter formal totals and gates.

## Admission gate

Verify actual evidence, exact location/root cause, realistic trigger or stated
limitation, concrete impact, current-Diff attribution, deduplication, and
severity based on impact, reachability/exploitability, scope, and reversibility.
Reject generic advice, unsupported possibility, style preference, raw warning,
duplicate symptom, and unrelated history.

## Metric scope

Assign each Confirmed finding one density classification: `Production Code`,
`Test Code`, or `Out of Density`. This controls density inclusion only, never
reality, severity, or gate effect. Configuration/migration defects remain real
and may block even when out of density.

## Security and tool candidates

Classify security from category, reachable impact, and evidence, not detecting
lane. A confirmed Semgrep SQL injection and a confirmed Requirement-lane
authorization failure are security findings.

Every Semgrep warning starts as a tool candidate. Confirm only after checking
code, reachability, controllable input where applicable, defenses, semantics,
Diff attribution, unique root cause, and impact. Raw warnings never become the
formal count without admission.

## Severity and record

Use `Critical`, `High`, `Medium`, or `Low`; confirmed current-change Critical
and High findings block merge. Tool labels do not set severity.

Record canonical ID, state, detecting lanes, severity, category, metric scope,
location, evidence, expected/actual behavior, trigger/path, impact,
attribution, remediation, verification, and limitation.
