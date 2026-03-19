# Context Orchestration Tactical Engine

## 🗺️ Contextual Navigation Steps
1. **Structural Scan (Macro)**: Identify project structure via `list_dir`. Skip `build/` and `node_modules/`.
2. **Topography Cutting**: Isolate the active feature domain to preserve token quota.
3. **Symbolic Analysis (Micro)**: Use `view_file_outline` to map hierarchies without reading full logic.
4. **Byte-Level Extraction**: Pull strictly necessary code snippets using StartLine/EndLine arguments.
5. **Index Refresh**: Re-run outlines after code mutations to keep symbol maps accurate.

## 🛠️ Symbolic Mapping Examples
**Scenario**: "Find authentication logic."
**Actions**: 
- Find `auth_service.dart` -> Outline hierarchies -> Extract `AuthService.login` specific lines.

## 🛡️ Navigation Guardrails
- **Max-3-Cycle Rule**: Limit iterative retrieval loops (grep -> view -> grep) to 3 cycles to prevent hallucination loops.
- **Minimalism**: Never read files > 100 lines without an outline first.

---
*Preserved from Portable Brainvibing Infrastructure*