# Independent Review Model

Use independent factual passes to reduce implementation bias.

## Orchestrator responsibilities

The orchestrator:

1. freezes and records the review scope;
2. collects requirements, design, repository rules, Diff, affected context,
   and actual command evidence;
3. identifies the technology stack and attack surfaces;
4. runs shared safe commands once when practical;
5. prepares clean reviewer packets;
6. dispatches independent dimensions;
7. consolidates candidates without changing their evidence;
8. verifies, attributes, deduplicates, and calibrates findings;
9. calculates only supportable metrics;
10. writes the two final reports.

Do not delegate final admission or gate responsibility.

## Clean reviewer packet

Provide only:

- review objective and assigned dimension;
- exact scope and Diff;
- original confirmed requirements;
- technical design and implementation constraints;
- repository instructions;
- necessary affected context;
- actual test and tool output;
- relevant language, framework, or security guidance.

Do not provide:

- implementation defenses or subjective rationale;
- the implementer's self-evaluation;
- unproven explanations;
- statements that an area is probably safe;
- another reviewer's preliminary conclusions;
- unrelated development conversation.

Ask each reviewer for candidates with file location, evidence, trigger,
impact, remediation, suggested verification, attribution, and confidence.
Reviewer output is not automatically an admitted finding.

## Default dimensions

Use separate fresh reviewers when capacity permits:

1. Requirement and design compliance.
2. Repository standards and code structure.
3. Correctness and test quality.
4. Impact and compatibility.
5. Security and reliability.

Combining dimensions is acceptable only when capacity is limited; disclose the
combination and preserve independent context. Reviewers must not see each
other's initial conclusions.

## Fallback without independent agents

Continue with separate semantic and tool-assisted passes, but label the work
`Non-independent preliminary review`. State:

- no fresh independent reviewer ran;
- full context isolation was unavailable;
- the result is not a formal independent review.

Do not block basic review because optional host capability is absent. For
high-risk changes, choose `Unable to Conclude` when the missing independent
pass prevents a trustworthy merge decision. A prior build self-check remains
an `Implementation Self-check` and never satisfies this model.
