# Linting LLM Configs Validation Guide

## Table of Contents

- [Overview](#overview)
- [Workflows](#workflows)

---

## Overview

The **linting-llm-configs** skill covers both optimization and validation of AI agent configuration files. Its validation workflow ensures configs are syntactically correct, follow best practices, and remain optimized for LLM triggering and performance.

It leverages two core utilities:

- **claudelint**: A deep-validation tool specifically designed for the Claude Code ecosystem. It handles `CLAUDE.md`, skill structures, hooks, and MCP configurations.
- **agnix**: A broad-spectrum linter supporting multiple agent platforms including Cursor, Copilot, Kiro, Cline, and Gemini.

Using these tools helps prevent common issues such as non-triggering skills due to naming violations or inefficient context usage in configuration files.

---

## Workflows

### 1. Initializing and Validating a Claude Code Project

Use `claudelint` for projects primarily targeting Claude Code.

1.  **Installation**:
    Install the `claudelint` CLI as a uv tool:
    ```bash
    uv tool install claudelint
    ```
    Alternatively, install via npm:
    ```bash
bun install -g claude-code-lint
    ```

2.  **Initialization**:
    Run the `init` command to set up configuration files (`.claudelintrc.json` and `.claudelintignore`):
    ```bash
    claudelint init
    ```

3.  **Full Validation**:
    Run the check-all command to perform a comprehensive validation:
    ```bash
    claudelint check-all
    ```

4.  **Auto-fix Issues**:
    Automatically resolve safe issues using the `--fix` flag:
    ```bash
    claudelint check-all --fix
    ```

### 2. Multi-Platform Agent Validation

Use `agnix` for broad-spectrum agent configuration linting across multiple platforms like Cursor, Copilot, Cline, and Gemini.

1.  **Installation**:
    Install `agnix` globally:
    ```bash
    bun install -g agnix
    ```

2.  **Basic Linting**:
    Run `agnix` on your project directory to lint all supported agent configurations:
    ```bash
    agnix .
    ```

3.  **Targeted Linting**:
    Specify a target platform (e.g., Cursor, Copilot, Kiro) to focus linting rules:
    ```bash
    agnix --target kiro .
    ```

4.  **Safe Auto-fixing**:
    Automatically fix safe issues across your configuration files:
    ```bash
    agnix --fix-safe .
    ```

---
