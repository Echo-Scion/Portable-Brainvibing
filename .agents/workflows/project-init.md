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
- [ ] **⚡ STEP 0.1: MONOREPO CONFIG (Double Lean)**:
  - **IF monorepo detected**: AI asks the user which sub-apps to initialize.
  - *"I've detected a monorepo structure. Should I initialize context for [App A, App B, Root]? (Default is Double Lean for all)."*
  - AI **WAITS** for user response.
- [ ] **⚡ STEP 0.2: THE KNOWLEDGE-BRIDGE (Deepening)**:
  - AI uses `@project-architect` and `startup_knowledge_base.md` to analyze `$PROJECT_BRIEF`.
  - AI proposes **10-15 "Industry-Standard" SaaS features** (e.g., Auth, Role-based access, Audit logs, Invoicing, etc.) specific to the project's domain.
  - AI presents this list to the user: *"Based on your brief, I recommend these 12 industry-standard features to ensure a deep SaaS context. Which ones should I include in the blueprint? (You can also type 'Include All' or 'Skip' to use my expert defaults)."*
  - AI **WAITS** for user confirmation/refinement.
- [ ] AI activates `@project-architect` skill with the expanded brief to generate structured PRD data and synthesize Blueprint chapters 1–7.
- [ ] **⚡ STEP 0.2: BLUEPRINT INGESTION (Alternative Path)**:
  - **IF a Blueprint/Spec file was detected in Step 0 (Intent Detection)**:
    - AI reads the specified file.
    - AI applies the **U2S (Unstructured-to-Surgical)** mapping protocol from `rules/common/context_naming_policy.md`.
    - AI skips the manual questions and Step 0.1, using the blueprint as the finalized `$PROJECT_BRIEF`.
    - AI identifies gaps in the blueprint and warns: *"Blueprint ingested. I've detected missing info for [Domain X, Y] and will use Best-Practice Defaults to ensure Zero N/A compliance."*
- [ ] AI holds generated content in memory, ready for slot-fill in Step 5.

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
- [ ] **Monorepo Detection**: If Melos, Nx, or nested `apps/` folders are present, initialize the **Double Lean** hierarchy:
    - **Root Context**: Create Lean folders in the root `context/` (reserved for Global Platform/DevOps).
    - **App Context**: For each specified sub-app in `apps/[app]/`, create independent Lean folders (`00-overview/`, `01-product/`, `02-creative/`, `03-tech/`).
- [ ] **Standard Project (Lean)**: If NOT a monorepo and user confirms Lean density, create `00-overview/`, `01-product/`, `02-creative/`, and `03-tech/` inside root `context/`.
- [ ] **Standard Project (Startup)**: If NOT a monorepo and user confirms Startup density, create the 16-category sub-folder structure defined in `templates/SAAS_STARTUP_STRUCTURE.md` inside root `context/`.
- [ ] **Verification**: Run `list_dir` on `context/` (and `apps/*/context/` if applicable) to confirm all directories exist before proceeding.

---

## 5. SCAFFOLDING (Auto-Populated via Slot-Fill)
> [!IMPORTANT]
> Do NOT create blank files. For each template:
> 1. Load and enforce `project-architect/resources/` (Pillars & Rigor).
> 2. Fill all `{{slots}}` using `$PROJECT_BRIEF` and the generated Blueprint data.
> 3. Write the fully populated content to the target file.
> 4. **SAFETY GUARD**: Do not run more than 5 `write_file` tools in a single parallel turn. Batch your writes to prevent timeout.

- [ ] **BLUEPRINT.md**: 
  - Read `.agents/templates/BLUEPRINT.template.md`
  - Fill all `{{slots}}` with synthesized blueprint content.
  - **Granular SaaS Synthesis (Startup Mode)**: If Startup density is chosen, read `.agents/templates/BLUEPRINT_SAAS_CHAPTER.template.md`. Instead of 82 granular points, generate a 1-sentence high-level summary for each of the 16 Categories to save token generation limits. Inject the result into `{{saas_startup_mapping}}`. If Lean density, replace `{{saas_startup_mapping}}` with "*Lean Mode Active - Detailed SaaS mapping omitted.*"
  - **Verification**: Ensure the total line count of `BLUEPRINT.md` remains manageable.
  - Write to `context/00-overview/BLUEPRINT.md` (Lean) or `context/Planning/MVP Scope.md` (Startup)

- [ ] **MEMORY.md**: 
  - Read `.agents/templates/MEMORY.template.md`
  - Fill `{{project_name}}`, `{{date}}`, `{{next_steps}}` from intake data
  - Write to `context/00-overview/MEMORY.md`

- [ ] **ROADMAP.md**: 
  - Read `.agents/templates/ROADMAP.template.md`
  - Fill with MVP phases derived from Blueprint Chapter 6
  - Write to `context/01-product/ROADMAP.md`

- [ ] **STYLE_GUIDE.md (Lean only)**:
  - Read `.agents/templates/STYLE_GUIDE.template.md`
  - Fill `{{visual_aesthetic_keywords}}`, `{{primary_persona}}`, etc.
  - Write to `context/02-creative/STYLE_GUIDE.md`

- [ ] **ARCHITECTURE.md (Lean only)**:
  - Read `.agents/templates/ARCHITECTURE.template.md`
  - Fill `{{primary_languages}}`, `{{frontend_framework}}`, `{{state_management_choice}}`, etc.
  - Write to `context/03-tech/ARCHITECTURE.md`


- [ ] **SaaS Category Population (Startup only)**: 
  - **Anti-Paralysis Protocol (JIT Expansion)**: Do NOT create all 82 files upfront.
  - Create ONLY the most critical initialization files based on the `$PROJECT_BRIEF` (e.g., `Idea/Problem Discovery.md`, `Planning/MVP Scope.md`, `Development/Tech Stack.md`).
  - Read `.agents/templates/SAAS_MEMORY.template.md` for these critical files and fill `{{slots}}`.
  - The remaining files from the `SAAS_STARTUP_STRUCTURE.md` baseline are left uncreated and will be generated **Just-In-Time (JIT)** when that specific feature/domain is actively worked on.

- [ ] **Proactive Prompt**: AI confirms: *"All context has been auto-populated. Review BLUEPRINT.md and MEMORY.md before we proceed to the first feature?"*

---

## 6. MIGRATION (Density Upgrade)
- [ ] **Scenario**: If user confirms upgrading an existing "Lean" project or sub-app to Startup density:
  - **Monorepo Check**: If in a monorepo, ask which sub-app to upgrade. Target `apps/[app]/context/`.
  - Agent must scan existing folders (`00-overview`, `01-product`, etc.).
  - **Optional Proactive Intake**: AI proposes 3-5 deepening questions specific to the new SaaS structure.
  - **Interpolation**: AI informs user: *"Using industry-standard defaults for skipped domains. I've mapped your existing context and will apply JIT Expansion for the 16 SaaS categories."*
  - Propose move/categorization of each file into the new 16-category structure (following the names in `SAAS_STARTUP_STRUCTURE.md`).
- [ ] **Merge Back**: Continue to Step 8 (Registration & Verification).

---

## 7. LEGACY INGESTION (Half-Finished Projects)
- [ ] **Scenario**: If AI detects an existing codebase in Step 0 (Intent Detection) OR user indicates an "Existing Codebase" during intake:
  - **⚡ STEP 7.1: DEEP AUDIT**:
    - AI runs `list_dir` and `grep_search` on core directories (`lib/`, `src/`, `api/`, `docs/`).
    - AI identifies existing features (e.g., "Auth detected via Firebase", "Stripe detected in payments/").
  - **⚡ STEP 7.2: REVERSE-ENGINEERED MAPPING**:
    - AI applies the **U2S (Unstructured-to-Surgical)** mapping logic from `rules/common/context_naming_policy.md` to the *discovered code architecture*.
    - AI creates context files in the 82-file baseline for **everything already built**, initializing the specs from the actual implementation.
  - **⚡ STEP 7.3: MIGRATION MEMORY**:
    - AI populates `MEMORY.md` with an integration log: *"Integrated into legacy project. Discovered [X] modules. Mapped to [Y] surgical context files."*
- [ ] **Merge Back**: Continue to Step 8 (Registration & Verification).

---

## 8. REGISTRATION & VERIFICATION
- [ ] **Workspace Map**: Update `.agents/workspace_map.md` with new project entry.
- [ ] **Test Mention**: Try to `@` mention a local skill to verify indexing.

---

> [!TIP]
> This unified `/project-init` replaces the legacy `/root-init` and `/canon-init`. The Intake Gate (Step 0) ensures zero manual file editing — all context is AI-generated from a 5-question brief.