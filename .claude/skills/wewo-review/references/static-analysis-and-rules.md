# Static Analysis & Engineering Rules Lane

Combine deterministic evidence with independent semantic static review. Do not
split this lane into additional reviewers.

Run relevant safe repository-native compiler/type, lint, rule, test, build,
static, secret, dependency, or security checks. Attempt Semgrep under
[tool-policy.md](tool-policy.md) for every formal review. Treat all tool output
as candidates.

Begin with the changed-file manifest, applicable standards, language/framework
facts, and deterministic tool context. Progress from changed code or tool
evidence to the relevant surrounding construct, then inspect callers or shared
components only when needed; do not reread unrelated modules for completeness.

Independently inspect the Diff and affected code for concrete correctness
defects, repository-rule violations, invalid state assumptions, error/resource
lifecycle problems, shared-component regressions, API/contract drift,
dependency misuse, dangerous coupling, changed-test quality defects, and
obvious transaction/concurrency/retry failures.

Treat changed tests, executable fixtures, and helpers as first-class code.
Check for assertions that pass for the wrong reason, wrong/excessive mocks,
meaningless regressions, unsafe shared state/order dependence, lifecycle leaks,
brittle timing, false async behavior, and mismatched test intent. Do not create
a separate Test Quality lane.

Repository-documented standards override generic preferences. Do not report
subjective style or theoretical maintainability concerns without concrete
impact.

Return actual commands and outcomes plus candidates with precise code evidence,
trigger, impact, attribution, remediation, verification, and limitations.
