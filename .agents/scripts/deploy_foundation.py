import os
import shutil
import argparse
import sys
import re

def deploy(source_root, target_root):
    """
    Copies foundation skills and rules to the target project.
    """
    source_agents = os.path.join(source_root, ".agents")
    target_agents = os.path.join(target_root, ".agents")

    if not os.path.exists(source_agents):
        print(f"Error: Source foundation not found at {source_agents}")
        return False

    if not os.path.exists(target_agents):
        os.makedirs(target_agents)
        print(f"Created local .agents/ at {target_agents}")

    # Folders to sync physically for IDE compatibility
    FOLDERS_TO_SYNC = ["skills", "rules", "workflows", "canons", "templates"]
    
    BLACKLIST = {
        "deploy_foundation.py",
        ".git",
        "node_modules"
    }

    for folder in FOLDERS_TO_SYNC:
        src_path = os.path.join(source_agents, folder)
        dest_path = os.path.join(target_agents, folder)

        if not os.path.exists(src_path):
            continue

        print(f"Syncing {folder}...")
        
        # Surgical sync: create directories, copy/overwrite foundation files, but KEEP local files.
        def sync_recursive(src, dest):
            if not os.path.exists(dest):
                os.makedirs(dest)
            
            for item in os.listdir(src):
                if item in BLACKLIST:
                    continue
                
                s = os.path.join(src, item)
                d = os.path.join(dest, item)
                
                if os.path.isdir(s):
                    sync_recursive(s, d)
                else:
                    # Overwrite existing foundation files, but this preserves other files in dest
                    shutil.copy2(s, d)

        sync_recursive(src_path, dest_path)

    # Copy catalog and map
    for root_file in ["catalog.json", "workspace_map.md"]:
        src_file = os.path.join(source_agents, root_file)
        dest_file = os.path.join(target_agents, root_file)
        if os.path.exists(src_file):
            if root_file == "workspace_map.md":
                if os.path.exists(dest_file):
                    print(f"Updating skills section in {root_file}...")
                    try:
                        with open(src_file, 'r', encoding='utf-8') as f:
                            src_content = f.read()
                        with open(dest_file, 'r', encoding='utf-8') as f:
                            dest_content = f.read()
                        
                        # Extract skills section from source
                        pattern = r"<!-- SKILLS_START -->.*?<!-- SKILLS_END -->"
                        src_match = re.search(pattern, src_content, flags=re.DOTALL)
                        
                        if src_match:
                            # Replace in destination
                            if re.search(pattern, dest_content, flags=re.DOTALL):
                                updated_dest = re.sub(pattern, src_match.group(0), dest_content, flags=re.DOTALL)
                                with open(dest_file, 'w', encoding='utf-8') as f:
                                    f.write(updated_dest)
                            else:
                                # If no markers in dest, append it or just overwrite? 
                                # Safer to overwrite if no markers
                                shutil.copy2(src_file, dest_file)
                        else:
                            shutil.copy2(src_file, dest_file)
                    except Exception as e:
                        print(f"⚠️ Warning: Could not surgical-update {root_file}: {e}")
                        shutil.copy2(src_file, dest_file)
                else:
                    # INITIAL CREATION: Prune foundation-specific paths to avoid context pollution
                    print(f"Creating fresh {root_file} for target project...")
                    try:
                        with open(src_file, 'r', encoding='utf-8') as f:
                            src_content = f.read()
                        
                        # Very aggressive pruning for first-time deploy
                        # 1. Keep the Header and Rules section
                        # 2. Extract Skills section
                        # 3. Use a Generic Active Projects table
                        
                        header = "# WORKSPACE MAP: Local Project (.agents)\n\nA high-level topography of the workspace.\n\n"
                        active_projects = "## Active Projects\n\n| Project | Type | Status | Path |\n|---|---|---|---|\n| `MainApp` | Flutter | Active | `./` |\n\n"
                        
                        rules_pattern = r"## Global Foundation.*?### Rules \(.*?\).*?(?=\n### Skills)"
                        rules_match = re.search(rules_pattern, src_content, flags=re.DOTALL)
                        rules_section = rules_match.group(0) if rules_match else "### Rules (`rules/`)\n(Rules list auto-populated from foundation)\n"
                        
                        skills_pattern = r"### Skills \(.*?\).*?<!-- SKILLS_START -->.*?<!-- SKILLS_END -->"
                        skills_match = re.search(skills_pattern, src_content, flags=re.DOTALL)
                        skills_section = skills_match.group(0) if skills_match else "### Skills\n(Skills list auto-populated from foundation)\n"
                        
                        # Memory footer
                        
                        new_content = header + active_projects + "## Global Foundation (`.agents/`)\n\n" + rules_section + "\n" + skills_section + footer
                        
                        with open(dest_file, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                    except Exception as e:
                        print(f"⚠️ Warning: Could not create sanitized {root_file}, falling back to copy: {e}")
                        shutil.copy2(src_file, dest_file)
            else:
                shutil.copy2(src_file, dest_file)

    # Persist the source foundation path for bi-directional sync support
    try:
        with open(os.path.join(target_agents, ".foundation_path"), "w", encoding="utf-8") as f:
            f.write(os.path.abspath(source_root))
        print(f"📌 Foundation path persisted for sync support.")
    except Exception as e:
        print(f"⚠️ Warning: Could not persist foundation path: {e}")

    print("\n✅ Foundation deployed physically to local project.")
    print("IDE should now be able to resolve @ mentions and symbols.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy Global Foundation physically to a local project.")
    parser.add_argument("--source", help="Path to the global foundation root", default=None)
    parser.add_argument("--target", help="Path to the target project root", default=".")
    
    args = parser.parse_args()
    
    # Try to auto-detect source if not provided
    source = args.source
    if not source:
        # Assume the script is in .agents/scripts/ of the foundation
        script_dir = os.path.dirname(os.path.abspath(__file__))
        source = os.path.abspath(os.path.join(script_dir, "..", ".."))

    deploy(source, args.target)