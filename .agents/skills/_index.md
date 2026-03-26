---
description: Single entry point for skill discovery. Contains the SKILL ROUTING TABLE and a 2-line summary for all 25 available skills.
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
| Node.js memory leaks, event loop performance, backend bottlenecks | `backend-optimizer` |
| API endpoint definition, request/response contracts, data schemas | `skill-api-contract` |
| Database schema design, SQL migrations, Supabase RLS, 3NF | `skill-db-expert` |
| Flutter widget bug, layout error, hot reload, dart MCP inspection | `flutter-debugger` |
| Data modeling, immutable state, DTO design, data transformations | `skill-data-logic` |
| Flutter UI polish, Liquid Glass aesthetic, micro-interactions, animations | `skill-ui-finish` |
| UX flows, user motivation, interaction cadence, behavioral design | `ux-designer` |
| LLM evaluation pipeline, prompt regression testing, eval metrics | `eval-engineer` |
| QA automation, TDD, widget tests, load testing, user journey tests | `skill-qa-engineer` |
| Application security, JWT, sensitive data, injection vulnerabilities | `security-expert` |
| Cloud cost reduction, LLM token optimization, tiered service routing | `cost-optimizer` |
| SaaS growth, viral marketing, acquisition strategy, retention loops | `skill-saas-growth` |
| Distributed caching strategy, Redis, cache invalidation design | `cache-optimizer` |
| Codebase navigation, symbol mapping, zero-waste context reading | `context-manager` |
| Promoting patterns into permanent Rules/Skills/Workflows, system self-improvement | `skill-agent-evolution` |
| Acquiring domain knowledge, reading documentation, rapid research | `skill-knowledge` |
| README, developer docs, tutorials, API documentation writing | `tech-writer` |
| CI/CD pipelines, deployment workflows, production readiness checklist | `release-manager` |

---

## Skill Directory (25 skills)

### 🏛️ Strategy, Architecture & Admin

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `project-architect` | Premium | Product Requirements Synthesis, Structural Logic, and Sprint Prioritization. The go-to skill for turning ideas into engineered system blueprints. |
| `agent-architect` | Premium | Designer of robust autonomous AI agent loops, multi-agent collaboration, and state machine transitions. Use for AI pipeline and orchestration design. |
| `backend-architect` | Premium | Extracts enterprise architecture patterns for large-scale backend systems. Use for service decomposition and system-level design decisions. |

### 🏗️ Backend, API & Database

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `backend-optimizer` | Standard | Optimization specialist for Node.js backends focused on memory leaks, the event loop, and bottleneck reduction. |
| `skill-api-contract` | Standard | Backend Node.js API definition and safety layer. Expert in defining strict data contracts between services and clients. |
| `skill-db-expert` | Standard | Database architect and migration specialist. Expert in 3NF schema design, zero-downtime migrations, and Supabase security (RLS). |

### 🎨 Data, UI & UX

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `flutter-debugger` | Standard | Deep integration with dart-mcp-server for live widget inspection, runtime error analysis, and hot reloading. Use for any Flutter visual or runtime bug. |
| `skill-data-logic` | Standard | High-density skill for handling immutable data modeling, DTOs, and complex data transformation pipelines. |
| `skill-ui-finish` | Budget | Expert skill for premium "Liquid Glass" aesthetics, delightful micro-interactions, and inclusive visual design prompts for Flutter. |
| `ux-designer` | Budget | Behavioral psychology specialist that adapts software interaction cadences and styles to maximize user motivation. |

### 🛡️ Quality, Security & Audit

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `eval-engineer` | Standard | Architect establishing deterministic, automated LLM evaluation pipelines and prompt regression testing. |
| `skill-qa-engineer` | Standard | QA Automation specialist focusing on multi-sequence user journeys, TDD, Widget testing, and Systems Load Testing. |
| `security-expert` | Premium | Expert application security engineer specializing in threat modeling, secure storage, and API security for Flutter applications. Use when asked to "review security", "store sensitive data", or "threat model". Do NOT use for general feature logic. |

### 📈 Marketing & Business (SaaS Growth)

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `cost-optimizer` | Standard | Cloud and LLM infrastructure cost reduction expert utilizing precise architectural shifts, token-clipping, and tiered service routing. |
| `skill-saas-growth` | Budget | Expert SaaS growth consultant specialized in Viral Marketing, acquisition funnels, and retention loop design. |

### 📚 Knowledge & Optimization

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `cache-optimizer` | Standard | Expert in designing advanced distributed caching strategies (Redis, in-memory, CDN layers) and cache invalidation patterns. |
| `context-manager` | Standard | Integrated protocol for zero-waste codebase navigation and deep symbolic mapping. Use to plan surgical reading strategies for large codebases. |
| `skill-agent-evolution` | Standard | Self-improving agentic infrastructure engine that promotes recurring patterns into permanent Rules, Skills, or Workflows. |
| `skill-knowledge` | Budget | High-efficiency protocol for rapid domain expertise acquisition and real-time documentation ingestion via Context7. |
| `tech-writer` | Budget | Expert technical writer specializing in developer documentation, READMEs, and tutorials for Flutter projects. |

### 🔧 Other

| Skill | Tier | Description |
| :--- | :--- | :--- |
| `release-manager` | Standard | Deployment workflows, CI/CD pipeline strategies, and production readiness checklists. |

---

## How to Invoke a Skill

1. Identify the matching keyword in the **SKILL ROUTING TABLE** above.
2. Read the full instructions: `skills/[skill-name]/SKILL.md`
3. Adopt the persona and follow the protocol defined in that file.
4. Declare the skill in your pre-flight Binary Oratory: `[SKILL: flutter-debugger]`