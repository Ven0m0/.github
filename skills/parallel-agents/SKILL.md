---
name: parallel-agents
description: Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive analysis requires multiple perspectives.
---

# Native Parallel Agents

> Orchestration through Claude Code's built-in Agent Tool

## Overview

This skill enables coordinating multiple specialized agents through Claude Code's native agent system. Unlike external scripts, this approach keeps all orchestration within Claude's control.

## When to Use Orchestration

✅ **Good for:**

- Complex tasks requiring multiple expertise domains
- Code analysis from security, performance, and quality perspectives
- Comprehensive reviews (architecture + security + testing)
- Feature implementation needing backend + frontend + database work

❌ **Not for:**

- Simple, single-domain tasks
- Quick fixes or small changes
- Tasks where one agent suffices

---

## Native Agent Invocation

### Single Agent

```
Use the security-auditor agent to review authentication
```

### Sequential Chain

```
First, use the explorer-agent to discover project structure.
Then, use the backend-specialist to review API endpoints.
Finally, use the test-engineer to identify test gaps.
```

### With Context Passing

```
Use the frontend-specialist to analyze React components.
Based on those findings, have the test-engineer generate component tests.
```

### Resume Previous Work

```
Resume agent [agentId] and continue with additional requirements.
```

---

## Orchestration Patterns

### Pattern 1: Comprehensive Analysis

```
Agents: explorer-agent → [domain-agents] → synthesis

1. explorer-agent: Map codebase structure
2. security-auditor: Security posture
3. backend-specialist: API quality
4. frontend-specialist: UI/UX patterns
5. test-engineer: Test coverage
6. Synthesize all findings
```

### Pattern 2: Feature Review

```
Agents: affected-domain-agents → test-engineer

1. Identify affected domains (backend? frontend? both?)
2. Invoke relevant domain agents
3. test-engineer verifies changes
4. Synthesize recommendations
```

### Pattern 3: Security Audit

```
Agents: security-auditor → penetration-tester → synthesis

1. security-auditor: Configuration and code review
2. penetration-tester: Active vulnerability testing
3. Synthesize with prioritized remediation
```

---

## Available Agents

| Agent                    | Expertise          | Trigger Phrases                                         |
| ------------------------ | ------------------ | ------------------------------------------------------- |
| `orchestrator`           | Pipeline driver    | "comprehensive", "multi-phase", "end-to-end"            |
| `explorer`               | Discovery          | "explore", "map", "structure", "find files"             |
| `planner`                | Architecture/DAG   | "plan", "design", "roadmap", "wave"                     |
| `researcher`             | Deep investigation | "research", "investigate", "best practices"             |
| `coder`                  | Implementation     | "implement", "build", "code", "write"                   |
| `reviewer`               | Code/plan review   | "review", "audit", "check", "OWASP"                     |
| `frontend-specialist`    | UI/React/Next.js   | "React", "UI", "components", "Next.js", "CSS"           |
| `debug`                  | Bug fixing         | "bug", "error", "not working", "fix"                    |
| `workflow-engineer`      | GitHub Actions     | "CI/CD", "workflow", "actions", "deploy"                |
| `doc-writer`             | Documentation      | "write docs", "README", "API docs"                      |
| `codebase-maintainer`    | Cleanup/tech debt  | "cleanup", "refactor", "dead code", "tech debt"         |
| `git`                    | Version control    | "git", "branch", "PR", "commit"                         |
| `arch-linux-expert`      | Arch Linux         | "arch", "pacman", "systemd", "AUR"                      |
| `repo-architect`         | Repo structure     | "repo setup", "AI config", "AGENTS.md", "Copilot"      |
| `janitor`                | Dead code removal  | "janitor", "clean", "remove unused", "bloat"            |
| `swe`                    | General engineering | "senior engineer", "direct task", "implement for me"   |
| `qa`                     | Test planning      | "QA", "test plan", "bug hunt", "test coverage"          |

---

## Claude Code Built-in Agents

These work alongside custom agents:

| Agent               | Model  | Purpose                          |
| ------------------- | ------ | -------------------------------- |
| **Explore**         | Haiku  | Fast read-only codebase search   |
| **Plan**            | Sonnet | Research during plan mode        |
| **General-purpose** | Sonnet | Complex multi-step modifications |

Use **Explore** for quick searches, **custom agents** for domain expertise.

---

## Synthesis Protocol

After all agents complete, synthesize:

```markdown
## Orchestration Synthesis

### Task Summary

[What was accomplished]

### Agent Contributions

| Agent              | Finding      |
| ------------------ | ------------ |
| security-auditor   | Found X      |
| backend-specialist | Identified Y |

### Consolidated Recommendations

1. **Critical**: [Issue from Agent A]
2. **Important**: [Issue from Agent B]
3. **Nice-to-have**: [Enhancement from Agent C]

### Action Items

- [ ] Fix critical security issue
- [ ] Refactor API endpoint
- [ ] Add missing tests
```

---

## Best Practices

1. **Available agents** - 17 specialized agents can be orchestrated (see table above)
2. **Logical order** - Discovery → Analysis → Implementation → Testing
3. **Share context** - Pass relevant findings to subsequent agents
4. **Single synthesis** - One unified report, not separate outputs
5. **Verify changes** - Always include test-engineer for code modifications

---

## Key Benefits

- ✅ **Single session** - All agents share context
- ✅ **AI-controlled** - Claude orchestrates autonomously
- ✅ **Native integration** - Works with built-in Explore, Plan agents
- ✅ **Resume support** - Can continue previous agent work
- ✅ **Context passing** - Findings flow between agents
