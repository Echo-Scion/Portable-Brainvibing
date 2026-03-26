# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
import os
import shutil
import subprocess
import sys
import re
import argparse

def deploy(source_root: str, target_root: str, dry_run: bool = False):
    """
    Copies foundation skills and rules to the target project.
    """
    if dry_run:
        print("🧪 [DRY RUN] Mode enabled. No files will be physically modified.")

    source_agents = os.path.join(source_root, ".agents")
    target_agents = os.path.join(target_root, ".agents")

    if not os.path.exists(source_agents):
        print(f"Error: Source foundation not found at {source_agents}")
        return False

    if not os.path.exists(target_agents):
        if not dry_run:
            os.makedirs(target_agents, exist_ok=True)
        print(f"Created local .agents/ at {target_agents}")

    # Folders to sync physically for IDE compatibility
    FOLDERS_TO_SYNC = ["skills", "rules", "canons", "templates"]

    # Exclude list: items that must never be overwritten on target
    BLACKLIST = {
        "deploy_foundation.py",
        ".git",
        "node_modules"
    }

    def sync_recursive(src: str, dest: str, blacklist: set[str] | None = None):
        """Surgical sync: create directories, copy/overwrite files from src, but KEEP local-only files."""
        if blacklist is None:
            blacklist = set()
        if not os.path.exists(dest):
            if not dry_run:
                os.makedirs(dest, exist_ok=True)
            print(f"  [CREATE] {dest}")

        for item in os.listdir(src):
            if item in blacklist:
                continue

            s = os.path.join(src, item)
            d = os.path.join(dest, item)

            if os.path.isdir(s):
                sync_recursive(s, d, blacklist)
            else:
                if not dry_run:
                    shutil.copy2(s, d)
                print(f"  [COPY] {item} -> {dest}")

    # 1. Sync standard folders
    for folder in FOLDERS_TO_SYNC:
        src_path = os.path.join(source_agents, folder)
        dest_path = os.path.join(target_agents, folder)

        if not os.path.exists(src_path):
            continue

        print(f"Syncing {folder}...")
        sync_recursive(src_path, dest_path, BLACKLIST)

    # 2. Sync workflows/ root files ONLY
    src_workflows = os.path.join(source_agents, "workflows")
    dest_workflows = os.path.join(target_agents, "workflows")
    if os.path.exists(src_workflows):
        print("Syncing workflows (root files only, skipping tasks/)...")
        if not os.path.exists(dest_workflows):
            if not dry_run:
                os.makedirs(dest_workflows, exist_ok=True)
        for item in os.listdir(src_workflows):
            s = os.path.join(src_workflows, item)
            d = os.path.join(dest_workflows, item)
            if os.path.isfile(s) and item not in BLACKLIST:
                if not dry_run:
                    shutil.copy2(s, d)
                print(f"  [COPY] {item} -> workflows/")
        tasks_dir = os.path.join(dest_workflows, "tasks")
        if not os.path.exists(tasks_dir):
            if not dry_run:
                os.makedirs(tasks_dir, exist_ok=True)
            print("  Created workflows/tasks/ for project-specific tasks.")

    # 3. Handle workspace_map.md
    src_map = os.path.join(source_agents, "workspace_map.md")
    dest_map = os.path.join(target_agents, "workspace_map.md")

    if os.path.exists(src_map):
        project_name = os.path.basename(os.path.abspath(target_root))

        if os.path.exists(dest_map):
            print(f"Updating workspace_map.md (surgical sections only)...")
            try:
                with open(src_map, 'r', encoding='utf-8') as f:
                    src_content = f.read()
                with open(dest_map, 'r', encoding='utf-8') as f:
                    dest_content = f.read()

                sections_to_update = [
                    r"<!-- SKILLS_START -->.*?<!-- SKILLS_END -->",
                    r"<!-- RULES_START -->.*?<!-- RULES_END -->",
                    r"<!-- WORKFLOWS_START -->.*?<!-- WORKFLOWS_END -->",
                    r"<!-- CANONS_START -->.*?<!-- CANONS_END -->",
                    r"<!-- SCRIPTS_START -->.*?<!-- SCRIPTS_END -->",
                    r"<!-- TEMPLATES_START -->.*?<!-- TEMPLATES_END -->",
                ]

                updated = dest_content
                for pattern in sections_to_update:
                    src_match = re.search(pattern, src_content, flags=re.DOTALL)
                    if src_match and re.search(pattern, updated, flags=re.DOTALL):
                        updated = re.sub(pattern, src_match.group(0), updated, flags=re.DOTALL)

                if not dry_run:
                    with open(dest_map, 'w', encoding='utf-8') as f:
                        f.write(updated)
                print(f"  [UPDATE] workspace_map.md sections{' (SIMULATED)' if dry_run else ''}")

            except Exception as e:
                print(f"⚠️  Warning: Could not surgical-update workspace_map.md: {e}")

        else:
            print(f"Creating fresh workspace_map.md for '{project_name}'...")
            try:
                with open(src_map, 'r', encoding='utf-8') as f:
                    src_content = f.read()

                header = (
                    f"# WORKSPACE MAP: {project_name} (.agents)\n\n"
                    "A high-level topography of the workspace for AI navigation and context initialization.\n\n"
                    "> [!IMPORTANT]\n"
                    "> This document is the **ORCHESTRATION ENTRY POINT**. \n"
                    "> - **Lazy-Loading**: Read this index FIRST, then read ONLY the relevant rule/skill files.\n"
                    "> - **Relative Paths**: Always use paths relative to the workspace root.\n\n"
                )
                active_projects = (
                    f"## Active Projects\n\n"
                    f"| Project | Type | Status | Path |\n"
                    f"|---|---|---|---|\n"
                    f"| `{project_name}` | Flutter Web | 🟢 Active | `./` |\n\n"
                )

                def extract_section(pattern, content, fallback=""):
                    m = re.search(pattern, content, flags=re.DOTALL)
                    return m.group(0) if m else fallback

                foundation_section = "## Global Foundation (`.agents/`)\n> High-density technical standards.\n> **Note**: Use `deploy_foundation.py` to sync to local apps.\n\n"
                rules_label = "### Rules (`rules/`)\n"
                rules_block = extract_section(r"<!-- RULES_START -->.*?<!-- RULES_END -->", src_content, "<!-- RULES_START -->\n<!-- RULES_END -->")
                skills_label = "\n### Skills (`skills/`)\n"
                skills_block = extract_section(r"<!-- SKILLS_START -->.*?<!-- SKILLS_END -->", src_content, "<!-- SKILLS_START -->\n<!-- SKILLS_END -->")
                canons_label = "\n### Domain Canon (`canons/`)\n"
                canons_block = extract_section(r"<!-- CANONS_START -->.*?<!-- CANONS_END -->", src_content, "<!-- CANONS_START -->\n<!-- CANONS_END -->")
                workflows_label = "\n### Workflows (`workflows/`)\n"
                workflows_block = extract_section(r"<!-- WORKFLOWS_START -->.*?<!-- WORKFLOWS_END -->", src_content, "<!-- WORKFLOWS_START -->\n<!-- WORKFLOWS_END -->")
                scripts_label = "\n### Maintenance Scripts (`scripts/`)\n"
                scripts_block = extract_section(r"<!-- SCRIPTS_START -->.*?<!-- SCRIPTS_END -->", src_content, "<!-- SCRIPTS_START -->\n<!-- SCRIPTS_END -->")
                templates_label = "\n### Templates (`templates/`)\n"
                templates_block = extract_section(r"<!-- TEMPLATES_START -->.*?<!-- TEMPLATES_END -->", src_content, "<!-- TEMPLATES_START -->\n<!-- TEMPLATES_END -->")

                memory_footer = (
                    "\n## Memory & Implementation\n"
                    f"- **Project Blueprint**: `context/00_Strategy/BLUEPRINT.md` — Master architecture & feature scope.\n"
                    "- **Workspaces**: `.agents/workspace_map.md` — (This file) Orchestration entry point.\n"
                    "- **Foundation Link**: `.agents/.foundation_path` → `_foundation` root for sync support.\n"
                )

                new_content = (
                    header + active_projects
                    + foundation_section
                    + rules_label + rules_block
                    + skills_label + skills_block
                    + canons_label + canons_block
                    + workflows_label + workflows_block
                    + scripts_label + scripts_block
                    + templates_label + templates_block
                    + memory_footer
                )

                if not dry_run:
                    with open(dest_map, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                print(f"  Created project-local workspace_map.md for '{project_name}'{' (SIMULATED)' if dry_run else ''}.")

            except Exception as e:
                print(f"⚠️  Warning: Could not create sanitized workspace_map.md: {e}")

    # 4. Copy catalog.json
    src_catalog = os.path.join(source_agents, "catalog.json")
    dest_catalog = os.path.join(target_agents, "catalog.json")
    if os.path.exists(src_catalog):
        if not dry_run:
            shutil.copy2(src_catalog, dest_catalog)
        print(f"Synced catalog.json{' (SIMULATED)' if dry_run else ''}.")

    # 5. Persist the source foundation path
    if not dry_run:
        try:
            with open(os.path.join(target_agents, ".foundation_path"), "w", encoding="utf-8") as f:
                f.write(os.path.abspath(source_root))
            print("📌 Foundation path persisted for sync support.")
        except Exception as e:
            print(f"⚠️  Warning: Could not persist foundation path: {e}")

    # 6. Run build_graph and update_catalog automatically post-deploy
    if not dry_run:
        scripts_dir = os.path.join(target_agents, "scripts")
        build_graph_script = os.path.join(scripts_dir, "build_graph.py")

        if os.path.exists(build_graph_script):
            print("\n🧠 Running build_graph.py to rebuild knowledge graph...")
            subprocess.run([sys.executable, build_graph_script], cwd=target_root)
        
        if os.path.exists(update_catalog_script):
            subprocess.run([sys.executable, update_catalog_script], cwd=target_root)

    print(f"\n✅ Deployment finished{' (SIMULATED)' if dry_run else ''}.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Deploy Global Foundation physically to a local project.")
    parser.add_argument("--source", help="Path to the global foundation root", default=None)
    parser.add_argument("--target", help="Path to the target project root", default=".")
    parser.add_argument("--dry-run", action="store_true", help="Simulate deployment without modifying files.")

    args = parser.parse_args()

    source = args.source
    if not source:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        source = os.path.abspath(os.path.join(script_dir, "..", ".."))

    deploy(source, args.target, dry_run=args.dry_run)

if __name__ == "__main__":
    main()