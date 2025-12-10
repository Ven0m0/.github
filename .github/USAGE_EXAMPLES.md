# Reusable Workflows - Usage Examples

Complete usage examples for all reusable workflows in this repository.

## Table of Contents

- [Full Stack Node.js Application](#full-stack-nodejs-application)
- [Python Library](#python-library)
- [Docker Application](#docker-application)
- [Multi-Language Monorepo](#multi-language-monorepo)
- [Complete CI/CD Pipeline](#complete-cicd-pipeline)

---

## Full Stack Node.js Application

A complete workflow for a Node.js application with testing, linting, security scanning, and Docker deployment.

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  # Run linting first
  lint:
    uses: Ven0m0/.github/.github/workflows/lint.yml@main
    permissions:
      contents: read
      pull-requests: write
    with:
      run-eslint: true
      run-prettier: true
      run-actionlint: true

  # Run tests across Node.js versions
  test:
    needs: lint
    strategy:
      matrix:
        node-version: ['18', '20', '22']
    uses: Ven0m0/.github/.github/workflows/nodejs-ci.yml@main
    with:
      node-version: ${{ matrix.node-version }}
      package-manager: 'npm'
      run-tests: true
      run-build: true
      coverage: true
    secrets:
      NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
      CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}

  # Security scanning
  security:
    needs: lint
    uses: Ven0m0/.github/.github/workflows/security-scan.yml@main
    permissions:
      contents: read
      security-events: write
      pull-requests: write
    with:
      language: 'javascript'
      run-codeql: true
      run-trivy: true
      run-dependency-review: true

  # Build and push Docker image (only on main)
  docker:
    if: github.ref == 'refs/heads/main'
    needs: [test, security]
    uses: Ven0m0/.github/.github/workflows/docker-build.yml@main
    permissions:
      contents: read
      packages: write
      id-token: write
      attestations: write
      security-events: write
    with:
      image-name: 'myorg/myapp'
      registry: 'ghcr.io'
      platforms: 'linux/amd64,linux/arm64'
      dockerfile: './Dockerfile'
      push: true
      scan-image: true
      generate-sbom: true
      provenance: true

  # PR automation
  pr-automation:
    if: github.event_name == 'pull_request'
    uses: Ven0m0/.github/.github/workflows/pr-automation.yml@main
    permissions:
      contents: read
      pull-requests: write
      issues: write
    with:
      enable-auto-label: true
      enable-size-label: true
      enable-conflict-check: true
      enable-conventional-commits: true
```

---

## Python Library

Workflow for a Python library with multiple Python versions, linting, and PyPI publishing.

```yaml
name: Python Library CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  release:
    types: [published]

permissions:
  contents: read

jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/lint.yml@main
    permissions:
      contents: read
      pull-requests: write
    with:
      run-ruff: true
      run-actionlint: true
      run-yamllint: true

  test:
    needs: lint
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']
    uses: Ven0m0/.github/.github/workflows/python-ci.yml@main
    with:
      python-version: ${{ matrix.python-version }}
      package-manager: 'uv'
      run-lint: true
      run-format-check: true
      run-type-check: true
      run-tests: true
      coverage: true
    secrets:
      CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}

  security:
    uses: Ven0m0/.github/.github/workflows/security-scan.yml@main
    permissions:
      contents: read
      security-events: write
    with:
      language: 'python'
      run-codeql: true
      run-trivy: true

  release:
    if: github.event_name == 'release'
    needs: [test, security]
    uses: Ven0m0/.github/.github/workflows/release.yml@main
    permissions:
      contents: write
      id-token: write
    with:
      create-github-release: true
      generate-changelog: true
      publish-pypi: true
    secrets:
      PYPI_TOKEN: ${{ secrets.PYPI_TOKEN }}
```

---

## Docker Application

Complete Docker workflow with multi-stage builds, security scanning, and multi-platform support.

```yaml
name: Docker Build & Deploy

on:
  push:
    branches: [main]
    tags: ['v*']
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  docker:
    uses: Ven0m0/.github/.github/workflows/docker-build.yml@main
    permissions:
      contents: read
      packages: write
      id-token: write
      attestations: write
      security-events: write
    with:
      image-name: 'myorg/myapp'
      registry: 'ghcr.io'
      platforms: 'linux/amd64,linux/arm64'
      dockerfile: './Dockerfile'
      context: '.'
      build-args: |
        NODE_ENV=production
        BUILD_DATE=${{ github.event.repository.updated_at }}
        VCS_REF=${{ github.sha }}
      push: ${{ github.event_name != 'pull_request' }}
      scan-image: true
      generate-sbom: true
      provenance: true
      cache-to: 'type=gha,mode=max'
```

---

## Multi-Language Monorepo

Workflow for a monorepo with multiple languages and services.

```yaml
name: Monorepo CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  # Detect changes
  changes:
    runs-on: ubuntu-24.04
    outputs:
      frontend: ${{ steps.filter.outputs.frontend }}
      backend: ${{ steps.filter.outputs.backend }}
      api: ${{ steps.filter.outputs.api }}
    steps:
      - uses: actions/checkout@v4
      - uses: dorny/paths-filter@v3
        id: filter
        with:
          filters: |
            frontend:
              - 'apps/frontend/**'
            backend:
              - 'apps/backend/**'
            api:
              - 'apps/api/**'

  # Frontend (Node.js)
  frontend:
    needs: changes
    if: needs.changes.outputs.frontend == 'true'
    uses: Ven0m0/.github/.github/workflows/nodejs-ci.yml@main
    with:
      working-directory: './apps/frontend'
      package-manager: 'pnpm'
      node-version: '20'
      run-tests: true
      run-build: true

  # Backend (Python)
  backend:
    needs: changes
    if: needs.changes.outputs.backend == 'true'
    uses: Ven0m0/.github/.github/workflows/python-ci.yml@main
    with:
      working-directory: './apps/backend'
      package-manager: 'uv'
      python-version: '3.12'
      run-tests: true
      coverage: true

  # API (Go - custom workflow)
  api:
    needs: changes
    if: needs.changes.outputs.api == 'true'
    runs-on: ubuntu-24.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'
      - run: go test ./...
        working-directory: ./apps/api

  # Security scanning for entire repo
  security:
    uses: Ven0m0/.github/.github/workflows/security-scan.yml@main
    permissions:
      contents: read
      security-events: write
    with:
      language: 'javascript'
      run-codeql: true
      run-trivy: true
```

---

## Complete CI/CD Pipeline

End-to-end pipeline with testing, security, release, and deployment.

```yaml
name: Complete CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]
  release:
    types: [published]

permissions:
  contents: read

jobs:
  # Stage 1: Code Quality
  lint:
    uses: Ven0m0/.github/.github/workflows/lint.yml@main
    permissions:
      contents: read
      pull-requests: write
    with:
      run-eslint: true
      run-prettier: true
      run-actionlint: true
      run-markdownlint: true

  # Stage 2: Testing
  test:
    needs: lint
    uses: Ven0m0/.github/.github/workflows/nodejs-ci.yml@main
    with:
      node-version: '20'
      package-manager: 'bun'
      run-tests: true
      run-build: true
      coverage: true
    secrets:
      CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}

  # Stage 3: Security
  security:
    needs: lint
    uses: Ven0m0/.github/.github/workflows/security-scan.yml@main
    permissions:
      contents: read
      security-events: write
      pull-requests: write
    with:
      language: 'typescript'
      run-codeql: true
      run-trivy: true
      run-dependency-review: true
      trivy-severity: 'CRITICAL,HIGH,MEDIUM'
      fail-on-severity: 'HIGH'
    secrets:
      SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

  # Stage 4: Build & Push Container (main/tags only)
  build-image:
    if: github.ref == 'refs/heads/main' || startsWith(github.ref, 'refs/tags/v')
    needs: [test, security]
    uses: Ven0m0/.github/.github/workflows/docker-build.yml@main
    permissions:
      contents: read
      packages: write
      id-token: write
      attestations: write
      security-events: write
    with:
      image-name: '${{ github.repository }}'
      registry: 'ghcr.io'
      platforms: 'linux/amd64,linux/arm64'
      push: true
      scan-image: true
      generate-sbom: true
      provenance: true
      tags: |
        type=ref,event=branch
        type=semver,pattern={{version}}
        type=semver,pattern={{major}}.{{minor}}
        type=sha

  # Stage 5: Release (on tag push)
  release:
    if: startsWith(github.ref, 'refs/tags/v')
    needs: build-image
    uses: Ven0m0/.github/.github/workflows/release.yml@main
    permissions:
      contents: write
      id-token: write
    with:
      create-github-release: true
      generate-changelog: true
      publish-npm: true
      prerelease: false
      artifact-paths: |
        dist/**
        build/**
    secrets:
      NPM_TOKEN: ${{ secrets.NPM_TOKEN }}

  # PR Automation (PRs only)
  pr-automation:
    if: github.event_name == 'pull_request'
    uses: Ven0m0/.github/.github/workflows/pr-automation.yml@main
    permissions:
      contents: read
      pull-requests: write
      issues: write
    with:
      enable-auto-label: true
      enable-size-label: true
      enable-conflict-check: true
      enable-conventional-commits: true
      enable-checklist: true
```

---

## Advanced Patterns

### Conditional Workflow Based on File Changes

```yaml
jobs:
  changes:
    runs-on: ubuntu-24.04
    outputs:
      code: ${{ steps.filter.outputs.code }}
      docs: ${{ steps.filter.outputs.docs }}
    steps:
      - uses: actions/checkout@v4
      - uses: dorny/paths-filter@v3
        id: filter
        with:
          filters: |
            code:
              - 'src/**'
              - 'package.json'
            docs:
              - 'docs/**'
              - '**/*.md'

  test:
    needs: changes
    if: needs.changes.outputs.code == 'true'
    uses: Ven0m0/.github/.github/workflows/nodejs-ci.yml@main
    # ... rest of config
```

### Matrix Strategy with Reusable Workflows

```yaml
jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-24.04, windows-latest, macos-latest]
        node: ['18', '20', '22']
    uses: Ven0m0/.github/.github/workflows/nodejs-ci.yml@main
    with:
      node-version: ${{ matrix.node }}
```

### Deployment Pipeline with Environments

```yaml
jobs:
  deploy-staging:
    if: github.ref == 'refs/heads/develop'
    needs: [test, security]
    uses: Ven0m0/.github/.github/workflows/docker-build.yml@main
    with:
      image-name: 'myapp'
      tags: 'staging'
      push: true
    environment:
      name: staging
      url: https://staging.example.com

  deploy-production:
    if: github.ref == 'refs/heads/main'
    needs: [test, security]
    uses: Ven0m0/.github/.github/workflows/docker-build.yml@main
    with:
      image-name: 'myapp'
      tags: 'production,latest'
      push: true
    environment:
      name: production
      url: https://example.com
```

---

## Tips & Best Practices

1. **Pin workflow versions**: Use specific commits/tags instead of `@main` in production
   ```yaml
   uses: Ven0m0/.github/.github/workflows/nodejs-ci.yml@v1.0.0
   ```

2. **Use concurrency controls**: Prevent duplicate workflow runs
   ```yaml
   concurrency:
     group: ${{ github.workflow }}-${{ github.ref }}
     cancel-in-progress: true
   ```

3. **Separate dev and prod workflows**: Use different workflow files or conditions

4. **Cache aggressively**: All workflows include intelligent caching

5. **Use required checks**: Configure branch protection with required status checks

6. **Monitor workflow usage**: Track Actions minutes in GitHub Insights

7. **Use environments**: Leverage GitHub Environments for deployment approval

8. **Secrets management**: Use environment-specific secrets

9. **Failed workflow notifications**: Set up Slack/email notifications

10. **Regular audits**: Review and update workflows quarterly
