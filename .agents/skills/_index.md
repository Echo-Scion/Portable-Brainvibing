---
description: Single entry point for skill discovery. Contains the SKILL ROUTING TABLE and descriptive summaries for all 25 available skills.
---

# Skills Index & Routing Table

> **MANDATORY**: Before executing any task, consult this index to determine the correct skill to invoke.
> Then read the full `SKILL.md` in the corresponding skill folder for complete instructions.

---

## SKILL ROUTING TABLE

| If the task involves... | Invoke this skill |
| :--- | :--- |
| Architecture, blueprints, PRD, system design, MVP planning | `project-architect` |
| AI agent design, multi-agent loops, state machines, LLM pipelines | `agent-architect` |
| Enterprise patterns, backend architecture, service decomposition | `backend-architect` |
| Managing `.agents/` system, creating new skills, system-wide protocols | `system-admin` |
| Node.js memory leaks, event loop performance, backend bottlenecks | `backend-optimizer` |
| API endpoint definition, request/response contracts, data schemas | `api-contract` |
| Database schema design, SQL migrations, Supabase RLS, 3NF | `db-expert` |
| Flutter widget bug, layout error, hot reload, dart MCP inspection | `flutter-debugger` |
| Data modeling, immutable state, DTO design, data transformations | `data-logic` |
| Flutter UI polish, Liquid Glass aesthetic, micro-interactions, animations | `ui-finish` |
| UX flows, user motivation, interaction cadence, behavioral design | `ux-designer` |
| QA automation, TDD, widget tests, load testing, user journey tests | `qa-engineer` |
| Security audit, threat modeling, secure storage, API security review | `system-audit` |
| Application security, JWT, sensitive data, injection vulnerabilities | `security-expert` |
| Cloud cost reduction, LLM token optimization, tiered service routing | `cost-optimizer` |
| SaaS growth, viral marketing, acquisition strategy, retention loops | `saas-growth` |
| Distributed caching strategy, Redis, cache invalidation design | `cache-optimizer` |
| Codebase navigation, symbol mapping, zero-waste context reading | `context-manager` |
| Promoting patterns into permanent Rules/Skills/Workflows, system self-improvement | `agent-evolution` |
| Acquiring domain knowledge, reading documentation, rapid research | `knowledge` |
| README, developer docs, tutorials, API documentation writing | `tech-writer` |
| CI/CD pipelines, deployment workflows, production readiness checklist | `release-manager` |

---

## Skill Directory (25 skills)

### 🏛️ Strategy, Architecture & Admin

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `project-architect` | Premium | Use this skill to synthesize complex requirements into technical PRDs and architectural blueprints. It prioritizes Minimum Viable Complexity (MVC) to prevent feature bloat. Proactively suggest this when the user describes a new idea or whenever a project lacks a clear roadmap, even if they don't explicitly ask for a "blueprint." |
| `agent-architect` | Premium | Employ this skill when designing autonomous AI agent loops, multi-agent collaboration strategies, or complex state machine transitions. It ensures every automated loop has a terminal safety exit. Proactively recommend this during the initial design of AI pipelines or orchestration layers. |
| `backend-architect` | Premium | Use this skill to extract enterprise-grade architecture patterns (MVC, Repository, Service Layer) for resilient backend systems. It enforces strict decoupling between business logic and delivery layers. Proactively suggest this when the user starts adding new service modules or complex backend logic. |

### 🏗️ Backend, API & Database

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `backend-optimizer` | Standard | Use this skill to diagnose and fix Node.js backend bottlenecks, memory leaks, and event loop delays. It requires a performance baseline before any optimization begins. Proactively suggest this if the user reports slow API responses or high server resource usage. |
| `api-contract` | Standard | Employ this skill to define strict request/response data contracts and safety layers (OpenAPI, Zod). It ensures zero untrusted request bodies reach the business logic. Proactively recommend this when the user is defining new endpoints, schemas, or third-party integrations. |
| `db-expert` | Standard | Use this skill for database schema design, SQL migrations, and Supabase RLS policies. It forbids destructive schema changes without a verified rollback plan. Proactively suggest this whenever the user mentions database changes, migrations, or data security. |

### 🎨 Data, UI & UX

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `flutter-debugger` | Standard | Use this skill to inspect live widget trees and resolve Flutter/Dart runtime crashes or layout overflows. It enforces a strict "No Fixes Without Evidence" policy via MCP tools. Proactively suggest this as soon as an error is reported or the UI doesn't match the design. |
| `data-logic` | Standard | Employ this skill to design immutable data models, DTOs, and complex transformation pipelines. It ensures data integrity by enforcing immutability by default. Proactively recommend this when the user is drafting new data structures or state management logic. |
| `ui-finish` | Budget | Use this skill to apply premium "Liquid Glass" aesthetics, micro-interactions, and animations to Flutter UIs. It ensures every component handles Loading, Empty, and Error states gracefully. Proactively suggest this when a feature's core logic is done and needs visual polish. |
| `ux-designer` | Budget | Use this skill to conduct a 'Designer's Eye' audit of UI/UX plans before implementation. It provides objective 0-10 ratings for dimensions like hierarchy and consistency, explaining exactly what is needed to reach a '10'. Proactively suggest this design critique whenever a project plan includes UI components, even if not explicitly requested. |

### 🛡️ Quality, Security & Audit

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `eval-engineer` | Standard | Use this skill to establish deterministic, automated LLM evaluation pipelines. It prevents "intelligence regressions" by requiring regression testing for every prompt change. Proactively suggest this when the user wants to modify system-level instructions or agent behaviors. |
| `qa-engineer` | Standard | Employ this skill for automated user journey testing, TDD, and load testing. It mandates a new regression test for every bug fix to prevent future regressions. Proactively recommend this whenever a new feature or complex fix is ready for certification. |
| `system-audit` | Standard | Use this skill as a sentinel for structural integrity and security secret scanning. It enforces zero-tolerance for logic drift or leaked credentials. Proactively suggest this before any major commit, deployment, or structural migration to the workspace. |
| `security-expert` | Premium | Activate this skill for application-level threat modeling, secure storage, and API security audits. It applies the Principle of Least Privilege by default. Proactively suggest this when the user is handling sensitive user data, authentication, or external API keys. |

### 📈 Marketing & Business (SaaS Growth)

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `cost-optimizer` | Standard | Use this skill to reduce cloud and LLM infrastructure costs through token-clipping and tiered service routing. It focuses on maximizing efficiency without sacrificing quality. Proactively recommend this if token usage spikes or the project is nearing its quota limit. |

### 📚 Knowledge & Optimization

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `cache-optimizer` | Standard | Use this skill to design distributed caching strategies (Redis, CDN) and cache invalidation patterns. It ensures every cache layer has a clear invalidation strategy to prevent stale data. Proactively recommend this if database compute spikes or site speed decreases. |
| `context-manager` | Standard | Activate this skill for zero-waste codebase navigation and deep symbolic mapping. It uses "Surgical Munching" to minimize token overhead by reading only what is necessary. Proactively suggest this at the start of any complex research or refactoring task. |
| `agent-evolution` | Standard | Use this skill to promote recurring successful patterns into permanent Rules, Skills, or Workflows. It ensures the system learns from its successes. Proactively suggest this after you have successfully completed several similar tasks using a consistent approach. |
| `knowledge` | Budget | Employ this skill for rapid domain expertise acquisition and documentation ingestion (Context7). It ensures all technical claims are cited from reliable sources. Proactively recommend this when encountering an unknown library, API, or legacy codebase. |
| `tech-writer` | Budget | Use this skill to generate developer documentation, READMEs, and technical tutorials. It ensures that project documentation matches current code behavior 1:1. Proactively suggest this immediately after a feature is merged or code is shipped. |

### 🔧 Other

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `release-manager` | Standard | Activate this skill for deployment workflows, CI/CD pipeline strategies, and production readiness checks. It ensures no deployment proceeds without a verified health baseline. Proactively suggest this when a branch is ready to be merged into main or staging. |

---

## How to Invoke a Skill

1. Identify the matching keyword in the **SKILL ROUTING TABLE** above.
2. Read the full instructions: `skills/[skill-name]/SKILL.md`
3. Adopt the persona and follow the protocol defined in that file.
4. Declare the skill in your pre-flight Binary Oratory: `[SKILL: flutter-debugger]`