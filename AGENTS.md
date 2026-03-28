# AGENTS: The AI-Surgical Ecosystem Simulation (.agents)

Welcome to the **Portable AI-Surgical Infrastructure**. This document catalogs the core components, skills, and workflows of the `.agents` ecosystem.

> [!TIP]
> This is a **Universal Guide** reflecting the actual structure of the `portable brainvibing/.agents` directory.

---

## 🏛️ CANONS (`canons/`)
Architectural constitutions that define the project's foundational laws. These are the non-negotiable architectural truths that agents must respect.
- **Global Architecture** (`global/core-architecture.md`): The overarching system patterns, state management principles, and structural boundaries.
- **Automated Harnesses** (`global/harnesses/README.md`): Definitions for automated Action-Verifier execution loops.
- **Microservices** (`micro/README.md`): Rules governing edge-functions, lightweight service limits, and inter-service communication.

## 🛡️ RULES (`rules/`)
Absolute behavioral constraints and security protocols. This folder acts as the "Pre-Execution Firewall" for the AI, ensuring safe and standardized operations.
- **Cognitive & Constraint Rules**: 
  - `core-guardrails.md` & `reasoning-standards.md`: Defines how the agent must think, plan, and execute (e.g., "Anti-Affirmation Mandate").
  - `tier-execution-protocol.md` & `context-standards.md`: Dictates context limits and whether a task uses Budget (fast) or Premium (deep) reasoning.
- **Engineering Standards**: 
  - `flutter-standards.md` & `web.md`: Strict coding paradigms for mobile and web front-ends.
  - `performance-optimization.md`: Mandatory performance and efficiency checks.
- **Security & Workflow**: 
  - `security-guardrails.md`: Zero-trust security enforcement.
  - `git-workflow.md` & `interaction-protocols.md`: How the AI handles version control and communicates with the human user.
  - `api-connector-protocols.md` & `autoharness-protocol.md`: Strict rules for API design and automated self-testing.

## 🎯 SKILLS (`skills/`)
Specialized personas (roles) ready for activation. An agent channels these skills to gain deep, domain-specific expertise based on the task.
- **`api-contract`**: Enforces strict Data Transfer Objects (DTOs), Zod schemas, and OpenAPI specs. Prevents malformed data from entering business logic.
- **`backend-orchestrator`**: The master architect for database schemas, PostgreSQL RLS, caching layers, and enterprise backend patterns.
- **`cost-optimizer`**: Monitors token usage, clips redundant context, and routes tasks to cheaper models without losing fidelity.
- **`data-logic`**: Handles immutable data structures, pipeline transformations, and complex state management logic.
- **`frontend-experience`**: Fixes layout bugs, optimizes component hierarchies, and ensures pixel-perfect UI/UX flow.
- **`integrity-sentinel`**: The overarching gatekeeper for QA, system audits, STRIDE threat modeling, and zero-trust verification.
- **`meta-agent-admin`**: Manages the `.agents` ecosystem itself—defining new rules, updating the catalog, and maintaining AI documentation.
- **`project-architect`**: Synthesizes rough human ideas into concrete technical blueprints (PRDs), prioritizing Minimum Viable Complexity (MVC).
- **`project-operator`**: Manages CI/CD pipelines, repository rebasing, tech debt cleanup, and handles "chaos" debugging loops.
- **`saas-strategist`**: Analyzes business viability, monetization logic, and growth integration (e.g., Stripe, analytics).
- **`ui-finish`**: Applies premium visual polish ("Liquid Glass" aesthetics), micro-animations, and perfect empty/loading states.

## 🔄 WORKFLOWS (`workflows/`)
Automated, repeatable step-by-step sequences for specific development lifecycles. Agents execute these sequentially to yield predictable results.
- **Project Setup**:
  - `project-init.md`: Bootstraps documentation (BLUEPRINT, ROADMAP) and scaffolds the initial repository layer.
- **Development Loops**:
  - `strict-tdd.md`: Forces a Red-Green-Refactor test-driven development cycle.
  - `app-builder.md`: Rapid feature scaffolding and integration sequence.
  - `flutter-debug.md`: Specialized sequence for resolving deep Flutter/Dart environment or widget errors.
- **Maintenance & Release**:
  - `context-prune.md`: Compresses memory and clears old context to save LLM tokens.
  - `code-review.md`: Deep architectural review of arbitrary Feature PRs or module changes.
  - `prod-deploy.md` & `full-lifecycle.md`: CI/CD pipelines and end-to-end task completion checklists.

## ⚙️ SCRIPTS, TEMPLATES & EVALS
The mechanical tooling that supports the AI ecosystem's memory, file generation, and systemic operation.
- **`scripts/`**: Python utilities for ecosystem maintenance. Includes tools to build knowledge graphs (`build_graph.py`), compress prompt memory (`compress_memory.py`), and synchronize the workspace (`verify_agents.py`, `update_catalog.py`).
- **`templates/`**: Standardized Markdown scaffolds. Includes project-level files (`BLUEPRINT`, `ARCHITECTURE`, `ROADMAP`), AI prompt integrations (`CLAUDE`, `COPILOT`, `GEMINI`), and specialized SaaS start-up documents.
- **`evals/` & `metrics/`**: System auditing tools (`audit_aesthetics.py`) and JSON-based benchmarks to deterministically test an agent's compliance and behavioral drift over time.
- **`docs/`**: Human-readable deployment manuals (`MULTI_AI_DEPLOYMENT.md`) and comprehensive guides on how to combine these agents effectively (`workflows_guide.md`).

---
*Portable AI-Surgical Infrastructure - Standard Protocol 2026*
