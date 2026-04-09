---
applyTo: "**/*.{yml,yaml}"
description: "CI/CD, GitHub Actions, and deployment standards for workflow and automation YAML"
---

# CI/CD and DevOps Standards

<Goals>

- Security-first: explicit action versions, least-privilege permissions, OIDC auth
- Reliability: path filtering, concurrency, timeouts, staged deployments, rollback planning
- Maintainability: reusable workflows, clear naming, predictable job structure

</Goals>

## Before Any CI/CD or Deployment Work

**READ**: `.github/skills/workflow-development/SKILL.md`

## Workflow Structure

```yaml
name: CI
on:
  push:
    branches: [main]
    paths: ["src/**", "tests/**", "package.json"]
  pull_request:
    branches: [main]
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.head_ref || github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 15
    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-node@v6
        with:
          node-version: "24"
          cache: "npm"
      - run: npm ci
      - run: npm test
```

<Standards>

**Triggers**: Use path filtering to skip irrelevant runs. Add `workflow_dispatch` for manual recovery or one-off tasks. Use `schedule` for recurring maintenance. Set `cancel-in-progress: false` for deployments.

**Jobs**: Use clear phase-oriented names. Model dependencies with `needs`, share data with `outputs`, guard optional work with `if`, and set `timeout-minutes` on every job.

**Matrix**: Use `fail-fast: false` for broader failure visibility. Use `include` and `exclude` to keep the matrix intentional.

**Deployments**: Gate production with `environment`, required reviewers, smoke tests, and documented rollback steps.

</Standards>

---

## Security (Non-Negotiable)

<Security>

### Action References

```yaml
# CORRECT: explicit major version tag
- uses: actions/checkout@v6

# ALSO VALID WHEN POLICY REQUIRES IMMUTABLE PINS
- uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2

# WRONG: moving branch reference
- uses: actions/checkout@main

# WRONG: floating latest tag
- uses: owner/action@latest
```

- Prefer maintained major-version tags for first-party and trusted actions
- Use full SHAs when repository or organization policy requires immutable third-party pinning
- Never use branch refs such as `@main` or floating refs such as `@latest`

### Permissions (Least Privilege)

```yaml
permissions:
  contents: read
# Add only when needed:
# pull-requests: write
# packages: write
# checks: write
```

### Secrets and Auth

- Access secrets via `${{ secrets.NAME }}` only; never hardcode or echo them
- Prefer OIDC over long-lived cloud credentials
- Use environment-scoped secrets for deployment jobs

### Scanning

- Run CodeQL for SAST where supported
- Use dependency review on pull requests
- Enable secret scanning and push protection

</Security>

---

## Performance

### Caching

```yaml
- uses: actions/cache@v5
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
    node-version: ["22", "24"]
```

### Fast Checkout

```yaml
- uses: actions/checkout@v6
  with:
    fetch-depth: 1
```

---

## Reusable Workflows

```yaml
# Caller pattern
jobs:
  ci:
    uses: Ven0m0/.github/.github/workflows/reusable-ci-python.yml@main
    with:
      python-version: "3.12"
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
        default: "3.12"
    secrets:
      CODECOV_TOKEN:
        required: false
```

---

## Deployment Patterns

<HighLevelDetails>

- **Manual Approval**: Use `environment` with required reviewers for production
- **Blue-Green**: Deploy green, smoke test, then shift traffic
- **Canary**: Route a small percentage first, monitor, then expand
- **Rollback**: Keep previous artifacts and automate revert on health check failure

</HighLevelDetails>

```yaml
deploy:
  environment:
    name: production
    url: https://prod.example.com
  runs-on: ubuntu-latest
  needs: [build, test]
```

### Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Code reviewed
- [ ] Environment variables and secrets verified
- [ ] Backup or restore point ready
- [ ] Rollback path documented

### Deployment Order

1. **Prepare**: Verify build artifacts, inputs, and environment configuration
2. **Deploy**: Release with monitoring enabled
3. **Verify**: Run health checks and critical smoke tests
4. **Confirm**: Watch metrics and logs for a stabilization window
5. **Rollback**: Revert immediately if health checks or key metrics fail

## Testing Strategy

| Level       | When           | Focus                                                |
| ----------- | -------------- | ---------------------------------------------------- |
| Unit        | Every push/PR  | Individual components, fast feedback, high coverage  |
| Integration | PR merge       | Component interactions, real services via `services` |
| E2E         | Pre-deploy     | Full user flows, staging environment                 |
| Performance | Nightly/weekly | Load testing, threshold enforcement                  |

## Deployment Strategies

| Strategy      | When                           | Benefit                     |
| ------------- | ------------------------------ | --------------------------- |
| Rolling       | Default for stateless apps     | Gradual replacement         |
| Blue/Green    | Zero-downtime critical apps    | Instant rollback            |
| Canary        | Controlled blast radius        | Early issue detection       |
| Feature Flags | Decoupling deploy from release | A/B testing, staged rollout |

## Debugging

| Error                   | Cause               | Fix                                   |
| ----------------------- | ------------------- | ------------------------------------- |
| Resource not accessible | Missing permissions | Add the required scope to `permissions:` |
| Cache never hits        | Wrong key format    | Check `hashFiles()` paths and restore keys |
| Secrets undefined       | Wrong context       | Use `secrets: inherit` or define workflow-call secrets |
| Workflow not triggered  | Event config wrong  | Verify `on:` filters, branches, and paths |
| Timeout                 | Inefficient steps   | Profile, split jobs, or improve caching |
| Flaky tests             | Race conditions     | Add explicit waits and stabilize the test environment |

```yaml
# Debug context
- run: |
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    echo "SHA: ${{ github.sha }}"
```

## Anti-Patterns

- Do not use `@main`, `@master`, or `@latest` for actions
- Do not deploy without a rollback path
- Do not combine unrelated infrastructure changes in one release
- Do not skip staging or smoke validation for risky production changes

<Limitations>

- Permissions must be explicit and minimal
- Secrets must never be logged or exposed
- Every job needs `timeout-minutes`
- Tests must pass before deployment
- Production deployments require approval or an equivalent protection rule

</Limitations>
