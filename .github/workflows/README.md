# Reusable GitHub Actions Workflows

This repository contains hardened, production-ready reusable workflows for your organization. All workflows follow security best practices and are designed for maximum flexibility.

## 📋 Table of Contents

- [Available Workflows](#available-workflows)
- [Quick Start](#quick-start)
- [Security Features](#security-features)
- [Validation & Testing](#validation--testing)
- [Contributing](#contributing)

## 🚀 Available Workflows

### 1. Node.js CI/CD (`nodejs-ci.yml`)

Comprehensive Node.js testing and build workflow supporting npm, yarn, pnpm, and bun.

**Features:**
- Multi-package manager support (npm, yarn, pnpm, bun)
- Dependency caching
- Configurable linting, testing, and building
- Code coverage with Codecov integration
- Build artifact uploads

**Usage:**
```yaml
jobs:
  test:
    uses: Ven0m0/.github/.github/workflows/nodejs-ci.yml@main
    with:
      node-version: '20'
      package-manager: 'npm'
      run-tests: true
      run-build: true
      coverage: true
    secrets:
      NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
      CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}
```

**Inputs:**
- `node-version` (default: `'20'`) - Node.js version
- `package-manager` (default: `'npm'`) - Package manager: npm, yarn, pnpm, or bun
- `working-directory` (default: `'.'`) - Working directory
- `run-install` (default: `true`) - Run package installation
- `run-lint` (default: `true`) - Run linting
- `run-tests` (default: `true`) - Run tests
- `run-build` (default: `true`) - Run build
- `coverage` (default: `false`) - Generate code coverage
- `cache-dependency-path` (default: `''`) - Path to lock file
- `timeout-minutes` (default: `15`) - Job timeout

---

### 2. Python CI/CD (`python-ci.yml`)

Complete Python testing workflow supporting pip, uv, and poetry.

**Features:**
- Multi-package manager support (pip, uv, poetry)
- Dependency caching
- Linting with Ruff
- Format checking
- Type checking with mypy
- Code coverage with pytest

**Usage:**
```yaml
jobs:
  test:
    uses: Ven0m0/.github/.github/workflows/python-ci.yml@main
    with:
      python-version: '3.12'
      package-manager: 'uv'
      run-lint: true
      run-tests: true
      coverage: true
    secrets:
      CODECOV_TOKEN: ${{ secrets.CODECOV_TOKEN }}
```

**Inputs:**
- `python-version` (default: `'3.12'`) - Python version
- `package-manager` (default: `'pip'`) - Package manager: pip, uv, or poetry
- `working-directory` (default: `'.'`) - Working directory
- `run-install` (default: `true`) - Run package installation
- `run-lint` (default: `true`) - Run linting
- `run-format-check` (default: `true`) - Check formatting
- `run-type-check` (default: `false`) - Run mypy type checking
- `run-tests` (default: `true`) - Run tests
- `coverage` (default: `false`) - Generate code coverage
- `requirements-file` (default: `'requirements.txt'`) - Path to requirements
- `timeout-minutes` (default: `15`) - Job timeout

---

### 3. Security Scanning (`security-scan.yml`)

Comprehensive security scanning with CodeQL, Trivy, and Dependency Review.

**Features:**
- CodeQL SAST analysis
- Trivy vulnerability scanning
- Dependency review (for PRs)
- Optional Snyk integration
- SARIF report uploads to GitHub Security

**Usage:**
```yaml
jobs:
  security:
    permissions:
      contents: read
      security-events: write
    uses: Ven0m0/.github/.github/workflows/security-scan.yml@main
    with:
      language: 'javascript'
      run-codeql: true
      run-trivy: true
      run-dependency-review: true
    secrets:
      SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

**Inputs:**
- `language` (default: `'javascript'`) - CodeQL language
- `working-directory` (default: `'.'`) - Working directory
- `run-codeql` (default: `true`) - Run CodeQL analysis
- `run-trivy` (default: `true`) - Run Trivy scanner
- `run-dependency-review` (default: `true`) - Run dependency review
- `trivy-scan-type` (default: `'fs'`) - Trivy scan type
- `trivy-severity` (default: `'CRITICAL,HIGH'`) - Severity filter
- `fail-on-severity` (default: `'CRITICAL'`) - Fail threshold
- `timeout-minutes` (default: `20`) - Job timeout

---

### 4. Docker Build & Push (`docker-build.yml`)

Secure Docker image building with SBOM generation and vulnerability scanning.

**Features:**
- Multi-platform builds (arm64, amd64)
- SBOM generation with Syft
- Provenance attestation
- Trivy vulnerability scanning
- Build caching
- GitHub Container Registry support

**Usage:**
```yaml
jobs:
  docker:
    permissions:
      contents: read
      packages: write
      id-token: write
      attestations: write
      security-events: write
    uses: Ven0m0/.github/.github/workflows/docker-build.yml@main
    with:
      image-name: 'myorg/myapp'
      registry: 'ghcr.io'
      platforms: 'linux/amd64,linux/arm64'
      push: true
      scan-image: true
      generate-sbom: true
      provenance: true
    secrets:
      DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
      DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
```

**Inputs:**
- `image-name` (required) - Docker image name
- `registry` (default: `'docker.io'`) - Container registry
- `platforms` (default: `'linux/amd64'`) - Target platforms
- `dockerfile` (default: `'./Dockerfile'`) - Dockerfile path
- `context` (default: `'.'`) - Build context
- `build-args` (default: `''`) - Build arguments
- `tags` (default: `''`) - Additional tags
- `push` (default: `true`) - Push to registry
- `scan-image` (default: `true`) - Scan with Trivy
- `generate-sbom` (default: `true`) - Generate SBOM
- `provenance` (default: `true`) - Generate provenance
- `cache-to` (default: `'type=gha,mode=max'`) - Cache destination
- `timeout-minutes` (default: `30`) - Job timeout

---

### 5. Linting & Formatting (`lint.yml`)

Multi-language linting and formatting validation.

**Features:**
- ESLint for JavaScript/TypeScript
- Prettier for formatting
- Ruff for Python
- actionlint for workflows
- yamllint, markdownlint, shellcheck
- Super-Linter fallback

**Usage:**
```yaml
jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/lint.yml@main
    with:
      run-eslint: true
      run-prettier: true
      run-actionlint: true
      run-yamllint: true
```

**Inputs:**
- `working-directory` (default: `'.'`) - Working directory
- `run-eslint` (default: `false`) - Run ESLint
- `run-prettier` (default: `false`) - Run Prettier
- `run-ruff` (default: `false`) - Run Ruff
- `run-black` (default: `false`) - Run Black
- `run-mypy` (default: `false`) - Run mypy
- `run-actionlint` (default: `true`) - Run actionlint
- `run-yamllint` (default: `false`) - Run yamllint
- `run-markdownlint` (default: `false`) - Run markdownlint
- `run-shellcheck` (default: `false`) - Run shellcheck
- `eslint-extensions` (default: `'js,ts,jsx,tsx'`) - ESLint extensions
- `timeout-minutes` (default: `10`) - Job timeout

---

### 6. Release Management (`release.yml`)

Automated release creation with changelog generation.

**Features:**
- Automatic version detection
- Changelog generation
- GitHub releases
- npm and PyPI publishing
- Artifact uploads

**Usage:**
```yaml
jobs:
  release:
    permissions:
      contents: write
      id-token: write
    uses: Ven0m0/.github/.github/workflows/release.yml@main
    with:
      create-github-release: true
      generate-changelog: true
      publish-npm: true
    secrets:
      NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```

**Inputs:**
- `working-directory` (default: `'.'`) - Working directory
- `create-github-release` (default: `true`) - Create GitHub release
- `generate-changelog` (default: `true`) - Generate changelog
- `publish-npm` (default: `false`) - Publish to npm
- `publish-pypi` (default: `false`) - Publish to PyPI
- `prerelease` (default: `false`) - Mark as prerelease
- `draft` (default: `false`) - Create as draft
- `tag-name` (default: `''`) - Release tag name
- `release-notes` (default: `''`) - Custom release notes
- `artifact-paths` (default: `''`) - Artifact paths
- `timeout-minutes` (default: `20`) - Job timeout

---

### 7. PR Automation (`pr-automation.yml`)

Automated pull request management and validation.

**Features:**
- Auto-labeling based on changed files
- Size labeling (XS, S, M, L, XL)
- Merge conflict detection
- Conventional commits validation
- Auto-reviewer assignment
- Checklist validation

**Usage:**
```yaml
jobs:
  pr-automation:
    permissions:
      contents: read
      pull-requests: write
    uses: Ven0m0/.github/.github/workflows/pr-automation.yml@main
    with:
      enable-auto-label: true
      enable-size-label: true
      enable-conflict-check: true
      enable-conventional-commits: true
```

**Inputs:**
- `enable-auto-label` (default: `true`) - Auto-label PRs
- `enable-size-label` (default: `true`) - Add size labels
- `enable-conflict-check` (default: `true`) - Check conflicts
- `enable-auto-assign` (default: `false`) - Auto-assign reviewers
- `enable-conventional-commits` (default: `false`) - Validate commit format
- `enable-checklist` (default: `false`) - Validate checklist
- `size-xs-lines` (default: `10`) - Max lines for XS
- `size-s-lines` (default: `100`) - Max lines for S
- `size-m-lines` (default: `500`) - Max lines for M
- `size-l-lines` (default: `1000`) - Max lines for L
- `timeout-minutes` (default: `10`) - Job timeout

---

## 🔐 Security Features

All workflows implement these security best practices:

1. **Hardened Runner** - Step Security's harden-runner for egress auditing
2. **Pinned Action Versions** - All actions pinned to specific SHA hashes
3. **Least Privilege Permissions** - Explicit, minimal permissions per job
4. **No Credential Persistence** - `persist-credentials: false` on checkouts
5. **Shallow Clones** - `fetch-depth: 1` to minimize exposure
6. **Secret Scanning** - Trivy and other scanners check for exposed secrets
7. **Dependency Validation** - Dependency review on PRs
8. **SBOM Generation** - Software Bill of Materials for containers
9. **Provenance Attestation** - Cryptographic proof of build integrity

## ✅ Validation & Testing

### Local Validation

Install actionlint:
```bash
bash <(curl https://raw.githubusercontent.com/rhysd/actionlint/main/scripts/download-actionlint.bash)
```

Validate workflows:
```bash
actionlint .github/workflows/*.yml
```

### YAML Linting

Install yamllint:
```bash
pip install yamllint
```

Lint workflows:
```bash
yamllint .github/workflows/
```

### Local Testing with Act

Install act:
```bash
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```

Test workflow locally:
```bash
act -W .github/workflows/nodejs-ci.yml
```

## 📊 Workflow Matrix

| Workflow | Languages | Security | Caching | Artifacts | Publishing |
|----------|-----------|----------|---------|-----------|------------|
| nodejs-ci | JS/TS | ✅ | ✅ | ✅ | ❌ |
| python-ci | Python | ✅ | ✅ | ❌ | ❌ |
| security-scan | All | ✅✅✅ | ❌ | ✅ | ❌ |
| docker-build | All | ✅✅ | ✅ | ✅ | ✅ |
| lint | Multi | ✅ | ✅ | ❌ | ❌ |
| release | All | ✅ | ❌ | ✅ | ✅ |
| pr-automation | All | ❌ | ❌ | ❌ | ❌ |

## 🔄 Rollback Instructions

If you need to rollback to a previous version:

1. **Identify the commit to rollback to:**
   ```bash
   git log --oneline .github/workflows/
   ```

2. **Revert to specific commit:**
   ```bash
   git revert <commit-hash>
   git push origin main
   ```

3. **Update workflow references in consuming repositories:**
   ```yaml
   # Change from @main to specific commit
   uses: Ven0m0/.github/.github/workflows/nodejs-ci.yml@<commit-sha>
   ```

## 🤝 Contributing

When adding or modifying workflows:

1. Always pin action versions to SHA hashes
2. Run actionlint validation before committing
3. Test with act if possible
4. Update this README with new inputs/features
5. Follow existing patterns for consistency
6. Maintain explicit permissions
7. Add step descriptions for clarity

## 📝 Validation Status

All workflows validated with:
- ✅ actionlint v1.7.9
- ✅ GitHub Actions schema validation
- ✅ YAML syntax validation
- ✅ Security best practices review

## 🔗 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Reusable Workflows Guide](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [Security Hardening Guide](https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions)
- [actionlint Documentation](https://github.com/rhysd/actionlint)
