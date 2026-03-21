---
name: prd
description: Generate Product Requirements Documents (PRDs) with executive summaries, user stories, technical specs, and risk analysis. Use when asked to "write a PRD", "document requirements", or "plan a feature".
allowed-tools: "Read, Write, Edit, Glob, Grep"
---

# Product Requirements Document (PRD)

Design comprehensive PRDs that bridge business vision and technical execution.

<instructions>

## Phase 1: Discovery

Before writing, ask about (never skip this):

- **Core Problem**: Why are we building this now?
- **Success Metrics**: How do we know it worked? (must be measurable)
- **Constraints**: Budget, tech stack, deadline, team size?
- **Users**: Who is this for? (specific personas, not "everyone")

Ask at least 2 clarifying questions before drafting.

## Phase 2: Analysis

Synthesize inputs:

1. Map user flows from trigger to completion
2. Define non-goals to protect timeline
3. Identify technical unknowns and risks
4. Research existing patterns in the codebase (if applicable)

## Phase 3: Draft

Use the schema below. Every criterion must be concrete and measurable - never use vague terms like "fast", "easy", "intuitive" without quantifying them.

</instructions>

<schema>

### 1. Executive Summary

- **Problem Statement**: 1-2 sentences
- **Proposed Solution**: 1-2 sentences
- **Success Criteria**: 3-5 measurable KPIs (with numbers)

### 2. User Experience

- **Personas**: Who, with context on their needs
- **User Stories**: `As a [user], I want [action] so that [benefit]`
- **Acceptance Criteria**: Testable "Done" definitions per story
- **Non-Goals**: What we are NOT building (and why)

### 3. Technical Specifications

- **Architecture**: Data flow and component interaction
- **Integration Points**: APIs, databases, auth
- **Security and Privacy**: Data handling, compliance requirements
- **AI Requirements** (if applicable): Models, tools, evaluation strategy

### 4. Risks and Roadmap

- **Phased Rollout**: MVP (week 1-2) -> v1.1 (month 1) -> v2.0 (quarter)
- **Technical Risks**: Probability, impact, mitigation for each

</schema>

<constraints>
- Never write a PRD without asking clarifying questions first
- If tech stack is unspecified, ask or label as TBD
- Present draft and ask for feedback on specific sections
- Every user story must have testable acceptance criteria
- Use numbers: "loads in <200ms" not "loads quickly"
</constraints>

<examples>

### User story with acceptance criteria

```
As a team lead, I want to see a dashboard of my team's PR review times
so that I can identify bottlenecks in our review process.

Acceptance Criteria:
- Dashboard shows average review time per team member (last 30 days)
- Data refreshes every hour
- Supports filtering by repository
- Loads in <2 seconds with up to 50 team members
- Exports to CSV
```

### Non-goal example

```
Non-Goals (v1):
- Real-time updates (polling every hour is sufficient for v1)
- Cross-organization data (single org only)
- Custom date ranges (fixed to 7/30/90 day windows)
```

### Risk entry example

```
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| GitHub API rate limiting | Medium | High | Cache responses, use GraphQL for batch queries |
| Large org slow queries | Low | Medium | Paginate results, add loading states |
```

</examples>
