---
description: Steps for end-to-end feature creation (Model -> Provider -> UI -> Test).
---

# WORKFLOW: APP BUILDER GUIDE

Follow these steps to build a new feature/module in any project app.

## 0. CONTEXT RETRIEVAL (JIT)
*   [ ] **Verify Residency**: Ensure the project has a physical `.agents/skills/` directory. 
    - **IF MISSING**: Run `python [GlobalRoot]\.agents\scripts\deploy_foundation.py --target .`.
*   [ ] **Verify Binary Oratory compliance**. IF unsure, use `@common/agent_protocols.md`.
*   [ ] **Verify architecture compliance**. IF unsure, use `@flutter/flutter_hybrid_architecture.md`.
*   [ ] If working in a **monorepo**, activate the `context-manager` skill from the local `.agents/skills/`.
*   [ ] Run `view_file` on the project's `context/README.md` or `BLUEPRINT.md` to identify the target app.
*   [ ] Scope ALL tool paths to the target app only (e.g., `MainSystem/apps/[sub_app]/lib/...`).
*   [ ] Call `task_boundary` with the app name in the `TaskName` before proceeding.

## 1. SPECIFICATION (Living Spec)
- [ ] **MANDATORY**: Update `BLUEPRINT.md` and `MEMORY.md` with the new feature logic.
- [ ] **Surgical Context Expansion**: If the feature introduces a new domain (e.g., Loyalty, SEO, Security), AI **MUST** create the corresponding context file from the **82 SaaS Startup Files** baseline (see `rules/common/context_naming_policy.md`).
- [ ] User MUST approve the blueprint and context expansion before any code is written.

## 2. AESTHETIC PROTOTYPING (Liquid Glass)
- [ ] Create UI screens using `skill-ui-finish`.
- [ ] Use high-fidelity placeholders for data.
- [ ] Ensure the "vibe" and micro-interactions are solid before logic.

## 3. DOMAIN & STATE (UDF)
- [ ] Create `lib/src/domain/feature_model.dart` (Freezed).
- [ ] Create `lib/src/presentation/feature_provider.dart` (Riverpod Notifier).
- [ ] Connect UI to the Provider (Model -> UI).

## 4. VERIFY & TEST
- [ ] Create tests in `test/presentation/feature_test.dart`.
- [ ] Run `/verify-loop`.