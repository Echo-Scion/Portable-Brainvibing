---
description: Single entry point for skill discovery. Contains the SKILL ROUTING TABLE and descriptive summaries for all 24 available skills.
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
| Security, QA, System Audit, Load Testing, and LLM Eval Orchestration | `integrity-sentinel` |
| Adversarial staging tests, injecting network latency, garbled data, chaos testing | `chaos-engineer` |
| Cloud cost reduction, LLM token optimization, tiered service routing | `cost-optimizer` |
| SaaS growth, viral marketing, acquisition strategy, retention loops | `saas-growth` |
| Distributed caching strategy, Redis, cache invalidation design | `cache-optimizer` |
| Codebase navigation, symbol mapping, zero-waste context reading | `context-manager` |
| Promoting patterns into permanent Rules/Skills/Workflows, system self-improvement | `agent-evolution` |
| Acquiring domain knowledge, reading documentation, rapid research | `knowledge` |
| README, developer docs, tutorials, API documentation writing | `tech-writer` |
| SaaS idea validation, market viability, brutal co-founder assessment, drop or pivot decision | `saas-viability` |
| CI/CD pipelines, deployment workflows, production readiness checklist | `release-manager` |

---

## Skill Directory (24 skills)

### 🏛️ Strategy, Architecture & Admin

| Skill | Description |
| :--- | :--- |
| `project-architect` | Use this skill to synthesize complex requirements into technical PRDs and architectural blueprints. It prioritizes Minimum Viable Complexity (MVC) to prevent feature bloat. Proactively suggest this when the user describes a new idea or whenever a project lacks a clear roadmap, even if they don't explicitly ask for a "blueprint." |
| `agent-architect` | Employ this skill when designing autonomous AI agent loops, multi-agent collaboration strategies, or complex state machine transitions. It ensures every automated loop has a terminal safety exit. Proactively recommend this during the initial design of AI pipelines or orchestration layers. |
| `backend-architect` | Use this skill to extract enterprise-grade architecture patterns (MVC, Repository, Service Layer) for resilient backend systems. It enforces strict decoupling between business logic and delivery layers. Proactively suggest this when the user starts adding new service modules or complex backend logic. |

### 🏗️ Backend, API & Database

| Skill | Description |
| :--- | :--- |
| `backend-optimizer` | Use this skill to diagnose and fix Node.js backend bottlenecks, memory leaks, and event loop delays. It requires a performance baseline before any optimization begins. Proactively suggest this if the user reports slow API responses or high server resource usage. |
| `api-contract` | Employ this skill to define strict request/response data contracts and safety layers (OpenAPI, Zod). It ensures zero untrusted request bodies reach the business logic. Proactively recommend this when the user is defining new endpoints, schemas, or third-party integrations. |
| `db-expert` | Use this skill for database schema design, SQL migrations, and Supabase RLS policies. It forbids destructive schema changes without a verified rollback plan. Proactively suggest this whenever the user mentions database changes, migrations, or data security. |

### 🎨 Data, UI & UX

| Skill | Description |
| :--- | :--- |
| `flutter-debugger` | Use this skill to inspect live widget trees and resolve Flutter/Dart runtime crashes or layout overflows. It enforces a strict "No Fixes Without Evidence" policy via MCP tools. Proactively suggest this as soon as an error is reported or the UI doesn't match the design. |
| `data-logic` | Employ this skill to design immutable data models, DTOs, and complex transformation pipelines. It ensures data integrity by enforcing immutability by default. Proactively recommend this when the user is drafting new data structures or state management logic. |
| `ui-finish` | Use this skill to apply premium "Liquid Glass" aesthetics, micro-interactions, and animations to Flutter UIs. It ensures every component handles Loading, Empty, and Error states gracefully. Proactively suggest this when a feature's core logic is done and needs visual polish. |
| `ux-designer` | Use this skill to conduct a 'Designer's Eye' audit of UI/UX plans before implementation. It provides objective 0-10 ratings for dimensions like hierarchy and consistency, explaining exactly what is needed to reach a '10'. Proactively suggest this design critique whenever a project plan includes UI components, even if not explicitly requested. |

### 🛡️ Quality, Security & Audit

| Skill | Description |
| :--- | :--- |
| `integrity-sentinel` | The overarching Gatekeeper for security, quality assurance, system audits, and LLM evaluation. It orchestrates zero-trust, reality-based certification routes before any code is approved. Proactively suggest this before deployment or when enforcing zero-trust principles. |
| `chaos-engineer` | Use this skill for adversarial staging tests. It actively injects failures (network latency, garbage data, auth drops) to verify true graceful degradation. Proactively suggest this before production releases to ensure resilience. |

### 📈 Marketing & Business (SaaS Growth)

| Skill | Description |
| :--- | :--- |
| `cost-optimizer` | Use this skill to reduce cloud and LLM infrastructure costs through token-clipping and tiered service routing. It focuses on maximizing efficiency without sacrificing quality. Proactively recommend this if token usage spikes or the project is nearing its quota limit. |
| `saas-growth` | Employ this skill to design acquisition funnels, viral referral loops, and retention strategies. It prioritizes "North Star" metrics to drive startup growth. Proactively suggest this during product strategy sessions or whenever the user discusses scaling. |

### 📚 Knowledge & Optimization

| Skill | Description |
| :--- | :--- |
| `cache-optimizer` | Use this skill to design distributed caching strategies (Redis, CDN) and cache invalidation patterns. It ensures every cache layer has a clear invalidation strategy to prevent stale data. Proactively recommend this if database compute spikes or site speed decreases. |
| `context-manager` | Activate this skill for zero-waste codebase navigation and deep symbolic mapping. It uses "Surgical Munching" to minimize token overhead by reading only what is necessary. Proactively suggest this at the start of any complex research or refactoring task. |
| `agent-evolution` | Use this skill to promote recurring successful patterns into permanent Rules, Skills, or Workflows. It ensures the system learns from its successes. Proactively suggest this after you have successfully completed several similar tasks using a consistent approach. |
| `knowledge` | Employ this skill for rapid domain expertise acquisition and documentation ingestion (Context7). It ensures all technical claims are cited from reliable sources. Proactively recommend this when encountering an unknown library, API, or legacy codebase. |
| `tech-writer` | Use this skill to generate developer documentation, READMEs, and technical tutorials. It ensures that project documentation matches current code behavior 1:1. Proactively suggest this immediately after a feature is merged or code is shipped. |

### 🔧 System & Operations

| Skill | Description |
| :--- | :--- |
| `release-manager` | Activate this skill for deployment workflows, CI/CD pipeline strategies, and production readiness checks. It ensures no deployment proceeds without a verified health baseline. Proactively suggest this when a branch is ready to be merged into main or staging. |
| `project-relocator` | Activate this skill to safely move or relocate projects, especially Flutter/Dart apps, while maintaining path integrity and performing deep cache clearing. Proactively offer this if the user reports path-related errors or environment drift. Note: excluded from portable/template deployment. |
| `debt-manager` | Orchestrator of codebase modernization. Identifies, scopes, and safely executes removal of deprecated libraries, dead code, and massive refactors. Do NOT use for writing new features or blank-slate design. |

---

## How to Invoke a Skill

1. Identify the matching keyword in the **SKILL ROUTING TABLE** above.
2. Read the full instructions: `skills/[skill-name]/SKILL.md`
3. Adopt the persona and follow the protocol defined in that file.
4. Declare the skill in your pre-flight Binary Oratory: `[SKILL: flutter-debugger]`

## Routing Arbitration (When Multiple Skills Match)
If more than one skill appears valid:

1. Prefer the skill with the narrowest domain fit to the user task.
2. If still tied, pick the one with stricter safety guarantees first.
3. Declare `PRIMARY_SKILL` and optional `SUPPORT_SKILL` explicitly.
4. Do not execute with an implicit or undeclared skill path.

If confidence in routing is below 0.7, escalate to `context-manager` for targeted context isolation before proceeding.