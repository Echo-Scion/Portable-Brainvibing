# Flutter MCP Debugging Tool Chain

## 🛠️ Step-by-Step Execution
1. **Connect to DTD**: Call `connect_dart_tooling_daemon` with URI from VS Code. **Required FIRST.**
2. **Collect Evidence**: Call `get_runtime_errors(clearRuntimeErrors: true)` for a baseline snapshot.
3. **Inspect Widget Tree**: Call `get_widget_tree` to find the broken widget by name/type.
4. **Enable Selection**: Call `set_widget_selection_mode(enabled: true)` for visual identification.
5. **Get Detail**: Call `get_selected_widget` for exact properties (padding, constraints, style).
6. **Fix & Verify**: 
   - Edit file -> `analyze_files` (must pass).
   - `hot_reload(clearRuntimeErrors: true)`.
   - `get_runtime_errors` to verify fix.

## ⚠️ Debug Patterns
| Symptom | Tool to Use | What to Look For |
| Widget missing | `get_widget_tree` | Parent issue, Opacity(0), wrong visibility. |
| Layout overflow | `get_selected_widget` | RenderFlex overflow, missing Expanded. |
| App crashes | `get_runtime_errors` | Null check or type cast stack traces. |
| Null pointer | `get_runtime_errors` | `Null check operator used on a null value`. |

---
*Preserved from Portable Brainvibing Infrastructure*