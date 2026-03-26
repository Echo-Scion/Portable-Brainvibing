# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
import os
import shutil
import argparse
import sys
import subprocess
import re

# Configuration
# Path to your central Foundation repository (Relatively determined from script location)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOUNDATION_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR)) 
FOUNDATION_AGENTS = os.path.join(FOUNDATION_ROOT, ".agents")

# Folders that represent "The Brain" and should evolve
EVOLVABLE_FOLDERS = ["skills", "rules", "workflows", "canons", "templates", "scripts"]

# Files/Folders to NEVER sync back to foundation (project-specific)
BLACKLIST = {
    "local",         # Project-specific experiments
    "tasks",         # Project-specific atomic tasks (inside workflows/)
    "personal",
    "debug_scripts",
    "pull_planning_context.py", # Local drive specific sync script
    ".git",
    "node_modules",
    "vitals",
    "MEMORY.md",
    "SAAS_MEMORY.md"
}

def increment_patch_version(content):
    """
    Finds 'version: "x.y.z"' or 'version: x.y.z' and increments z.
    """
    version_pattern = r'^(version:\s*["\']?)(\d+\.\d+\.)(\d+)(["\']?)$'
    
    def replace_version(match):
        prefix = match.group(1)
        base = match.group(2)
        patch = int(match.group(3))
        suffix = match.group(4)
        return f"{prefix}{base}{patch + 1}{suffix}"

    new_content, count = re.subn(version_pattern, replace_version, content, flags=re.MULTILINE)
    return new_content, count > 0

def sync_upstream(project_root, dry_run=False):
    """
    Syncs changes from the local project's .agents back to the Foundation.
    Automatically increments version if SKILL.md or metadata files are changed.
    """
    if dry_run:
        print("🧪 [DRY RUN] Mode enabled. No files will be physically modified.")

    project_agents = os.path.join(project_root, ".agents")
    foundation_path_marker = os.path.join(project_agents, ".foundation_path")
    
    # Prioritize persisted foundation path from deployment
    if os.path.exists(foundation_path_marker):
        with open(foundation_path_marker, "r", encoding="utf-8") as f:
            dynamic_foundation_root = f.read().strip()
        target_foundation_agents = os.path.join(dynamic_foundation_root, ".agents")
    else:
        # Fallback to legacy relative detection
        target_foundation_agents = FOUNDATION_AGENTS

    if not os.path.exists(project_agents):
        print(f"Error: Local .agents folder not found at {project_agents}")
        return False

    if not os.path.exists(target_foundation_agents):
        print(f"Error: Foundation .agents not found at {target_foundation_agents}")
        print("Please check the .agents/.foundation_path file or FOUNDATION_ROOT in this script.")
        return False

    print(f"🚀 Starting Upstream Sync: [Project] -> [_foundation]")
    print(f"Target: {target_foundation_agents}\n")

    class SyncStatus:
        def __init__(self):
            self.changes_count: int = 0
            self.version_bumps: int = 0

    status = SyncStatus()

    for folder in EVOLVABLE_FOLDERS:
        src_path = os.path.join(project_agents, folder)
        dest_path = os.path.join(target_foundation_agents, folder)

        if not os.path.exists(src_path):
            continue

        print(f"Checking {folder}...")

        for root, dirs, files in os.walk(src_path):
            # Skip blacklisted directories
            filtered_dirs = [d for d in dirs if d not in BLACKLIST]
            dirs.clear()
            dirs.extend(filtered_dirs)
            
            for file in files:
                # Skip blacklisted items or local-specific evolution (prefixed with 'local-')
                if file in BLACKLIST or file.startswith("local-") or file == ".gitkeep":
                    continue

                # Get relative path to maintain structure
                rel_path = os.path.relpath(os.path.join(root, file), src_path)

                # Double check if any part of the path starts with 'local-'
                path_parts = rel_path.split(os.sep)
                if any(p.startswith("local-") for p in path_parts):
                    continue

                local_file = os.path.join(root, file)
                foundation_file = os.path.join(dest_path, rel_path)

                # Check if foundation file exists and if content is different
                should_copy = False
                if not os.path.exists(foundation_file):
                    print(f"  [NEW] {os.path.join(folder, rel_path)}")
                    should_copy = True
                else:
                    with open(local_file, 'rb') as f:
                        local_content_bytes = f.read()
                    with open(foundation_file, 'rb') as f:
                        foundation_content_bytes = f.read()
                    
                    if local_content_bytes != foundation_content_bytes:
                        print(f"  [MODIFIED] {os.path.join(folder, rel_path)}")
                        should_copy = True

                if should_copy:
                    if not dry_run:
                        # Ensure directory exists in foundation
                        os.makedirs(os.path.dirname(foundation_file), exist_ok=True)
                        
                        # Logic: If it's a versioned file (like SKILL.md), increment version during copy
                        if file.endswith((".md", ".json", ".yaml")):
                            try:
                                with open(local_file, 'r', encoding='utf-8') as f:
                                    content = f.read()
                                
                                new_content, bumped = increment_patch_version(content)
                                
                                with open(foundation_file, 'w', encoding='utf-8') as f:
                                    f.write(new_content)
                                
                                if bumped:
                                    print(f"    ↳ ✨ Auto-bumped version for {file}")
                                    status.version_bumps += 1
                            except Exception as e:
                                print(f"    ⚠️ Warning: Could not auto-bump {file}: {e}")
                                shutil.copy2(local_file, foundation_file)
                        else:
                            shutil.copy2(local_file, foundation_file)
                    else:
                        print(f"  [SIMULATED] Copy {file} -> {os.path.dirname(foundation_file)}")
                    
                    status.changes_count += 1

    if int(status.changes_count) > 0:
        print(f"\n✅ Successfully synced {status.changes_count} files to Foundation.")
        if int(status.version_bumps) > 0:
            print(f"✨ Total versions bumped: {status.version_bumps}")
        
        if not dry_run:
            # Trigger Neural Graph Update
            graph_script = os.path.join(target_foundation_agents, "scripts", "build_graph.py")
            if os.path.exists(graph_script):
                print("🧠 Regenerating Knowledge Graph...")
                try:
                    subprocess.run([sys.executable, graph_script], cwd=os.path.dirname(target_foundation_agents), check=True)
                except Exception as e:
                    print(f"⚠️ Warning: Failed to update Knowledge Graph: {e}")

            # Trigger Catalog Update in Foundation
            if os.path.exists(catalog_script):
                print("🔄 Updating Foundation Catalog...")
                try:
                    # We run it using the foundation's own script to ensure context
                    subprocess.run([sys.executable, catalog_script], cwd=os.path.dirname(target_foundation_agents), check=True)
                    print("✅ Foundation Catalog & Workspace Map updated.")
                except Exception as e:
                    print(f"⚠️ Warning: Failed to auto-update catalog: {e}")
        else:
            print("\n🧪 [DRY RUN] Would trigger graph and catalog updates in foundation.")
    else:
        print("\n✨ No changes detected. Foundation is already up-to-date.")

    return True

def main():
    parser = argparse.ArgumentParser(description="Sync local agent evolution back to the Global Foundation.")
    parser.add_argument("--project", help="Path to the local project root", default=".")
    parser.add_argument("--dry-run", action="store_true", help="Simulate sync without modifying files.")
    
    args = parser.parse_args()
    
    # Resolve absolute path for project root
    project_root = os.path.abspath(args.project)
    
    sync_upstream(project_root, dry_run=args.dry_run)

if __name__ == "__main__":
    main()