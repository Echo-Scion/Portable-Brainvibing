import os
import shutil
import argparse
import sys
import re

def create_ai_bridges(target_root, selected_bridges):
    """
    Creates standard AI instruction files only for selected IDEs.
    """
    if not selected_bridges:
        return

    print(f"🌉 Building selected AI Bridges: {', '.join(selected_bridges)}...")
    
    bridge_content = """# AI CONTEXT
This project uses an Agentic Foundation. Refer to:
- `.agents/workspace_map.md` for project structure.
- `.agents/rules/` for coding standards.
"""

    if "cursor" in selected_bridges:
        with open(os.path.join(target_root, ".cursorrules"), "w", encoding="utf-8") as f:
            f.write(bridge_content)

    if "windsurf" in selected_bridges:
        with open(os.path.join(target_root, ".windsurfrules"), "w", encoding="utf-8") as f:
            f.write(bridge_content)

    if "copilot" in selected_bridges:
        github_dir = os.path.join(target_root, ".github")
        if not os.path.exists(github_dir):
            os.makedirs(github_dir)
        with open(os.path.join(github_dir, "copilot-instructions.md"), "w", encoding="utf-8") as f:
            f.write(bridge_content)
    
    print("✅ Selected AI Bridges established.")

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
    
    stats = {folder: 0 for folder in FOLDERS_TO_SYNC}
    warnings = []

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
        def sync_recursive(src, dest, current_folder):
            if not os.path.exists(dest):
                os.makedirs(dest)
            
            items = os.listdir(src)
            if not items and current_folder == "skills":
                warnings.append(f"⚠️ Empty skill directory found: {src}")

            for item in items:
                if item in BLACKLIST:
                    continue
                
                s = os.path.join(src, item)
                d = os.path.join(dest, item)
                
                if os.path.isdir(s):
                    sync_recursive(s, d, current_folder)
                else:
                    try:
                        shutil.copy2(s, d)
                        stats[current_folder] += 1
                    except Exception as e:
                        warnings.append(f"❌ Failed to copy {s}: {e}")

        sync_recursive(src_path, dest_path, folder)

    # Verify skills specifically
    if os.path.exists(os.path.join(target_agents, "skills")):
        for skill_dir in os.listdir(os.path.join(target_agents, "skills")):
            skill_path = os.path.join(target_agents, "skills", skill_dir)
            if os.path.isdir(skill_path) and skill_dir not in BLACKLIST:
                if not os.path.exists(os.path.join(skill_path, "SKILL.md")):
                    warnings.append(f"⚠️ Skill '{skill_dir}' is missing SKILL.md in target!")

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

    # Create AI Bridges for Cursor, Windsurf, Copilot
    create_ai_bridges(target_root, getattr(deploy, "selected_bridges", []))

    print("\n--- Deployment Summary ---")
    for folder, count in stats.items():
        print(f"  - {folder.capitalize()}: {count} files synced")
    
    if warnings:
        print("\n--- Warnings/Errors ---")
        for warning in warnings:
            print(f"  {warning}")

    print("\n✅ Foundation deployed physically to local project.")

    # Knowledge Graph Integration
    build_script = os.path.join(target_agents, "scripts", "build_graph.py")
    if os.path.exists(build_script):
        should_build = False
        if getattr(deploy, "auto_build", False):
            should_build = True
        else:
            try:
                answer = input("\n📊 Build Knowledge Graph for the target project? (y/N): ").lower()
                if answer == 'y':
                    should_build = True
            except EOFError:
                # Fallback for non-interactive environments
                pass

        if should_build:
            print("🚀 Generating Knowledge Graph...")
            import subprocess
            try:
                # Use sys.executable to ensure we use the same python interpreter
                subprocess.run([sys.executable, build_script], check=True, cwd=target_root)
                print("✅ Knowledge Graph updated successfully.")
            except subprocess.CalledProcessError as e:
                print(f"❌ Error building Knowledge Graph: {e}")
            except Exception as e:
                print(f"❌ Unexpected error during graph build: {e}")

    print("IDE should now be able to resolve @ mentions and symbols.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deploy Global Foundation physically to a local project.")
    parser.add_argument("--source", help="Path to the global foundation root", default=None)
    parser.add_argument("--target", help="Path to the target project root", default=".")
    parser.add_argument("--build-graph", help="Automatically run build_graph.py after sync", action="store_true")
    
    parser.add_argument("--cursor", help="Build Cursor bridge", action="store_true")
    parser.add_argument("--windsurf", help="Build Windsurf bridge", action="store_true")
    parser.add_argument("--copilot", help="Build Copilot bridge", action="store_true")
    parser.add_argument("--all-bridges", help="Build all AI bridges", action="store_true")
    
    args = parser.parse_args()
    
    # Handle bridge selection
    selected_bridges = []
    if args.all_bridges:
        selected_bridges = ["cursor", "windsurf", "copilot"]
    else:
        if args.cursor: selected_bridges.append("cursor")
        if args.windsurf: selected_bridges.append("windsurf")
        if args.copilot: selected_bridges.append("copilot")
    
    # Interactive prompt if no bridges selected via CLI
    if not selected_bridges and not args.all_bridges:
        try:
            print("\n🌉 Optional: Build AI Bridges for specific IDEs?")
            print("  [c]ursor, [w]indsurf, [g]ithub copilot, [a]ll, [n]one (default)")
            choice = input("Selection (e.g. 'cw' for Cursor and Windsurf): ").lower()
            if 'a' in choice:
                selected_bridges = ["cursor", "windsurf", "copilot"]
            else:
                if 'c' in choice: selected_bridges.append("cursor")
                if 'w' in choice: selected_bridges.append("windsurf")
                if 'g' in choice: selected_bridges.append("copilot")
        except EOFError:
            pass

    deploy.selected_bridges = selected_bridges
    deploy.auto_build = args.build_graph
    
    # Try to auto-detect source if not provided
    source = args.source
    if not source:
        # Assume the script is in .agents/scripts/ of the foundation
        script_dir = os.path.dirname(os.path.abspath(__file__))
        source = os.path.abspath(os.path.join(script_dir, "..", ".."))

    deploy(source, args.target)