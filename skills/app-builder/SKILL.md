---
name: app-builder
description: Main application building and rapid prototyping orchestrator. Creates full-stack applications from natural language requests, selects stacks, scaffolds projects, and guides fast iteration.
---

# App Builder - Application Building Orchestrator

> Analyzes user requests, determines the right stack, scaffolds projects, and supports rapid local prototyping.

## 🎯 Selective Reading Rule

**Read ONLY files relevant to the request!** Check the content map, find what you need.

| File                                               | Description                            | When to Read                        |
| -------------------------------------------------- | -------------------------------------- | ----------------------------------- |
| `project-detection.md`                             | Keyword matrix, project type detection | Starting new project                |
| `tech-stack.md`                                    | 2025 default stack, alternatives       | Choosing technologies               |
| `agent-coordination.md`                            | Agent pipeline, execution order        | Coordinating multi-agent work       |
| `scaffolding.md`                                   | Directory structure, core files        | Creating project structure          |
| `feature-building.md`                              | Feature analysis, error handling       | Adding features to existing project |
| [templates/REFERENCE.md](./templates/REFERENCE.md) | **Project templates index**            | Scaffolding new project             |

---

## 📦 Templates (13)

Quick-start scaffolding for new projects. **Read the matching template only!**

| Template                                                       | Tech Stack          | When to Use           |
| -------------------------------------------------------------- | ------------------- | --------------------- |
| [nextjs-fullstack](templates/nextjs-fullstack/TEMPLATE.md)     | Next.js + Prisma    | Full-stack web app    |
| [nextjs-saas](templates/nextjs-saas/TEMPLATE.md)               | Next.js + Stripe    | SaaS product          |
| [nextjs-static](templates/nextjs-static/TEMPLATE.md)           | Next.js + Framer    | Landing page          |
| [nuxt-app](templates/nuxt-app/TEMPLATE.md)                     | Nuxt 3 + Pinia      | Vue full-stack app    |
| [express-api](templates/express-api/TEMPLATE.md)               | Express + JWT       | REST API              |
| [python-fastapi](templates/python-fastapi/TEMPLATE.md)         | FastAPI             | Python API            |
| [react-native-app](templates/react-native-app/TEMPLATE.md)     | Expo + Zustand      | Mobile app            |
| [flutter-app](templates/flutter-app/TEMPLATE.md)               | Flutter + Riverpod  | Cross-platform mobile |
| [electron-desktop](templates/electron-desktop/TEMPLATE.md)     | Electron + React    | Desktop app           |
| [chrome-extension](templates/chrome-extension/TEMPLATE.md)     | Chrome MV3          | Browser extension     |
| [cli-tool](templates/cli-tool/TEMPLATE.md)                     | Node.js + Commander | CLI app               |
| [monorepo-turborepo](templates/monorepo-turborepo/TEMPLATE.md) | Turborepo + pnpm    | Monorepo              |

---

## 🔗 Related Agents

| Agent                 | Role                             |
| --------------------- | -------------------------------- |
| `project-planner`     | Task breakdown, dependency graph |
| `frontend-specialist` | UI components, pages             |
| `backend-specialist`  | API, business logic              |
| `database-architect`  | Schema, migrations               |
| `devops-engineer`     | Deployment, preview              |

---

## Usage Example

```
User: "Make an Instagram clone with photo sharing and likes"

App Builder Process:
1. Project type: Social Media App
2. Tech stack: Next.js + Prisma + Cloudinary + Clerk
3. Create plan:
   ├─ Database schema (users, posts, likes, follows)
   ├─ API routes (12 endpoints)
   ├─ Pages (feed, profile, upload)
   └─ Components (PostCard, Feed, LikeButton)
4. Coordinate agents
5. Report progress
6. Start preview
```

---

## 🚀 Rapid Prototyping Mode

Use this skill for fast, local-first web app iteration when the user wants to quickly create, prototype, or polish an application.

### Inputs to Gather

- **App description**: purpose, users, key flows
- **Tech preferences**: framework, styling, data layer
- **Design direction**: references, colors, layout expectations
- **Deploy target**: Vercel, Netlify, self-hosted, desktop, etc.

### Build Workflow

1. **Research current setup commands** before scaffolding
2. **Initialize the app** with the framework's official starter
3. **Establish the design system**: tokens, spacing, typography, base UI
4. **Build features incrementally** with loading, error, and empty states
5. **Polish for accessibility and performance**
6. **Document setup and deployment**

### Conventions

| Area | Guidance |
| --- | --- |
| Architecture | Small reusable components, TypeScript by default |
| UX | Mobile-first, semantic HTML, keyboard accessible |
| Styling | Tailwind preferred for speed; use consistent design tokens |
| Data | Handle loading, error, and empty states everywhere |
| Backend | Validate inputs at API boundaries; prefer type-safe ORMs |
| Public apps | Include metadata, Open Graph, sitemap, and robots.txt |

### Verification

Run the standard project lifecycle commands for the chosen stack:

```bash
npm install          # or bun install / pnpm install
npm run type-check   # if available
npm run lint
npm test
npm run build
npm run dev
```

Completion means the app builds, runs locally, and covers the critical flows across the target screen sizes.
