# Agent Chain Refactor - Design Spec

## Overview

Refactor the `.github` repository's agent architecture from a flat collection of 20 independent agents into a chained workflow: **explorer -> planner -> researcher -> coder -> reviewer**, driven by a configurable orchestrator with structured output files.

Additionally: light cleanup of instructions/, skills/, and conversion of overlapping prompts into orchestrator input templates.

**Design change from existing pipeline**: The current `multi-agent-workflow` uses Planning -> Execution -> Refactoring -> Cleanup -> Review. The new pipeline replaces this with Explore -> Plan -> Research -> Implement -> Review. Refactoring and cleanup concerns are handled within the Implement phase (coder agent) and by the `codebase-maintainer` supporting agent when needed, rather than as dedicated pipeline stages.

---

## Agent Architecture

### Phase Agents (5 new, replace 8 existing)

| Phase | Agent File | Model | Replaces |
|-------|-----------|-------|----------|
| 1. Explore | `explorer.agent.md` | claude-haiku-4-5 | repo-index, parts of strategic-planner |
| 2. Plan | `planner.agent.md` | claude-opus-4-6 | strategic-planner, parts of multi-agent-workflow |
| 3. Research | `researcher.agent.md` | claude-opus-4-6 | task-researcher, context7-expert |
| 4. Implement | `coder.agent.md` | claude-sonnet-4-6 | language-optimizer, github-issue-fixer |
| 5. Review | `reviewer.agent.md` | claude-opus-4-6 | critical-thinking, app-optimizer |

### Orchestrator (1 new, replaces 1)

| Agent File | Model | Replaces |
|-----------|-------|----------|
| `orchestrator.agent.md` | claude-sonnet-4-6 | multi-agent-workflow |

**Model rationale**: Sonnet for orchestrator because it performs routing and coordination, not deep reasoning. The phase agents that need deep reasoning (planner, researcher, reviewer) use Opus. The orchestrator's decisions are structured (sequential phase dispatch) rather than open-ended.

### MCP Server Configuration

| Agent | MCP Servers |
|-------|------------|
| orchestrator | (none - delegates to phase agents) |
| explorer | serena, context7 |
| planner | serena, context7, sequential-thinking |
| researcher | context7, exa, ref-tools, grep-app |
| coder | serena, context7, exa |
| reviewer | serena, context7, sequential-thinking |

### Supporting Agents (kept as-is, 8)

| Agent | Reason |
|-------|--------|
| git-expert | Cross-phase utility |
| workflow-engineer | CI/CD specialization |
| gh-aw-builder | GitHub Agentic Workflows niche |
| frontend-specialist | Deep React/Next.js domain knowledge |
| debug | Standalone debugging workflow |
| documentation-writer | On-demand only |
| codebase-maintainer | Maintenance utility |
| arch-linux-expert | Platform specialization |

### Removed Agents (4)

| Agent | Disposition |
|-------|------------|
| profile-maintainer | Convert to prompt |
| ai-config-expert | Absorbed into planner + reviewer |
| mise-environment | Convert to prompt |
| context7-expert | Absorbed into researcher |

### Final Count: 14 agents (down from 20)

---

## Orchestrator Behavior

### Execution Flow

The orchestrator always runs phases sequentially: explore -> plan -> research -> implement -> review. No phases are skipped. Each phase receives the full artifact chain (all previous phase artifacts) as context.

### Task ID Format

Task IDs use the format `YYYY-MM-DD-{slug}` where slug is a lowercase hyphenated summary derived from the user's task description (e.g., `2026-03-17-add-auth-middleware`).

### Phase Dispatch

For each phase, the orchestrator:
1. Constructs the agent prompt with: task description + all previous artifacts
2. Dispatches the phase agent
3. Validates the returned artifact has correct frontmatter and required sections
4. Logs the phase transition to `orchestrator.log`
5. In gated mode: pauses and presents artifact to user
6. Proceeds to next phase (or terminates if review is complete)

### Review Verdict Handling

When the reviewer returns a verdict:
- **pass**: Orchestrator reports completion, workflow ends
- **conditional**: Orchestrator reports issues + suggestions, workflow ends (human decides next steps)
- **fail**: Orchestrator loops back to the implement phase with the review feedback appended to context, then re-runs review. Maximum 2 retry loops before escalating to human.

### Orchestrator Log Format

```
[ISO-8601] PHASE_START  explore  agent=explorer  model=claude-haiku-4-5
[ISO-8601] PHASE_END    explore  status=complete  artifact=01-exploration.md
[ISO-8601] PHASE_START  plan     agent=planner   model=claude-opus-4-6
...
[ISO-8601] REVIEW_VERDICT fail   retries=1/2
[ISO-8601] PHASE_START  implement agent=coder    model=claude-sonnet-4-6  (retry)
```

---

## Structured Output Contract

### Artifact Directory

Each workflow run writes to `.workflow/{task-id}/` (gitignored - add `.workflow/` to `.gitignore`):

```
.workflow/
  {task-id}/
    01-exploration.md
    02-plan.md
    03-research.md
    04-implementation.md
    05-review.md
    orchestrator.log
```

### Artifact Frontmatter

```yaml
---
task: "{task-id}"
phase: "explore|plan|research|implement|review"
status: "complete|blocked|needs-input"
timestamp: "ISO-8601"
agent: "agent-name"
model: "model-id"
---
```

### Phase-Specific Content Sections

| Phase | Key Sections | Target Size |
|-------|-------------|-------------|
| Explorer | `## Codebase Map`, `## Relevant Files`, `## Patterns Found`, `## Risks` | Under 300 lines |
| Planner | `## Requirements`, `## Architecture`, `## Task Breakdown`, `## Dependencies` | Under 500 lines |
| Researcher | `## Findings`, `## Best Practices`, `## Library Recommendations`, `## Constraints` | Under 400 lines |
| Coder | `## Changes Made`, `## Files Modified`, `## Tests Added`, `## Remaining TODOs` | Under 200 lines |
| Reviewer | `## Verdict` (pass/fail/conditional), `## Issues`, `## Suggestions`, `## Sign-off` | Under 200 lines |

### Orchestrator Modes

```yaml
mode: "auto"    # Runs all 5 phases without stopping
mode: "gated"   # Pauses after each phase for human approval
```

In gated mode, the orchestrator outputs:
`Phase {n} complete. Artifact: .workflow/{task-id}/{artifact}. Proceed? (y/n/feedback)`

---

## Instructions Cleanup

| Action | Files | Reason |
|--------|-------|--------|
| Merge | `typescript.instructions.md` content into `javascript.instructions.md` (keep existing filename, applyTo already covers both) | 90% overlap, TS is superset |
| Remove | Dead INDEX.md references (C#, Swift, Ruby, PHP, Scala, Elixir) | Referenced but files don't exist |
| Remove | `instructions.instructions.md` | Covered by `meta-authoring.instructions.md` |
| Update | INDEX.md | Reflect changes |

**Net reduction: 2 instruction files** (1 merge saves 1 file, 1 removal)

---

## Skills Cleanup

| Action | Files | Reason |
|--------|-------|--------|
| Merge | `docs-writer/` + `documentation-templates/` -> `docs-writer/` | Templates belong inside writer |
| Merge | `personal-site-search/` + `research-paper-search/` + `x-search/` -> `web-search/` | Three thin Exa wrappers, same pattern |
| Remove | `Unified-search-discover/` | Covered by explorer agent + tool preferences |

All other skills (gh-aw-operations, linting-llm-configs, playwright-cli, migrate-component, etc.) are kept as-is.

**Net reduction: 4 skill directories** (1 merge saves 1, 1 merge saves 2, 1 removal)

---

## Prompts Restructure

### Converted to Orchestrator Input Templates

| Source | Target |
|--------|--------|
| `develop-feature.prompt.md` | `prompts/templates/feature-request.md` |
| `create-implementation-plan.prompt.md` | `prompts/templates/implementation-plan.md` |
| `maint.prompt.md` | `prompts/templates/maintenance-task.md` |
| `context-map.prompt.md` | `prompts/templates/context-map.md` |

### Removed (redundant)

| File | Reason |
|------|--------|
| `optimize-llm-config.prompt.md` | Duplicate of `generate-custom-instructions-from-codebase.prompt.md` |
| `cleanup.prompt.md` | Covered by codebase-maintainer agent |

### Kept (standalone utilities)

- `bash.prompt.md`, `python.prompt.md`, `best-practices.prompt.md`
- `create-readme.prompt.md`, `create-agentsmd.prompt.md`, `create-docs.prompt.md`
- `create-llms.prompt.md`, `update-llms.prompt.md`
- `update-implementation-plan.prompt.md`, `update-markdown-file-index.prompt.md`
- `graalvm-native-image.prompt.md`, `remember.prompt.md`
- `generate-custom-instructions-from-codebase.prompt.md`
- `setup-cloud-infrastructure.prompt.md`

### New Directory Structure

```
prompts/
  templates/
    feature-request.md
    implementation-plan.md
    maintenance-task.md
    context-map.md
  *.prompt.md (standalone utilities)
```

---

## Implementation Approach

All changes are made in a single feature branch and PR. The implementation order is:

1. Instructions cleanup (smallest blast radius)
2. Skills cleanup (merges and removals)
3. Prompts restructure (convert + remove + create templates/)
4. Create new phase agents + orchestrator
5. Remove replaced agents
6. Add `.workflow/` to `.gitignore`
7. Update AGENTS.md / CLAUDE.md to reflect new architecture

No deprecation period for removed agents since this is a single-org config repo with no external consumers.

---

## Success Criteria

1. Orchestrator can chain all 5 phases in both auto and gated modes
2. Each phase agent produces a well-formed artifact with standard frontmatter
3. Phase agents can read previous phase artifacts and build on them
4. Supporting agents remain independently usable
5. Instructions count reduced by 2 files
6. Skills count reduced by 4 directories
7. Prompts reorganized with templates/ subdirectory, 2 removed, 4 converted
8. AGENTS.md / CLAUDE.md updated to reflect new architecture
9. `.workflow/` added to `.gitignore`
