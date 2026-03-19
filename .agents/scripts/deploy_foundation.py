import os
import shutil
import argparse
import sys

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
        "audit_repo.py",
        ".git",
        "node_modules"
    }

    for folder in FOLDERS_TO_SYNC:
        src_path = os.path.join(source_agents, folder)
        dest_path = os.path.join(target_agents, folder)

        if not os.path.exists(src_path):
            continue

        print(f"Syncing {folder}...")
        
        # We use a simple copytree with an ignore function
        def ignore_func(directory, contents):
            return [c for c in contents if c in BLACKLIST]

        if os.path.exists(dest_path):
            # For simplicity in this script, we remove and recopy
            # In a production script, we might want a more surgical sync
            shutil.rmtree(dest_path)
        
        shutil.copytree(src_path, dest_path, ignore=ignore_func)

    # Copy catalog and map
    for root_file in ["catalog.json", "workspace_map.md"]:
        src_file = os.path.join(source_agents, root_file)
        dest_file = os.path.join(target_agents, root_file)
        if os.path.exists(src_file):
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