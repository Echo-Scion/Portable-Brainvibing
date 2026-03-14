# WORKSPACE MAP: MainSystem (.agents)

A high-level topography of the workspace for AI navigation and context initialization.

> [!IMPORTANT]
> This document is the **ORCHESTRATION ENTRY POINT**. 
> - **Lazy-Loading**: Read this index FIRST, then read ONLY the relevant rule/skill files for your task.
> - **Relative Paths**: Always use paths relative to the workspace root.

## Active Projects

| Project | Type | Status | Path |
|---|---|---|---|
| `MainSystem` | Flutter / Node / Supabase | Active Habitat | `./MainSystem/` |
| `Other Projects` | Various | Auxiliary | `./[project_alpha, project_beta, project_gamma, etc]` |

## Global Foundation (`.agents/`)
> High-density technical and interaction standards for all projects.

### Rules (`rules/`)
> High-precision technical constraints. See [AGENTS.md: Rules](../AGENTS.md#ground-rules) for human context.
- `common/context_hierarchy.md` — Inheritance logic (Global vs Project).
- `common/interaction_protocols.md` — Lazy-loading, Binary Oratory, Error Recovery.
- `common/performance.md` — LLM Model Tiers and Context Optimization.
- `common/reasoning_protocols.md` — Mandates deliberative reasoning for Budget models (Flash).
- `common/agent_protocols.md` — Management & Behavior standards.
- `common/analytical_standards.md` — Deconstruction and Brutal Honesty.
- `common/connector_protocols.md` — Cross-project bridges and SOP.
- `common/security.md` — Core security protocols.
- `flutter/flutter_standards.md` — High-efficiency Flutter tech standards.
- `flutter/dart-style.md` — Dart language style conventions.
- `flutter/flutter_hybrid_architecture.md` — Next.js + Flutter interop.
- `web/web_standards.md` — Web development performance standards.

### Skills (`skills/`)
> Specialized Tier-S Hybrid Skills, designed for deterministic workflows and autonomous execution.

#### 🏛️ Strategy, Architecture & Admin
- `project-architect` — Architectural design & product logic.
- `agent-architect` — Autonomous AI system blueprinting.
- `context-manager` — Intelligent project traversal & deep searches.
- `skill-project-relocator` — Safe project moves & path integrity.
- `skill-agent-evolution` — Self-improving engine for rules, skills, and workflows.
- `tech-writer` — Structured documentation and README generation.

#### 🏗️ Backend, API & Database
- `skill-api-contract` — Defensive API design (Zod, OpenAPI) and safety layer.
- `skill-db-expert` — 3NF modeling, migrations, and Supabase RLS policies.
- `backend-architect` — Enterprise design patterns (MVC, Repository).
- `backend-optimizer` — GC & event-loop bottleneck diagnosis.
- `cache-optimizer` — Distributed caching and ETag logic.

#### 🎨 Data, UI & UX
- `skill-data-logic` — Immutable models (Freezed) and reactive state (Riverpod).
- `skill-ui-finish` — "Liquid Glass" aesthetics and delightful micro-interactions.
- `ux-designer` — UI psychology and motivation cadences.
- `flutter-debugger` — Deep Dart-MCP-server integration.

#### 🛡️ Quality, Security & Audit
- `skill-qa-engineer` — TDD, Widget testing, E2E, and Accessibility (A11y).
- `security-expert` — Application-layer threat modeling.
- `release-manager` — CI/CD, production readiness loops.
- `eval-engineer` — Deterministic LLM evaluation automation.

#### 📚 Knowledge & Optimization
- `skill-knowledge` — Rapid domain acquisition and real-time doc ingestion.
- `cost-optimizer` — Cloud/LLM token & infrastructure cost reduction.


## Domain Canon (`canons/`)
> Specialized philosophy and design for specific domain modules and technology stacks.
- `auth/canon.md` — Standard authentication patterns.
- `notifications/canon.md` — Standard notification logic.
- `ui-patterns/canon.md` — Standard UI layouts.

## Maintenance Scripts (`.agents/scripts/`)
- `verify_agents.py` — Mechanical integrity linter and link validator.

## Memory & Implementation
- **Lean**: `context/overview/MEMORY.md` — Project specific memory.
- **Startup**: `context/Idea/Market Research.md` — Granular project memory.
- **Global**: `context/overview/MEMORY.md` — Foundation workspace memory.