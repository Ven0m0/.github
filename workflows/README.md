# Reusable GitHub Actions Workflows

This repository contains a collection of optimized, reusable GitHub Actions workflows that can be called from other repositories to maintain consistency and reduce code duplication.

## Available Workflows

### 1. MegaLinter (`mega-linter.yml`)

Comprehensive linting for multiple file types using OxSecurity MegaLinter.

**Usage:**
```yaml
name: Lint Code
on: [push, pull_request]

jobs:
  megalinter:
    uses: Ven0m0/.github/.github/workflows/mega-linter.yml@main
    with:
      exclude_dirs: '.git,.cache,node_modules'
      validate_all: false
      apply_fixes: 'all'
    secrets: inherit
```

**Inputs:**
- `exclude_dirs` (string): Comma-separated directories to exclude (default: `.github,.git,.cache,node_modules`)
- `config_file` (string): Path to MegaLinter config (default: `.megalinter.yml`)
- `apply_fixes` (string): Apply fixes automatically (default: `all`)
- `validate_all` (boolean): Validate all files, not just changed (default: `false`)

**Features:**
- Auto-fixes linting issues
- Archives reports as artifacts
- Creates detailed job summaries
- Commits fixes back to PRs

---

### 2. Shell Lint (`shell-lint.yml`)

Focused shell script linting with ShellCheck, shfmt, and shellharden.

**Usage:**
```yaml
name: Shell Lint
on: [push, pull_request]

jobs:
  shell-lint:
    uses: Ven0m0/.github/.github/workflows/shell-lint.yml@main
    with:
      shellcheck_severity: 'style'
      shfmt_indent: 2
      apply_fixes: true
      commit_changes: true
    secrets: inherit
```

**Inputs:**
- `exclude_pattern` (string): Regex to exclude files (default: `(^|/)\.(git|cache|claude)(/|$)`)
- `shellcheck_severity` (string): Min severity level (default: `style`)
- `shfmt_indent` (number): Indentation spaces (default: `2`)
- `apply_fixes` (boolean): Apply auto-fixes (default: `true`)
- `commit_changes` (boolean): Commit and push fixes (default: `true`)

**Features:**
- Runs ShellCheck, shfmt, and shellharden
- Caches tools for faster execution
- Detailed file counts in job summary
- Auto-commits fixes with proper attribution

---

### 3. Unified Linters (`unified-linters.yml`)

Multi-linter workflow combining ShellCheck (via Reviewdog) and Super-Linter.

**Usage:**
```yaml
name: Unified Linting
on: [pull_request]

jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/unified-linters.yml@main
    with:
      enable_shellcheck: true
      enable_super_linter: true
      enable_reviewdog: true
      apply_fixes: true
    secrets: inherit
```

**Inputs:**
- `enable_shellcheck` (boolean): Enable ShellCheck (default: `true`)
- `enable_super_linter` (boolean): Enable Super-Linter (default: `true`)
- `enable_reviewdog` (boolean): Enable Reviewdog for PR comments (default: `true`)
- `validate_all_codebase` (boolean): Validate entire codebase (default: `false`)
- `exclude_paths` (string): Paths to exclude (default: `*/.git/*,./.cache/*,./.claude/*`)
- `apply_fixes` (boolean): Apply automatic fixes (default: `true`)

**Features:**
- Reviewdog integration for inline PR comments
- Multiple linting jobs that can run in parallel
- Caches Super-Linter for performance
- Separate fix and review jobs

---

### 4. Image Optimization (`img-opt.yml`)

Optimize and convert images to modern formats (WebP, AVIF).

**Usage:**
```yaml
name: Optimize Images
on:
  push:
    paths:
      - '**.png'
      - '**.jpg'
      - '**.jpeg'
      - '**.gif'
      - '**.svg'

jobs:
  optimize:
    uses: Ven0m0/.github/.github/workflows/img-opt.yml@main
    with:
      export_webp: true
      export_avif: false
      replace_original: false
      quality: 85
    secrets: inherit
```

**Inputs:**
- `export_webp` (boolean): Export to WebP format (default: `true`)
- `export_avif` (boolean): Export to AVIF format (default: `false`)
- `replace_original` (boolean): Replace originals after conversion (default: `false`)
- `compress_png` (boolean): Compress PNG images (default: `true`)
- `compress_jpg` (boolean): Compress JPG/JPEG images (default: `true`)
- `compress_svg` (boolean): Compress SVG images (default: `true`)
- `quality` (number): Output quality 1-100 (default: `85`)

**Features:**
- Finds and counts images before processing
- Calculates space savings
- Comments on PRs with results
- Archives optimization reports
- Smart original file removal

---

### 5. Dependabot Auto-Merge (`dependabot-automerge.yml`)

Automatically approve and merge Dependabot PRs based on update type.

**Usage:**
```yaml
name: Dependabot Auto-Merge
on: pull_request

jobs:
  dependabot:
    uses: Ven0m0/.github/.github/workflows/dependabot-automerge.yml@main
    with:
      merge_method: 'squash'
      auto_approve: true
      auto_merge: true
      update_types: 'patch,minor'
      exclude_packages: 'react,next'
    secrets: inherit
```

**Inputs:**
- `merge_method` (string): Merge method (merge, squash, rebase) (default: `squash`)
- `auto_approve` (boolean): Auto-approve Dependabot PRs (default: `true`)
- `auto_merge` (boolean): Auto-merge Dependabot PRs (default: `true`)
- `update_types` (string): Allowed update types (default: `patch,minor`)
- `exclude_packages` (string): Packages to exclude from auto-merge (default: `''`)

**Features:**
- Fetches Dependabot metadata
- Validates update types
- Excludes specific packages
- Comments on PRs when skipped
- Detailed job summaries

---

### 6. Submodule Update (`submodules.yml`)

Automatically update git submodules and create PRs.

**Usage:**
```yaml
name: Update Submodules
on:
  schedule:
    - cron: '0 0 * * 1'  # Weekly on Monday
  workflow_dispatch:

jobs:
  update:
    uses: Ven0m0/.github/.github/workflows/submodules.yml@main
    with:
      strategy: 'merge'
      auto_merge: false
      filter_blob: true
    secrets: inherit
```

**Inputs:**
- `strategy` (string): Update strategy (merge, rebase, checkout) (default: `merge`)
- `auto_merge` (boolean): Enable auto-merge for PR (default: `false`)
- `branch_prefix` (string): Branch name prefix (default: `chore/submodule-updates`)
- `filter_blob` (boolean): Use blob:none for partial clone (default: `true`)

**Features:**
- Lists current submodules
- Shows detailed change logs
- Creates or updates existing PRs
- Comprehensive update summaries
- Optional auto-merge support

---

## Best Practices

### 1. Version Pinning
Always reference a specific version or commit SHA in production:
```yaml
uses: Ven0m0/.github/.github/workflows/mega-linter.yml@v1.0.0
# or
uses: Ven0m0/.github/.github/workflows/mega-linter.yml@abc123def
```

### 2. Secrets Inheritance
Most workflows require `secrets: inherit` to access repository secrets:
```yaml
jobs:
  my-job:
    uses: Ven0m0/.github/.github/workflows/workflow.yml@main
    secrets: inherit
```

### 3. Concurrency Control
All workflows include built-in concurrency controls to prevent race conditions. You can add additional concurrency at the caller level:
```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/mega-linter.yml@main
```

### 4. Conditional Execution
Use path filters to run workflows only when relevant files change:
```yaml
on:
  push:
    paths:
      - '**.sh'
      - '**.bash'

jobs:
  shell-lint:
    uses: Ven0m0/.github/.github/workflows/shell-lint.yml@main
```

### 5. Combining Workflows
You can combine multiple reusable workflows:
```yaml
jobs:
  shell-lint:
    uses: Ven0m0/.github/.github/workflows/shell-lint.yml@main

  megalinter:
    uses: Ven0m0/.github/.github/workflows/mega-linter.yml@main

  images:
    uses: Ven0m0/.github/.github/workflows/img-opt.yml@main
```

---

## Common Configurations

### Minimal Setup
```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]

jobs:
  lint:
    uses: Ven0m0/.github/.github/workflows/mega-linter.yml@main
    secrets: inherit
```

### Full-Featured Setup
```yaml
# .github/workflows/quality.yml
name: Code Quality
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

concurrency:
  group: quality-${{ github.ref }}
  cancel-in-progress: true

jobs:
  shell-lint:
    uses: Ven0m0/.github/.github/workflows/shell-lint.yml@main
    with:
      shellcheck_severity: 'warning'
      apply_fixes: true
    secrets: inherit

  unified-linters:
    uses: Ven0m0/.github/.github/workflows/unified-linters.yml@main
    with:
      enable_reviewdog: true
      validate_all_codebase: false
    secrets: inherit

  images:
    if: contains(github.event.head_commit.message, '[optimize-images]')
    uses: Ven0m0/.github/.github/workflows/img-opt.yml@main
    with:
      export_webp: true
      quality: 90
    secrets: inherit
```

### Dependabot Integration
```yaml
# .github/workflows/dependabot.yml
name: Dependabot
on: pull_request

jobs:
  auto-merge:
    if: github.actor == 'dependabot[bot]'
    uses: Ven0m0/.github/.github/workflows/dependabot-automerge.yml@main
    with:
      update_types: 'patch,minor'
      exclude_packages: 'typescript,react'
    secrets: inherit
```

---

## Troubleshooting

### Workflow Not Triggering
- Ensure the calling workflow has the correct `on:` triggers
- Verify the workflow file is in `.github/workflows/`
- Check that `secrets: inherit` is set if the workflow needs secrets

### Permission Errors
All workflows declare their required permissions. If you encounter permission errors:
1. Check your repository settings → Actions → General → Workflow permissions
2. Ensure "Read and write permissions" is enabled
3. Verify specific permissions in the workflow file

### Commit Failures
If auto-commit features fail:
- Ensure the workflow has `contents: write` permission
- Check that branch protection rules allow bot commits
- Verify the repository allows GitHub Actions to create PRs

### Cache Issues
To clear workflow caches:
1. Go to Actions → Caches in your repository
2. Delete relevant caches
3. Re-run the workflow

---

## Contributing

To add a new reusable workflow:

1. Create the workflow file in `.github/workflows/`
2. Use `workflow_call` trigger
3. Define clear inputs with descriptions
4. Set appropriate permissions
5. Add concurrency controls
6. Include job summaries
7. Update this README

---

## License

These workflows are part of the Ven0m0/.github repository and are available for use in all Ven0m0 projects.

---

## Support

For issues or questions:
- Open an issue in the Ven0m0/.github repository
- Review the workflow file for detailed inline documentation
- Check GitHub Actions logs for specific error messages
