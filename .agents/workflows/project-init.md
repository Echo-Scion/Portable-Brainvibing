---
description: Unified initialization for both Root and Sub-projects (Canon). Includes Auto-Population Intake Gate.
---

# Workflow: Project Initialization (`/project-init`)

This workflow consolidates the initialization logic for both "Root Projects" and "Sub-projects" with support for different context densities. **Critically: it auto-populates all context files using AI — zero manual writing required.**

## 0. FLAGS & CONFIGURATION
- **`--startup`**: Creates a 16-category SaaS-oriented granular structure.

---

## ⚡ STEP 0: INTAKE GATE (Auto-Population) — MANDATORY
> [!IMPORTANT]
> The AI MUST complete this step before creating ANY files or directories.
> Do NOT scaffold anything until the user answers the intake questions.

- [ ] AI asks the user the following questions (in a single message):
  ```
  Before we begin scaffolding, please answer these questions:
  1. Project name & short tagline?
  2. Core problem being solved?
  3. Primary target user / persona?
  4. Planned tech stack? (Flutter? Supabase? Node? etc.)
  5. Fresh start or existing codebase?
  
  [Additional for --startup mode]:
  6. Primary monetization model? (Subscriptions, Freemium, Marketplace, etc.)
  7. Key competitors or inspiration?
  ```
- [ ] AI **WAITS** for user response. Do not proceed until baseline (1-5) and mode-specific questions are answered.
- [ ] AI compiles `$PROJECT_BRIEF` internally from all answers.
- [ ] AI activates `@project-architect` skill with `$PROJECT_BRIEF` to generate structured PRD data and synthesize Blueprint chapters 1–7.
- [ ] AI holds generated content in memory, ready for slot-fill in Step 5.

---

## 1. ENVIRONMENT DETECTION
- [ ] **Check Directory**: Does the current directory already contain a `.agents/` folder?
  - **YES**: This is a **Root Project**. Skip to Step 3.
  - **NO**: This is a **Sub-project**. Proceed to Step 2.

---

## 2. SUB-PROJECT SETUP (Hybrid Tiered Junctions)
- [ ] **Find Foundation**: Identify the absolute path to the global `.agents/` foundation.
- [ ] **Create Local Shell**: Create physical directories: `.agents/`, `.agents/skills/`, `.agents/rules/`, `.agents/workflows/`.
- [ ] **Link Global Skills**: Run `cmd /c "mklink /j .agents\skills\foundation "[GlobalPath]\.agents\skills""`.
- [ ] **Link Global Rules**: Run `cmd /c "mklink /j .agents\rules\foundation "[GlobalPath]\.agents\rules""`.
- [ ] **Link Global Workflows**: Run `cmd /c "mklink /j .agents\workflows\foundation "[GlobalPath]\.agents\workflows""`.
- [ ] **Create Workspace**: Generate a `[project-name].code-workspace` file with Multi-Root configuration (including both `.agents` and `.`).
- [ ] **Action**: Open the `.code-workspace` file and click "Open Workspace" in VS Code to enable `@` mentions.

---

## 3. INITIALIZE LOCAL PROJECT SOUL
- [ ] **Create Soul Directory**: Create `.agent/` (singular), `.agent/rules/`, and `.agent/skills/`.
- [ ] **Deploy Templates**: 
  - Copy `.agents/templates/canon.md.example` to `.agent/canon.md`.
  - Copy `.agents/templates/global-bridge.md.example` to `.agent/global_bridge.md`.
- [ ] **Create Inheritance**: Create `.agent/rules/protocols.md` that inherits from `.agents/rules/`.

---

## 4. GENERATE CONTEXT HIERARCHY
- [ ] **Infrastructure**: Create the `context/` parent directory first.
- [ ] **If `--startup` flag**: Inside `context/`, create the 16-category sub-folder structure defined in `SAAS_STARTUP_STRUCTURE.md`.
- [ ] **Verification**: Run `list_dir` on `context/` to confirm all directories exist before proceeding.

---

## 5. SCAFFOLDING (Auto-Populated via Slot-Fill)
> [!IMPORTANT]
> Do NOT create blank files. For each template:
> 2. Load and enforce `project-architect/resources/` (Pillars & Rigor).
> 3. Fill all `{{slots}}` using `$PROJECT_BRIEF` and the generated Blueprint data.
> 3. Write the fully populated content to the target file.

- [ ] **BLUEPRINT.md**: 
  - Read `.agents/templates/BLUEPRINT.template.md`
  - Fill all `{{slots}}` with synthesized blueprint content.
  - **Granular SaaS Synthesis (Startup Mode)**: Map the core strategy of **all 82 context files** defined in `SAAS_STARTUP_STRUCTURE.md` into Chapter 8.
  - **Verification**: Ensure the total line count of `BLUEPRINT.md` remains manageable for AI context windows.
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
  - Read `.agents/templates/SAAS_MEMORY.template.md`
  - Iterate through all 16 categories from `SAAS_STARTUP_STRUCTURE.md`
  - For each, fill `{{slots}}` with granular domain data generated by `@project-architect`
  - Write to `context/[Category]/data.md`

- [ ] **Proactive Prompt**: AI confirms: *"All context has been auto-populated. Review BLUEPRINT.md and MEMORY.md before we proceed to the first feature?"*

---

## 6. MIGRATION (Lean → Startup)
- [ ] **Scenario**: If `--startup` is run in an existing "Lean" project:
  - Agent must scan `context/overview`, `product`, etc.
  - Propose move/categorization of each file into the new 16-category structure.

---

## 7. REGISTRATION & VERIFICATION
- [ ] **Workspace Map**: Update `.agents/workspace_map.md` with new project entry.
- [ ] **Test Mention**: Try to `@` mention a local skill to verify indexing.

---

> [!TIP]
> This unified `/project-init` replaces the legacy `/root-init` and `/canon-init`. The Intake Gate (Step 0) ensures zero manual file editing — all context is AI-generated from a 5-question brief.