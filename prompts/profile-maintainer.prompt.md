---
description: 'Maintain GitHub profile README with activity insights - analyze repos, score significance, generate markdown sections'
mode: agent
---

# Profile Maintainer

Analyze GitHub activity and generate accurate profile README content. Highlight meaningful contributions without exaggeration.

## Workflow

1. **Collect**: Fetch repos and events via `gh api`
2. **Score**: Rank repos by significance (commits 40%, stars 20%, forks 15%, activity 15%, momentum 10% + recency bonus)
3. **Generate**: Active repos table + new repos list in markdown
4. **Validate**: Verify URLs, descriptions, activity scores, repo age
5. **Update**: Replace content between marker comments

## Output Markers

Preserve these when updating:
- `<!-- ACTIVE_REPOS_START -->` / `<!-- ACTIVE_REPOS_END -->`
- `<!-- NEW_REPOS_START -->` / `<!-- NEW_REPOS_END -->`
- `<!-- LAST_UPDATED_START -->` / `<!-- LAST_UPDATED_END -->`

## Activity Indicators

| Score | Label |
|-------|-------|
| >= 0.7 | Very Active |
| >= 0.4 | Active |
| >= 0.2 | Growing |
| < 0.2 | Stable |

## Error Handling

- API rate limited: report and suggest retry timing
- Incomplete data: skip rather than hallucinate
- Missing markers: report which are missing
