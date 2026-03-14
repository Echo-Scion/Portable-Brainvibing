---
description: Using visual screenshots + MCP tools to identify and fix UI bugs.
---

# WORKFLOW: FLUTTER DEBUGGING PROCESS

Follow these steps to diagnose and fix a UI or logic issue in a Flutter app.

## 0. CONTEXT RETRIEVAL (JIT)
*   [ ] Verify architecture compliance. IF unsure, use `grep_search` on `@agent_protocols.md`.
*   [ ] Run `view_file` on `MainSystem/context/README.md` to identify the target app.
*   [ ] Scope ALL tool paths to the target app only.

## 1. VISUAL DIAGNOSIS
*   [ ] Capture a screenshot or recording of the issue.
*   [ ] Attach it to the conversation for AI analysis.
*   [ ] Use the `flutter-debugger` skill to enable `set_widget_selection_mode`.

## 2. INSPECT WIDGET TREE
*   [ ] // turbo
    [ ] Run `get_widget_tree` from `dart-mcp-server`.
*   [ ] Review the tree and identify the widget's properties (padding, constraints, etc.).

## 3. CHECK RUNTIME ERRORS
*   [ ] // turbo
    [ ] Run `get_runtime_errors` via MCP to see any exceptions or stack traces.

## 4. APPLY FIX & RELOAD
*   [ ] Verify the fix adheres to project standards. IF unsure, use `grep_search` on `@flutter_standards.md`.
*   [ ] Modify the code based on the diagnosis.
*   [ ] // turbo
    [ ] Run `hot_reload` to see the results instantly.

## 5. RE-VERIFY
*   [ ] Update existing tests or add a new test case if a regression is found.
*   [ ] // turbo
    [ ] Run `analyze_files` from `dart-mcp-server`.