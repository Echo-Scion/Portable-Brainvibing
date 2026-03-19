# Bi-directional Mapping: Lean ↔ SaaS Startup

This document defines how the 82 granular SaaS topics map to the 5 Lean folders (and vice-versa) during migration.

## 1. SaaS to Lean (Condensation)
Use this mapping when a user "downgrades" from Startup to Lean mode.

| SaaS Folder (16) | Lean Target Folder | Target Content/File |
| :--- | :--- | :--- |
| **Idea, Validation, Launch, Scaling** | `overview/` | `BLUEPRINT.md` (Strategy Chapters) |
| **Planning, Design, Conversion, Revenue, Analytics, Retention, Growth** | `product/` | `ROADMAP.md` & `PRD.md` |
| **Development, Infrastructure, Testing** | `tech/` | `TECH_STACK.md` & `ARCHITECTURE.md` |
| **Design** (Assets) | `creative/` | Assets & Design Tokens |

## 2. Lean to SaaS (Distillation)
Use this mapping when a project "upgrades" to full Startup mode.

*   **overview/BLUEPRINT.md** ➔ Distributed into `Idea/`, `Validation/`, `Launch/`, `Scaling/`.
*   **product/ROADMAP.md** ➔ Distributed into `Planning/`, `Revenue/`, `Growth/`, `Retention/`.
*   **tech/ARCHITECTURE.md** ➔ Distributed into `Development/`, `Infrastructure/`, `Testing/`.

## 3. Migration Logic
1. **Extraction**: AI reads the existing source files.
2. **Contextual Split**: AI uses `@project-architect` to slice information based on the 82-topic taxonomy.
3. **Drafting**: AI populates the new structure, marking inherited data as `[MIGRATED]`.
4. **Cleanup**: AI asks user for permission before deleting the old structure.

---
*Portable Brainvibing Infrastructure - Context Migration Protocol*