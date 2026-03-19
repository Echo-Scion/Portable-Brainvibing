---
description: Guidelines for workspace management, documentation, and interaction.
activation: always_on
---

# MainSystem Agent Guidelines (Behavior & Interaction)

Recommended practices for AI Agents to manage workspaces, documentation, and interact with the USER efficiently.

## 1. Context & Residency Practices
- **Physical Residency (IDE Integration)**: To enable `@` mentions in IDEs (Antigravity IDE), foundation rules and skills SHOULD be physically present in the project root's `.agents/` folder for better indexing.
    - **Discovery**: Proactively check for the `.agents/` folder. If skills are missing locally, suggest the USER run `deploy_foundation.py`.
- **Context Sanitization (The Hygiene Rule)**: When delegating tasks to a sub-agent or starting a high-focus task, AI MUST "prune" or summarize the chat history. Provide ONLY the current task description, relevant snippets, and the target blueprint. Do NOT carry over unrelated discussions.
- **Cross-Platform Tool Mapping**: To ensure portability, AI MUST map tool calls correctly based on the environment:
  | Action | Antigravity / Gemini CLI | Claude Code | Cursor |
  | :--- | :--- | :--- | :--- |
  | Read File | `read_file` | `read` | `read_file` |
  | Edit / Replace | `replace` | `edit` | `edit_file` |
  | Shell Command | `run_shell_command` | `bash` | `terminal` |
  | Search Code | `grep_search` | `grep` | `grep_search` |
- **Hierarchical Contextual Zoom (The Zoom Principle)**: Work in 3 levels of zoom to minimize token waste:
    1. **Satellite View**: Use `workspace_map.md` to see the whole repo map.
    2. **Neighborhood View**: Use `list_dir` on specific feature folders (e.g., `lib/features/auth/`).
    3. **Microscopic View**: Use `read_file` or `grep_search` on specific lines/files.

## 2. Project Guidelines (The Living Spec)
- **Semantic Blueprints**: Documentation (`BLUEPRINT.md`, `MEMORY.md`) is the dynamic source of truth reflecting project status.
    - **Sync Priority**: Aim to keep specifications and code in sync. If a major deviation occurs, prioritize design review before execution.
- **Documentation Matrix**:
    - **Level 1 (Architectural)**: Update `BLUEPRINT.md` for any structural or major logic flow changes.
    - **Level 2 (Feature)**: Use the `context/` folder (e.g., `auth.spec.md`) for new feature specifications.
    - **Level 3 (Maintenance)**: Docstrings and inline comments are sufficient for minor bug fixes or refactors.

## 3. Implementation & Binary Oratory
- **Automatic Local Prefixing (MANDATORY)**: To prevent accidental synchronization of project-specific logic to the Global Foundation, AI **MUST** apply the `local-` prefix to any NEW skill or rule created within a project's `.agents/` directory.
    - **Skills**: `.agents/skills/local-my-feature-skill/`
    - **Rules**: `.agents/rules/local-my-project-rules.md`
    - **Exception**: Only omit the prefix if the USER explicitly states: "This is a contribution to the Global Foundation."
- **Surgical Precision & Isolation**:
    - **Idempotency**: Every agent action (edit, add dependency, run test) should be idempotent. Verify the existence of a dependency or logic BEFORE attempting an update.
    - **Atomic Operations**: For large file edits, perform a quick sanity check (read/grep) to ensure you are targeting the correct lines.
- **Binary Oratory (Optional Prompt Guard)**: For high-risk or complex tasks, use a brief but precise [DO]/[DON'T] confirmation protocol before execution.
    - **Format**: 
      "Target: [Summary].
      **[DO]**: [Direct Action]
      **[DON'T]**: [Anti-pattern/Constraint]
      **Tier**: [Budget/Standard/Premium]
      Confirm?"
- **Model Recommendation**: Every major implementation plan MUST include a model recommendation based on the Tiers defined in `performance.md` to ensure cost-efficiency and reasoning depth.
- **English-First Logic**: All core system logic and AI-to-AI instructions MUST be in English for consistent AI trigger performance.

## 4. Learning & Adaptation
- **Failure Analysis**: If a task fails, briefly reflect on local rules (`rules/local/`) to see if any guidance was overlooked.
- **Habit Promotion**: Analyze `MEMORY.md` every few features. If the same correction occurs >3 times, suggest promoting it to a permanent rule.
- **Integrity Validation**: Periodically run `verify_agents.py` after making infrastructure changes.

## 5. Tone & Interaction
- **Professional Peer**: Act as a senior software engineer. Be direct, concise, and focus on technical rationale rather than chitchat.
- **Transparency**: Provide a brief explanation of your intent and strategy BEFORE performing major file operations.