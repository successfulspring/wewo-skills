# Three-Lane Independent Review

Formal review requires three isolated reviewer contexts. Independence is part
of review correctness, not a performance optimization.

## Main Review Orchestrator

Main owns scope and baseline resolution, factual context collection, Diff and
metrics preparation, compact factual packet preparation, reviewer dispatch,
candidate admission, evidence
verification, current-change attribution, root-cause deduplication, severity,
metrics, gates, and the unified `review.md`.

Main is not a fourth reviewer. Do not repeat all three lane reviews before or
after dispatch, and do not delegate admission or final conclusions.

## Exactly three lanes

1. **Requirement Consistency**
2. **Static Analysis & Engineering Rules**
3. **Contextual Security**

Each lane runs in its own context and returns before seeing another lane's
candidates. Do not combine lanes, add permanent lanes, or share preliminary
conclusions.

## Factual context packets

Orient each lane with a compact factual packet rather than eagerly loading the
entire scope. It may identify the fixed target and baseline, tracked and
explicitly included untracked manifests, production/test/configuration
classifications, requirement/design availability, applicable instruction
locations, language/framework facts, obvious changed entry points, and useful
deterministic scope or metric facts.

Tailor the packet to the lane. Add confirmed requirement/design evidence only
where applicable. The Static lane may receive deterministic tool context it
owns. Contextual Security must not receive Static or Semgrep candidates before
completing its reasoning. Do not send any lane's candidates, Main's suspected
defects, implementation defenses, implementer self-evaluation, unverified
explanations, prior conclusions, or the full development conversation.

## Progressive repository discovery

Each lane starts from its packet and reads changed or supporting code only as
needed to prove or reject candidates. Start narrow and expand through callers,
data paths, shared components, or other files when evidence requires it. Do not
impose numeric file or token limits, and do not prevent broad inspection when a
real cross-file issue requires it. Main may identify factual entry points but
must not pre-review the change to seed likely defects or vulnerabilities.

Ask each lane to return compact candidate data:

- candidate ID and lane;
- category and precise location;
- code or requirement evidence;
- expected/secure and actual behavior;
- realistic trigger or reachable path;
- concrete impact and current-change attribution;
- remediation and suggested verification;
- confidence or limitation.

Reviewer output is candidate data, not an admitted finding. Reviewer contexts
create no project reports or other workflow artifacts.

## Unavailable independent contexts

If the host cannot supply all three isolated contexts, do not simulate formal
independence in Main or one shared context. Preserve factual partial evidence,
disclose which lanes did not run, and report the formal review as unable to
conclude using the canonical code and security conclusion vocabulary.
