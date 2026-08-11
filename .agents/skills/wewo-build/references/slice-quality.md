# Implementation Unit Quality

A good unit is:

- coherent;
- observable or directly verifiable;
- small enough for one focused implementation context;
- explicit about blocking dependencies;
- connected to its Binding Implementation Obligations;
- clear about `TDD: Yes / No`;
- closable with real evidence.

Reject a unit that:

- combines unrelated behaviors;
- splits only by architecture layer when a behavioral unit is practical;
- has no observable completion condition;
- starts while blocked;
- silently crosses a material boundary or explicit non-goal.

Close it only when the target result is complete, binding obligations remain
preserved, required verification actually ran, failures are visible, and every
material gap is resolved or confirmed. A passing focused test alone is not
enough.
