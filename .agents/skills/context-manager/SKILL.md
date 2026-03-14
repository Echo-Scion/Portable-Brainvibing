---
name: context-manager
description: Integrated protocol for zero-waste codebase navigation. Use when starting a new codebase analysis or when searching for symbols. Do NOT use for writing actual feature logic.
compatibility: Optimized for Antigravity (Google Deepmind Advanced Agentic Coding) and standard Markdown-based agent tooling.
Recommended_Tier: Budget
---

# Context Orchestrator: Deep Symbolic & Structural Mapping

You are an Elite Agent operating exactly within parameter limits. This protocol combines the precision of **Symbolic/AST Analysis** with **Structural Orchestration** to achieve maximum token efficiency across any codebase.

## Critical Validation
- **Token Efficiency:** Never use full `view_file` on files > 100 lines without running `view_file_outline` first. Data transmission must always be minimalist and target-oriented.
- **The Max-3-Cycle Rule:** When investigating an issue or searching for context, limit iterative retrieval loops (e.g. grep -> view -> grep) to a strict maximum of 3 cycles. 

## Workflow Pattern (Contextual Navigation)
**Step 1: Structural Scan (Macro)**
- Identify the core project structure using `list_dir` and `find_by_name`. 
- Analyze `pubspec.yaml` or `package.json` to understand dependencies. Skip irrelevant directories (build/, node_modules/).

**Step 2: Topography Cutting**
- For large structures, forcibly isolate the active feature or application domain. Ignore implementation details in unrelated modules to preserve token quota.
- Create a linear spatial navigation summary in your notes to prevent repetitive scans.

**Step 3: Symbolic Analysis (Micro)**
- Run `view_file_outline` on target files to map class, method, and property hierarchies without reading the full logic.
- Identify the exact symbol locations and their line metadata.

**Step 4: Byte-Level Extraction**
- Use `view_code_item` or line-specific `view_file` arguments (StartLine/EndLine) to pull only the strictly necessary memory block (code snippet) for your task. 

**Step 5: Dynamic Index Refresh**
- After any code mutation, immediately refresh your "mental index" by re-running `view_file_outline` to ensure your symbol maps remain accurate.

## Examples
**User says:** "Find the authentication logic in this repo"
**Actions:**
1. Call `find_by_name` for `auth` or `login`.
2. Discover `auth_service.dart`.
3. Call `view_file_outline` on `auth_service.dart`.
4. Call `view_code_item` for `AuthService.login`.
**Result:** Precise extraction of strictly relevant authentication logic without reading thousands of lines.

## Troubleshooting
- **Error:** Searching for a symbol keeps failing after multiple `grep_search` and `view_file` attempts.
- **Cause:** Hallucination loop triggered by bad initial search parameters or missing files.
- **Solution:** Stop immediately upon hitting the 3-cycle limit. Assume the symbol does not exist in the immediate area. Ask the user for clarification or pointers.