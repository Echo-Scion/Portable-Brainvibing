---
description: Comprehensive rules for Context Management, Context Hierarchy, Token Economy, and Skeleton-first loading.
activation: always on
---

# 1. Context Hierarchy & Resolution Layer
# Rule: Plug & Play Context Hierarchy

This rule defines how the agent resolves and prioritizes rules, skills, and memory in a **Physical Residency** environment (Plug & Play).

## 1. Resolution Layers

The context is resolved in two or three layers depending on project type:

### Standard Project (Single Layer)
| Level | Name | Scope | Location |
| :--- | :--- | :--- | :--- |
| **0** | **Global Foundation** | General AI behavior & standards. | `.agents/rules/` |
| **1** | **Project Local** | Project-specific rules & memory. | `.agents/rules/local/` & `context/` |

### Monorepo Project (Double Lean Layer)
| Level | Name | Scope | Location |
| :--- | :--- | :--- | :--- |
| **0** | **Global Foundation** | General AI behavior & standards. | `.agents/rules/` |
| **1** | **Monorepo Root** | Shared infrastructure, DevOps, & Design. | `/context/` (Root) |
| **2** | **App Local** | Specific business logic & features. | `/apps/[app_name]/context/` |

## 2. Monorepo Context Distribution (Double Lean)

In a monorepo environment, context MUST be distributed to prevent "Context Bloat" and ensure app-specific isolation:

- **Root Context**: Reserved ONLY for global platform infrastructure, monorepo DevOps (e.g., Melos, Docker), and unified design systems.
- **App Context**: Every sub-app MUST maintain its own **4-Pillar Context** folders (`00_Strategy`, `01_Product`, `02_Creative`, `03_Tech`).
- **Distributed SaaS Mapping**: Detailed SaaS context (Idea, Planning, Development, etc.) is stored in the specific app's context directory using the Prefix-Based Registry.

## 3. Plug & Play Residency (Physical)

To ensure 100% IDE compatibility and symbol indexing (Antigravity IDE), this system uses **Physical Residency**:

- **No Symlinks/Junctions**: All rules and skills are physically copied into the project's `.agents/` folder.
- **Self-Contained**: Every project is a standalone "Intelligence Unit" that carries its own brain.
- **IDE Native**: Because files are local, `@` mentions and clickable file links work out-of-the-box.

## 4. Domain Canons (The Truth)

Beyond rules and behaviors, this system uses **Canons** (`canons/`) to store the "Static Truth" of the project:

- **Identity & Philosophy**: Foundational values and aesthetic standards (`canons/global/`).
- **Standard Logic**: Pre-approved architectural patterns for `auth/`, `notifications/`, etc.
- **Lazy-Loading**: The agent MUST lazy-load relevant `.md` files from the `canons/` directory based on the task domain to minimize context usage while maintaining high fidelity to standards.
- **BUDGET Restriction**: `BUDGET` tasks are **prohibited** from loading canons unless the canon is explicitly referenced by name in the user's request. Canons are architectural context; atomic tasks do not require them.

## 4. Override Logic
- **Local Overrides Global**: If a rule exists in `.agents/rules/local/`, it automatically overrides the same rule in `.agents/rules/`.
- **Skill Priority**: The agent always checks for a local version of a skill in `.agents/skills/` before execution.

## 5. Initialization
- **Active Discovery**: At start, the agent checks for the `.agents/` folder in the project root.
- **Sync Status**: The agent verifies if the foundation metadata (`catalog.json`) matches the local skill files.

# 2. Context Economy (Surgical Munching)
# Context7 Economical Usage

## 1. Resource Management
- Minimize token consumption during context retrieval.
- Prioritize high-value information snippets over full-text reads.
- Reuse context objects efficiently to avoid redundant processing.

## 2. Query Optimization
- Use specific and targeted queries to filter relevant documentation.
- Cache common query results for faster subsequent access.
- Limit the depth of recursive context generation.

## 3. Cost Control
- Monitor usage patterns to identify potential inefficiencies.
- Use lower-tier models for non-critical context processing.
- Periodically review and purge outdated context data.

## 4. Integration Guidelines
- Integrate Context7 seamlessly with existing agent workflows.
- Ensure consistent data formatting for all retrieved context.
- Provide clear error messages when context retrieval fails.

# 3. Context Diet for Budget Models
# Context Diet Protocol (Skeleton-First)

## 1. The Core Problem
Small/Budget Models hallucinate when fed too much raw code. If a model reads an 800-line file just to find one method, its context window gets "poisoned" by irrelevant noise, dropping reasoning accuracy drastically.

## 2. The Skeleton-First Law
Jika agen beroperasi pada **[TIER: BUDGET]**, agen **DILARANG KERAS** menggunakan tool `read_file` pada file yang panjang (>200 baris) sebagai langkah pertama.

**Urutan Wajib Navigasi File:**
1. **Grep/Search Skeleton:** Gunakan `grep_search` untuk mencari nama fungsi, class, atau *header* file.
   *Contoh:* `grep_search` dengan pola `class |function |interface ` untuk mendapatkan gambaran kerangka.
2. **Targeted Read:** Setelah baris fungsi ditemukan, agen hanya boleh membaca blok spesifik tersebut (misal: baris 45-80) menggunakan rentang baris di `read_file`.
3. **No Blind Full-Reads:** Jika tertangkap melakukan *blind full-read* pada file besar, itu adalah pelanggaran protokol.

## 3. Surgical Munching
Hanya ekstrak apa yang benar-benar esensial untuk tugas tersebut. Jika tugas hanya mengubah warna *button*, dilarang membaca modul *Auth*.

*Aturan ini menjamin Model Kecil tetap tajam, fokus, dan tidak terdistraksi oleh variabel yang tidak relevan.*


---
trigger: model_decision
description: Mandatory naming policy for context files to ensure architectural consistency.
---

# Rule: Context Naming Policy (The 82-File Mandate)

> **Scope Guard**: This rule applies ONLY to **target deployment projects** (SaaS apps built using this foundation). It does NOT apply to `_foundation` itself, which is a tooling project. If working within `_foundation/.agents/`, ignore the 82-file mapping requirement.

To prevent architectural drift and naming inconsistency, all files created within the `context/` directory MUST follow a deterministic naming convention.

## 1. The Mapping Requirement
- AI **MUST NOT** invent arbitrary file names for context or knowledge items.
- If a new piece of context or domain knowledge is provided, the AI must first map it to the **82 SaaS Startup Files** defined in `.agents/templates/SAAS_STARTUP_STRUCTURE.md`.
- **Naming Source**: Use only the identifiers listed in `SAAS_STARTUP_STRUCTURE.md`.

## 2. Selection Logic
1. **Direct Match**: If the knowledge fits a specific category (e.g., SEO strategy), use the designated file (e.g., `01_Product/Acq_SEO_Wins.md`).
2. **Expansion Match**: If the knowledge is an expansion of an idea, append it to the relevant existing file rather than creating a "shadow" file.
3. **New Creation**: If the knowledge is truly unique but falls within a category, propose a name that follows the existing pattern and seek confirmation.

## 3. Unstructured-to-Surgical (U2S) Mapping
- When a user provides an **Info-Dump** or a **Monolithic Master Blueprint** (single-file specs), the AI **MUST NOT** simply store it as a single file.
- AI MUST taxonomize the input and distribute it across the **82 SaaS Startup Files** baseline.
- **Protocol**: 
    1. Parse the dump.
    2. Map snippets to specific domain files (e.g., "we will charge $10" -> `01_Product/Rev_Subscriptions.md`).
    3. Update `00_Strategy/BLUEPRINT.md` as the index.
    4. Interpolate missing details to ensure "Zero N/A" compliance.

## 4. Lean-to-Startup Evolution (Just-In-Time Expansion)
- **Anti-Paralysis**: Do NOT generate all 82 SaaS files upfront. Start with the minimal files needed for the current sprint.
- The 82 files in `SAAS_STARTUP_STRUCTURE.md` act as a **dictionary of allowed names**, not a mandate to create empty files.
- Even in **Lean** or **Startup** projects, any NEW idea or feature MUST trigger a **Surgical Expansion (JIT)**.
- Instead of creating random files, the AI "promotes" the relevant category from the 82-file baseline. 
- *Example*: Adding a "Referral Program" to a project results in the creation of `context/01_Product/Growth_Referral_Programs.md`, initializing that specific file ONLY when needed.

## 5. Monorepo Distribution (Double Lean)
- In a monorepo, context is **split** between the root and the apps.
- **Root Context**: Reserved for shared infra (e.g., `03_Tech/Infra_Melos_Config.md`).
- **App Context**: Reserved for feature logic (e.g., `apps/[app]/context/01_Product/Plan_Product_Roadmap.md`).
- AI MUST ensure that app-specific details do NOT leak into the root context to maintain strict isolation.

## 6. Enforcement
- All initialization (`/project-init`) and migration tasks MUST verify that the `context/` topography matches the selected baseline (Lean, Startup, or Double Lean).
- Standardized naming is the core driver for this rule to prevent naming inconsistency. Consistency is prioritized over brevity.

## 7. Surgical Context Eviction (Token Efficiency)
- **Rule**: Upon completion of an atomic task (Tier-1+) or a major architectural phase, the agent MUST perform "Context Offloading."
- **Protocol**:
    1. **Declare Closure**: State explicitly which phase or atomic task is now FINAL in the session handoff or task log.
    2. **Evict**: Explicitly declare in the handoff: "Phase [X] is FINAL. Sub-sequent sessions MUST NOT read raw files from [directory/path] unless a bug is explicitly found."
    3. **Cleanup**: Close all tabs related to the finished phase before ending the session.
- **Goal**: Maintain 100% focus and prevent the "Context Bloat" that leads to AI hallucinations.
