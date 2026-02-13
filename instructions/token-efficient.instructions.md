---
description: 'Symbol-enhanced communication for compressed clarity (-50% tokens, >=95% quality)'
applyTo: '**/*'
---

# Token Efficiency

<Goals>

Compress output -50% tokens while preserving quality and correctness.

**Activate when**: context >75%, resource constraints, user requests brevity (`--uc`), large-scale operations

</Goals>

<Standards>

- Result before cause; symbols + abbreviations; lists <=7 items
- Bullets/tables over paragraphs; runnable code over descriptions
- No filler words, no verbose explanations unless asked

</Standards>

## Symbols

### Flow
| Sym | Meaning | Example |
|-----|---------|---------|
| -> | leads to | `auth.js:45 -> sec risk` |
| => | transforms | `input => validated_output` |
| << | prerequisite | `<< deps install` |
| >> | sequence | `build >> test >> deploy` |
| .: | therefore | `tests fail .: code broken` |
| b/c | because | `slow b/c O(n^2)` |

### Status
| Sym | Meaning |
|-----|---------|
| [x] | completed |
| [!] | failed/error |
| [~] | in progress |
| [?] | warning/review |
| [ ] | pending |

### Abbreviations
`cfg` config | `impl` implementation | `perf` performance | `deps` dependencies | `val` validation | `fn` function | `mod` module | `sec` security | `err` error | `opt` optimization

## Templates

**Report**: `scope: status; metric >> b/c cause >> act: 1,2,3`
Example: `auth: [!]; latency +200ms >> b/c N+1 queries >> opt: 1.batch, 2.cache, 3.index`

**Plan**: `plan >> A >> B >> risk: X (sev: H) .: mitigation`
Example: `deploy >> build >> test >> risk: db migration (sev: H) .: backup + rollback`

**CI/CD**: `build [x]; test [!] (n=3) >> fix: <file:line>`
