# 🤖 AGENTS Handbook: Human Manual

Welcome to the **Portable Brainvibing** Agent Infrastructure. This manual is designed for humans to understand, audit, and orchestrate the AI agents living in this repository.

---

## 📖 Mixed-Media Documentation Strategy

We use a "Split-Brain" approach to documentation:

1.  **Machine-First (`.agents/` folder)**: Highly technical, imperative instructions optimized for the AI's "System Prompt". These files are designed for machine parsing and precise tool triggering.
2.  **Human-Manual (`AGENTS.md` & `README.md`)**: This file and the main README provide context, philosophy, tutorials, and "How-To" guides for the human developer.

> [!TIP]
> **Why?** Documentation that is good for humans (conversational, verbose) is often "fuzzy" for AI. Documentation that is good for AI (schematic, strict) is often dry for humans. We maintain both to ensure maximum harmony.

---

## 🗺️ Interactive Knowledge Map

The entry point for any AI agent is the [workspace_map.md](file:///<ROOT>/.agents/workspace_map.md).

*   **Active Projects**: A registry of every project connected to this foundation.
*   **Skill Registry**: A mapping of specialized capabilities (e.g., "I need an SEO expert").
*   **Workflow Index**: Standardized procedures for complex tasks (e.g., "Build a full feature").
*   **Global Rules**: Foundational behaviors (e.g., "How to talk to the user").

---

## 🛠️ Agent Skill Catalog

Our agents are not generic. They are specialized "Lego bricks" of intelligence.

### 🏛️ Strategy, Architecture & Admin
| Skill | Human Description | When to Invoke |
| :--- | :--- | :--- |
| [project-architect](file:///<ROOT>/.agents/skills/project-architect/SKILL.md) | The "Big Picture" designer. | When starting a new app or major feature. |
| [agent-architect](file:///<ROOT>/.agents/skills/agent-architect/SKILL.md) | Architect for AI loops. | When designing multi-agent systems. |
| [context-manager](file:///<ROOT>/.agents/skills/context-manager/SKILL.md) | Codebase navigator. | To find symbols or analyze complex structures efficiently. |
| [eval-engineer](file:///<ROOT>/.agents/skills/eval-engineer/SKILL.md) | Deterministic logic validator. | To audit agent plans and enforce guardrails. |
| [tech-writer](file:///<ROOT>/.agents/skills/tech-writer/SKILL.md) | Clarity specialist. | Writing READMEs, API docs, and user guides. |

### 🏗️ Backend, API & Database
| Skill | Human Description | When to Invoke |
| :--- | :--- | :--- |
| [skill-api-contract](file:///<ROOT>/.agents/skills/skill-api-contract/SKILL.md) | Defensive API specialist. | Designing 400-level safety gates and Zod schemas. |
| [skill-db-expert](file:///<ROOT>/.agents/skills/skill-db-expert/SKILL.md) | Production DB architect. | 3NF schema, migrations, and Supabase RLS policies. |
| [backend-architect](file:///<ROOT>/.agents/skills/backend-architect/SKILL.md) | Enterprise pattern expert. | Applying MVC, Repository, and Service layers. |
| [cache-optimizer](file:///<ROOT>/.agents/skills/cache-optimizer/SKILL.md) | Speed specialist. | Implementing Redis, CDNs, and ETags. |
| [backend-optimizer](file:///<ROOT>/.agents/skills/backend-optimizer/SKILL.md) | Bottleneck hunter. | Fixing memory leaks and Event Loop blocks. |

### 🎨 Data, UI & UX
| Skill | Human Description | When to Invoke |
| :--- | :--- | :--- |
| [skill-data-logic](file:///<ROOT>/.agents/skills/skill-data-logic/SKILL.md) | Immutable data architect. | Generating Freezed models and Riverpod logic. |
| [skill-ui-finish](file:///<ROOT>/.agents/skills/skill-ui-finish/SKILL.md) | The Visual Alchemist. | High-end "Liquid Glass" aesthetics, Typography Scales, and Color Harmony. |
| [ux-designer](file:///<ROOT>/.agents/skills/ux-designer/SKILL.md) | Behavioral psychologist. | Reducing cognitive load and designing "nudges". |
| [flutter-debugger](file:///<ROOT>/.agents/skills/flutter-debugger/SKILL.md) | Tooling integrator. | Using Dart/Flutter DevTools and Widget Trees. |

### 🛡️ Quality, Security & Audit
| Skill | Human Description | When to Invoke |
| :--- | :--- | :--- |
| [skill-qa-engineer](file:///<ROOT>/.agents/skills/skill-qa-engineer/SKILL.md) | Total Verification specialist. | TDD, Widget tests, E2E journey, and A11y. |
| [security-expert](file:///<ROOT>/.agents/skills/security-expert/SKILL.md) | Threat modeling pro. | Secure storage, API audits, and risk assessment. |
| [release-manager](file:///<ROOT>/.agents/skills/release-manager/SKILL.md) | Deployment & readiness pilot. | CI/CD pipelines and production health checks. |
| [skill-knowledge](file:///<ROOT>/.agents/skills/skill-knowledge/SKILL.md) | Knowledge extractor. | Rapidly learning new topics or real-time docs ingestion. |
| [cost-optimizer](file:///<ROOT>/.agents/skills/cost-optimizer/SKILL.md) | Token economist. | Reducing LLM overhead and optimizing model tiering. |



---

## 🔄 Workflow Manual: How to Build

Workflows are multi-step "recipes" that orchestrate multiple skills.

### 🐣 `/project-init`: Starting from Zero
Connects your new project to the MainSystem Global Foundation using **System Junctions**.
1. Create folder.
2. Link `.agents` (Global Brain).
3. Initialize `.agent` (Local Soul).
4. Register in Workspace Map.

### 📐 `@project-architect`: The Blueprint
Starts the design phase. It interrogates your idea and generates a **7-Chapter Master Blueprint** (Soul, Brand, Logic, Scale, etc.).

### 🏗️ `/app-builder`: End-to-End Feature Creation
The most common daily workflow. Takes a feature from Model to UI to Test.
- **Model**: `skill-data-logic` -> Immutable Freezed model.
- **Logic**: `skill-data-logic` -> Riverpod Notifier.
- **UI**: `skill-ui-finish` -> Premium Widgets.
- **Test**: `skill-qa-engineer` -> Widget/End-to-End verification.

### 🔴 `/strict-tdd`: Defense-First Development
For critical logic. The AI is forbidden from writing the feature until it has a failing test.
- Red (Fail) -> Green (Pass) -> Refactor.

### 🧹 `/code-review`: Quality Gate
Audits your code for security leaks (API keys), file size (>800 lines), and function complexity.

### 🚀 `/prod-deploy`: The final check
Environment variable audits, database pre-flights, and health-check verification before hitting "Go".

---

## 🛡️ Infrastructure Protocols {#ground-rules}

To protect your tokens and codebase integrity, the AI follows these strict protocols:

1.  **Binary Oratory (Mandatory)**: The AI will ask for "YES/NO" confirmation before any destructive or major architectural change (Prompt Guard).
2.  **Token Shield**: AI uses "File Outlines" and "Line-Targeting" to save context costs.
3.  **Vibecode Limit**: Strict 500-line cap on all modular logic files to prevent "Lost in the Middle" syndrome.
4.  **Context Integrity**: Every code modification is NOT complete until relevant `context/` markdown files are updated (Documentation Sync).

---

## 🧪 Customization Guide: Personalizing your AI Soul

Each project has a singular `.agent/` folder (The Soul). 
*   **canon.md**: Defines the specific philosophy of *this* project.
*   **rules/**: You can add local `.md` files here to give the AI project-specific instructions (e.g., "Always use Spanish for variable names").

---
*Portable Brainvibing Infrastructure v1.0.0*
