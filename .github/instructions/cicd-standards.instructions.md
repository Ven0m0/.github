---
description: 'GitHub Actions workflow standards for CI/CD: security, performance, reusable patterns'
applyTo: '.github/workflows/*.yml,.github/workflows/*.yaml'
---

# CI/CD and GitHub Actions Standards

<Goals>

- Security-first: SHA-pinned actions, least-privilege permissions, OIDC auth
- Performance: caching, matrix builds, path filtering, concurrency control
- Maintainability: reusable workflows, clear naming, timeouts on all jobs

</Goals>

## Workflow Structure

```yaml
name: CI
on:
  push:
    branches: [main]
    paths: ['src/**', 'tests/**', 'package.json']
  pull_request:
    branches: [main]
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.head_ref || github.ref }}
  cancel-in-progress: true

permissions:
  contents: read
```

<Standards>

**Triggers**: Use path filtering to skip irrelevant runs. `workflow_dispatch` for manual triggers. `schedule` for nightly/weekly. Set `cancel-in-progress: false` for deployments.

**Jobs**: Clear names representing distinct phases. Use `needs` for dependencies, `outputs` for inter-job data, `if` for conditional execution, `timeout-minutes` on all jobs.

**Matrix**: `fail-fast: false` for comprehensive reporting. Use `exclude` to skip unsupported combinations.

</Standards>

---

## Security (Non-Negotiable)

<Security>

### Action Pinning
```yaml
# CORRECT: Version tag
- uses: actions/checkout@v4

# WRONG: SHA pinning (harder to maintain, less readable)
- uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683

# WRONG: branch reference (vulnerable to compromise)
- uses: actions/checkout@main
```

### Permissions (Least Privilege)
```yaml
permissions:
  contents: read          # Default, safe starting point
# Add only when needed:
# contents: write, pull-requests: write, packages: write, checks: write
```

### Secrets
- Access via `${{ secrets.NAME }}` only, never hardcode
- Use environment-specific secrets for deployment
- OIDC preferred over long-lived credentials for cloud auth

### Scanning
- CodeQL for SAST, Dependabot for dependency review
- Enable secret scanning with push protection
- `dependency-review-action` on PRs

</Security>

---

## Performance

### Caching
```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-npm-
```

### Matrix Builds
```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, macos-latest]
    node-version: ['20', '22']
```

### Fast Checkout
```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 1    # Shallow clone unless full history needed
```

---

## Reusable Workflows

```yaml
# Caller pattern
jobs:
  ci:
    uses: Ven0m0/.github/.github/workflows/reusable-ci-python.yml@main
    with:
      python-version: '3.12'
      coverage-threshold: 80
    secrets: inherit
```

```yaml
# Defining a reusable workflow
on:
  workflow_call:
    inputs:
      python-version:
        type: string
        default: '3.12'
    secrets:
      CODECOV_TOKEN:
        required: false
```

---

## Deployment Patterns

<HighLevelDetails>

- **Manual Approval**: Use `environment` with required reviewers for production
- **Blue-Green**: Deploy green, smoke test, switch traffic
- **Canary**: Route small % of traffic, monitor, expand
- **Rollback**: Keep previous artifacts, automate revert on health check failure

</HighLevelDetails>

```yaml
deploy:
  environment:
    name: production
    url: https://prod.example.com
  runs-on: ubuntu-latest
  needs: [build, test]
```

## Testing Strategy

| Level | When | Focus |
|-------|------|-------|
| Unit | Every push/PR | Individual components, fast feedback, high coverage |
| Integration | PR merge | Component interactions, real services via `services` |
| E2E | Pre-deploy | Full user flows, staging environment |
| Performance | Nightly/weekly | Load testing, threshold enforcement |

## Deployment Strategies

| Strategy | When | Benefit |
|----------|------|---------|
| Rolling | Default for stateless apps | Gradual replacement |
| Blue/Green | Zero-downtime critical apps | Instant rollback |
| Canary | Controlled blast radius | Early issue detection |
| Feature Flags | Decoupling deploy from release | A/B testing, staged rollout |

## Debugging

| Error | Cause | Fix |
|-------|-------|-----|
| Resource not accessible | Missing permissions | Add to `permissions:` |
| Cache never hits | Wrong key format | Check `hashFiles()` paths |
| Secrets undefined | Wrong context | Use `secrets: inherit` |
| Workflow not triggered | Event config wrong | Verify `on:` block |
| Timeout | Inefficient steps | Profile, add matrix, optimize caching |
| Flaky tests | Race conditions | Explicit waits, standardize env |

```yaml
# Debug context
- run: |
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    echo "SHA: ${{ github.sha }}"
```

<Limitations>

- All workflows must use SHA-pinned actions
- Permissions must be explicit and minimal
- Secrets must never be logged or exposed
- All jobs must have `timeout-minutes`
- Tests must pass before deployment
- Production requires manual approval

</Limitations>
