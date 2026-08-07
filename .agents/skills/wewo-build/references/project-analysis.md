# Project Analysis and Implementation Baseline

Use this guide before creating the implementation plan.

## Check task sufficiency

Confirm:

- the change to implement, modify, or fix;
- user- or caller-observable outcomes;
- mandatory business rules;
- explicit exclusions;
- authorization and security requirements;
- consistency requirements;
- permission to change interfaces, database, or dependencies;
- evidence that will establish completion.

Ask only for missing decisions that materially change implementation. Suggest
full requirement clarification only when the user wants it; never make another
skill a prerequisite.

## Analyze the actual project

Read relevant:

- repository instruction files;
- language, framework, package manager, and directory structure;
- layers, pages, components, modules, and services;
- public interfaces and data models;
- authentication and authorization;
- dependency injection and object lifetimes;
- persistence and transactions;
- errors, logs, cache, queues, schedules, and integrations;
- test framework, directories, fixtures, data setup, mocks, and fakes;
- lint, formatter, type-check, build, migration, and test commands;
- similar implementations;
- current Git repository, branch, and worktree state.

Do not invent project content or commands. Prefer existing architecture, test
seams, shared capability, response formats, and conventions.

## Protect user work

Inspect uncommitted changes before editing. Determine whether overlapping
changes belong to the user or current task. Preserve unrelated work and stop
when safe isolation is impossible.

Suggest a separate branch or worktree for broad, risky, or overlapping work.
Do not automatically commit, merge, or discard changes.

## Establish global implementation constraints

Derive applicable constraints:

- follow existing architecture and layers;
- reuse modules and shared capability;
- avoid unjustified patterns, singleton state, and global mutable state;
- keep user and request state out of shared objects;
- never hardcode secrets or environment configuration;
- enforce authorization at the server boundary;
- do not swallow exceptions;
- avoid unrelated changes;
- never change expectations or weaken assertions to pass tests;
- never add test-only behavior or hardcode responses for test inputs;
- require confirmation for new dependencies;
- preserve clear testing seams and project style.

## Summarize the baseline

Record what is in scope, what is excluded, required observable behavior,
technical constraints, source material, and unresolved blockers. Use verified
facts, not assumptions.
