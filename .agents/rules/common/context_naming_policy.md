---
description: Mandatory naming policy for context files to ensure architectural consistency.
activation: always_on
---
# Rule: Context Naming Policy (The 82-File Mandate)

To prevent architectural drift and naming inconsistency, all files created within the `context/` directory MUST follow a deterministic naming convention.

## 1. The Mapping Requirement
- AI **MUST NOT** invent arbitrary file names for context or knowledge items.
- If a new piece of context or domain knowledge is provided, the AI must first map it to the **82 SaaS Startup Files** defined in `.agents/templates/SAAS_STARTUP_STRUCTURE.md`.
- **Naming Source**: Use only the identifiers listed in `SAAS_STARTUP_STRUCTURE.md`.

## 2. Selection Logic
1. **Direct Match**: If the knowledge fits a specific category (e.g., SEO strategy), use the designated file (e.g., `Acquisition/SEO Wins.md`).
2. **Expansion Match**: If the knowledge is an expansion of an idea, append it to the relevant existing file rather than creating a "shadow" file.
3. **New Creation**: If the knowledge is truly unique but falls within a category, propose a name that follows the existing pattern and seek confirmation.

## 3. Unstructured-to-Surgical (U2S) Mapping
- When a user provides an **Info-Dump** or a **Monolithic Master Blueprint** (single-file specs), the AI **MUST NOT** simply store it as a single file.
- AI MUST taxonomize the input and distribute it across the **82 SaaS Startup Files** baseline.
- **Protocol**: 
    1. Parse the dump.
    2. Map snippets to specific domain files (e.g., "we will charge $10" -> `Revenue/Subscriptions.md`).
    3. Update `BLUEPRINT.md` as the index.
    4. Interpolate missing details to ensure "Zero N/A" compliance.

## 4. Lean-to-Startup Evolution
- Even in **Lean** projects (which start with only 5 core context files), any NEW idea or feature MUST trigger a **Surgical Expansion**.
- Instead of creating random files, the AI "promotes" the relevant category from the 82-file baseline. 
- *Example*: Adding a "Referral Program" to a Lean project results in the creation of `context/Acquisition/Referral Programs.md`, initializing that specific folder in the project.

## 5. Enforcement
- All initialization (`/project-init`) and migration tasks MUST verify that the `context/` topography matches the selected baseline (Lean or Startup).
- "Agar inkonsistensi penamaan tidak terulang" is the core driver for this rule. Consistency is prioritized over brevity.

---
*Portable Brainvibing - Governance Tier-S*