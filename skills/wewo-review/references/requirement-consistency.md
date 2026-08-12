# Requirement Consistency Lane

Determine whether the fixed Diff faithfully implements confirmed requirements
and explicitly available material design constraints.

Use the Diff, necessary affected code, confirmed current requirement,
explicitly supplied/referenced requirement or technical-design material, and
relevant repository facts. Never discover historical workflow documents.
Begin with the obligation, design evidence, scope manifest, and relevant
changed entry points. Map each obligation to its implementation seam, then
inspect changed code and expand to affected callers or data paths only when
needed; do not eagerly load every changed file.

Review for missing or partial behavior, wrong observable outcomes, scope creep,
explicit non-goal violations, requirement contradictions, incompatible API or
data semantics, material design deviation, and explicitly required
compatibility.

Changed tests may support the assessment by exposing missing evidence for
important confirmed behavior or encoding inconsistent behavior. Assertions are
implementation evidence, never requirement authority or a replacement for
explicit facts. Do not invent QA expectations; admit missing verification only
when its absence has concrete impact, not because more tests would be useful.

When requirement evidence is absent, return `Requirement Compliance: Not
Evaluated`. When design evidence is absent, return `Design Compliance: Not
Evaluated`. Do not invent either.

Every candidate must cite the exact requirement/design evidence, code location,
conflicting behavior, trigger, impact, and current-Diff attribution.
