# Agent Chain Refactor Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactor 20 flat agents into a 5-phase chained workflow (explorer -> planner -> researcher -> coder -> reviewer) with orchestrator, plus cleanup of instructions, skills, and prompts.

**Architecture:** Orchestrator-driven pipeline with structured artifact files in `.workflow/{task-id}/`. Configurable auto/gated modes. 14 agents total (6 phase + 8 supporting), down from 20.

**Tech Stack:** Markdown agent definitions with YAML frontmatter, MCP server configs (context7, serena, exa, sequential-thinking, ref-tools, grep-app)

**Spec:** `docs/superpowers/specs/2026-03-17-agent-chain-refactor-design.md`

---

### Task 0: Create Feature Branch

- [ ] **Step 1: Create and switch to feature branch**

```bash
git checkout -b feature/agent-chain-refactor
```

---

### Task 1: Instructions Cleanup

**Files:**
- Modify: `instructions/javascript.instructions.md`
- Delete: `instructions/typescript.instructions.md`
- Delete: `instructions/instructions.instructions.md`
- Modify: `instructions/INDEX.md`

- [ ] **Step 1: Read both JS and TS instruction files to understand merge points**

Already read. JS file at `instructions/javascript.instructions.md` (62 lines) is the comprehensive one with types, patterns, accessibility, limitations, security. TS file at `instructions/typescript.instructions.md` (43 lines) adds naming conventions, function rules, error handling, import order. Merge TS-unique content into JS file.

- [ ] **Step 2: Merge TypeScript-unique content into JavaScript instructions**

Add to `instructions/javascript.instructions.md`:
- Update `applyTo` to include both patterns: `'**/*.{js,jsx,ts,tsx,mjs}'` (already covers both)
- Add naming conventions section from TS file (camelCase, PascalCase, SCREAMING_SNAKE_CASE, boolean naming)
- Add function rules (max 20 lines, max 3 args, single responsibility)
- Add error handling section (try/catch async, meaningful messages)
- Keep existing import order (already better than TS version)

```markdown
## Naming Conventions

- **Variables/Functions**: camelCase (`getUserById`, `isActive`)
- **Classes/Interfaces/Types**: PascalCase (`UserService`, `AuthConfig`)
- **Constants**: SCREAMING_SNAKE_CASE (`MAX_RETRIES`, `API_BASE_URL`)
- **Booleans**: question form (`isActive`, `hasPermission`, `canEdit`)

## Function Rules

- Maximum 20 lines per function (ideally 5-10)
- Maximum 3 arguments (prefer 0-2)
- Single responsibility - one function = one job
- No unexpected side effects

## Error Handling

- Always use try/catch for async operations
- Provide meaningful error messages with context
- Never swallow errors silently
```

Insert after the `## Patterns` section, before `<Limitations>`.

- [ ] **Step 3: Delete typescript.instructions.md**

```bash
git rm instructions/typescript.instructions.md
```

- [ ] **Step 4: Delete instructions.instructions.md**

Content is covered by `meta-authoring.instructions.md`.

```bash
git rm instructions/instructions.instructions.md
```

- [ ] **Step 5: Update INDEX.md - remove dead references and reflect changes**

Remove these rows from the Language Standards table (files don't exist):
- csharp, swift, ruby, php, scala, elixir, r

Remove the `typescript` row. Update the `javascript` row description to "JavaScript/TypeScript standards".

In the "Navigation by File Type" table:
- Remove TypeScript separate row, update JS row to "JS/TS"
- Remove rows for csharp, swift, ruby, php, scala, elixir, r

- [ ] **Step 6: Commit**

```bash
git add instructions/javascript.instructions.md instructions/INDEX.md
git add -u instructions/typescript.instructions.md instructions/instructions.instructions.md
git commit -m "refactor(instructions): merge JS/TS, remove dead refs and meta-authoring duplicate"
```

---

### Task 2: Skills Cleanup

**Files:**
- Modify: `skills/docs-writer/SKILL.md`
- Delete: `skills/documentation-templates/` (entire directory)
- Create: `skills/web-search/SKILL.md`
- Delete: `skills/personal-site-search/` (entire directory)
- Delete: `skills/research-paper-search/` (entire directory)
- Delete: `skills/x-search/` (entire directory)
- Delete: `skills/Unified-search-discover/` (entire directory)

- [ ] **Step 1: Merge documentation-templates content into docs-writer**

Append the templates from `skills/documentation-templates/SKILL.md` (README, API docs, code comments, changelog, ADR, AI-friendly docs) to the end of `skills/docs-writer/SKILL.md` as a new `## Templates` section.

```markdown
## Templates

### README Structure

| Section | Purpose |
|---------|---------|
| **Title + One-liner** | What is this? |
| **Quick Start** | Running in <5 min |
| **Features** | What can I do? |
| **Configuration** | How to customize |
| **API Reference** | Link to detailed docs |
| **Contributing** | How to help |
| **License** | Legal |

### API Documentation (Per-Endpoint)

```
## GET /users/:id
Get a user by ID.
**Parameters:** | Name | Type | Required | Description |
**Response:** 200: User object, 404: User not found
**Example:** [Request and response]
```

### Code Comment Guidelines

| Comment | Don't Comment |
|---------|--------------|
| Why (business logic) | What (obvious) |
| Complex algorithms | Every line |
| Non-obvious behavior | Self-explanatory code |
| API contracts | Implementation details |

### Changelog (Keep a Changelog format)

Categories: Added, Changed, Fixed, Deprecated, Removed, Security

### Architecture Decision Record (ADR)

Sections: Status, Context, Decision, Consequences

### AI-Friendly Documentation

- Clear H1-H3 hierarchy for RAG indexing
- JSON/YAML examples for data structures
- Self-contained sections
```

- [ ] **Step 2: Delete documentation-templates directory**

```bash
git rm -r skills/documentation-templates/
```

- [ ] **Step 3: Create unified web-search skill**

Create `skills/web-search/SKILL.md` combining the three Exa search skills (personal-site, research-paper, tweet) into one skill with category sections:

```yaml
---
name: web-search
description: Search web content using Exa advanced search across categories - personal sites/blogs, research papers, and tweets/X. Use when searching for web content, academic papers, blog posts, or social media discussions.
context: fork
---
```

Body: tool restriction (use `web_search_advanced_exa` only), token isolation rule, then three sections:
- `## Personal Sites & Blogs` - category: "personal site", full filter support, examples
- `## Research Papers` - category: "research paper", full filter support, academic sources
- `## Tweets & X Content` - category: "tweet", limited filter support (no text/domain filters), examples

Each section: when to use, supported params, example query, output format.

- [ ] **Step 4: Delete the three individual search skill directories**

```bash
git rm -r skills/personal-site-search/
git rm -r skills/research-paper-search/
git rm -r skills/x-search/
```

- [ ] **Step 5: Delete Unified-search-discover directory**

Covered by explorer agent + tool preferences in CLAUDE.md.

```bash
git rm -r skills/Unified-search-discover/
```

- [ ] **Step 6: Commit**

```bash
git add skills/docs-writer/SKILL.md skills/web-search/SKILL.md
git add -u skills/documentation-templates/ skills/personal-site-search/ skills/research-paper-search/ skills/x-search/ skills/Unified-search-discover/
git commit -m "refactor(skills): merge doc templates into docs-writer, consolidate search skills, remove unified-search"
```

---

### Task 3: Prompts Restructure

**Files:**
- Create: `prompts/templates/` directory
- Create: `prompts/templates/feature-request.md`
- Create: `prompts/templates/implementation-plan.md`
- Create: `prompts/templates/maintenance-task.md`
- Create: `prompts/templates/context-map.md`
- Delete: `prompts/develop-feature.prompt.md`
- Delete: `prompts/create-implementation-plan.prompt.md`
- Delete: `prompts/maint.prompt.md`
- Delete: `prompts/context-map.prompt.md`
- Delete: `prompts/optimize-llm-config.prompt.md`
- Delete: `prompts/cleanup.prompt.md`

- [ ] **Step 1: Create prompts/templates directory**

```bash
mkdir -p prompts/templates
```

- [ ] **Step 2: Create feature-request.md template**

Convert `develop-feature.prompt.md` into an orchestrator input template. Strip the multi-chat workflow mechanics (orchestrator handles that now). Keep the structured input format.

```markdown
---
description: Orchestrator input template for feature development tasks
template-for: orchestrator
---

# Feature Request

## Task Description

{{task_description}}

## Requirements

- [ ] {{requirement_1}}
- [ ] {{requirement_2}}

## Constraints

- Target languages/frameworks: {{languages}}
- Must integrate with: {{existing_systems}}
- Performance requirements: {{performance}}

## Acceptance Criteria

- [ ] {{criterion_1}}
- [ ] {{criterion_2}}

## Additional Context

{{context}}
```

- [ ] **Step 3: Create implementation-plan.md template**

Convert `create-implementation-plan.prompt.md`. Keep the structured phase/task format, remove the Copilot-specific tool references.

```markdown
---
description: Orchestrator input template for implementation planning tasks
template-for: orchestrator
---

# Implementation Plan Request

## Goal

{{goal}}

## Scope

- Purpose: {{upgrade|refactor|feature|infrastructure|architecture}}
- Components affected: {{components}}
- Estimated complexity: {{low|medium|high}}

## Requirements

- **REQ-001**: {{functional_requirement}}
- **SEC-001**: {{security_requirement}}
- **CON-001**: {{constraint}}

## Existing Context

- Relevant files: {{file_paths}}
- Existing patterns to follow: {{patterns}}
- Dependencies: {{dependencies}}
```

- [ ] **Step 4: Create maintenance-task.md template**

Convert `maint.prompt.md`. Keep the phased analysis approach, strip multi-chat mechanics.

```markdown
---
description: Orchestrator input template for code maintenance and cleanup tasks
template-for: orchestrator
---

# Maintenance Task

## Task Description

{{task_description}}

## Scope

- Directories to analyze: {{directories}}
- Languages: {{languages}}
- Focus areas: {{dead_code|unused_imports|tech_debt|dependencies|all}}

## Safety Constraints

- Files/patterns to never modify: {{protected_patterns}}
- Require confirmation before: {{deletion|refactoring|dependency_changes}}

## Expected Outcomes

- [ ] {{outcome_1}}
- [ ] {{outcome_2}}
```

- [ ] **Step 5: Create context-map.md template**

Convert `context-map.prompt.md` directly - it's already a clean template.

```markdown
---
description: Orchestrator input template for generating context maps before implementation
template-for: orchestrator
---

# Context Map Request

## Task

{{task_description}}

## Output Format

### Files to Modify
| File | Purpose | Changes Needed |
|------|---------|----------------|

### Dependencies (may need updates)
| File | Relationship |
|------|--------------|

### Test Files
| Test | Coverage |
|------|----------|

### Reference Patterns
| File | Pattern |
|------|---------|

### Risk Assessment
- [ ] Breaking changes to public API
- [ ] Database migrations needed
- [ ] Configuration changes required
```

- [ ] **Step 6: Delete converted and redundant prompts**

```bash
git rm prompts/develop-feature.prompt.md
git rm prompts/create-implementation-plan.prompt.md
git rm prompts/maint.prompt.md
git rm prompts/context-map.prompt.md
git rm prompts/optimize-llm-config.prompt.md
git rm prompts/cleanup.prompt.md
```

- [ ] **Step 7: Commit**

```bash
git add prompts/templates/
git add -u prompts/
git commit -m "refactor(prompts): convert 4 prompts to orchestrator templates, remove 2 redundant prompts"
```

---

### Task 4: Create Explorer Agent

**Files:**
- Create: `agents/explorer.agent.md`

- [ ] **Step 1: Write explorer.agent.md**

Combines capabilities from `repo-index.agent.md` (fast codebase scanning, PROJECT_INDEX generation) and exploration parts of `strategic-planner.agent.md` (codebase structure analysis, pattern identification).

```yaml
---
name: explorer
description: 'Fast codebase exploration and mapping. Scans structure, identifies patterns, surfaces relevant files and risks for downstream agents.'
model: claude-haiku-4-5
modelParameters:
  temperature: 0.25
mcp-servers:
  context7:
    type: http
    url: "https://mcp.context7.com/mcp"
    headers: {CONTEXT7_API_KEY: "${{ secrets.COPILOT_MCP_CONTEXT7_API_KEY }}"}
    tools: ["get-library-docs", "resolve-library-id"]
  serena:
    type: local
    command: uvx
    args: ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server", "--context", "ide", "--project-from-cwd"]
    tools: ["*"]
---
```

Body sections:
- `## Role`: Fast codebase scout. Produces exploration artifact for the planner.
- `## Standards Reference`: `instructions/quality-standards.instructions.md`, `instructions/file-reading-optimization.instructions.md`
- `## Workflow`: 1) Scan directory structure 2) Identify entry points, service boundaries 3) Surface recently changed/high-risk files 4) Map relevant files to task 5) Identify patterns and conventions 6) Assess risks
- `## Artifact Output`: Write to `.workflow/{task-id}/01-exploration.md` with standard frontmatter. Sections: `## Codebase Map`, `## Relevant Files`, `## Patterns Found`, `## Risks`. Target: under 300 lines.
- `## Artifact Frontmatter`: Standard template with task, phase, status, timestamp, agent, model fields
- `## Operating Rules`: Keep responses data-driven and compact. Use rg/fd for discovery. Don't read entire files unless necessary. Focus on what's relevant to the task.

- [ ] **Step 2: Commit**

```bash
git add agents/explorer.agent.md
git commit -m "feat(agents): add explorer phase agent for codebase scanning"
```

---

### Task 5: Create Planner Agent

**Files:**
- Create: `agents/planner.agent.md`

- [ ] **Step 1: Write planner.agent.md**

Absorbs `strategic-planner.agent.md` planning capabilities (PRD, strategic plan, implementation plan levels) and the planning coordination from `multi-agent-workflow.agent.md`.

```yaml
---
name: planner
description: 'Architecture design and implementation planning. Creates requirements, task breakdowns, and dependency maps from exploration artifacts.'
model: claude-opus-4-6
mcp-servers:
  context7:
    type: http
    url: "https://mcp.context7.com/mcp"
    headers: {CONTEXT7_API_KEY: "${{ secrets.COPILOT_MCP_CONTEXT7_API_KEY }}"}
    tools: ["get-library-docs", "resolve-library-id"]
  serena:
    type: local
    command: uvx
    args: ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server", "--context", "ide", "--project-from-cwd"]
    tools: ["*"]
  sequential-thinking:
    type: stdio
    command: npx
    args: ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    tools: ["*"]
---
```

Body sections:
- `## Role`: Senior architect. Reads exploration artifact, designs architecture, creates actionable task breakdown.
- `## Standards Reference`: `skills/prd/SKILL.md`, `skills/agent-patterns/SKILL.md`, `instructions/quality-standards.instructions.md`
- `## Input`: Reads `.workflow/{task-id}/01-exploration.md` + original task description
- `## Workflow`: 1) Analyze exploration findings 2) Clarify requirements from codebase context 3) Design architecture approach 4) Break down into atomic tasks with file paths 5) Identify dependencies and risks 6) Define testing strategy
- `## Artifact Output`: Write to `.workflow/{task-id}/02-plan.md`. Sections: `## Requirements`, `## Architecture`, `## Task Breakdown`, `## Dependencies`. Target: under 500 lines.
- `## Planning Principles`: Architecture first, follow existing patterns, plan for maintenance, explain reasoning. Use standardized prefixes (REQ-, TASK-, DEP-, TEST-, RISK-).
- `## Rules`: Do NOT make code edits - only generate plans. All tasks include specific file paths. Measurable success criteria for each task.

- [ ] **Step 2: Commit**

```bash
git add agents/planner.agent.md
git commit -m "feat(agents): add planner phase agent for architecture and task breakdown"
```

---

### Task 6: Create Researcher Agent

**Files:**
- Create: `agents/researcher.agent.md`

- [ ] **Step 1: Write researcher.agent.md**

Combines `task-researcher.agent.md` (deep analysis, external research, findings synthesis) and `context7.agent.md` (library documentation, version checking, best practices).

```yaml
---
name: researcher
description: 'Deep research specialist. Investigates libraries, patterns, and external docs. Provides verified findings and best practices for implementation.'
model: claude-opus-4-6
mcp-servers:
  context7:
    type: http
    url: "https://mcp.context7.com/mcp"
    headers: {CONTEXT7_API_KEY: "${{ secrets.COPILOT_MCP_CONTEXT7_API_KEY }}"}
    tools: ["get-library-docs", "resolve-library-id"]
  exa:
    type: http
    url: "https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,get_code_context_exa,crawling_exa"
    headers: {EXA_API_KEY: "${{ secrets.COPILOT_MCP_EXA_API_KEY }}"}
    tools: ["*"]
  ref-tools:
    type: http
    url: "https://api.ref.tools/mcp"
    headers: {x-ref-api-key: "${{ secrets.COPILOT_MCP_REF_API_KEY }}"}
    tools: ["*"]
  grep-app:
    type: http
    url: "https://mcp.grep.app"
    tools: ["*"]
---
```

Body sections:
- `## Role`: Research specialist. Reads plan artifact, investigates libraries/frameworks/patterns, provides verified findings.
- `## Core Rules`: 1) Document ONLY verified findings 2) Cross-reference across sources 3) Guide toward one optimal approach 4) Use Context7 for ALL library questions (resolve-library-id -> get-library-docs -> answer)
- `## Input`: Reads `.workflow/{task-id}/02-plan.md` + exploration artifact
- `## Workflow`: 1) Identify research needs from plan 2) Investigate libraries via Context7 3) Search for patterns via Exa/grep-app 4) Check official docs via ref-tools 5) Evaluate approaches with evidence 6) Synthesize findings
- `## Artifact Output`: Write to `.workflow/{task-id}/03-research.md`. Sections: `## Findings`, `## Best Practices`, `## Library Recommendations`, `## Constraints`. Target: under 400 lines.
- `## Research Tools`: Context7 (library docs, version info), Exa (web search, code context), ref-tools (official docs), grep-app (GitHub code patterns)
- `## Quality Standards`: Verified across multiple sources, latest versions identified, actionable details for project context

- [ ] **Step 2: Commit**

```bash
git add agents/researcher.agent.md
git commit -m "feat(agents): add researcher phase agent for library and pattern investigation"
```

---

### Task 7: Create Coder Agent

**Files:**
- Create: `agents/coder.agent.md`

- [ ] **Step 1: Write coder.agent.md**

Absorbs `language-optimizer.agent.md` (multi-language optimization, safety, TDD) and `github-issue-fixer.agent.md` (implementation workflow, testing, minimal changes).

```yaml
---
name: coder
description: 'Implementation specialist. Writes code following plan and research artifacts. Multi-language, TDD-driven, minimal focused changes.'
model: claude-sonnet-4-6
modelParameters:
  temperature: 0.35
mcp-servers:
  context7:
    type: http
    url: "https://mcp.context7.com/mcp"
    headers: {CONTEXT7_API_KEY: "${{ secrets.COPILOT_MCP_CONTEXT7_API_KEY }}"}
    tools: ["get-library-docs", "resolve-library-id"]
  serena:
    type: local
    command: uvx
    args: ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server", "--context", "ide", "--project-from-cwd"]
    tools: ["*"]
  exa:
    type: http
    url: "https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,get_code_context_exa,crawling_exa"
    headers: {EXA_API_KEY: "${{ secrets.COPILOT_MCP_EXA_API_KEY }}"}
    tools: ["*"]
---
```

Body sections:
- `## Role`: Implementation engineer. Reads plan + research artifacts, implements changes with tests.
- `## Standards Reference`: Language-specific instructions (auto-detect from file extensions), `instructions/quality-standards.instructions.md`, `skills/language-optimization/SKILL.md`
- `## Input`: Reads `.workflow/{task-id}/02-plan.md` + `.workflow/{task-id}/03-research.md`
- `## Workflow`: 1) Review plan task breakdown 2) For each task: write failing test -> implement -> verify green 3) Follow existing code patterns 4) Run linters and tests 5) Document changes
- `## Language Detection`: Auto-detect from file extensions. Apply corresponding instruction file.
- `## Artifact Output`: Write to `.workflow/{task-id}/04-implementation.md`. Sections: `## Changes Made`, `## Files Modified`, `## Tests Added`, `## Remaining TODOs`. Target: under 200 lines.
- `## Rules`: Minimal focused changes. Never refactor unrelated code. Always add/update tests. Follow existing conventions. Confirm plan before major deviations.

- [ ] **Step 2: Commit**

```bash
git add agents/coder.agent.md
git commit -m "feat(agents): add coder phase agent for TDD-driven implementation"
```

---

### Task 8: Create Reviewer Agent

**Files:**
- Create: `agents/reviewer.agent.md`

- [ ] **Step 1: Write reviewer.agent.md**

Combines `critical-thinking.agent.md` (assumption challenging, root cause analysis, devil's advocate) and `app-optimizer.agent.md` (code cleanup review, architecture review, performance analysis).

```yaml
---
name: reviewer
description: 'Critical review specialist. Challenges assumptions, checks quality, security, and architecture. Returns pass/fail/conditional verdict.'
model: claude-opus-4-6
mcp-servers:
  context7:
    type: http
    url: "https://mcp.context7.com/mcp"
    headers: {CONTEXT7_API_KEY: "${{ secrets.COPILOT_MCP_CONTEXT7_API_KEY }}"}
    tools: ["get-library-docs", "resolve-library-id"]
  serena:
    type: local
    command: uvx
    args: ["--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server", "--context", "ide", "--project-from-cwd"]
    tools: ["*"]
  sequential-thinking:
    type: stdio
    command: npx
    args: ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    tools: ["*"]
---
```

Body sections:
- `## Role`: Senior reviewer. Reads all artifacts + actual code changes. Provides verdict.
- `## Standards Reference`: `instructions/code-review.instructions.md`, `instructions/quality-standards.instructions.md`, `skills/code-review/SKILL.md`
- `## Input`: Reads all `.workflow/{task-id}/` artifacts + examines actual modified files
- `## Review Checklist`: 1) Requirements met (compare plan vs implementation) 2) Code quality (SOLID, DRY, naming, structure) 3) Test coverage and quality 4) Security (OWASP, input validation, secrets) 5) Architecture fit (existing patterns, maintainability) 6) Performance (no regressions, efficient patterns) 7) Documentation (comments where needed, API docs)
- `## Artifact Output`: Write to `.workflow/{task-id}/05-review.md`. Sections: `## Verdict`, `## Issues`, `## Suggestions`, `## Sign-off`. Target: under 200 lines.
- `## Verdict Types`: `pass` (merge-ready), `fail` (blocking issues, requires re-implementation), `conditional` (non-blocking suggestions, human decides)
- `## Rules`: Be specific in feedback (file:line references). Distinguish blocking vs non-blocking issues. Challenge assumptions but hold opinions loosely. No code edits - review only.

- [ ] **Step 2: Commit**

```bash
git add agents/reviewer.agent.md
git commit -m "feat(agents): add reviewer phase agent for critical analysis and verdicts"
```

---

### Task 9: Create Orchestrator Agent

**Files:**
- Create: `agents/orchestrator.agent.md`

- [ ] **Step 1: Write orchestrator.agent.md**

Replaces `multi-agent-workflow.agent.md`. Drives the 5-phase pipeline with configurable auto/gated modes.

```yaml
---
name: orchestrator
description: 'Drives the 5-phase development pipeline: explorer -> planner -> researcher -> coder -> reviewer. Configurable auto/gated modes.'
model: claude-sonnet-4-6
modelParameters:
  temperature: 0.25
---
```

No MCP servers - orchestrator delegates all work to phase agents.

Body sections:

- `## Role`: Pipeline coordinator. Dispatches phase agents sequentially, validates artifacts, handles review verdicts.

- `## Modes`:
  - `auto`: Runs all 5 phases without stopping. Reports final verdict.
  - `gated`: Pauses after each phase. Outputs: "Phase {n} complete. Artifact: .workflow/{task-id}/{artifact}. Proceed? (y/n/feedback)"
  - Default mode: `gated`

- `## Task ID`: Format `YYYY-MM-DD-{slug}` derived from task description.

- `## Execution Flow`:
  1. Generate task-id from task description
  2. Create `.workflow/{task-id}/` directory
  3. For each phase (explore, plan, research, implement, review):
     a. Construct prompt: task description + all previous artifact paths
     b. Dispatch phase agent
     c. Validate artifact has correct frontmatter and required sections
     d. Log transition to `orchestrator.log`
     e. In gated mode: pause for human approval
  4. After review: handle verdict

- `## Review Verdict Handling`:
  - `pass`: Report completion, workflow ends
  - `conditional`: Report issues + suggestions, workflow ends (human decides)
  - `fail`: Loop back to implement phase with review feedback, re-run review. Max 2 retries before escalating to human.

- `## Log Format`:
  ```
  [ISO-8601] PHASE_START  {phase}  agent={agent}  model={model}
  [ISO-8601] PHASE_END    {phase}  status={status}  artifact={file}
  [ISO-8601] REVIEW_VERDICT {verdict}  retries={n}/2
  ```

- `## Phase Agent Dispatch Table`:
  | Phase | Agent | Model | Artifact |
  |-------|-------|-------|----------|
  | 1. Explore | explorer | claude-haiku-4-5 | 01-exploration.md |
  | 2. Plan | planner | claude-opus-4-6 | 02-plan.md |
  | 3. Research | researcher | claude-opus-4-6 | 03-research.md |
  | 4. Implement | coder | claude-sonnet-4-6 | 04-implementation.md |
  | 5. Review | reviewer | claude-opus-4-6 | 05-review.md |

- `## Supporting Agents`: Can invoke git-expert, frontend-specialist, debug, documentation-writer, codebase-maintainer, workflow-engineer, gh-aw-builder, arch-linux-expert as needed during any phase.

- `## Artifact Frontmatter Template`:
  ```yaml
  ---
  task: "{task-id}"
  phase: "{phase}"
  status: "complete|blocked|needs-input"
  timestamp: "{ISO-8601}"
  agent: "{agent-name}"
  model: "{model-id}"
  ---
  ```

- `## Triggers`:
  - `@orchestrator [task] --mode=auto`
  - `@orchestrator [task] --mode=gated`
  - `@orchestrator [task]` (defaults to gated)

- [ ] **Step 2: Commit**

```bash
git add agents/orchestrator.agent.md
git commit -m "feat(agents): add orchestrator agent for 5-phase pipeline coordination"
```

---

### Task 10: Remove Replaced Agents

**Files:**
- Delete: `agents/multi-agent-workflow.agent.md`
- Delete: `agents/strategic-planner.agent.md`
- Delete: `agents/task-researcher.agent.md`
- Delete: `agents/repo-index.agent.md`
- Delete: `agents/context7.agent.md`
- Delete: `agents/critical-thinking.agent.md`
- Delete: `agents/language-optimizer.agent.md`
- Delete: `agents/app-optimizer.agent.md`
- Delete: `agents/github-issue-fixer.agent.md`
- Delete: `agents/profile-maintainer.agent.md`
- Delete: `agents/ai-config-expert.agent.md`
- Delete: `agents/mise-environment.agent.md`

- [ ] **Step 1: Convert profile-maintainer to a prompt before deletion**

Create `prompts/profile-maintainer.prompt.md` with the agent's core functionality as a prompt template.

- [ ] **Step 2: Convert mise-environment to a prompt before deletion**

Create `prompts/mise-environment.prompt.md` with the agent's core functionality as a prompt template.

- [ ] **Step 3: Delete all replaced agent files**

```bash
git rm agents/multi-agent-workflow.agent.md
git rm agents/strategic-planner.agent.md
git rm agents/task-researcher.agent.md
git rm agents/repo-index.agent.md
git rm agents/context7.agent.md
git rm agents/critical-thinking.agent.md
git rm agents/language-optimizer.agent.md
git rm agents/app-optimizer.agent.md
git rm agents/github-issue-fixer.agent.md
git rm agents/profile-maintainer.agent.md
git rm agents/ai-config-expert.agent.md
git rm agents/mise-environment.agent.md
```

- [ ] **Step 4: Commit**

```bash
git add prompts/profile-maintainer.prompt.md prompts/mise-environment.prompt.md
git add -u agents/
git commit -m "refactor(agents): remove 12 replaced agents, convert 2 niche agents to prompts"
```

---

### Task 11: Add .workflow to .gitignore

**Files:**
- Modify: `.gitignore`

- [ ] **Step 1: Add .workflow/ to .gitignore**

Append to `.gitignore`:

```
# Orchestrator workflow artifacts
.workflow/
```

- [ ] **Step 2: Commit**

```bash
git add .gitignore
git commit -m "chore: add .workflow/ to gitignore for orchestrator artifacts"
```

---

### Task 12: Update CLAUDE.md / AGENTS.md

**Files:**
- Modify: `CLAUDE.md` (which is also AGENTS.md via symlink, or vice versa)

- [ ] **Step 1: Verify symlink relationship**

```bash
ls -la CLAUDE.md AGENTS.md
```

Determine which is the source file and which is the symlink.

- [ ] **Step 2: Update the AI Agents section**

Replace the current agent tables with the new architecture:

**Pipeline Agents (6)**:
| Agent | File | Model | Purpose |
|-------|------|-------|---------|
| Orchestrator | orchestrator.agent.md | sonnet | Drives 5-phase pipeline (auto/gated modes) |
| Explorer | explorer.agent.md | haiku | Fast codebase scanning and mapping |
| Planner | planner.agent.md | opus | Architecture design and task breakdown |
| Researcher | researcher.agent.md | opus | Library investigation and best practices |
| Coder | coder.agent.md | sonnet | TDD-driven implementation |
| Reviewer | reviewer.agent.md | opus | Critical analysis and verdict |

**Supporting Agents (8)**:
| Agent | File | Purpose |
|-------|------|---------|
| Git Expert | git.agent.md | Version control, branching, GitHub CLI |
| Workflow Engineer | workflow-engineer.agent.md | GitHub Actions, CI/CD |
| GH AW Builder | gh-aw-builder.agent.md | GitHub Agentic Workflows |
| Frontend Specialist | frontend-specialist.agent.md | React/Next.js |
| Debug | debug.agent.md | Bug finding and fixing |
| Documentation Writer | doc-writer.agent.md | Technical docs |
| Codebase Maintainer | codebase-maintainer.agent.md | Cleanup, tech debt |
| Arch Linux Expert | arch-linux-expert.agent.md | Arch administration |

- [ ] **Step 3: Add Pipeline Workflow section**

Add a new section describing the chained workflow:

```markdown
## Pipeline Workflow

The orchestrator drives a 5-phase pipeline for complex development tasks:

```
explorer -> planner -> researcher -> coder -> reviewer
```

Each phase produces a structured artifact in `.workflow/{task-id}/`:
1. `01-exploration.md` - Codebase map, relevant files, patterns, risks
2. `02-plan.md` - Requirements, architecture, task breakdown, dependencies
3. `03-research.md` - Findings, best practices, library recommendations
4. `04-implementation.md` - Changes made, files modified, tests added
5. `05-review.md` - Verdict (pass/fail/conditional), issues, suggestions

**Modes**: `auto` (uninterrupted) or `gated` (pause after each phase for review)

**Invoke**: `@orchestrator [task description] --mode=auto|gated`
```

- [ ] **Step 4: Update counts throughout the file**

Update "18 specialized autonomous agents" to "14 agents (6 pipeline + 8 supporting)". Update skills count to reflect merges. Update prompts description to mention templates/ subdirectory.

- [ ] **Step 5: Update the Skills section**

Remove entries for `documentation-templates`, `personal-site-search`, `research-paper-search`, `x-search`, `Unified-search-discover`. Add `web-search` entry. Update `docs-writer` description to mention templates.

- [ ] **Step 6: Update the Prompts mention if present**

Mention the new `prompts/templates/` subdirectory for orchestrator input templates.

- [ ] **Step 7: Commit**

```bash
git add CLAUDE.md AGENTS.md
git commit -m "docs: update CLAUDE.md with new pipeline architecture, agent counts, and workflow docs"
```

---

### Task 13: Verification

- [ ] **Step 1: Verify file counts**

```bash
ls agents/*.agent.md | wc -l  # Should be 14
ls instructions/*.instructions.md | wc -l  # Should be 37 (was 39, minus 2)
ls skills/*/SKILL.md | wc -l  # Should be 29 (was 33, minus 4)
ls prompts/*.prompt.md | wc -l  # Should be 16 (was 20, minus 6 deleted, plus 2 converted agents)
ls prompts/templates/*.md | wc -l  # Should be 4
```

- [ ] **Step 2: Verify no broken references**

```bash
# Check that removed agent names aren't referenced in remaining agents
rg "strategic-planner|task-researcher|repo-index|context7\.agent|critical-thinking|language-optimizer|app-optimizer|github-issue-fixer|multi-agent-workflow|profile-maintainer|ai-config-expert|mise-environment" agents/ --type md
```

Fix any stale references found.

- [ ] **Step 3: Verify .gitignore includes .workflow/**

```bash
rg "\.workflow" .gitignore
```

- [ ] **Step 4: Verify symlinks are intact**

```bash
ls -la CLAUDE.md AGENTS.md GEMINI.md
```

- [ ] **Step 5: Final commit if fixes needed**

```bash
git add -A
git commit -m "fix: resolve stale references from agent refactor"
```
