# Finding Admission, Evidence, and Severity

Maintain a candidate ledger before producing formal findings.

## Contents

- [Candidate states](#candidate-states)
- [Admission checklist](#admission-checklist)
- [Root-cause deduplication](#root-cause-deduplication)
- [Evidence levels](#evidence-levels)
- [Severity](#severity)
- [Finding formats](#finding-formats)

## Candidate states

- `Confirmed`: evidence establishes the defect or security/reliability issue.
- `Potential`: a reasonable risk exists but evidence is insufficient.
- `Unverified`: missing code, environment, permission, or tooling prevents a
  decision.
- `Rejected`: evidence does not support the candidate, it is irrelevant, or it
  is a false positive.
- `Existing Issue`: the issue predates and is not materially exposed or
  amplified by the current change.

Only Confirmed current-change findings count in formal totals, densities, and
gates. Preserve other states in separate report sections for transparency.

## Admission checklist

Admit a formal finding only when all are present:

1. actual code or execution evidence;
2. a causal link to the current change;
3. exact file and line or tight code range;
4. a realistic trigger condition;
5. a concrete impact;
6. actionable remediation;
7. suggested verification;
8. a unique root cause;
9. calibrated severity and supported evidence level.

Reject generic advice, unsupported possibility, personal style preference,
unverified raw warnings, duplicated symptoms, and unrelated history.

## Root-cause deduplication

Group symptoms produced by one defect into one finding. List affected paths and
impacts under that root cause. Split findings only when they require different
fixes or can occur independently. Do not inflate counts by reporter, tool,
endpoint, or repeated occurrence.

## Evidence levels

| Level | Evidence |
|---|---|
| E1 | Static code and an explicit reachable path |
| E2 | Code evidence plus a repository-native static tool |
| E3 | Code evidence plus an actual test, build, or runtime result |
| E4 | Code evidence plus a specialty tool and independent verification |

Evidence level measures confidence, not severity. Never assign a level whose
supporting check did not run.

## Severity

- `Critical`: remote code execution, systemic authorization bypass,
  large-scale sensitive-data exposure, major financial/data loss, or valid
  production-secret disclosure. Block merge and release.
- `High`: resource or administrative authorization bypass, SQL or command
  injection, core business failure, transaction/data-consistency corruption,
  arbitrary file access, or severe compatibility break. Block merge.
- `Medium`: important boundary or error-handling gap, sensitive logging,
  important test gap, localized data risk, or material maintainability defect.
  Fix or obtain explicit risk acceptance.
- `Low`: localized readability, minor duplication, non-blocking convention
  issue, or low-impact hardening. Record for later handling.

Calibrate severity from reachable impact and exploitability, not from tool
labels alone.

## Finding formats

Code finding:

```markdown
### REV-001 {Title}

- **Status:**
- **Severity:**
- **Review dimension:**
- **File and location:**
- **Requirement or design:**
- **Code evidence:**
- **Trigger:**
- **Impact:**
- **Remediation:**
- **Suggested verification:**
- **Evidence level:**
```

Security finding:

```markdown
### SEC-001 {Title}

- **Status:**
- **Severity:**
- **Security category:**
- **File and location:**
- **Attacker capability:**
- **Entry point and attack path:**
- **Code evidence:**
- **Impact:**
- **Remediation:**
- **Suggested security test:**
- **Evidence level:**
```
