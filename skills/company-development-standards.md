# Company Development Standards

## MyBatis custom SQL

Apply to custom SQL in production DAO/Mapper code in company Java projects
using MyBatis. Establish company scope from the current task or project
guidance, and verify the module's framework or confirmed design choice;
Java alone does not establish MyBatis usage.

- Keep custom SQL in Mapper XML, not in SQL annotations on DAO/Mapper
  interfaces. Preserve method contracts and necessary annotations such as
  `@Param` and `@Mapper`.
- Follow the target module's established XML directory and naming conventions.
  Inspect relevant DAO/XML pairs and mapper loading configuration; do not
  impose another project's resource path.
- When relocating existing SQL, preserve its behavior, parameter binding,
  result mapping, and statement options. Check XML loading and
  namespace/statement IDs as well as affected behavior.

This is company policy, not a claim that MyBatis annotations are invalid.
Historical code is not an automatic exception. Surface material conflicts with
explicit user or project constraints through the invoking workflow's existing
conflict handling. Apply within the requested scope; do not expand into an
unrelated SQL migration. This bundled reference is read-only during project work.
