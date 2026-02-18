---
name: agent-patterns
description: Reusable workflow patterns, templates, and standards for agent development. Use when designing or reviewing agent workflows, writing structured plans, or enforcing consistent execution patterns.
user-invocable: false
disable-model-invocation: false
allowed-tools: [Read, Glob, Grep]
---

# Agent Patterns Skill

Reusable patterns and templates for creating consistent, well-structured agents in the .github repository.

## Workflow Templates

Common workflow patterns used across multiple agents.

### Pattern 1: Analyze-Implement-Verify

**Used by**: Language optimizers, refactoring agents, code quality agents

**Structure**:
1. **Analyze**: Examine current state, identify issues
2. **Implement**: Apply fixes or improvements
3. **Verify**: Test changes, ensure correctness

**Example**:
```markdown
## Workflow

1. **Analyze**: Check problems tab, run linters, identify issues
2. **Implement**: Apply fixes following language standards
3. **Verify**: Run tests, ensure all checks pass
```

### Pattern 2: Discover-Generate-Validate

**Used by**: Documentation generators, configuration agents

**Structure**:
1. **Discover**: Scan project, extract metadata
2. **Generate**: Create documentation or configuration
3. **Validate**: Verify accuracy and completeness

**Example**:
```markdown
## Workflow

1. **Discover**: Analyze project structure and configuration
2. **Generate**: Create AGENTS.md with all required sections
3. **Validate**: Test commands, verify outputs
```

### Pattern 3: Understand-Strategize-Present

**Used by**: Planning agents, research agents

**Structure**:
1. **Understand**: Gather requirements and context
2. **Strategize**: Design approach and architecture
3. **Present**: Document plan or findings

**Example**:
```markdown
## Workflow

1. **Understand**: Analyze requirements and constraints
2. **Strategize**: Design architecture and implementation approach
3. **Present**: Document strategic plan with trade-offs
```

### Pattern 4: Research-Plan-Execute

**Used by**: Multi-phase agents, comprehensive workflows

**Structure**:
1. **Research**: Deep investigation and discovery
2. **Plan**: Strategic planning based on research
3. **Execute**: Implementation following plan

**Example**:
```markdown
## Workflow

1. **Research**: Investigate existing patterns and requirements
2. **Plan**: Create detailed implementation strategy
3. **Execute**: Implement changes with tests
```

## Agent Structure Template

Standard agent file structure:

```yaml
---
name: agent-name
description: 'Brief description. See instructions/[file].instructions.md.'
model: claude-4-6-[sonnet|opus|haiku]-latest
tools: [list, of, tools]
---

# Agent Title

Brief agent purpose statement.

## Role

Primary responsibilities and expertise.

## Standards Reference

**Full standards**: `instructions/[domain].instructions.md`

## Workflow

1. **Step Name**: Description
2. **Step Name**: Description
3. **Step Name**: Description

## Triggers

**GitHub Labels**:
- `agent:name` - Description

**Commands**:
- `/agent run command` - Description
```

## Model Selection Guidelines

Choose the appropriate Claude model based on agent purpose:

### Opus (claude-4-6-opus-latest)
**Use for**: Strategic planning, complex analysis, critical thinking

**Characteristics**:
- Temperature: 0.6-0.7 (creative, exploratory)
- Best for: Architecture decisions, trade-off analysis, deep research
- Examples: strategic-planner.agent.md, critical-thinking.agent.md, task-researcher.agent.md

### Sonnet (claude-4-6-sonnet-latest)
**Use for**: Code implementation, optimization, refactoring

**Characteristics**:
- Temperature: 0.3-0.4 (focused, consistent)
- Best for: Code generation, bug fixes, safe refactoring
- Examples: language-optimizer.agent.md, github-issue-fixer.agent.md, refactoring-expert.agent.md

### Haiku (claude-4-6-haiku-latest)
**Use for**: Fast, lightweight operations

**Characteristics**:
- Temperature: 0.3-0.4 (focused, efficient)
- Best for: Cleanup, indexing, simple transformations
- Examples: janitor.agent.md, repo-index.agent.md

## Tool Profile Templates

Common tool combinations by agent type:

### Code Analyzer Profile
```yaml
tools: [codebase, semanticSearch, read, search, usages, problems]
```

**Use for**: Agents that need to understand code structure and identify issues.

### Code Executor Profile
```yaml
tools: [codebase, read, edit, write, execute, search]
```

**Use for**: Agents that modify code and run commands.

### Researcher Profile
```yaml
tools: [codebase, read, search, fetch, githubRepo]
```

**Use for**: Agents that gather information without modifying code.

### Documentation Profile
```yaml
tools: [codebase, read, write, edit, search]
```

**Use for**: Agents that create or update documentation.

### Full-Stack Profile
```yaml
tools: [codebase, semanticSearch, read, write, edit, search, execute, usages, changes, problems, fetch, github, githubRepo]
```

**Use for**: Comprehensive agents that need all capabilities.

## Trigger Patterns

Standard trigger formats:

### GitHub Labels
```markdown
- `agent:name` - Primary agent trigger
- `agent:name:variant` - Variant-specific trigger
```

### Commands
```markdown
- `/agent run command` - Basic command
- `/agent run command arg1 arg2` - Command with arguments
```

### Context Triggers
```markdown
- Use when: [specific scenarios]
- Don't use when: [inappropriate scenarios]
```

## Standards Reference Pattern

All agents should reference appropriate instruction files:

```markdown
## Standards Reference

**Full standards**: `instructions/[domain].instructions.md`
```

Common instruction files:
- `bash.instructions.md` - Bash/shell scripts
- `python.instructions.md` - Python code
- `rust.instructions.md` - Rust code
- `javascript.instructions.md` - JS/TS code
- `ai-tuning.instructions.md` - AI configuration
- `quality-standards.instructions.md` - General quality
- `cicd-standards.instructions.md` - CI/CD workflows

## Read-Only Agent Pattern

For agents that analyze but don't modify:

```markdown
## Role

[Analysis or research role]

**IMPORTANT**: This is a read-only agent. Never modify source code.

## Workflow

1. **[Analysis Step]**: [Description]
2. **[Evaluation Step]**: [Description]
3. **[Presentation Step]**: Document findings

**No code edits**: This agent only analyzes and reports.
```

**Examples**: critical-thinking.agent.md, task-researcher.agent.md

## Language-Branching Pattern

For agents that support multiple languages:

```markdown
## Language Detection

Auto-detects language from:
- **File extensions**: `*.ext1`, `*.ext2`
- **Project files**: config files
- **Explicit request**: User specifies language

## [Language 1] Workflow

1. **Step 1**: Description
2. **Step 2**: Description

## [Language 2] Workflow

1. **Step 1**: Description
2. **Step 2**: Description
```

**Examples**: language-optimizer.agent.md, mcp-expert.agent.md

## Success Criteria Pattern

Define clear success criteria:

```markdown
## Success Criteria

[Task] is successful when:
- ✅ [Criterion 1]
- ✅ [Criterion 2]
- ✅ [Criterion 3]
- ✅ [Criterion 4]
```

## Error Handling Pattern

For agents with failure modes:

```markdown
## Failure Handling

If [scenario] fails:
1. **Document issues**: [What to document]
2. **Notify user**: [How to notify]
3. **Recovery**: [How to recover]
```

## Best Practices

1. **Single Responsibility**: Each agent has one clear purpose
2. **Standards Reference**: All agents point to instruction files
3. **Workflow Documentation**: Explicit step-by-step processes
4. **Trigger Clarity**: Clear labels and commands
5. **Model Appropriateness**: Choose model based on task complexity
6. **Tool Minimalism**: Only include tools the agent needs
7. **Description Clarity**: Clear, concise descriptions in frontmatter
8. **Formatting Consistency**: Follow standard template structure

## Anti-Patterns

Avoid these common mistakes:

1. **Vague descriptions**: "Does things" vs "Optimizes Python code for type safety and performance"
2. **Tool bloat**: Including all tools when only a few are needed
3. **Missing standards**: Not referencing instruction files
4. **Unclear triggers**: Missing or ambiguous activation conditions
5. **Inconsistent naming**: Using different formats for similar agents
6. **Duplicate roles**: Multiple agents with overlapping purposes

## Migration Guide

When consolidating agents:

1. **Document replacements**: List replaced agents
2. **Explain benefits**: Why consolidation improves system
3. **Preserve functionality**: Ensure all features retained
4. **Update references**: Fix any references to old agents

## Examples

See these agents for pattern examples:
- `language-optimizer.agent.md` - Language-branching pattern
- `mcp-expert.agent.md` - Multi-language support
- `multi-agent-workflow.agent.md` - Orchestration pattern
- `critical-thinking.agent.md` - Read-only pattern
- `github-issue-fixer.agent.md` - Full-stack executor pattern
