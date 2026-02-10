---
description: 'Comprehensive CI/CD pipeline best practices using GitHub Actions'
applyTo: '.github/workflows/*.yml,.github/workflows/*.yaml'
---

# GitHub Actions CI/CD Best Practices

For core workflow standards, see `cicd-standards.instructions.md`. This file covers advanced patterns.

<Goals>

- Efficient, secure, reliable automated pipelines
- Security-first: OIDC, least privilege, dependency review, SAST
- Fast feedback: caching, parallelization, shallow clones
- Robust deployments: staging validation, rollback strategies

</Goals>

## Workflow Design

<Standards>

**Structure**: Descriptive `name`, appropriate `on` triggers with path/branch filters, `concurrency` for shared resources, explicit `permissions`

**Jobs**: Clear names for distinct phases. `needs` for dependencies, `outputs` for inter-job data, `if` conditions for conditional execution, `timeout-minutes` on all jobs

**Steps**: SHA-pinned `uses`, descriptive `name`, multi-line `run` with `|`, `env` for non-sensitive config

**Reusability**: `workflow_call` for common CI patterns across repos

</Standards>

## Security

<Security>

**Secrets**: GitHub Secrets only, `secrets.<NAME>` access, environment-specific for deployments. Never construct dynamically or print.

**OIDC**: Short-lived credentials for AWS/Azure/GCP. Eliminates static secrets.

**GITHUB_TOKEN**: `contents: read` default. Add write permissions only when needed, prefer job-level overrides.

**Scanning**: `dependency-review-action` for SCA, CodeQL for SAST, secret scanning with push protection

**Actions**: Pin to full commit SHA. Audit marketplace actions. Use `dependabot` for version updates.

</Security>

## Performance

| Technique | Implementation |
|-----------|---------------|
| Caching | `actions/cache` with `hashFiles()` keys, `restore-keys` fallbacks |
| Matrix | `strategy.matrix` for multi-version/OS parallel testing |
| Shallow clone | `fetch-depth: 1` for most builds |
| Artifacts | `upload-artifact`/`download-artifact` for inter-job data |

## Testing Strategy

| Level | When | Focus |
|-------|------|-------|
| Unit | Every push/PR | Individual components, fast feedback, high coverage |
| Integration | PR merge | Component interactions, real services via `services` |
| E2E | Pre-deploy | Full user flows, staging environment |
| Performance | Nightly/weekly | Load testing, threshold enforcement |

<WhatToAdd>

- Code coverage collection and threshold enforcement
- Test reports as artifacts (JUnit XML, HTML)
- Status badges in README
- Smoke tests after deployment

</WhatToAdd>

## Deployment Strategies

| Strategy | When | Benefit |
|----------|------|---------|
| Rolling | Default for stateless apps | Gradual replacement |
| Blue/Green | Zero-downtime critical apps | Instant rollback |
| Canary | Testing with controlled blast radius | Early issue detection |
| Feature Flags | Decoupling deploy from release | A/B testing, staged rollout |

<HighLevelDetails>

**Staging**: Mirror production, automated promotion, environment protection rules
**Production**: Manual approvals, rollback capabilities, monitoring during deploy
**Rollback**: Automated on health check failure, versioned artifacts available, documented runbooks

</HighLevelDetails>

## Troubleshooting

| Issue | Likely Cause | Fix |
|-------|-------------|-----|
| Workflow not triggering | Wrong `on` config, path filters | Verify triggers, check `paths-ignore` |
| Permission denied | Insufficient GITHUB_TOKEN | Add to `permissions:` block |
| Cache miss | Dynamic key, wrong path | Use `hashFiles()`, verify cache path |
| Timeout | Inefficient steps, no parallelism | Profile, add matrix, optimize caching |
| Flaky tests | Race conditions, env mismatch | Explicit waits, standardize env, `services` |
| Deploy failure | Config drift, missing deps | Validate config, health checks, rollback |

<Limitations>

- All actions must be SHA-pinned
- No hardcoded secrets in workflow files
- No deployments without passing tests
- No production deploy without manual approval
- No workflows without timeout-minutes
- No broad GITHUB_TOKEN permissions

</Limitations>
