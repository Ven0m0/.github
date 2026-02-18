---
name: prd
description: 'Generate Product Requirements Documents (PRDs) with executive summaries, user stories, technical specs, and risk analysis. Use when asked to "write a PRD", "document requirements", or "plan a feature".'
user-invocable: true
disable-model-invocation: false
---

# Product Requirements Document (PRD)

Design comprehensive PRDs that bridge business vision and technical execution.

## When to Use

- Starting new product or feature development
- Translating ideas into concrete specifications
- Stakeholders need unified "source of truth" for scope

## Workflow

### Phase 1: Discovery

Before writing, ask about:
- **Core Problem**: Why are we building this now?
- **Success Metrics**: How do we know it worked?
- **Constraints**: Budget, tech stack, deadline?

### Phase 2: Analysis

Synthesize input. Map user flows. Define non-goals to protect timeline.

### Phase 3: Draft

Use the strict schema below. Concrete, measurable criteria only - no "fast", "easy", "intuitive".

## PRD Schema

### 1. Executive Summary
- **Problem Statement**: 1-2 sentences
- **Proposed Solution**: 1-2 sentences
- **Success Criteria**: 3-5 measurable KPIs

### 2. User Experience
- **Personas**: Who is this for?
- **User Stories**: `As a [user], I want [action] so that [benefit]`
- **Acceptance Criteria**: Testable "Done" definitions
- **Non-Goals**: What we are NOT building

### 3. Technical Specifications
- **Architecture**: Data flow and component interaction
- **Integration Points**: APIs, databases, auth
- **Security & Privacy**: Data handling, compliance
- **AI Requirements** (if applicable): Tools, APIs, evaluation strategy

### 4. Risks & Roadmap
- **Phased Rollout**: MVP -> v1.1 -> v2.0
- **Technical Risks**: Latency, cost, dependency failures

## Rules

- Never write a PRD without at least 2 clarifying questions first
- If tech stack unspecified, ask or label as TBD
- Present draft and ask for feedback on specific sections
- Every user story must be testable with clear acceptance criteria
