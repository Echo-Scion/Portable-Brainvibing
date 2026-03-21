# WORKSPACE MAP: Foundation & Brainvibing (.agents)

A high-level topography of the workspace for AI navigation and context initialization.

> [!IMPORTANT]
> This document is the **ORCHESTRATION ENTRY POINT**. 
> - **Lazy-Loading**: Read this index FIRST, then read ONLY the relevant rule/skill files for your task.
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
#### 🏛️ Strategy, Architecture & Admin
- `agent-architect` [Premium] — Designer of robust autonomous AI agent loops, multi-agent collaboration, and state machine transitions.
- `backend-architect` [Premium] — Extracts enterprise architecture patterns
- `project-architect` [Premium] — "The Architect" — Product Requirements Synthesis, Structural Logic, and Sprint Prioritization
- `skill-project-relocator` [Standard] — Specialist in safely moving projects, particularly Flutter/Dart, with a focus on path integrity and deep cache clearing.

#### 🏗️ Backend, API & Database
- `backend-optimizer` [Standard] — Optimization specialist for Node.js backends focused on memory leaks, the event loop, and bottleneck reduction.
- `skill-api-contract` [Standard] — Backend Node.js API definition and safety layer. Expert in defining strict data contracts
- `skill-db-expert` [Standard] — Database architect and migration specialist. Expert in 3NF schema design, zero-downtime migrations, and Supabase security

#### 🎨 Data, UI & UX
- `flutter-debugger` [Standard] — Deep integration with dart-mcp-server for live widget inspection, runtime error analysis, and hot reloading.
- `skill-data-logic` [Standard] — High-density skill for handling immutable data modeling
- `skill-ui-finish` [Budget] — Expert skill for premium "Liquid Glass" aesthetics, delightful micro-interactions, and inclusive visual design prompts for Flutter.
- `ux-designer` [Budget] — Behavioral psychology specialist that adapts software interaction cadences and styles to maximize user motivation.

#### 🛡️ Quality, Security & Audit
- `eval-engineer` [Standard] — Architect establishing deterministic, automated LLM evaluation pipelines and prompt regression testing.
- `skill-qa-engineer` [Standard] — QA Automation specialist focusing on multi-sequence user journeys, TDD, Widget testing, and Systems Load Testing

#### 📈 Marketing & Business (SaaS Growth)
- `cost-optimizer` [Standard] — Cloud and LLM infrastructure cost reduction expert utilizing precise architectural shifts, token-clipping, and tiered service routing.
- `skill-saas-growth` [Budget] — Expert SaaS growth consultant specialized in Viral Marketing

#### 📚 Knowledge & Optimization
- `cache-optimizer` [Standard] — Expert in designing advanced distributed caching strategies
- `context-manager` [Standard] — Integrated protocol for zero-waste codebase navigation and deep symbolic mapping.
- `skill-agent-evolution` [Standard] — Self-improving agentic infrastructure engine that promotes patterns into permanent Rules, Skills, or Workflows.
- `skill-knowledge` [Budget] — High-efficiency protocol for rapid domain expertise acquisition and real-time documentation ingestion.
- `tech-writer` [Budget] — Expert technical writer specializing in developer documentation, READMEs, and tutorials for Flutter projects.

#### Other
- `release-manager` [Standard] — Deployment workflows, CI/CD pipeline strategies, and production readiness checklists.
- `security-expert` [Premium] — Expert application security engineer specializing in threat modeling, secure storage, and API security for Flutter applications. Use when asked to "review security", "store sensitive data", or "threat model". Do NOT use for general feature logic.

<!-- SKILLS_END -->

### Domain Canon (`canons/`)
<!-- CANONS_START -->
  - **Global**
    - `global/01_identity_and_philosophy.md` — Identity & Philosophy
    - `global/02_keywords_and_ecosystem.md` — Keywords & MainSystem Mapping
    - `global/03_aesthetics_and_design_system.md` — Aesthetics & Design System
    - `global/04_documentation_and_saas_standards.md` — **Node Identifier**: foundation.standards.docs
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
- `project-relocation.md` — Safe guide for moving projects (especially Flutter) to a new directory without path or cache errors.
- `repo-squash.md` — Squash repository history into a single initial commit while preserving the current file state.
- `safe-migration.md` — Safe and downtime-free guide for modifying active database table structures.
- `strict-tdd.md` — Strict test-driven development cycle (RED-GREEN-REFACTOR).
  - **Tasks**
    - `tasks/improve-session-handoff.md` — Atomic Task: Improve Session Handoff Logic
<!-- WORKFLOWS_END -->

### Maintenance Scripts (`scripts/`)
<!-- SCRIPTS_START -->
- `audit_structure.py` — Configuration - Relative to project root
- `build_graph.py` — Configuration
- `deploy_foundation.py` — def deploy(source_root, target_root):
- `migrate_tier_s.py` — Path relative to the script location
- `reset_system.py` — """
- `sync_to_foundation.py` — Configuration
- `verify_agents.py` — Use relative paths from script location
<!-- SCRIPTS_END -->

### Templates (`templates/`)
<!-- TEMPLATES_START -->
- `ARCHITECTURE.template.md` — Technical Architecture: {{project_name}}
- `ATOMIC_TASK.template.md` — TaskID: {{task_id}}
- `BLUEPRINT.template.md` — BLUEPRINT Template
- `BLUEPRINT_SAAS_CHAPTER.template.md` — > {{idea_category_summary}}
- `LEAN_TO_SAAS_MAPPING.md` — Bi-directional Mapping: Lean ↔ SaaS Startup
- `MEMORY.template.md` — MEMORY Template
- `PROJECT_BRIEF.template.md` — Schema definition for the core $PROJECT_BRIEF object holding intake parameters
- `ROADMAP.template.md` — ROADMAP Template
- `SAAS_MEMORY.template.md` — SaaS Category Memory: {{category_name}}
- `SAAS_STARTUP_STRUCTURE.md` — SaaS Startup Context Structure (16 Categories)
- `SESSION_HANDOFF.template.md` — Session Handoff: [Project Name]
- `STYLE_GUIDE.template.md` — Style Guide: {{project_name}}
- `canon.md.example` — name: canon_identity
- `global-bridge.md.example` — Pointer to the central Global Foundation for shared rules and skills.
- `startup_knowledge_base.md` — Startup Domain Knowledge Base (`startup_knowledge_base.md`)
<!-- TEMPLATES_END -->

## Memory & Implementation
- **Workspaces**: `.agents/workspace_map.md` — (This file) Orchestration entry point.