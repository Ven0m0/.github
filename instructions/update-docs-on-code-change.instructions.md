---
description: "Auto-update documentation when application code changes require doc updates"
applyTo: "**/*.{md,js,mjs,cjs,ts,tsx,jsx,py,java,cs,go,rb,php,rs,cpp,c,h,hpp}"
---

# Update Documentation on Code Change

<Goals>

Keep documentation synchronized with code. Detect when README.md, API docs, config guides, and other docs need updates based on code modifications.

</Goals>

## Trigger Conditions

Update docs when:

- New features or functionality added
- API endpoints, methods, or interfaces change
- Breaking changes introduced
- Dependencies or requirements change
- Configuration options or environment variables modified
- Installation or setup procedures change
- CLI commands or scripts updated
- Code examples in docs become outdated

## Update Rules

<Standards>

**README.md**: Update features section, installation steps, CLI docs, config examples when corresponding code changes.

**API Docs**: Sync endpoints (method, path, params, request/response), authentication changes, breaking changes with OpenAPI/Swagger specs.

**Code Examples**: Verify snippets still compile/run when function signatures change. Update imports and SDK usage.

**Config Docs**: Add new env vars to `.env.example`, document new options with defaults, mark deprecated options.

**Migration Guides**: Create for breaking API changes, major version updates, and feature deprecations. Include before/after examples and step-by-step instructions.

</Standards>

## Documentation Files

- `README.md` - Overview, quick start, basic usage
- `CHANGELOG.md` - Version history (Added, Changed, Fixed, Deprecated, Removed, Security)
- `docs/` - Detailed docs (installation, configuration, API, contributing, migration guides)
- `examples/` - Working code examples

<WhatToAdd>

When updating documentation:

1. Update in the same commit as code changes
2. Include before/after examples for changes
3. Test code examples before committing
4. Use consistent formatting and terminology
5. Provide migration paths for breaking changes
6. Keep docs DRY (link instead of duplicate)

</WhatToAdd>

<Limitations>

- No committing code changes without doc updates
- No outdated examples in documentation
- No documenting features that don't exist yet
- No vague or ambiguous language
- No broken links or failing examples
- No implementation details users don't need

</Limitations>
