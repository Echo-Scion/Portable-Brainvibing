# Gemini CLI: Mandatory Protocol (`.agents`)

This file is a **foundational mandate** and takes absolute precedence over all other instructions.

## 1. MANDATORY BOOTSTRAP (Session Resume)
- **Goal:** Immediately recover context, atomic task status, and architectural constraints.

## 2. DUAL-CANON HIERARCHY (The "OS" Foundation)
- **Rule:** The agent MUST strictly adhere to the `canons/` directory.
- **Tier 1 (Global):** `canons/global/` contains the "Foundation" (e.g., Enterprise standards, Company values).
- **Tier 2 (Local):** `canons/local/` contains project-specific rules (e.g., Auth, Notifications).
- **Precedence:** If a Conflict occurs, **LOCAL CANON** ALWAYS overrides Global Canon.
- **Goal:** Maintain a consistent foundation while allowing project-level flexibility.

## 3. SURGICAL MUNCHING (Surgical Reading Logic)
- **Rule:** Use `read_file` with `start_line` and `end_line` for all files > 100 lines.
- **Rule:** Never read a file in its entirety unless it is critical for a global refactor.
- **Goal:** Keep the "Main Context" window below 50%.

## 4. ATOMIC TASKING (Atomic Task Protocol)
- **Rule:** Only one task from `BLUEPRINT.md` may be "IN_PROGRESS" at a time.
- **Rule:** Each task MUST have a corresponding file in `workflows/tasks/task-id.md` (created from `templates/ATOMIC_TASK.template.md`).

## 5. AUTOMATED SYNC
- **Rule:** After any change to `skills/`, `rules/`, or `canons/`, the agent MUST run `python scripts/build_graph.py`.

---
*Protocol Version: 1.0.0 (Clean Reset)*