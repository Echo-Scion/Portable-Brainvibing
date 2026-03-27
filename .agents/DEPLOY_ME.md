# 🚀 Agentic Deployment (Plug & Play)

This file allows any AI Agent (like Gemini CLI) to deploy the Foundation to a new project without requiring Python or external scripts.

## 🤖 Instructions for the AI Agent

If a user asks you to "Deploy the foundation" or "Initialize the agents" in a new project, follow these steps using your internal tools:

### 1. Identify Target
Confirm the target directory (usually the current working directory `.`).

### 2. Create Structure
Ensure the `.agents/` directory structure exists in the target:
- `.agents/skills/`
- `.agents/rules/`
- `.agents/workflows/`
- `.agents/canons/`
- `.agents/templates/`
- `.agents/scripts/`

### 3. Copy Essential Files
Read the following files from this source and write them to the same relative paths in the target:
- `.agents/catalog.json`
- `.agents/workspace_map.md`

### 4. Selective Sync (Agentic)
Iterate through the directories in this source and copy all `.md`, `.json`, `.py`, and `SKILL.md` files to the target. 
- **Priority**: Workflows, Rules, and Scripts (like `build_graph.py` and `update_catalog.py`) are mandatory for operational integrity.

### 5. Create Path Marker
Write the absolute path of THIS source foundation directory into a file named `.agents/.foundation_path` in the target project. This is critical for enabling the `sync_to_foundation.py` tool.

### 6. Validate
Once copied, try to `@` mention a rule (e.g., `@common/agent_protocols.md`) to verify that your indexing system recognizes the new local files.

---

> [!TIP]
> This method is preferred over `deploy_foundation.py` to minimize environment dependencies.