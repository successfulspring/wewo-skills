# Requirements and Project Analysis

Use this guide before proposing a technical design.

## Assess requirement sufficiency

Establish at least:

- what must be implemented, changed, or fixed;
- affected users, business situations, or system modules;
- the core business result;
- primary scope boundaries;
- rules that materially constrain implementation.

Proceed directly to project analysis when this is clear. If only a few details
are missing, ask for those details inside this skill, such as roles, historical
data compatibility, interface or database change permission, rollback versus
partial success, audit needs, or new-dependency permission.

If the goal is too vague to select a basic implementation direction, clarify
it progressively. Suggest product-requirement work only when the user wants a
complete product rediscovery; never make another skill a prerequisite.

## Combine input material

Use only sources the user explicitly provides, references, or confirms in this
interaction. Do not scan `docs/wewo/` or the repository for historical
requirement documents; a discovered candidate requires explicit user
confirmation before use.

Accept and synthesize:

- current conversation and requirement descriptions;
- Markdown, TXT, office documents, and PDFs;
- screenshots, prototypes, and other images;
- existing PRDs, including `01-prd.md`;
- issues, tasks, change notes, and bug reports;
- relevant project requirement documents;
- current project code;
- multiple related sources.

Do not assume one file is the sole source of truth. Preserve source identity,
distinguish confirmed statements from proposals, and surface conflicts for
user resolution.

Use capabilities available in the current host to read supported formats. If a
format or image cannot be inspected, request an accessible export, screenshot,
or pasted excerpt and continue with the available evidence.

## Inspect the existing project

When code exists, inspect only what is relevant to the requirement:

- technology stack and directory structure;
- system layers and module boundaries;
- pages, components, modules, and services;
- existing interfaces and data models;
- authentication and authorization;
- error handling, logging, and auditing;
- configuration management;
- dependency injection and object lifetimes;
- cache, queues, scheduled work, and third-party services;
- similar implementations;
- coding and architecture conventions.

Use repository instruction files when needed for conventions. Trace relevant
control flow far enough to understand existing responsibilities and reuse
points.

Never invent a file path, class, function, interface, table, shared module, or
framework. Label an inference as an inference and verify it before using it as
a design fact.

## Separate facts from decisions

Obtain project facts directly, including framework, layering, existing
services, database, dependency management, response formats, error handling,
authorization, and similar features.

Ask the user only about choices whose answers materially change the solution,
such as:

- changing versus adding an interface;
- allowing a new dependency or database change;
- supporting old data or clients;
- failure, retry, or partial-success behavior;
- consistency guarantees and audit needs;
- synchronous versus asynchronous processing;
- performance, consistency, and complexity tradeoffs.

Recommend a choice based on verified project facts, then request confirmation.
