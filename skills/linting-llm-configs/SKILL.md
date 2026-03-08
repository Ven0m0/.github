---
name: linting-llm-configs
description: "Lint, validate, format, and auto-fix LLM agent configuration files using claudelint and agnix. Use when validating CLAUDE.md, SKILL.md, AGENTS.md, hooks.json, settings.json, MCP configs, or any agent config file. Triggers on: lint, validate, format, check, fix, claudelint, agnix, CLAUDE.md, SKILL.md, AGENTS.md, copilot-instructions, .cursorrules, hooks.json, mcp.json, agent config, LLM config, skill structure, skill syntax, skill triggering, skill frontmatter, invalid config, broken config, agent file, optimize CLAUDE.md. Covers Claude Code, Cursor, Copilot, Kiro, Cline, Gemini CLI, OpenCode, AGENTS.md, MCP servers, and Agent Skills."
---

# linting-llm-configs

<overview>
Two complementary tools: claudelint (Claude Code-specific, deep validation + formatting) and agnix (multi-tool, 342 rules, broad coverage). Use claudelint for Claude Code projects, agnix for multi-tool stacks or when targeting non-CC tools.
</overview>

## Tool Coverage

```toon
tools[2]{name,install,scope,rules}:
  claudelint,npm install -g claude-code-lint,Claude Code only,CLAUDE.md+skills+settings+hooks+MCP+plugins
  agnix,npm install -g agnix,CC+Cursor+Copilot+Kiro+Cline+Gemini+AGENTS.md+MCP,342 rules

```

## Workflows

### Validate a Claude Code project (claudelint)

```bash
claudelint init          # creates .claudelintrc.json + .claudelintignore
claudelint check-all     # full project validation
claudelint check-all --fix       # auto-fix all fixable issues
claudelint check-all --strict    # zero-tolerance mode
```

Targeted validators:
```bash
claudelint validate-skills --path .
claudelint validate-hooks
claudelint validate-mcp
claudelint validate-settings
claudelint validate-cc-md
```

Format + optimize:
```bash
claudelint format --check     # dry-run formatting
claudelint format             # apply formatting
claudelint optimize-cc-md     # interactive CLAUDE.md optimization
```

### Validate any agent config (agnix)

```bash
agnix .                          # validate current dir
agnix --fix .                    # apply HIGH + MEDIUM confidence fixes
agnix --fix-safe .               # HIGH confidence fixes only
agnix --fix-unsafe .             # all fixes incl. LOW confidence
agnix --dry-run --show-fixes .   # preview diffs before applying
agnix --strict .                 # warnings become errors
agnix --target claude-code .     # CC-specific rule preset
agnix --target kiro .            # Kiro preset
```

### Decision: which tool for which file?

```toon
files[10]{file,claudelint,agnix}:
  CLAUDE.md,validate-cc-md,CC-* rules
  SKILL.md,validate-skills,AS-* + CC-SK-* rules
  settings.json,validate-settings,CC-* rules
  hooks.json,validate-hooks,CC-* rules
  *.mcp.json,validate-mcp,MCP-* rules
  plugin.json,validate-plugin,CC-* rules
  AGENTS.md,no,AGM-* + XP-* rules
  .github/copilot-instructions.md,no,COP-* rules
  .cursor/rules/*.mdc,no,CUR-* rules
  .kiro/skills/**/SKILL.md,no,KIRO-* + KR-SK-* rules

```

## Key Rules to Know

**SKILL.md (agnix AS-*/CC-SK-*)**: name must be lowercase-kebab, description max 1024 chars third-person, required frontmatter fields. Wrong syntax → skill invokes at 0% (per Vercel research on skill triggering).

**CLAUDE.md (claudelint)**: size limits, import syntax `@path/to/file`, circular reference detection, frontmatter schema.

**hooks.json**: valid event names (`PreToolUse`, `PostToolUse`, `Stop`, `Notification`), script existence, type field required.

**MCP servers**: transport type validation, URL format, required env vars.

## Install

```bash
# claudelint
npm install -g claude-code-lint
npx claudelint init

# agnix
npm install -g agnix
# or: brew tap agent-sh/agnix && brew install agnix
# or: cargo install agnix-cli
```

## GitHub Actions

```yaml
- uses: agent-sh/agnix@v0
  with:
    target: 'claude-code'
```

## References

- [claudelint rules + config](references/claudelint-rules.md)
- [agnix rules reference](references/agnix-rules.md)
