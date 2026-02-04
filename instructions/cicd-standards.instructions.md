---
description: 'Comprehensive standards for GitHub Actions workflows, continuous integration, continuous deployment, and infrastructure automation'
applyTo: '.github/workflows/*.yml, .github/workflows/*.yaml, **/*.yml, **/*.yaml'
---

# CI/CD and GitHub Actions Standards

Comprehensive standards for GitHub Actions workflows, continuous integration, continuous deployment, and infrastructure automation. Focus on security, performance, and maintainability.

## Workflow Fundamentals

### Workflow Structure

All workflows must include basic configuration:

```yaml
name: CI

on:
  push:
    branches: [main, develop]
    paths: ['src/**', 'tests/**', 'package.json']
  pull_request:
    branches: [main]
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.head_ref || github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

env:
  CACHE_KEY_PREFIX: v1

jobs:
  # Job definitions follow
```

### Triggers and Events

**Common triggers**:

| Event | Use Case |
|-------|----------|
| `push` | Run on every push to main/develop |
| `pull_request` | Run on PR creation and updates |
| `workflow_dispatch` | Manual trigger via GitHub UI |
| `schedule` | Cron-based execution (nightly, weekly) |
| `repository_dispatch` | External webhooks |
| `workflow_call` | Reusable workflow from other repos |

**Path filtering for performance**:

```yaml
on:
  push:
    paths:
      - 'src/**'
      - 'tests/**'
      - 'package.json'
      - '.github/workflows/ci.yml'
    paths-ignore:
      - 'docs/**'
      - '*.md'
```

### Concurrency and Cancellation

Prevent concurrent deployments and cancel outdated runs:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true  # Cancel old runs when new push occurs
```

For deployment jobs, set `cancel-in-progress: false`:

```yaml
concurrency:
  group: deployment-${{ github.environment }}
  cancel-in-progress: false  # Never cancel deployment
```

---

## Job Configuration

### Runners and Platforms

**Runner selection**:

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest  # Default; fastest for most tasks

  build-multi-platform:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        node-version: ['18', '20', '22']
      exclude:
        - os: windows-latest
          node-version: '18'  # Skip unsupported combinations
```

**Runner size** (for performance):

```yaml
runs-on: ubuntu-latest
timeout-minutes: 30  # Prevent hung jobs
```

### Job Dependencies and Ordering

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      artifact_path: ${{ steps.package.outputs.path }}
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683
      - id: package
        run: |
          zip -r dist.zip dist
          echo "path=dist.zip" >> "$GITHUB_OUTPUT"

  deploy:
    needs: [build, test]  # Wait for build and test
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying ${{ needs.build.outputs.artifact_path }}"
```

---

## Security Standards

### Permissions (Principle of Least Privilege)

**Default: Read-only**

```yaml
permissions:
  contents: read  # Default, safe starting point
```

**Add permissions only when needed**:

```yaml
permissions:
  contents: write          # For pushing commits
  pull-requests: write     # For PR comments
  packages: write          # For container registry
  checks: write            # For check runs
  issues: write            # For issue creation
```

**Job-level override** (most restrictive):

```yaml
jobs:
  lint:
    permissions:
      contents: read    # This job only needs read access

  deploy:
    permissions:
      contents: write   # Deploy job needs write access
```

### Action Pinning (Security Critical)

**MUST pin to full commit SHA** (not version tags):

```yaml
# ✅ CORRECT: SHA pinned with version comment
- uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2

# ❌ WRONG: Using tag (vulnerable to compromise)
- uses: actions/checkout@v4

# ❌ WRONG: Using branch (extremely dangerous)
- uses: actions/checkout@main
```

**How to find SHA**:

```bash
# Get latest SHA for a version
gh api repos/owner/repo/git/refs/tags/v4.2.2 --jq '.object.sha'

# Or check releases page: https://github.com/actions/checkout/releases/tag/v4.2.2
```

### Secrets Management

**Never hardcode secrets**:

```yaml
# ❌ BAD: Hardcoded credentials
- run: curl -H "Authorization: token ghp_xxxxxxxxxxxx" https://api.github.com/...

# ✅ GOOD: Use GitHub Secrets
- run: curl -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" https://api.github.com/...
```

**Environment-specific secrets**:

```yaml
deploy:
  environment:
    name: production
    url: https://prod.example.com
  steps:
    - run: ./deploy.sh
      env:
        API_KEY: ${{ secrets.PROD_API_KEY }}
        DATABASE_URL: ${{ secrets.PROD_DATABASE_URL }}
```

**Secret masking in logs** (automatic):

```yaml
- run: |
    echo "Token: ${{ secrets.API_TOKEN }}"  # Automatically masked in logs
```

### OIDC Authentication (Preferred over Long-Lived Tokens)

Replace static credentials with OIDC for cloud providers:

```yaml
# AWS example
permissions:
  id-token: write
  contents: read

steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::ACCOUNT_ID:role/github-oidc-role
      aws-region: us-east-1
  - run: aws s3 ls
```

### Dependency Review

Enable Dependabot and GitHub's Dependency Review on PRs:

```yaml
# In repository settings:
# 1. Enable "Require status checks to pass before merging"
# 2. Add "Dependency review" as required check
# 3. Enable Dependabot security/version updates
```

### Security Scanning

**CodeQL for SAST**:

```yaml
name: CodeQL

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * 0'  # Weekly

jobs:
  analyze:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683
      - uses: github/codeql-action/init@v3
        with:
          languages: ['python', 'javascript']
      - uses: github/codeql-action/autobuild@v3
      - uses: github/codeql-action/analyze@v3
```

**Secret Scanning**:

Enable in Settings → Security & analysis → Secret scanning.
Ensure "Push protection" is enabled to prevent commits with secrets.

---

## Job Configuration

### Steps and Actions

**Step anatomy**:

```yaml
- name: Build application
  id: build                          # For referencing outputs
  run: npm run build                 # Inline shell command
  shell: bash                        # Explicit shell
  working-directory: ./src           # Change directory
  env:                               # Step-level env vars
    NODE_ENV: production
  timeout-minutes: 10                # Step timeout
  continue-on-error: false           # Continue if fails?
```

**Action anatomy**:

```yaml
- name: Setup Node.js
  uses: actions/setup-node@11bd71901bbe5b1630ceea73d27597364c9af683  # SHA pinned
  with:
    node-version: '20'               # Action inputs
    cache: 'npm'                     # Enable caching
```

### Conditional Execution

```yaml
- name: Deploy to production
  if: |
    github.event_name == 'push' &&
    github.ref == 'refs/heads/main' &&
    github.repository == 'owner/repo'
  run: ./deploy.sh

# Or using job-level conditions
deploy:
  if: github.ref == 'refs/heads/main'
  runs-on: ubuntu-latest
```

### Artifact Handling

```yaml
- name: Upload build artifacts
  uses: actions/upload-artifact@v4
  with:
    name: build-artifacts
    path: dist/
    retention-days: 5              # Cleanup after 5 days
    compression-level: 9           # Maximum compression

- name: Download artifacts from previous job
  uses: actions/download-artifact@v4
  with:
    name: build-artifacts
    path: ./dist

- name: Clean up old artifacts
  run: |
    gh run list --repo ${{ github.repository }} \
      --status completed --json databaseId -q ".[].databaseId" | \
      xargs -I {} gh run delete {} --repo ${{ github.repository }}
```

---

## Performance Optimization

### Caching Strategy

**Cache dependencies with proper keys**:

```yaml
- name: Cache Node modules
  uses: actions/cache@0c907a75c2c80ebcb7f088228285e798b750cf8f
  with:
    path: |
      ~/.npm
      node_modules/
    key: ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}-${{ github.run_id }}
    restore-keys: |
      ${{ runner.os }}-npm-${{ hashFiles('**/package-lock.json') }}-
      ${{ runner.os }}-npm-
```

**Multiple cache levels**:

```yaml
- name: Cache Python dependencies
  uses: actions/cache@0c907a75c2c80ebcb7f088228285e798b750cf8f
  with:
    path: |
      ~/.cache/pip
      .venv/
    key: ${{ runner.os }}-python-${{ matrix.python-version }}-${{ hashFiles('**/requirements*.txt') }}
    restore-keys: |
      ${{ runner.os }}-python-${{ matrix.python-version }}-
      ${{ runner.os }}-python-
```

**Avoid cache bloat**:

```yaml
# Use multiple caches to avoid monolithic caches
- uses: actions/cache@0c907a75c2c80ebcb7f088228285e798b750cf8f
  with:
    path: ~/.cache/pip
    key: pip-${{ hashFiles('requirements.txt') }}

- uses: actions/cache@0c907a75c2c80ebcb7f088228285e798b750cf8f
  with:
    path: node_modules/
    key: npm-${{ hashFiles('package-lock.json') }}
```

### Matrix Builds (Parallel Testing)

```yaml
strategy:
  fail-fast: false
  matrix:
    os: [ubuntu-latest, macos-latest, windows-latest]
    python-version: ['3.11', '3.12', '3.13']
    exclude:
      - os: macos-latest
        python-version: '3.11'  # Not supported

jobs:
  test:
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pytest tests/
```

### Artifact Reuse Across Jobs

```yaml
build:
  runs-on: ubuntu-latest
  steps:
    - run: npm run build
    - uses: actions/upload-artifact@v4
      with:
        name: dist
        path: dist/

test:
  needs: build
  runs-on: ubuntu-latest
  steps:
    - uses: actions/download-artifact@v4
      with:
        name: dist
```

---

## Reusable Workflows

### Calling Reusable Workflows

```yaml
# In your project's .github/workflows/ci.yml
name: CI

on: [push, pull_request]

jobs:
  ci:
    uses: Ven0m0/.github/.github/workflows/reusable-ci-python.yml@main
    with:
      python-version: '3.12'
      coverage-threshold: 80
    secrets: inherit  # Pass all secrets to reusable workflow
```

**Explicit secrets**:

```yaml
uses: Ven0m0/.github/.github/workflows/reusable-ci.yml@main
with:
  python-version: '3.12'
secrets:
  CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}
  SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

### Creating Reusable Workflows

```yaml
# .github/workflows/reusable-ci-python.yml
name: Reusable Python CI

on:
  workflow_call:
    inputs:
      python-version:
        type: string
        required: false
        default: '3.12'
      coverage-threshold:
        type: number
        required: false
        default: 80
      test-args:
        type: string
        required: false
        default: ''
    secrets:
      CODECOV_TOKEN:
        required: false

permissions:
  contents: read
  checks: write

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ inputs.python-version }}
      - run: pip install -e ".[dev]"
      - run: ruff check .
      - run: mypy --strict .
      - run: pytest --cov ${{ inputs.test-args }}
      - uses: codecov/codecov-action@v3
        if: ${{ secrets.CODECOV_TOKEN }}
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
          fail_ci_if_error: true
          threshold: ${{ inputs.coverage-threshold }}
```

---

## Debugging Workflows

### Common Workflow Failures

| Error | Cause | Solution |
|-------|-------|----------|
| "Resource not accessible by integration" | Missing permissions | Add to `permissions:` section |
| Cache never hits | Wrong key format | Check `hashFiles()` paths exist |
| Secrets undefined | Wrong context | Use `secrets: inherit` for reusable workflows |
| Workflow not triggered | Event config wrong | Verify `on:` configuration |
| Timeout | Job too slow | Add `timeout-minutes`, optimize caching |

### Debug Steps

```yaml
- name: Debug context
  run: |
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    echo "SHA: ${{ github.sha }}"
    echo "Actor: ${{ github.actor }}"
    echo "Repo: ${{ github.repository }}"
```

### Enable Debug Logging

```bash
# Set in repository secrets:
ACTIONS_STEP_DEBUG: true
```

---

## Testing and Validation

### Code Quality Checks

```yaml
lint-and-format:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683

    # Python example
    - uses: actions/setup-python@v5
      with:
        python-version: '3.12'
        cache: 'pip'
    - run: pip install -e ".[dev]"
    - run: ruff check . && ruff format --check .
    - run: mypy --strict .

    # JavaScript example
    - uses: actions/setup-node@11bd71901bbe5b1630ceea73d27597364c9af683
      with:
        node-version: '20'
        cache: 'npm'
    - run: npm ci
    - run: npm run lint
    - run: npm run type-check
```

### Test Coverage Enforcement

```yaml
- name: Run tests with coverage
  run: pytest --cov=src --cov-report=xml --cov-report=term

- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    token: ${{ secrets.CODECOV_TOKEN }}
    fail_ci_if_error: true
    threshold: 80  # Fail if coverage < 80%
```

---

## Deployment Patterns

### Manual Approval Deployments

```yaml
deploy:
  environment:
    name: production
    url: https://prod.example.com
    auto_inactive_secs: 3600  # Timeout after 1 hour
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683
    - run: |
        echo "Deploying to ${{ github.environment }}"
        ./scripts/deploy.sh
```

### Blue-Green Deployment

```yaml
deploy-blue-green:
  environment: production
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683
    - name: Deploy to green environment
      run: |
        ./scripts/deploy-green.sh
    - name: Run smoke tests
      run: ./scripts/smoke-test.sh --target green
    - name: Switch traffic to green
      run: |
        ./scripts/switch-traffic.sh green
```

### Rollback Mechanism

```yaml
rollback:
  environment: production
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683
      with:
        ref: ${{ github.event.inputs.rollback_version }}
    - run: ./scripts/deploy.sh
    - name: Verify rollback
      run: ./scripts/verify.sh
```

---

## Workflow Templates and Examples

### Python Project Template

```yaml
name: Python CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  workflow_dispatch:

jobs:
  lint-and-test:
    uses: Ven0m0/.github/.github/workflows/reusable-ci-python.yml@main
    with:
      python-version: '3.12'
      coverage-threshold: 85

  security:
    uses: Ven0m0/.github/.github/workflows/reusable-security.yml@main
    secrets: inherit
```

### Node.js Project Template

```yaml
name: Node.js CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    uses: Ven0m0/.github/.github/workflows/reusable-ci-typescript.yml@main
    with:
      node-version: '20'
      coverage-threshold: 80
    secrets: inherit
```

---

## Workflow Validation

```bash
# Validate workflow YAML syntax
actionlint .github/workflows/

# Check for untracked secrets
gitleaks detect --source github -v

# Test workflow locally (requires act)
act push --job lint-and-test
```

---

## CI/CD Checklist

- [ ] All workflows use SHA-pinned actions
- [ ] Permissions are explicit and minimal
- [ ] Secrets are not logged or exposed
- [ ] Caching is configured for performance
- [ ] Workflows have timeouts
- [ ] Tests pass before deployment
- [ ] Coverage thresholds are enforced
- [ ] Security scanning is enabled
- [ ] Dependabot is configured
- [ ] Manual approval for production
- [ ] Rollback plan documented
- [ ] Artifacts cleaned up automatically

---

## Resources

- **GitHub Actions**: https://docs.github.com/en/actions
- **Workflow Syntax**: https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions
- **OIDC Guide**: https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect
- **Action Security**: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions
- **Reusable Workflows**: https://docs.github.com/en/actions/using-workflows/reusing-workflows

