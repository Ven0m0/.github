---
name: brainstorming
description: Socratic questioning and requirements clarification protocol. Use for complex requests, new features, or unclear requirements before implementation begins.
---

# Brainstorming & Communication Protocol

> **MANDATORY:** Use for complex/vague requests, new features, updates.

---

## 🛑 SOCRATIC GATE (ENFORCEMENT)

### When to Trigger

| Pattern                                     | Action                             |
| ------------------------------------------- | ---------------------------------- |
| "Build/Create/Make [thing]" without details | 🛑 ASK 3 questions                 |
| Complex feature or architecture             | 🛑 Clarify before implementing     |
| Update/change request                       | 🛑 Confirm scope                   |
| Vague requirements                          | 🛑 Ask purpose, users, constraints |

### 🚫 MANDATORY: 3 Questions Before Implementation

1. **STOP** - Do NOT start coding
2. **ASK** - Minimum 3 questions:
   - 🎯 Purpose: What problem are you solving?
   - 👥 Users: Who will use this?
   - 📦 Scope: Must-have vs nice-to-have?
3. **WAIT** - Get response before proceeding

---

## 🧠 Dynamic Question Generation

**⛔ NEVER use static templates.** Read `dynamic-questioning.md` for principles.

### Core Principles

| Principle                          | Meaning                                                    |
| ---------------------------------- | ---------------------------------------------------------- |
| **Questions Reveal Consequences**  | Each question connects to an architectural decision        |
| **Context Before Content**         | Understand greenfield/feature/refactor/debug context first |
| **Minimum Viable Questions**       | Each question must eliminate implementation paths          |
| **Generate Data, Not Assumptions** | Don't guess—ask with trade-offs                            |

### Question Generation Process

```
1. Parse request → Extract domain, features, scale indicators
2. Identify decision points → Blocking vs. deferable
3. Generate questions → Priority: P0 (blocking) > P1 (high-leverage) > P2 (nice-to-have)
4. Format with trade-offs → What, Why, Options, Default
```

### Question Format (MANDATORY)

```markdown
### [PRIORITY] **[DECISION POINT]**

**Question:** [Clear question]

**Why This Matters:**

- [Architectural consequence]
- [Affects: cost/complexity/timeline/scale]

**Options:**
| Option | Pros | Cons | Best For |
|--------|------|------|----------|
| A | [+] | [-] | [Use case] |

**If Not Specified:** [Default + rationale]
```

**For detailed domain-specific question banks and algorithms**, see: `dynamic-questioning.md`

---

## Communication Principles

| Principle        | Implementation                           |
| ---------------- | ---------------------------------------- |
| **Concise**      | No unnecessary details, get to point     |
| **Specific**     | "~2 minutes" not "wait a bit"            |
| **Alternatives** | Offer multiple paths when stuck          |
| **Proactive**    | Suggest next step after completion       |

---

## Anti-Patterns (AVOID)

| Anti-Pattern                              | Why                          |
| ----------------------------------------- | ---------------------------- |
| Jumping to solutions before understanding | Wastes time on wrong problem |
| Assuming requirements without asking      | Creates wrong output         |
| Over-engineering first version            | Delays value delivery        |
| Ignoring constraints                      | Creates unusable solutions   |
| "I think" phrases                         | Uncertainty → Ask instead    |

---
