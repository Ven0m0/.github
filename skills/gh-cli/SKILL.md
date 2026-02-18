---
name: gh-cli
description: GitHub CLI (gh) reference for repositories, issues, PRs, Actions, releases, and all GitHub operations from the command line. Use when working with GitHub API, automating workflows, or managing repos.
user-invocable: true
disable-model-invocation: false
---

# GitHub CLI (gh)

Reference for GitHub CLI. Current stable version (check with `gh --version`).

## Quick Reference

```bash
gh auth login          # Authenticate
gh auth status         # Check auth
gh auth setup-git      # Configure git credential helper
```

## Core Commands

### Repositories

```bash
gh repo create my-repo --public --description "Description"
gh repo clone owner/repo
gh repo view [--json name,description]
gh repo edit --description "New desc"
gh repo fork owner/repo --clone
gh repo sync                        # Sync fork with upstream
gh repo set-default owner/repo
```

### Issues

```bash
gh issue create --title "Title" --body "Body" --labels bug
gh issue list [--state all] [--assignee @me] [--labels bug]
gh issue view 123 [--comments] [--json title,body,state]
gh issue edit 123 --add-label high-priority
gh issue close 123 --comment "Fixed in PR #456"
gh issue develop 123 --branch fix/issue-123
```

### Pull Requests

```bash
gh pr create --title "Feature" --body "Description" [--draft]
gh pr list [--state all] [--author @me] [--json number,title]
gh pr view 123 [--comments] [--json title,body,files]
gh pr checkout 123
gh pr diff 123
gh pr merge 123 --squash --delete-branch
gh pr review 123 --approve
gh pr checks 123 --watch
gh pr ready 123                     # Mark draft as ready
gh pr update-branch 123
```

### GitHub Actions

```bash
gh run list [--workflow "ci.yml"] [--branch main]
gh run view 123456 [--log] [--job ID]
gh run watch 123456
gh run rerun 123456 [--job ID]
gh run download 123456 [--name build]

gh workflow list
gh workflow run ci.yml [--ref develop]
gh workflow enable/disable ci.yml

gh cache list [--branch main]
gh cache delete --all
```

### Secrets & Variables

```bash
gh secret list
gh secret set MY_SECRET [--env production]
echo "$VALUE" | gh secret set MY_SECRET

gh variable set MY_VAR "value" [--env production]
gh variable get MY_VAR
```

### Releases

```bash
gh release create v1.0.0 --notes "Release notes" [--draft]
gh release list
gh release download v1.0.0 [--pattern "*.tar.gz"]
gh release upload v1.0.0 ./file.tar.gz
```

### Search

```bash
gh search code "pattern" [--repo owner/repo]
gh search issues "label:bug state:open"
gh search prs "is:open review:required"
gh search repos "stars:>1000 language:python"
```

### Projects

```bash
gh project list [--owner owner]
gh project create --title "Project"
gh project item-add 123 --owner owner --repo repo --issue 456
```

## API Requests

```bash
gh api /user
gh api --method POST /repos/owner/repo/issues \
  --field title="Title" --field body="Body"
gh api /user/repos --paginate
gh api graphql -f query='{ viewer { login } }'
```

## Output Formatting

```bash
# JSON output with jq filtering
gh pr list --json number,title --jq '.[] | select(.number > 100)'
gh repo view --json owner,name --jq '.owner.login + "/" + .name'

# Template output
gh pr view 123 --template 'Title: {{.title}} State: {{.state}}'
```

## Common Workflows

```bash
# Create PR from issue
gh issue develop 123 --branch feature/issue-123
git add . && git commit -m "Fix #123" && git push
gh pr create --title "Fix #123" --body "Closes #123"

# Bulk close stale issues (Optimized: 1 API call via GraphQL)
gh issue list --search "label:stale" --json id --jq '
  if length == 0 then
    "query { __typename }" # A no-op query to prevent errors when no issues are found
  else
    "mutation { " + (to_entries | map("
    c\(.key): addComment(input:{subjectId:\"\(.value.id)\",body:\"Closing as stale\"}){clientMutationId}
    s\(.key): closeIssue(input:{issueId:\"\(.value.id)\"}){clientMutationId}
  ") | join("")) + " }"
  end
' | gh api graphql -f query=-
gh workflow run ci.yml --ref main
gh run list --workflow ci.yml --limit 1 --json databaseId --jq '.[0].databaseId' | \
  xargs gh run watch
```

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `GH_TOKEN` | Auth token for automation |
| `GH_HOST` | GitHub hostname |
| `GH_REPO` | Override default repository |
| `GH_PROMPT_DISABLED` | Disable interactive prompts |

## Global Flags

| Flag | Description |
|------|-------------|
| `--repo OWNER/REPO` | Target repository |
| `--json FIELDS` | JSON output with fields |
| `--jq EXPR` | Filter JSON with jq |
| `--web` | Open in browser |
| `--paginate` | Fetch all pages |

## References

- Manual: https://cli.github.com/manual/
- REST API: https://docs.github.com/en/rest
- GraphQL API: https://docs.github.com/en/graphql
