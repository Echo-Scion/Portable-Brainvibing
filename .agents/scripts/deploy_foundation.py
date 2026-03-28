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
    After deploy, runs build_graph.py and update_catalog.py automatically.
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
    FOLDERS_TO_SYNC = ["skills", "rules", "canons", "templates", "evals", "docs", "scripts"]

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

    # 3. Handle workspace_map.md and catalog.json (DEPRECATED PHYSICAL SYNC)
    # These are now generated fresh locally via update_catalog.py post-deploy.
    # Logic removed to prevent syncing outdated foundation maps.
    project_name = os.path.basename(os.path.abspath(target_root))

    # 4.5 Generate GEMINI.md from Template to Target Root (Smart Merge)
    src_gemini_template = os.path.join(source_agents, "templates", "GEMINI.template.md")
    dest_gemini = os.path.join(target_root, "GEMINI.md")
    if os.path.exists(src_gemini_template):
        print(f"\nProcessing GEMINI.md for '{project_name}'...")
        try:
            with open(src_gemini_template, 'r', encoding='utf-8') as f:
                raw_template = f.read()
            
            # Extract just the foundation block from template
            import re
            template_block_match = re.search(r"(<!-- START FOUNDATION MANDATES -->.*?<!-- END FOUNDATION MANDATES -->)", raw_template, re.DOTALL)
            foundation_block = template_block_match.group(1) if template_block_match else raw_template
            foundation_block = foundation_block.replace("{project_name}", project_name)

            final_content = ""
            status = ""
            
            if os.path.exists(dest_gemini):
                with open(dest_gemini, 'r', encoding='utf-8') as f:
                    local_content = f.read()
                
                # Check if it has the block
                if "<!-- START FOUNDATION MANDATES -->" in local_content and "<!-- END FOUNDATION MANDATES -->" in local_content:
                    final_content = re.sub(r"<!-- START FOUNDATION MANDATES -->.*?<!-- END FOUNDATION MANDATES -->", foundation_block, local_content, flags=re.DOTALL)
                    status = "UPDATED (Merged Block)"
                else:
                    # No marker, no obvious legacy traits: prepend foundation safely.
                    # We wrap the prepend in the marker so future updates work.
                    final_content = "# Workspace Rules & Mandates: " + project_name + "\n\n" + foundation_block + "\n\n## CUSTOM LOCAL RULES\n" + local_content
                    # Remove the original title from local_content if it existed to avoid double titles
                    final_content = re.sub(r"# Workspace Rules & Mandates:.*?\n", "", final_content, count=1)
                    status = "MERGED (Prepended to User Content)"
            else:
                final_content = raw_template.replace("{project_name}", project_name)
                status = "CREATED"

            if not dry_run:
                with open(dest_gemini, 'w', encoding='utf-8') as f:
                    f.write(final_content)
            
            print(f"  [{status}] GEMINI.md at project root{' (SIMULATED)' if dry_run else ''}.")
        except Exception as e:
            print(f"⚠️  Warning: Could not process GEMINI.md: {e}")

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
        update_catalog_script = os.path.join(scripts_dir, "update_catalog.py")

        if os.path.exists(build_graph_script):
            print("\n🧠 Running build_graph.py to rebuild knowledge graph...")
            subprocess.run([sys.executable, build_graph_script], cwd=target_root)
        
        if os.path.exists(update_catalog_script):
            print("\n📋 Running update_catalog.py to refresh catalog...")
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