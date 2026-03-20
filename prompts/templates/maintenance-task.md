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
