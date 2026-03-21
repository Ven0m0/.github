---
name: gh-cli
description: GitHub CLI (gh) reference for repositories, issues, PRs, Actions, releases, and all GitHub operations from the command line. Use when working with GitHub API, automating workflows, or managing repos.
user-invocable: true
disable-model-invocation: false
context: fork
agent: general-purpose
allowed-tools: "Bash(gh *), Bash(git *)"
---

# GitHub CLI (gh)

Reference for GitHub CLI. If arguments are provided, execute: `gh $ARGUMENTS` or `git $ARGUMENTS`

<instructions>

## Decision: Which Command?

Think about what the user needs, then select the right command family:

| Need              | Command                                      |
| ----------------- | -------------------------------------------- |
| Authenticate      | `gh auth login` / `gh auth status`           |
| Clone/create repo | `gh repo clone` / `gh repo create`           |
| Work with issues  | `gh issue create/list/view/edit/close`       |
| Work with PRs     | `gh pr create/list/view/checkout/merge`      |
| CI/CD status      | `gh run list/view/watch` / `gh workflow run` |
| Manage secrets    | `gh secret set/list` / `gh variable set/get` |
| Create releases   | `gh release create/list/download`            |
| Search GitHub     | `gh search code/issues/prs/repos`            |
| Direct API calls  | `gh api /endpoint`                           |

</instructions>

<reference>

## Repositories

```bash
gh repo create my-repo --public --description "Description"
gh repo clone owner/repo
gh repo view [--json name,description]
gh repo fork owner/repo --clone
gh repo sync                        # Sync fork with upstream
```

## Issues

```bash
gh issue create --title "Title" --body "Body" --labels bug
gh issue list [--state all] [--assignee @me] [--labels bug]
gh issue view 123 [--comments] [--json title,body,state]
gh issue edit 123 --add-label high-priority
gh issue close 123 --comment "Fixed in PR #456"
gh issue develop 123 --branch fix/issue-123
```

## Pull Requests

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
```

## Actions and Workflows

```bash
gh run list [--workflow "ci.yml"] [--branch main]
gh run view 123456 [--log] [--job ID]
gh run watch 123456
gh run rerun 123456 [--job ID]
gh workflow list
gh workflow run ci.yml [--ref develop]
gh cache list [--branch main]
gh cache delete --all
```

## Secrets and Variables

```bash
gh secret list
gh secret set MY_SECRET [--env production]
echo "$VALUE" | gh secret set MY_SECRET
gh variable set MY_VAR "value" [--env production]
```

## Releases

```bash
gh release create v1.0.0 --notes "Release notes" [--draft]
gh release list
gh release download v1.0.0 [--pattern "*.tar.gz"]
```

## Search

```bash
gh search code "pattern" [--repo owner/repo]
gh search issues "label:bug state:open"
gh search prs "is:open review:required"
gh search repos "stars:>1000 language:python"
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
gh pr list --json number,title --jq '.[] | select(.number > 100)'
gh repo view --json owner,name --jq '.owner.login + "/" + .name'
```

</reference>

<environment_variables>

| Variable             | Purpose                     |
| -------------------- | --------------------------- |
| `GH_TOKEN`           | Auth token for automation   |
| `GH_HOST`            | GitHub hostname (for GHES)  |
| `GH_REPO`            | Override default repository |
| `GH_PROMPT_DISABLED` | Disable interactive prompts |

</environment_variables>

<examples>

### Create PR from issue

```bash
gh issue develop 123 --branch feature/issue-123
git add . && git commit -m "Fix #123" && git push
gh pr create --title "Fix #123" --body "Closes #123"
```

### Check CI and wait for results

```bash
gh workflow run ci.yml --ref main
gh run list --workflow ci.yml --limit 1 --json databaseId \
  --jq '.[0].databaseId' | xargs gh run watch
```

### Bulk close stale issues

```bash
gh issue list --search "label:stale" --json id --jq '
  if length == 0 then
    "query { __typename }"
  else
    "mutation { " + (
      to_entries
      | map(
        "c\(.key): addComment(input:{subjectId:" + (.value.id | @json) + ",body:" + ("Closing as stale" | @json) + "}){clientMutationId}" +
        " s\(.key): closeIssue(input:{issueId:" + (.value.id | @json) + "}){clientMutationId}"
      )
      | join("")
    ) + " }"
  end
' | gh api graphql -f query=-
```

</examples>

## References

- Manual: https://cli.github.com/manual/
- REST API: https://docs.github.com/en/rest
- GraphQL API: https://docs.github.com/en/graphql
