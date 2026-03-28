---
description: Standard workflow for creating new projects or major features (Automated Lifecycle).
---

# 🚀 WORKFLOW: FULL LIFECYCLE (HIGH-DENSITY)

This workflow is the **Master Orchestrator**. It leverages the entire `.agents` ecosystem to build robust, secure, and cost-effective SaaS applications from zero.

## PHASE 0: INGESTION (THE SOUL)
> **Tier**: BUDGET — read-only context loading.
- [ ] **Global Alignment**: Read `workspace_map.md`, `canons/global/`, and `rules/core-guardrails.md`.
- [ ] **Context Loading**: Read the current `BLUEPRINT.md` (if exists) or the project's intake brief.
- [ ] **Skill Activation**: Identify and activate the necessary specialized skills for the project domain.

## PHASE 1: STRATEGIC BLUEPRINT (THE BRAIN)
> **Tier**: PREMIUM — architecture and cross-system reasoning. Sequential Thinking mandatory.
- [ ] **Architectural Design**: Invoke `@skills/project-architect` to synthesize requirements into Chapter 1-7 of the Master Blueprint.
- [ ] **Cost Guard**: Invoke `@skills/cost-optimizer` to validate the chosen tech stack and infrastructure for token and cloud efficiency.
- [ ] **Security Blueprint**: Invoke `@skills/integrity-sentinel` to identify potential threat vectors (Auth, Data Leakage, RLS) before code is written.
- [ ] **Socratic Challenge**: AI must present at least TWO architectural risks or trade-offs for user confirmation.

## PHASE 2: SCAFFOLDING (THE SKELETON)
> **Tier**: STANDARD — multi-file creation, template population.
- [ ] **Initialize Context**: Run `/project-init`.
- [ ] **Pillar Setup**: Ensure `00_Strategy/`, `01_Product/`, `02_Creative/`, and `03_Tech/` are established.
- [ ] **Master Files**: Populate `BLUEPRINT.md`, `ROADMAP.md`, `STYLE_GUIDE.md`, and `ARCHITECTURE.md` using slot-fill templates.

## PHASE 3: EXECUTION LOOP (THE MUSCLES)
> **Tier**: STANDARD per feature. Escalate to PREMIUM if the feature touches auth, RLS, or global state.
For each feature defined in the Roadmap:
- [ ] **Feature Initiation**: Run `/app-builder`.
- [ ] **Security Implementation**: Invoke `@skills/integrity-sentinel` during API and Database design (Phase B of app-builder).
- [ ] **Evaluation Loop**: Invoke `@skills/integrity-sentinel` to verify that the implementation meets the original prompt requirements without regression.

## PHASE 4: CERTIFICATION (THE SEAL)
> **Tier**: PREMIUM — exhaustive certification, adversarial testing, final audit.
- [ ] **Quality Assurance**: Invoke `@skills/integrity-sentinel` to perform exhaustive TDD, Widget Testing, and Edge Case verification.
- [ ] **System Audit**: Invoke `@skills/integrity-sentinel` for a final structural and logic certification.
- [ ] **Zero N/A Compliance**: Ensure all context files touched during execution are fully populated and relevant.

## PHASE 5: MAINTENANCE & SYNC (THE HEALTH)
> **Tier**: BUDGET — deterministic script execution, no reasoning required.
- [ ] **Graph Update**: Run `python .agents/scripts/build_graph.py` to update symbolic relationships.
- [ ] **Catalog Sync**: Run `python .agents/scripts/update_catalog.py` to reflect new files in `catalog.json`.

---
*Portable Brainvibing Infrastructure - Orchestrated Lifecycle Protocol*