# 🚀 Agentic Deployment (Plug & Play)

This file allows any AI Agent (like Gemini CLI or Antigravity) to deploy the Foundation to a new project **without requiring Python or external scripts**.

## 🤖 Instructions for the AI Agent

If a user asks you to "Deploy the foundation" or "Initialize the agents" in a new project, follow these steps using your internal tools:

### 1. Identify Target
Confirm the target directory (usually the current working directory `.`). Identify the project name from the folder name (e.g., `my_app` from path `/Users/USER/Projects/my_app`).

### 2. Create Structure
Ensure the `.agents/` directory structure exists in the target:
- `.agents/skills/`
- `.agents/rules/`
- `.agents/workflows/`
- `.agents/canons/`
- `.agents/templates/`
- `.agents/scripts/`

### 3. Selective Sync (Agentic)
Iterate through the directories in this source and copy all `.md`, `.json`, `.py`, and `SKILL.md` files to the target.
- **Priority**: Workflows, Rules, and Scripts (like `build_graph.py` and `update_catalog.py`) are mandatory for operational integrity.

### 5. Smart Merge GEMINI.md
This is the critical step that creates the **Master Boot Record** for the target project.

**Do NOT simply copy or blindly overwrite `GEMINI.md`.**

Use the following merge logic:

1. Read `.agents/templates/GEMINI.template.md` from the source.
2. Extract the `<!-- START FOUNDATION MANDATES -->...<!-- END FOUNDATION MANDATES -->` block from the template.
3. Replace `{project_name}` in the block with the actual project name from Step 1.
4. Check if a `GEMINI.md` already exists in the target root:
   - **If YES and has markers:** Replace only the `<!-- START FOUNDATION MANDATES -->...<!-- END FOUNDATION MANDATES -->` block in the existing file. All other content (custom local rules) is **preserved untouched**.
   - **If YES but no markers (legacy file):** Prepend the Foundation block at the top. Wrap the original content under a `## CUSTOM LOCAL RULES` heading below it.
   - **If NO:** Write the full template (with project name injected) as a new `GEMINI.md` in the target root.

### 6. Create Path Marker
Write the absolute path of THIS source foundation directory into a file named `.agents/.foundation_path` in the target project. This is critical for enabling the `sync_to_foundation.py` tool.

### 7. Validate
Once copied, confirm that `GEMINI.md` exists at the target root and contains the `<!-- START FOUNDATION MANDATES -->` marker. This confirms the Master Boot Record is correctly installed.

---

> [!TIP]
> This method is preferred over `deploy_foundation.py` to minimize environment dependencies and gives the AI agent full contextual control over the merge logic.

> [!IMPORTANT]
> **Merge, Never Overwrite.** The Smart Merge strategy ensures a project's custom `GEMINI.md` content is always preserved. The Foundation block (`<!-- START FOUNDATION MANDATES -->`) is treated as an updateable zone; everything else is inviolable.