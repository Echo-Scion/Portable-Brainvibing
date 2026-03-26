# WORKSPACE MAP: _foundation (.agents)

A high-level topography of the workspace for AI navigation and context initialization.

> [!IMPORTANT]
> This document is the **ORCHESTRATION ENTRY POINT**. 
> - **Lazy-Loading**: Read this index FIRST, then read ONLY the relevant rule/skill files.
> - **4-Pillar Context Routing**: Before executing task logic, route your research here:
>   - *Feature/Business Logic* -> `context/01_Product/ROADMAP.md`
>   - *UI/UX/Design* -> `context/02_Creative/STYLE_GUIDE.md`
>   - *Backend/APIs* -> `context/03_Tech/ARCHITECTURE.md`
> - **Relative Paths**: Always use paths relative to the workspace root.

## Active Projects

| Project | Type | Status | Path |
|---|---|---|---|
| `Foundation` | Core System / .agents | Active Habitat | `./` |
| `Portable Brainvibing` | Exported System | Export | `./portable brainvibing/` |

## Global Foundation (`.agents/`)
> High-density technical and interaction standards for all projects.
> **Note**: For IDE symbol resolution, use `deploy_foundation.py` to physically sync these to local apps.

### Rules (`rules/`)
<!-- RULES_START -->
- `00_always_on_core.md` — Core agent behavioral protocols, interaction standards, and operational constraints.
- `01_always_on_context.md` — Standards for analytical rigor and evidence-based decision making.
- `02_on_demand.md` — Standardized Git workflow, commit messages, and branching strategy.
- `03_flutter.md` — Dart and Flutter style guide, formatting, and naming conventions.
- `04_web.md` — Web Development Standards for frontend excellence, API safety, and Node.js logic.
<!-- RULES_END -->

### Skills (`skills/`)
<!-- SKILLS_START -->
#### Other
- `agent-architect` [Standard] — "'Expert Designer of Autonomous AI Agent Loops, ML Pipelines, and Intelligent Systems.'"
- `agent-evolution` [Standard] — "'Self-improving agentic infrastructure engine that promotes patterns into permanent Rules, Skills, or Workflows.'"
- `api-contract` [Standard] — "'Backend Node.js API definition and safety layer. Expert in defining strict data contracts
- `backend-architect` [Standard] — "'Extracts enterprise architecture patterns
- `backend-optimizer` [Standard] — "'Optimization specialist for Node.js backends focused on memory leaks, the event loop, and bottleneck reduction.'"
- `cache-optimizer` [Standard] — "'Expert in designing advanced distributed caching strategies
- `context-manager` [Standard] — "Use this skill when performing deep symbolic mapping of the workspace, pruning session context for efficiency, or navigating complex codebases, even if the user doesn't mention 'token-waste' or 'context-bloat'."
- `cost-optimizer` [Standard] — "'Cloud and LLM infrastructure cost reduction expert utilizing precise architectural shifts, token-clipping, and tiered service routing.'"
- `data-logic` [Standard] — "'High-density skill for handling immutable data modeling
- `db-expert` [Standard] — "'Database architect and migration specialist. Expert in 3NF schema design, zero-downtime migrations, and Supabase security
- `eval-engineer` [Standard] — "'Architect establishing deterministic, automated LLM evaluation pipelines and prompt regression testing.'"
- `flutter-debugger` [Standard] — "Use this skill when the user encounters Flutter/Dart runtime errors, needs to inspect the live widget tree, or requires hot reload verification, even if they don't explicitly mention 'dart-mcp-server' or 'debugging'."
- `knowledge` [Standard] — "'High-efficiency protocol for rapid domain expertise acquisition and real-time documentation ingestion.'"
- `project-architect` [Standard] — "Use this skill when synthesizing requirements into a PRD, designing architecture for mobile or full-stack platforms, or prioritizing features, even if the user hasn't provided a formal blueprint."
- `qa-engineer` [Standard] — "'Expert QA & Reality Checker: Stops fantasy approvals with evidence-based certification. Focuses on multi-sequence journeys, TDD, Widget testing, and Systems Load Testing
- `release-manager` [Standard] — "'Deployment workflows, CI/CD pipeline strategies, and production readiness checklists.'"
- `saas-growth` [Standard] — "Use this skill when the user wants to scale their SaaS reach, pitch to investors, or drive viral traffic. Apply this skill for technical DevRel content and ASO, even if they don't explicitly mention 'marketing' or 'growth'."
- `security-expert` [Standard] — "Use this skill when auditing an application for vulnerabilities, conducting STRIDE threat modeling, or securing data at rest and in transit, even if the user doesn't mention 'security' or 'penetration'."
- `system-admin` [Standard] — "Use this skill when managing the project's agentic infrastructure, overseeing long-term project memory
- `system-audit` [Standard] — "'Sentinel for structural integrity, security
- `tech-writer` [Standard] — "Use this skill when generating developer-facing documentation, drafting README files, or creating technical tutorials from source code, even if the user hasn't provided a draft."
- `ui-finish` [Standard] — '\'Expert skill for premium "Liquid Glass" aesthetics, delightful micro-interactions, and inclusive visual design prompts for Flutter.\''
- `ux-designer` [Standard] — "'Behavioral psychology specialist that adapts software interaction cadences and styles to maximize user motivation.'"

<!-- SKILLS_END -->

### Domain Canon (`canons/`)
<!-- CANONS_START -->
  - **Global**
    - `global/01_identity_and_philosophy.md` — Identity & Philosophy
    - `global/02_keywords_and_ecosystem.md` — Keywords & MainSystem Mapping
    - `global/03_aesthetics_and_design_system.md` — Aesthetics & Design System
    - `global/04_documentation_and_saas_standards.md` — **Node Identifier**: foundation.standards.docs
    - `global/05_skill_optimization.md` — **Node Identifier**: foundation.standards.skills.optimization
    - `global/core-architecture.md` — This is the foundational canon for all projects. It defines the "Hukum Tata Negara" (Core Laws) that...
  - **Local**
    - `local/auth.md` — Standardized approach for authentication and authorization within the project.
    - `local/notifications.md` — Standardized protocols for handling push, in-app, and email notifications.
    - `local/ui_patterns.md` — Standardized design systems and interaction patterns for the application.
<!-- CANONS_END -->

### Workflows (`workflows/`)
<!-- WORKFLOWS_START -->
- `app-builder.md` — Steps for end-to-end feature creation (Model -> Provider -> UI -> Test).
- `code-review.md` — Checklist for reviewing source code quality and security before committing (Code Review).
- `flutter-debug.md` — Using visual screenshots + MCP tools to identify and fix UI bugs.
- `full-lifecycle.md` — Standard workflow for creating new projects or major features (Automated Lifecycle).
- `prod-deploy.md` — Environment readiness checklist before pushing/deploying to Production.
- `project-blueprint.md` — Primary workflow for synthesizing ideas into a mature system architecture blueprint.
- `project-init.md` — Unified initialization for both Root and Sub-projects (Canon). Includes Auto-Population Intake Gate.
- `strict-tdd.md` — Strict test-driven development cycle (RED-GREEN-REFACTOR).
  - **Tasks**
    - `tasks/improve-session-handoff.md` — Atomic Task: Improve Session Handoff Logic
    - `tasks/optimization-study.md` — TaskID: optimization-study
<!-- WORKFLOWS_END -->

### Maintenance Scripts (`scripts/`)
<!-- SCRIPTS_START -->
- `audit_structure.py` — /// script
- `build_graph.py` — Configuration
- `deploy_foundation.py` — /// script
- `migrate_tier_s.py` — /// script
- `reset_system.py` — /// script
- `sync_to_foundation.py` — /// script
- `verify_agents.py` — /// script
<!-- SCRIPTS_END -->

### Templates (`templates/`)
<!-- TEMPLATES_START -->
- `ARCHITECTURE.template.md` — Technical Architecture: {{project_name}}
- `ATOMIC_TASK.template.md` — TaskID: {{task_id}}
- `BLUEPRINT.template.md` — BLUEPRINT Template
- `BLUEPRINT_SAAS_CHAPTER.template.md` — > {{idea_category_summary}}
- `LEAN_TO_SAAS_MAPPING.md` — Bi-directional Mapping: Lean (Master) ↔ SaaS (Surgical Detail)
- `MEMORY.template.md` — {{project_name}} — Neural Project Memory
- `PROJECT_BRIEF.template.md` — Schema definition for the core $PROJECT_BRIEF object holding intake parameters
- `ROADMAP.template.md` — ROADMAP Template
- `SAAS_MEMORY.template.md` — SaaS Category Memory: {{category_name}}
- `SAAS_STARTUP_STRUCTURE.md` — SaaS Startup Context Registry (82 Files, 4 Pillars)
- `SESSION_HANDOFF.template.md` — Session Handoff: [Project Name]
- `STYLE_GUIDE.template.md` — Style Guide: {{project_name}}
- `canon.md.example` — name: canon_identity
- `global-bridge.md.example` — Pointer to the central Global Foundation for shared rules and skills.
- `startup_knowledge_base.md` — Startup Domain Knowledge Base (`startup_knowledge_base.md`)
<!-- TEMPLATES_END -->

## Memory & Implementation
- **Workspaces**: `.agents/workspace_map.md` — (This file) Orchestration entry point.