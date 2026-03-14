---
description: Steps for end-to-end feature creation (Model -> Provider -> UI -> Test).
---

# WORKFLOW: APP BUILDER GUIDE

Follow these steps to build a new feature/module in any project app.

## 0. CONTEXT RETRIEVAL (JIT)
*   [ ] Verify Binary Oratory compliance. IF unsure, use `grep_search` on `@agent_protocols.md`.
*   [ ] Verify architecture compliance. IF unsure, use `grep_search` on `@flutter_hybrid_architecture.md`.
*   [ ] If working in a **monorepo**, activate the `context-manager` skill.
*   [ ] Run `view_file` on `MainSystem/context/README.md` to identify the target app.
*   [ ] Scope ALL tool paths to the target app only (e.g., `MainSystem/apps/[sub_app]/lib/...`).
*   [ ] Call `task_boundary` with the app name in the `TaskName` before proceeding.

## 1. DEFINE DOMAIN MODEL
*   [ ] Create `lib/src/domain/feature_name.dart`. 
*   [ ] Invoke `@skills/skill-data-logic` to generate a Freezed model.
   - Assert: Union types for states (Loading/Data/Error).
   - Assert: `json_serializable` for API parity.

## 2. IMPLEMENT STATE MANAGEMENT
*   [ ] Create `lib/src/presentation/feature_provider.dart`. 
*   [ ] Invoke `@skills/skill-data-logic` to provide a Riverpod Notifier.
   - Assert: No business logic in the UI.
   - Assert: Error handling in the Provider.

## 3. BUILD UI COMPONENTS
*   [ ] Create `lib/src/presentation/feature_widget.dart`. 
*   [ ] Use `Theme.of(context)` and project design tokens.
*   [ ] Wrap in a `ConsumerWidget`.

## 4. VERIFY & TEST
*   [ ] Create `test/presentation/feature_test.dart`.
*   [ ] Invoke `@skills/skill-qa-engineer` to write unit and widget tests.
*   [ ] // turbo
    [ ] Run `flutter test`.

## 5. ANALYSIS & SUBMIT
*   [ ] // turbo
    [ ] Run `analyze_files` from `dart-mcp-server`.
*   [ ] Finalize code.