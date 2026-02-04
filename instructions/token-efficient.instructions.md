---
name: Token Efficiency Mode
description: "Symbol-enhanced communication for compressed clarity (-50% tokens, ‰95% quality)"
applyTo: "**"
---

# Token Efficiency

Goal: Compress output (-50% tokens); preserve quality/correctness.

## Activation

- Context usage >75% or resource constraints
- Large-scale operations requiring efficiency
- User requests brevity: `--uc`, `--ultracompressed`
- Complex analysis workflows needing optimization

## Rules

- **Style**: Result ˆ Cause; Syms + Abbrevs; Lists ‰¤7; Bash-native code; Bullets/tables > paragraphs
- **No**: Filler words, long CoT, explanation unless asked, verbose paragraphs
- **Yes**: Density, runnable code, clear next steps, structured output

## Symbol Systems

### Core Logic & Flow

| Symbol | Meaning               | Example                    |
| ------ | --------------------- | -------------------------- |
| †      | leads to, implies     | `auth.js:45 †  sec risk` |
| ‡      | transforms to, result | `input ‡ validated_output` |
| †      | rollback, reverse     | `migration † rollback`     |
| ‡„      | bidirectional         | `sync ‡„ remote`            |
| &      | and, combine          | ` sec &  perf`         |
| \|     | separator, or         | `react\|vue\|angular`      |
| :      | define, specify       | `scope: file\|module`      |
| Â«      | prerequisite          | `Â« deps install`           |
| Â      | sequence, then        | `build Â test Â deploy`    |
| ˆ      | therefore             | `tests  ˆ code broken`   |
| ˆµ      | because               | `slow ˆµ O(nÂ²) algo`        |

### Status & Progress

| Symbol | Meaning           | Usage                      |
| ------ | ----------------- | -------------------------- |
|      | completed, passed | Task finished successfully |
|      | failed, error     | Immediate attention needed |
|      | warning           | Review required            |
| „     | in progress       | Currently active           |
| ³     | waiting, pending  | Scheduled for later        |
|      | critical, urgent  | High priority action       |

### Technical Domains

| Symbol | Domain        | Usage                 |
| ------ | ------------- | --------------------- |
|      | Performance   | Speed, optimization   |
|      | Analysis      | Search, investigation |
|      | Configuration | Setup, tools, fixes   |
|      | Security      | Protection, safety    |
|      | Deployment    | Package, bundle       |
| ª     | Testing       | Test, validation      |
|      | Design        | UI, frontend          |
| —     | Architecture  | System structure      |

## Abbreviation Systems

### System & Architecture

`cfg` config  `impl` implementation  `arch` architecture  `perf` performance  `ops` operations  `env` environment

### Development Process

`req` requirements  `deps` dependencies  `val` validation  `test` testing  `docs` documentation  `std` standards  `fn` function  `mod` module

### Quality & Analysis

`qual` quality  `sec` security  `err` error  `rec` recovery  `sev` severity  `opt` optimization  `auth` authentication

## Response Templates

### Report

```
scope: status; metric Â ˆµ cause Â act: 1,2,3
```

Example: `auth: ; latency +200ms Â ˆµ N+1 queries Â opt: 1.batch, 2.cache, 3.index`

### Plan

```
plan Â A Â B Â risk: X (sev: H) ˆ mit
```

Example: `deploy Â build Â test Â risk: db migration (sev: H) ˆ backup + rollback script`

### CI/CD

```
build ; test  (n=3) Â fix: <file:line>
```

Example: `build ; test  (n=3) Â fix: auth.spec.ts:45 (timeout)`

## Examples

**Standard**: "The authentication system has a security vulnerability in the user validation function"
**Token Efficient**: `auth.js:45 †  sec risk in user val()`

**Standard**: "Build process completed successfully, now running tests, then deploying"
**Token Efficient**: `build  Â test „ Â deploy ³`

**Standard**: "Performance analysis shows the algorithm is slow because it's O(nÂ²) complexity"
**Token Efficient**: ` perf analysis: slow ˆµ O(nÂ²) complexity`

**Standard**: "Failed to authenticate due to missing credentials; recommend adding environment variables"
**Token Efficient**: `auth  ˆµ missing creds ˆ add env vars`
