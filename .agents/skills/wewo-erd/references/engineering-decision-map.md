# Internal Engineering Decision Map

Use this protocol as runtime reasoning state. It is not a business artifact.
Never create `docs/wewo/.../engineering-decision-map.md`, and do not print the
map verbatim unless a concise decision summary helps the user.

## Decision ownership classes

Classify every material engineering issue before deciding whether to ask.

### Repository Fact

Discover current framework, module boundaries, persistence, authentication,
dependency injection, APIs, error formats, and similar current-state facts from
the actual project. Do not ask the user to repeat discoverable facts.

### User Technical Constraint

Preserve an explicit user constraint such as a required technology,
compatibility obligation, prohibited infrastructure addition, or public API
commitment. Do not broaden it into unstated engineering decisions.

### Engineering Default

Decide routine details using verified repository facts, existing conventions,
requirement constraints, and minimal-complexity engineering judgment. Examples
include reusing dependency injection, following established service and
repository layering, preserving error formats and lifecycle management, and
avoiding an unnecessary abstraction. Do not delegate these routine choices to
the user.

### Material Engineering Decision

Request explicit confirmation when alternatives materially change
architecture, infrastructure, persistence, a public or external contract, a
security boundary, consistency, operational burden, migration or rollback
difficulty, a major dependency, performance or cost, or a difficult-to-reverse
system direction.

Present viable options, recommend one using evidence, explain trade-offs and
consequences, and discuss reversibility when relevant.

### Blocking Requirement Ambiguity

Ask the user when design depends on a product, business, or security-policy
decision that engineering cannot legitimately infer, such as access policy,
partial-success acceptability, historical-client compatibility, or a
zero-downtime migration requirement.

## Conceptual state

For each material engineering decision, conceptually track:

- stable decision or question identity when useful;
- Decision Topic;
- decision type and owner;
- evidence;
- current status;
- selected approach;
- provenance;
- material assumptions and their provenance;
- trade-offs and consequences;
- reversibility when material;
- newly unlocked dependent branches;
- eliminated branches;
- unresolved material consequences.

Valid decision provenance includes verified repository evidence, an explicit
user technical constraint, an explicitly confirmed material decision, or a
documented Engineering Default grounded in those inputs. An unsupported
architecture fashion, invented fact, or implementation convenience is not
valid provenance.

## Qualify material assumptions

Engineering Defaults may use ordinary local reasoning, but an assumption is
material when it affects correctness, security, consistency, deployment,
availability, data safety, or scalability architecture. For each such
assumption, determine whether it is supported by:

- a verified Repository Fact;
- an explicit User Technical Constraint; or
- an already confirmed Material Engineering Decision.

If not, and changing the assumption would materially invalidate the design,
reclassify the issue as a Material Engineering Decision or Blocking Requirement
Ambiguity. Do not create another ownership category for assumptions.

For example, a process-local coordinator may be correct only under a
single-process deployment topology. If that topology is not verified, do not
silently treat it as a harmless Engineering Default.

## Distinguish Engineering Defaults from arbitrary tuning values

The agent may decide that a configurable parameter is needed. A numeric or
default value that materially influences behavior is not a confirmed design
fact unless supported by an explicit requirement, verified repository
configuration or convention, protocol requirement, measured benchmark,
capacity evidence, acceptance criterion, or verified external constraint.

Without that evidence, label the value honestly as a suggested starting value,
tuning hypothesis, evaluation-dependent value, or unresolved non-blocking
tuning parameter. Examples include concurrency, retry count, timeout, traversal
depth, top-k, batch size, queue limit, cache TTL, and maximum item count.

Do not ask the user to decide every tuning parameter. Escalate only when the
value is materially a product or operational decision. Never invent an SLO or
SLA.

## Update after each material answer

1. Update the current decision and selected approach.
2. Record its evidence and provenance.
3. Eliminate branches made irrelevant.
4. Identify newly unlocked material engineering branches.
5. Add those branches to the unresolved map.
6. Record unresolved material consequences.
7. Recheck whether any Engineering Default depends on an unverified material
   assumption or unsupported tuning value.
8. Choose the next highest-value Decision Topic.

A confirmed decision is not merely done. Introducing an independent graph
database, for example, may unlock deployment dependency, connection lifecycle,
data synchronization, migration or backfill, backup and recovery, failure
behavior, and observability decisions. Retain only branches material to the
current project; do not expand theoretical implementation consequences.

## Recommendation discipline

Ground recommendations preferentially in:

1. explicit requirements and user constraints;
2. verified repository facts;
3. existing architecture and conventions;
4. simplicity and minimal change;
5. direct engineering trade-offs;
6. operational burden;
7. reversibility.

Every new abstraction, component, or dependency must justify its complexity.
Work from the domain problem to technology. Patterns are tools, not badges.
Prefer a reversible choice when alternatives otherwise provide similar value,
and preserve dependency direction and existing boundaries unless concrete
evidence supports changing them.

Do not introduce microservices, queues, caches, event-driven architecture,
DDD, CQRS, a new database, or another pattern merely because it is fashionable.
Do not invent performance targets, cost assumptions, SLOs, or SLAs.
