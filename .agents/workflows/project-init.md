---
description: Unified initialization for both Root and Sub-projects (Canon). Includes Auto-Population Intake Gate.
---

# Workflow: Project Initialization (`/project-init`)

This workflow consolidates the initialization logic for both "Root Projects" and "Sub-projects" with support for different context densities. **Critically: it auto-populates all context files using AI — zero manual writing required.**

## 0. INTENT DETECTION (Passive Scan)
- AI automatically scans the directory BEFORE the first message.
- **Scenarios Detected**:
    - **Fresh Start**: Directory is empty or only contains basic setup files.
    - **Legacy Project**: Significant codebase detected (`lib/`, `src/`, `pubspec.yaml`).
    - **Monorepo**: Melos, Nx, or nested `apps/` folders detected.
    - **Blueprint-Driven**: A monolithic spec/blueprint file is found in the root.
- **Density Preference**: AI proposes **Lean** vs **Startup** density based on the detected project complexity. For monorepos, AI defaults to **Double Lean**.

---

## ⚡ STEP 0: INTAKE GATE (Auto-Population) — MANDATORY (OR SKIP IF BLUEPRINT DETECTED)
> [!IMPORTANT]
> The AI MUST complete this step before creating ANY files or directories.
> Do NOT scaffold anything until the user answers the intake questions.

- [ ] AI asks the user the following questions (consolidated based on detected intent):
  ```
  [Detected State: Legacy / Fresh / Blueprint]
  
  I've analyzed the environment. To finalize our setup:
  1. Confirm project name & tagline?
  2. [If Legacy]: Should I perform a Deep Audit to reverse-engineer specs from existing code?
  3. [If Blueprint found]: Use '[filename]' as the Master Blueprint?
  4. Core monetization & target persona?
  5. Density: Start with a Simple (Lean) or Professional SaaS (Startup) structure?
  ```
- [ ] AI **WAITS** for user response.
- [ ] **Socratic Challenge**: AI MUST identify and present at least ONE technical or product risk based on the user's answers. AI only proceeds after the user acknowledges or refines the choice.
- [ ] AI compiles `$PROJECT_BRIEF` internally following the schema defined in `templates/PROJECT_BRIEF.template.md`.

---

## ⚡ STEP 0.3: THE DEEPENING (Logical Inference)
> [!IMPORTANT]
> To ensure 100% success in Step 5 (Scaffolding), the AI MUST now expand the 5 user answers into the full 30+ data points required by the Blueprint.

- [ ] **Infer Identity**: Derive `etymology`, `node_identifier`, and `trinity_keywords` based on the project name and tagline.
- [ ] **Experience Design**: Define the `first_30_seconds` (Wow moment) and `dual_lens_concept` based on the target persona.
- [ ] **Risk Assessment**: Analyze the chosen tech stack against the features to identify `fragmentation_risk` and `scale_limitations`.
- [ ] **Protocol Check**: Ensure all inferences align with `canons/global/core-architecture.md`.
- [ ] **Presentation**: AI presents a "Conceptual Summary" to the user: *"I've expanded your brief into a full architectural concept. I've identified [Risk X] and designed the [Wow Moment Y]. Proceed to scaffolding?"*
- [ ] AI **WAITS** for user confirmation.

---

## 1. ENVIRONMENT DETECTION
- [ ] **Check Directory**: Does the current directory already contain a `.agents/` folder?
  - **YES**: This is a **Root Project**. Skip to Step 3.
  - **NO**: This is a **Sub-project**. Proceed to Step 2.

---

## 2. PROJECT SETUP (Plug & Play Deployment)
- [ ] **Agentic Deployment (Preferred)**: Ask the AI to read `.agents/DEPLOY_ME.md` and use its own tools to copy the foundation files to the local `.agents/` directory.
  - *Rationale*: No Python or external dependencies required.
- [ ] **Scripted Deployment (Fallback)**: If the agent is unable to perform file operations directly:
  - Verify **Python 3.10+** is installed (`python --version`).
  - Run: `python [GlobalPath]\.agents\scripts\deploy_foundation.py --target .`
- [ ] **Verification**: Confirm that `@` mentions and clickable file links work in the local environment.

## 3. INITIALIZE LOCAL PROJECT BRAIN
- [ ] **Local Evolution (MANDATORY)**: For project-specific rules or skills, **AI MUST** create folders and files with the `local-` prefix within the existing `rules/` and `skills/` directories.
    - *Rationale*: This prevents project-specific logic from being synced back to the global Foundation via `sync_to_foundation.py`.
- [ ] **Sync Index**: Run `python .agents/scripts/update_catalog.py` to ensure the local `catalog.json` reflects all items.

---

## 4. GENERATE CONTEXT HIERARCHY
- [ ] **Infrastructure**: Create the `context/` parent directory first.
- [ ] **Standard Pillar Hierarchy (ALWAYS ACTIVE)**: Create the 4 Master Pillars:
    - `00_Strategy/`
    - `01_Product/`
    - `02_Creative/`
    - `03_Tech/`
- [ ] **Monorepo Detection**: If Melos, Nx, or nested `apps/` folders are present:
    - **Root Context**: Create the 4 pillars in the root `context/`.
    - **App Context**: For each sub-app in `apps/[app]/`, create independent 4 pillars.
- [ ] **Verification**: Run `list_dir` on `context/` to confirm all 4 pillars exist.

---

## 5. SCAFFOLDING (Auto-Populated via Slot-Fill)
> [!IMPORTANT]
> Do NOT create blank files. For each template:
> 1. Load and enforce `project-architect/references/` (Pillars & Rigor).
> 2. Fill all `{{slots}}` using `$PROJECT_BRIEF` and the generated Blueprint data.
> 3. Write the fully populated content to the target file.

- [ ] **BLUEPRINT.md (Master Strategy)**: 
  - Read `.agents/templates/BLUEPRINT.template.md`
  - Write to `context/00_Strategy/BLUEPRINT.md`

- [ ] **MEMORY.md (Project Soul)**: 
  - Read `.agents/templates/MEMORY.template.md`
  - Write to `context/00_Strategy/MEMORY.md`

- [ ] **ROADMAP.md (Master Product)**: 
  - Read `.agents/templates/ROADMAP.template.md`
  - Write to `context/01_Product/ROADMAP.md`

- [ ] **STYLE_GUIDE.md (Master Design)**:
  - Read `.agents/templates/STYLE_GUIDE.template.md`
  - Write to `context/02_Creative/STYLE_GUIDE.md`

- [ ] **ARCHITECTURE.md (Master Tech)**:
  - Read `.agents/templates/ARCHITECTURE.template.md`
  - Write to `context/03_Tech/ARCHITECTURE.md`

- [ ] **SaaS Surgical Population (Startup Mode)**: 
  - **Anti-Paralysis Protocol (JIT Expansion)**: Do NOT create all 82 files upfront.
  - Create ONLY the most critical initialization files using the **Prefix-Based Registry** from `templates/SAAS_STARTUP_STRUCTURE.md`.
  - *Example*: `context/00_Strategy/Idea_Problem_Discovery.md`, `context/03_Tech/Dev_Tech_Stack.md`.
  - The remaining files are generated **Just-In-Time (JIT)** when actively worked on.

- [ ] **Proactive Prompt**: AI confirms: *"All context has been auto-populated. Review BLUEPRINT.md and MEMORY.md before we proceed to the first feature?"*

---

## 6. MIGRATION (Density Upgrade)
- [ ] **Scenario**: Upgrading an existing "Lean" project to Startup density:
  - Agent scans existing folders (`00_Strategy`, `01_Product`, etc.).
  - AI informs user: *"Using Prefix-Based Expansion for the 82 SaaS categories. I'll maintain the 4-pillar hierarchy for better AI context retention."*
  - AI generates required Prefix-based files without moving existing Master files.
- [ ] **Merge Back**: Continue to Step 8 (Registration & Verification).

---

## 7. LEGACY INGESTION (Half-Finished Projects)
- [ ] **Scenario**: Existing codebase detected:
  - **⚡ STEP 7.1: DEEP AUDIT**: AI reverse-engineers specs from code.
  - **⚡ STEP 7.2: REVERSE-ENGINEERED MAPPING**: AI creates Prefix-based context files for everything already built.
- [ ] **Merge Back**: Continue to Step 8 (Registration & Verification).

---

## 8. TASK INJECTION (Lifecycle Tracking)
- [ ] **Atomic Task Injection (MANDATORY)**: 
  - Create a new file in `.agents/workflows/tasks/task-[project_name]-planning.md`.
  - Set `Status: TODO`.
  - Fill the `Objective` with: "Blueprint & PRD Completion for [Project Name]".

---

## 9. REGISTRATION & VERIFICATION
- [ ] **Workspace Map**: Update `.agents/workspace_map.md`.

---

> [!TIP]
> This structure ensures AI can scan the entire project context in just 4 `list_dir` calls, regardless of project scale.