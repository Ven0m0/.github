---
name: claude-code-app
description: GitHub App template for Claude Code Action. Pre-configured with required permissions for AI-powered coding assistance.
---

# Claude Code GitHub App Template

## Tech Stack

| Component | Technology |
|-----------|------------|
| Platform | GitHub Apps |
| Integration | GitHub Actions |
| Configuration | Manifest JSON |

---

## Directory Structure

```
project-name/
├── .github/
│   └── workflows/
│       └── claude-code.yml  # Action workflow
├── manifest.json            # App manifest
└── README.md                # Setup guide
```

---

## Required Permissions

| Permission | Access |
|------------|--------|
| Contents | Read & Write |
| Issues | Read & Write |
| Pull Requests | Read & Write |
| Actions | Read |
| Metadata | Read |

---

## Events

| Event | Purpose |
|-------|---------|
| issue_comment | Respond to comments |
| issues | Handle issue tasks |
| pull_request | Review and edit PRs |
| pull_request_review | Handle reviews |
| pull_request_review_comment | Respond to review comments |

---

## Setup Steps

1. Create a new directory for your app.
2. Copy `manifest.json` to the directory.
3. Go to GitHub App settings and select "Create from manifest".
4. Upload or paste the `manifest.json`.
5. Generate a private key in the app settings.
6. Install the app on your target repositories.
7. Add `APP_ID` and `PRIVATE_KEY` to your repository secrets.
8. Create a workflow file in `.github/workflows/claude-code.yml`.

---

## Best Practices

- Use GitHub Secrets for the private key.
- Grant minimal repository access (only what's needed).
- Use a dedicated service account if possible.
- Regularly rotate the private key.
