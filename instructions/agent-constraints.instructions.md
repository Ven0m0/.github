---
applyTo: "agents/*.agent.md"
---

# Agent Shared Constraints

Canonical constraints for pipeline and supporting agents. Applied automatically when editing agent files.

## Tool Usage

- Always activate tools before use
- Built-in preferred: use dedicated tools (`read_file`, `create_file`, etc.) over terminal commands
- Batch tool calls: identify independent operations and execute them in parallel; prioritize I/O-bound calls
- Lightweight validation: use `get_errors` for quick feedback after edits; reserve `eslint`/`typecheck` for comprehensive analysis
- Context-efficient reading: prefer semantic search, file outlines, and targeted line-range reads; limit to 200 lines per read

## Reasoning

- Think-Before-Action: use `<thought>` for multi-step planning and error diagnosis; omit for routine tasks
- Self-correct: "Re-evaluating: [issue]. Revised approach: [plan]"
- Verify pathing, dependencies, and constraints before execution

## Error Handling & Retry

- Transient errors → handle locally; persistent errors → escalate
- Retry up to 2 times on verification failure; log each retry: "Retry N/2 for task_id"
- After max retries, apply mitigation or escalate

## Output

- Return ONLY the requested deliverable; zero explanation, preamble, or commentary
- All output must be raw JSON — no markdown code fences (```` ```json ````)
- Failures: write YAML logs to `docs/plan/{plan_id}/logs/{agent}_{task_id}_{timestamp}.yaml` only on `status=failed`
- Never create summary files

## Online Research Priority (when tools are available)

1. Library/framework docs → Context7 tools
2. Web search → `tavily_search` for up-to-date information
3. Fallback → `fetch_webpage` (can search Google via `https://www.google.com/search?q=query+2026`)
