---
description: Steps for end-to-end feature creation (Model -> Provider -> UI -> Test).
---

# 🏗️ WORKFLOW: APP BUILDER (SURGICAL)

This workflow defines the precision implementation cycle for individual features, fully integrated with the 4-Pillar hierarchy and SaaS Registry.

## 0. PRE-FLIGHT (JIT CONTEXT)
- [ ] **Verify Environment**: Ensure `.agents/` is synced and active.
- [ ] **Rule Alignment**: Read `rules/00_always_on_core.md` and `rules/01_always_on_context.md`.
- [ ] **Surgical Entry**: Identify the target folder (00-03) and the relevant Prefix from `templates/SAAS_STARTUP_STRUCTURE.md`.

## 1. SPECIFICATION (LIVING DATA)
- [ ] **Master Update**: Add the feature summary to `00_Strategy/BLUEPRINT.md` and `01_Product/ROADMAP.md`.
- [ ] **Registry Expansion**: Create a new Prefix-based detail file (e.g., `01_Product/Rev_Payment_Gateways.md`) if the domain is new or requires high depth.
- [ ] **Approval**: Present the "Surgical Spec" to the user for approval before writing code.

## 2. AESTHETIC DESIGN (LIQUID GLASS)
- [ ] **Vibe Check**: Invoke `@skills/ui-finish` to design the UI layout and micro-interactions.
- [ ] **Component Blueprint**: Define the Widget tree and design tokens in `02_Creative/STYLE_GUIDE.md`.

## 3. DOMAIN & LOGIC (TECHNICAL DEPTH)
- [ ] **Data Modeling**: Invoke `@skills/data-logic` to create immutable Freezed models.
- [ ] **Security Check**: Invoke `@skills/security-expert` to audit data parsing and storage logic.
- [ ] **State Management**: Implement Riverpod Notifiers and business logic services.
- [ ] **API Contract**: Invoke `@skills/api-contract` if backend interaction is required.

## 4. VERIFICATION & AUDIT (CERTIFICATION)
- [ ] **TDD Loop**: Invoke `@skills/qa-engineer`. Write and run tests (`flutter test`).
- [ ] **Logical Audit**: Invoke `@skills/system-audit` to certify the feature's mechanical integrity.
- [ ] **Regressive Evaluation**: Invoke `@skills/eval-engineer` to confirm no core logic was broken during the build.

## 5. WRAP-UP
- [ ] **Memory Persistence**: Update `00_Strategy/MEMORY.md` with the implementation log.
- [ ] **Next Step**: Propose the next logical atomic task based on the Roadmap.

---
*Portable Brainvibing Infrastructure - Surgical App Builder Protocol*