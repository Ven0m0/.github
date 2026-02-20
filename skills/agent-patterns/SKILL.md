---
name: agent-patterns
description: Reusable workflow patterns, templates, and standards for agent development. Use when designing or reviewing agent workflows, writing structured plans, or enforcing consistent execution patterns across the agent system.
user-invocable: false
disable-model-invocation: false
allowed-tools: [Read, Glob, Grep]
---

# Agent Patterns

Reusable patterns and templates for creating consistent agents in the .github repository.

<workflow_patterns>

## Pattern 1: Analyze-Implement-Verify
**For**: Code optimization, refactoring, bug fixes

1. **Analyze**: Examine current state, identify issues
2. **Implement**: Apply fixes following standards
3. **Verify**: Run tests, ensure correctness

## Pattern 2: Discover-Generate-Validate
**For**: Documentation, configuration generation

1. **Discover**: Scan project, extract metadata
2. **Generate**: Create documentation or config
3. **Validate**: Verify accuracy and completeness

## Pattern 3: Understand-Strategize-Present
**For**: Planning, research, architecture

1. **Understand**: Gather requirements and context
2. **Strategize**: Design approach with trade-offs
3. **Present**: Document plan or findings

## Pattern 4: Research-Plan-Execute
**For**: Multi-phase comprehensive workflows

1. **Research**: Deep investigation and discovery
2. **Plan**: Detailed implementation strategy
3. **Execute**: Implementation with tests

</workflow_patterns>

<agent_template>

## Standard Agent Structure

```yaml
---
name: agent-name
description: 'Brief description of what this agent does and when to use it.'
model: claude-4-6-[sonnet|opus|haiku]-latest
tools: [list, of, tools]
---

# Agent Title

Brief purpose statement.

<instructions>

## Role
Primary responsibilities and expertise.

## Standards Reference
**Full standards**: `instructions/[domain].instructions.md`

## Workflow
1. **Step Name**: Description with reasoning
2. **Step Name**: Description with reasoning
3. **Step Name**: Description with reasoning

</instructions>

<constraints>
- What the agent must NOT do
- Boundaries and limitations
</constraints>

<examples>
### Scenario
Input -> Expected behavior -> Output
</examples>

## Triggers
**Labels**: `agent:name` - Description
**Commands**: `/agent run command` - Description
```

</agent_template>

<model_selection>

## Choose by Task Type

| Model | Temperature | Best For | Examples |
|-------|------------|----------|----------|
| Opus | 0.6-0.7 | Strategic planning, complex analysis, architecture | strategic-planner, critical-thinking, task-researcher |
| Sonnet | 0.3-0.4 | Code generation, optimization, bug fixes | language-optimizer, github-issue-fixer |
| Haiku | 0.3-0.4 | Fast operations, cleanup, simple transforms | codebase-maintainer |

</model_selection>

<tool_profiles>

## Common Tool Combinations

| Profile | Tools | Use For |
|---------|-------|---------|
| Analyzer | `codebase, semanticSearch, read, search, usages, problems` | Understanding code, finding issues |
| Executor | `codebase, read, edit, write, execute, search` | Modifying code, running commands |
| Researcher | `codebase, read, search, fetch, githubRepo` | Gathering info without modification |
| Documenter | `codebase, read, write, edit, search` | Creating/updating docs |
| Full-Stack | All tools | Comprehensive agents |

</tool_profiles>

<special_patterns>

## Read-Only Agent
For agents that analyze but never modify:
```markdown
## Role
[Analysis or research role]
**IMPORTANT**: This is a read-only agent. Never modify source code.

## Workflow
1. **Analyze**: [Description]
2. **Evaluate**: [Description]
3. **Report**: Document findings (no code edits)
```

## Language-Branching Agent
For agents supporting multiple languages:
```markdown
## Language Detection
Auto-detects from: file extensions, project files, explicit user request

## [Language 1] Workflow
1. Step 1 (language-specific)
2. Step 2 (language-specific)

## [Language 2] Workflow
1. Step 1 (language-specific)
2. Step 2 (language-specific)
```

## Success Criteria Pattern
```markdown
## Success Criteria
- All tests pass
- No lint warnings
- Performance baseline met
- Documentation updated
```

## Error Recovery Pattern
```markdown
## If [operation] fails:
1. Document the error and context
2. Attempt recovery: [steps]
3. If unrecoverable, notify user with details
```

</special_patterns>

<best_practices>

| Do | Don't |
|----|-------|
| Single responsibility per agent | Vague descriptions ("does things") |
| Reference instruction files | Include tools the agent doesn't need |
| Explicit step-by-step workflows | Ambiguous trigger conditions |
| Clear trigger labels/commands | Duplicate roles across agents |
| Match model to task complexity | Use Opus for simple cleanup tasks |
| XML tags for structured sections | Flat unstructured prose |
| Concrete examples with I/O | Abstract descriptions without examples |

</best_practices>

## Standards Reference

Common instruction files for agent references:
- `bash.instructions.md` - Shell scripts
- `python.instructions.md` - Python code
- `rust.instructions.md` - Rust code
- `javascript.instructions.md` - JS/TS code
- `ai-tuning.instructions.md` - AI configuration
- `quality-standards.instructions.md` - General quality
- `cicd-standards.instructions.md` - CI/CD workflows
- `meta-authoring.instructions.md` - Agents, skills, instructions, prompts
