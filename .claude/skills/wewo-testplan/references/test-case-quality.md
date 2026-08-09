# Test Case Quality

Design cases after requirement analysis, risk analysis, and strategy selection.

## Required case fields

Include when applicable:

- stable test-case ID;
- requirement and risk traceability;
- title;
- priority;
- test objective;
- preconditions;
- test data;
- steps or behavior description;
- expected result;
- recommended test level;
- required evidence level (only where business risk or observable behavior
  requires it);
- test category or perspective;
- dependencies and blockers;
- cleanup considerations;
- notes and open questions.

Never include actual result, Passed or Failed status, execution time, or defect
ID during test design.

## ID and traceability rules

Use stable IDs such as `TC-001`. Preserve existing IDs when updating a
document, do not recycle removed IDs casually, and do not create a complex
requirement numbering scheme only for appearance.

When requirements have IDs, map them directly. Otherwise use concise business
rule descriptions. Trace requirements and risks to one or more cases and show
coverage without implying that one documented case must become one future test
function.

## Behavior versus execution

Keep two concepts explicit:

1. confirmed expected business behavior;
2. suggested execution method or level.

The first is a requirement expectation. The second is adjustable. Later
verification may split, merge, parameterize, or change the level without
silently changing the expectation.

## Recommended test level versus required evidence level

Keep two concepts explicit when useful:

1. Recommended Test Level: advisory guidance for later verification.
2. Required Evidence Level: the minimum evidence level considered sufficient
   to verify the scenario (a specific level, or "X or higher"). It defines only
   the evidence requirement.

Examples:

- pure formatting logic: Recommended Unit; Required Unit or higher;
- cross-page critical browser journey: Recommended E2E; Required E2E;
- subjective visual quality: Recommended Manual; Required Manual.

Set a Required Evidence Level only where the business risk or observable
behavior actually requires that level. Do not make every scenario require E2E.

## Case design quality

Each case must have a clear objective, satisfiable preconditions, concrete
data, specific steps or behavior, and an expected result that can be judged.
Do not use vague steps such as "operate the feature" or outcomes such as
"works as required."

Do not turn every requirement sentence into one case. Apply the selected
design methods and group only relevant normal, state/rule, negative, boundary,
authorization/security, consistency, API, UI, integration, E2E, regression,
performance, compatibility, and exploratory cases.

Do not convert an unresolved business question into a confirmed expectation.

## Internal review

Before user confirmation, review and revise:

- core requirement and high-risk rule coverage;
- normal, negative, and boundary coverage;
- authorization and security behavior;
- data consistency and reliability;
- regression scope;
- duplicate or mergeable cases;
- lowest reasonable test level;
- excessive E2E allocation;
- Recommended Test Level and Required Evidence Level classifications;
- satisfiable preconditions and data;
- specific steps;
- judgeable expected results;
- unsupported assumptions;
- dependencies, cleanup, and blockers.

Record in the final case document:

- core and high-risk coverage status;
- duplicates merged or retained;
- cases that cannot yet be designed;
- level and evidence-level review conclusions;
- remaining gaps and required follow-up.
