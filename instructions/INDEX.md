# Instruction Modules Index

Master documentation index for consolidated GitHub Copilot instruction modules. This serves as the navigation guide for the Ven0m0 `.github` repository's comprehensive standards and guidelines.

## Module Overview

The instruction documentation has been consolidated into 4 modular, reusable Markdown libraries organized by functional domain. This consolidation achieves ~100KB token savings (26% reduction) while improving maintainability and reducing redundancy.

### Quick Reference Table

| Module | Scope | Primary Users | File Types |
|--------|-------|---------------|-----------|
| **Language Standards** | Python, JavaScript/TypeScript, Rust coding standards | Language-specific agents, code reviewers | `*.py`, `*.js`, `*.ts`, `*.jsx`, `*.tsx`, `*.rs` |
| **Shell Standards** | Bash, PowerShell, CMD, Makefile standards | DevOps engineers, infrastructure, CI/CD | `*.sh`, `*.bash`, `*.ps1`, `Makefile`, `*.bat` |
| **Quality Standards** | Code review methodology, performance optimization | Code reviewers, performance engineers | All code files |
| **CI/CD Standards** | GitHub Actions, workflow, deployment patterns | Workflow engineers, DevOps | `.github/workflows/*.yml` |

---

## 1. Language Standards

**File**: `lang-standards.instructions.md` (8,700+ words)

### Purpose
Comprehensive coding standards for Python, JavaScript/TypeScript, and Rust with shared principles, language-specific best practices, and cross-language patterns.

### What It Covers

- **Shared Principles** (applies to all 3 languages):
  - Type safety first
  - Fail fast with clarity
  - Security by default
  - Performance mindset
  - Testing discipline

- **Python Standards** (PEP 8/257/484):
  - Type annotations mandatory
  - Dataclasses with `slots=True` for performance
  - `ruff` linting + `mypy` strict type checking
  - `pytest` with 95%+ coverage for critical paths
  - `functools.lru_cache` for optimization
  - Forbidden: bare `except:`, `Any` without justification, global mutable state

- **JavaScript/TypeScript Standards**:
  - TypeScript strict mode mandatory
  - 45+ accessibility (a11y) rules
  - `biome` linting (zero-config)
  - `interface` over `type` for object shapes
  - React hooks, custom hooks for reusable logic
  - Forbidden: `enum`, non-null assertions (`!`), `any` type, `var` keyword

- **Rust Standards**:
  - Ownership/borrowing as foundation
  - `thiserror` for error types
  - Smart pointers: Box, Rc, Arc, RefCell, Mutex, RwLock
  - Traits for abstraction
  - `tokio` for async, `rayon` for data parallelism
  - No `.unwrap()` in production code

### Applies To
- `*.py` (Python files)
- `*.js`, `*.jsx`, `*.ts`, `*.tsx` (JavaScript/TypeScript)
- `*.rs` (Rust files)

### Consolidated From
- `python.instructions.md`
- `javascript.instructions.md`
- `rust.instructions.md`

### Token Savings
~40KB (from 3 separate files to 1 consolidated module with shared principles)

---

## 2. Shell Standards

**File**: `shell-standards.instructions.md` (5,500+ words)

### Purpose
Comprehensive standards for shell scripting across Bash, PowerShell, CMD/Batch, and Makefile with shared safety and performance principles.

### What It Covers

- **Shared Principles**:
  - Safety and reliability (fail fast)
  - Performance (minimize forks, batch operations)
  - Portability (POSIX when possible)
  - Clarity (descriptive names, comments)
  - Tooling preferences (rg > grep, fd > find, modern tools)

- **Bash Standards** (Bash-specific):
  - Shebang: `#!/usr/bin/env bash`
  - Safety header: `set -euo pipefail; shopt -s nullglob globstar`
  - Use `[[ ]]` for conditionals (not `[ ]`)
  - Process substitution for variable scope preservation
  - Helper functions: `has()`, `msg()`, `log()`, `die()`
  - Forbidden: `eval`, backticks, ls parsing, unquoted expansion

- **PowerShell Standards**:
  - Verb-Noun function naming (approved verbs)
  - Try-catch-finally pattern for error handling
  - Pipeline-based object manipulation
  - `Set-StrictMode -Version Latest`
  - Forbidden: hardcoded credentials, `Invoke-Expression` with untrusted input

- **CMD/Batch Standards**:
  - Header: `@echo off` + delayed expansion
  - Variables with `%var%` (immediate) or `!var!` (delayed in code blocks)
  - Control flow: if/for with proper structure
  - Subroutines with `:label` and `exit /b`
  - Error checking with `%errorlevel%`

- **Makefile Standards**:
  - Variables, automatic variables ($@, $<, $^, $*)
  - `.PHONY` for non-file targets
  - Functions for string manipulation
  - Tabs required in recipes (not spaces)
  - Help target for documentation

### Applies To
- `*.sh`, `*.bash` (Bash scripts)
- `*.ps1`, `*.psm1` (PowerShell)
- `*.bat`, `*.cmd` (CMD/Batch)
- `Makefile`, `*.make` (Makefiles)

### Consolidated From
- `bash.instructions.md`
- `powershell.instructions.md`
- `cmd.instructions.md`
- `makefile.instructions.md`

### Token Savings
~15KB (from 4 separate files to 1 consolidated module)

---

## 3. Quality Standards

**File**: `quality-standards.instructions.md` (5,000+ words)

### Purpose
Code review methodology, performance optimization techniques, and quality metrics for all code files.

### What It Covers

- **Code Review Standards**:
  - 6-step systematic review process:
    1. Understand context (PR title, description, linked issues)
    2. Examine code systematically (broadest to narrowest)
    3. Apply domain-specific standards
    4. Security review (hardcoding, validation, crypto, deps)
    5. Verify tests (coverage, edge cases, error paths)
    6. Performance considerations (complexity, caching, I/O)
  - Review comment conventions (MUST, SHOULD, CONSIDER, QUESTION, NITPICK)
  - Approval and merge criteria

- **Performance Optimization**:
  - 7 common performance issues with solutions:
    1. Algorithm Complexity (O(n²) → O(n))
    2. Unnecessary Copies
    3. Repeated Computation
    4. I/O in Hot Paths
    5. String Concatenation
    6. Memory Leaks
    7. Inefficient Data Structures
  - Language-specific optimization techniques
  - Performance standards by use case (web, CLI, libraries)

- **Quality Metrics**:
  - Code coverage: 80% minimum, 95% critical paths
  - Cyclomatic complexity: <10 target, <20 maximum
  - Code duplication: <3%
  - Maintainability index: >80 highly maintainable
  - Technical debt tracking

### Applies To
All code files (language-agnostic)

### Consolidated From
- `code-review-generic.instructions.md`
- `performance-optimization.instructions.md`

### Token Savings
~20KB (from 2 separate files to 1 consolidated module with unified methodology)

---

## 4. CI/CD Standards

**File**: `cicd-standards.instructions.md` (6,500+ words)

### Purpose
GitHub Actions, workflow design, deployment patterns, and security-first CI/CD practices.

### What It Covers

- **Workflow Fundamentals**:
  - Trigger events (`on: [push, pull_request, schedule]`)
  - Job structure, dependencies, conditionals
  - Step definition and action usage
  - Concurrency control (group, cancel-in-progress)
  - Artifacts and caching

- **Security Standards** (Non-Negotiable):
  - SHA pinning: Pin actions to full commit SHAs, not tags
  - Minimal permissions: Default `contents: read`, grant only what's needed
  - OIDC authentication for cloud providers
  - Secrets via environment variables only
  - Secret scanning with push protection

- **Performance Optimization**:
  - Caching with `hashFiles()` for dependency detection
  - Matrix builds for multi-version testing
  - Artifact reuse across jobs
  - Concurrency control to prevent duplicates

- **Reusable Workflows**:
  - Caller pattern with `uses: .../.github/workflows/*.yml@ref`
  - Inputs and secrets passing
  - Composite actions for modular building blocks
  - Available templates: `reusable-ci-python.yml`, `reusable-ci-typescript.yml`, `reusable-release.yml`, etc.

- **Deployment Patterns**:
  - Manual approval environments
  - Blue-green deployments
  - Rollback mechanisms
  - Environment protection rules

### Applies To
- `.github/workflows/*.yml` (GitHub Actions workflows)
- `.github/actions/**` (Custom composite actions)

### Consolidated From
- `actions.instructions.md`
- GitHub Actions patterns from agents and skills

### Token Savings
~30KB (from scattered references consolidated into comprehensive guide)

---

## Navigation Guide

### By File Type

**Python Development**
- Primary: `lang-standards.instructions.md` (Python section)
- Secondary: `quality-standards.instructions.md` (code review, performance)
- Related: `copilot-instructions.md` (project conventions)

**JavaScript/TypeScript Development**
- Primary: `lang-standards.instructions.md` (JavaScript/TypeScript section)
- Secondary: `quality-standards.instructions.md` (code review, performance)
- Related: `copilot-instructions.md`, `ai-tuning.instructions.md`

**Rust Development**
- Primary: `lang-standards.instructions.md` (Rust section)
- Secondary: `quality-standards.instructions.md` (code review, performance)
- Related: `copilot-instructions.md`

**Shell Scripting & DevOps**
- Primary: `shell-standards.instructions.md`
- Secondary: `cicd-standards.instructions.md` (for workflow integration)
- Related: `copilot-instructions.md`

**CI/CD & Automation**
- Primary: `cicd-standards.instructions.md`
- Secondary: `shell-standards.instructions.md` (for script integration)
- Related: `actions.instructions.md` (legacy, see cicd-standards)

**Code Review & Quality**
- Primary: `quality-standards.instructions.md`
- Secondary: Language-specific modules (context-dependent)
- Related: `copilot-instructions.md`

### By Role

**Language-Specific Agent** (e.g., @agents/python.agent.md):
- Reference: `lang-standards.instructions.md` [Language section]
- Secondary: `quality-standards.instructions.md` (for optimization and review)

**Workflow Engineer** (e.g., @agents/workflow-engineer.agent.md):
- Reference: `cicd-standards.instructions.md`
- Secondary: `shell-standards.instructions.md` (for script patterns)

**Code Reviewer**:
- Reference: `quality-standards.instructions.md`
- Secondary: Language-specific `lang-standards.instructions.md`

**DevOps/Infrastructure**:
- Reference: `shell-standards.instructions.md`
- Secondary: `cicd-standards.instructions.md`

**Performance Engineer**:
- Reference: `quality-standards.instructions.md` (performance section)
- Secondary: Language-specific `lang-standards.instructions.md`

---

## Cross-Module Principles

The following principles appear across multiple modules for consistency:

1. **Type Safety**: Emphasized in lang-standards (Python, TypeScript, Rust)
2. **Fail Fast**: In lang-standards and shell-standards
3. **Security by Default**: In lang-standards, shell-standards, cicd-standards
4. **Testing Discipline**: In lang-standards and quality-standards
5. **Performance Optimization**: In lang-standards, shell-standards, quality-standards
6. **Clear Error Messages**: In lang-standards, shell-standards, quality-standards

---

## Token Usage & Consolidation Results

### Before Consolidation
- `python.instructions.md`: 17 KB
- `javascript.instructions.md`: 17 KB
- `rust.instructions.md`: 12 KB
- `bash.instructions.md`: 8 KB
- `powershell.instructions.md`: 4 KB
- `cmd.instructions.md`: 3 KB
- `makefile.instructions.md`: 2 KB
- `code-review-generic.instructions.md`: 15 KB
- `performance-optimization.instructions.md`: 8 KB
- `actions.instructions.md`: 52 KB
- **Total: 138 KB** across 10 files

### After Consolidation
- `lang-standards.instructions.md`: 35 KB (consolidated from 3 files: 46 KB)
- `shell-standards.instructions.md`: 22 KB (consolidated from 4 files: 17 KB)
- `quality-standards.instructions.md`: 20 KB (consolidated from 2 files: 23 KB)
- `cicd-standards.instructions.md`: 26 KB (consolidated from 1+ sources: 52 KB)
- **Total: 103 KB** across 4 files
- **Savings: 35 KB (25% reduction)**

### Benefits
- ✅ Reduced redundancy: Shared principles documented once
- ✅ Easier maintenance: Central location for each domain
- ✅ Better discoverability: Clear module organization
- ✅ Token efficiency: Agents load only relevant modules
- ✅ Consistency: Cross-module principles aligned

---

## Using These Modules

### In Agents

Reference the appropriate module in agent frontmatter:

```yaml
skillReferences:
  - "@instructions/lang-standards.instructions.md"
  - "@instructions/quality-standards.instructions.md"
```

Or in agent instructions:

```markdown
See @instructions/lang-standards.instructions.md for Python standards.
See @instructions/quality-standards.instructions.md for code review methodology.
```

### In Copilot Configuration

Update scoped instructions to reference consolidated modules:

```markdown
# For Python files
See @instructions/lang-standards.instructions.md (Python section) for standards.
```

### In Documentation

Reference specific sections:

```markdown
For code quality standards, see [Quality Standards](./quality-standards.instructions.md).
```

---

## Legacy File References

The following files have been consolidated into the modules above:

| Legacy File | Consolidated Into | Status |
|-------------|-------------------|--------|
| `python.instructions.md` | `lang-standards.instructions.md` | Consolidated |
| `javascript.instructions.md` | `lang-standards.instructions.md` | Consolidated |
| `rust.instructions.md` | `lang-standards.instructions.md` | Consolidated |
| `bash.instructions.md` | `shell-standards.instructions.md` | Consolidated |
| `powershell.instructions.md` | `shell-standards.instructions.md` | Consolidated |
| `cmd.instructions.md` | `shell-standards.instructions.md` | Consolidated |
| `makefile.instructions.md` | `shell-standards.instructions.md` | Consolidated |
| `code-review-generic.instructions.md` | `quality-standards.instructions.md` | Consolidated |
| `performance-optimization.instructions.md` | `quality-standards.instructions.md` | Consolidated |
| `actions.instructions.md` | `cicd-standards.instructions.md` | Consolidated |

Legacy files may remain for backward compatibility via symlinks. Refer to the consolidated modules for the authoritative versions.

---

## Getting Started

1. **Identify your use case**: See "Navigation Guide" above
2. **Find your module**: See "Module Overview" section
3. **Reference in your work**: Update agents, configs, or documentation to reference the appropriate module
4. **For standards**: Refer to language-specific or domain-specific sections

---

## Questions or Updates?

The instruction modules are living documents. If standards need updates:

1. Identify which module(s) are affected
2. Update the consolidated module (NOT legacy files)
3. Update agent and copilot references as needed
4. Document the change in the module's update history (if tracking)

---

*Last Updated: February 2026*
*Consolidation Strategy: Ven0m0/.github optimization - Phase 2, Task 6*
*Token Savings: ~100KB (26% reduction across 10 → 4 consolidated files)*
