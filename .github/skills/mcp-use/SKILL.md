---
name: mcp-use
description: Proactively discover and use MCP servers and MCP tools before native CLI tools. Use when searching, reading, editing, refactoring, planning, or researching so Copilot gets higher-signal results with less context waste.
allowed-tools: "Read, Write, Edit, Glob, Grep"
---

# MCP Use

Use MCP servers and MCP tools first. Prefer MCP-native search, analysis, and editing over shell-builtins or generic CLI commands whenever an MCP tool can do the job more safely or precisely.

## When to Use

- Starting any non-trivial task
- Discovering available MCP servers and tools
- Searching code, symbols, files, or external docs
- Reading or editing files with precision
- Structural refactors and code rewrites
- Multi-step planning, debugging, or investigation
- Research that benefits from GitHub or web context

## MCP-First Rule

1. Check which MCP servers and tools are available.
2. Pick the most specific MCP tool for the task.
3. Fall back to native tools only when no MCP tool fits or when the MCP tool cannot complete the task.
4. Prefer structured MCP output over raw shell output to reduce noise and mistakes.

## Tool Selection

| Need | Prefer | Avoid when MCP covers it |
| --- | --- | --- |
| Structural code search | `ast-grep/find_code` | plain text `grep`/`rg` only |
| Structural refactor | `ast-grep/rewrite_code` | manual `sed`/search-replace |
| Static issue scan | `ast-grep/scan-code` | ad-hoc manual review |
| GitHub code research | `octocode/githubSearchCode` | broad web search or raw `gh search code` |
| Read repo files | `fast-filesystem/fast_read_file` | `cat`, `sed`, large raw reads |
| Write new files | `fast-filesystem/fast_write_file` | shell heredocs for tracked files |
| Precise edits | `fast-filesystem/fast_edit_block` | fragile manual replace |
| Batch file ops | `fast-filesystem/fast_batch_file_operations` | repeated `cp`/`mv`/`rm` commands |
| Complex reasoning | `sequential-thinking/sequentialthinking` | jumping straight into edits |
| Web research | `exa/web_search_advanced_exa` | generic search first |

## Workflows

### 1) Start by checking MCP options

- Before using Bash or native editor flows, look for a matching MCP tool.
- If a task combines search + edit + reasoning, keep each step MCP-first.
- Prefer the highest-signal tool, not the most familiar one.

### 2) Search semantically or structurally

- Use `ast-grep/find_code` for AST-aware code matches.
- Use `octocode/githubSearchCode` for cross-repo or GitHub-hosted code examples.
- Use `exa/web_search_advanced_exa` for current docs, release notes, and external references.

### 3) Read and edit with filesystem MCP tools

- Use `fast-filesystem/fast_read_file` to inspect exact file ranges.
- Use `fast-filesystem/fast_edit_block` for surgical replacements in existing files.
- Use `fast-filesystem/fast_write_file` for new files or full rewrites.
- Use `fast-filesystem/fast_batch_file_operations` for coordinated copy/move/delete work.

### 4) Refactor with AST-aware tooling

- Run `ast-grep/scan-code` before or after edits to catch common issues.
- Use `ast-grep/rewrite_code` for repetitive transformations across files.
- Prefer AST rewrites over regex replacements when syntax matters.

### 5) Think before acting on multi-step tasks

- Use `sequential-thinking/sequentialthinking` for planning, tradeoffs, or debugging with uncertainty.
- Use it before large edits, workflow redesigns, or cross-file migrations.

## Examples

### Example: inspect code patterns

Instead of:

```text
rg "TODO|FIXME" .
```

Prefer:

```text
ast-grep/find_code -> search for syntax-aware patterns in the target language
fast-filesystem/fast_read_file -> inspect only the matching file ranges
```

### Example: perform a safe refactor

Instead of:

```text
rg "oldFunction" . && sed -i ...
```

Prefer:

```text
ast-grep/find_code -> locate exact call sites
ast-grep/rewrite_code -> apply the structural replacement
ast-grep/scan-code -> check for follow-up issues
```

### Example: edit a tracked file

Instead of:

```text
cat file && python script.py && mv tmp file
```

Prefer:

```text
fast-filesystem/fast_read_file -> read the current content
fast-filesystem/fast_edit_block -> patch a precise block
fast-filesystem/fast_write_file -> write a new file when needed
```

### Example: research a library or pattern

Instead of:

```text
generic web search + manual browsing
```

Prefer:

```text
exa/web_search_advanced_exa -> find current docs/articles
octocode/githubSearchCode -> inspect real GitHub usage patterns
sequential-thinking/sequentialthinking -> compare options before implementation
```

### Example: coordinate multiple file operations

Instead of:

```text
cp file1 file2 && mv file3 dir/ && rm file4
```

Prefer:

```text
fast-filesystem/fast_batch_file_operations -> execute the full batch safely
```

## Decision Rule

If an MCP tool can search, read, reason, rewrite, or research more precisely than a native tool, use the MCP tool first.
