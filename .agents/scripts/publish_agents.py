import os
import re
import shutil
import sys
from datetime import datetime
from typing import List, Set, cast, Any

# Configuration
SOURCE_BASE = r".agents"
TARGET_BASE = r"portable brainvibing\.agents"
EXPLANATION_DIR = r"portable brainvibing\.agentsexplanation"
VERSION_FILE = r"portable brainvibing\VERSION"
CHANGELOG_FILE = r"portable brainvibing\CHANGELOG.md"
SOURCE_SCRIPTS = os.path.join(SOURCE_BASE, "scripts")
TARGET_SCRIPTS = os.path.join(TARGET_BASE, "scripts")

# Replacement Dictionary
REPLACEMENTS = {
    re.escape(r"C:\Users\USER\AndroidStudioProjects\_foundation"): "<ROOT>",
    re.escape(r"C:/Users/USER/AndroidStudioProjects/_foundation"): "<ROOT>",
    re.escape(r"e:\BINTANG\Project Priority"): "<ROOT>",
    re.escape(r"e:/BINTANG/Project Priority"): "<ROOT>",
    re.escape(r"file:///e:/BINTANG/Project%20Priority"): "file:///<ROOT>",
    re.escape(r"file:///E:/BINTANG/Project%20Priority"): "file:///<ROOT>",
    re.escape(r"E:\BINTANG\Project"): "<ROOT>",
    re.escape(r"E:/BINTANG/Project"): "<ROOT>",
    re.escape(r"file:///E:/BINTANG/Project"): "file:///<ROOT>",
    re.escape(r"file:///e:/BINTANG/Project"): "file:///<ROOT>",
    r"Echosystem": "MainSystem",
    r"Starvia": "TargetApp",
    r"BINTANG": "User",
    # Specific project names leakage
    r"ethos": "project_alpha",
    r"halocast": "project_beta",
    r"khayalore": "project_gamma",
    r"hallo": "project_delta",
    r"echosystem": "mainsystem",
    # Generic path pattern for other projects
    r"\[ethos, halocast, khayalore, etc\]": "[project_a, project_b, project_c, etc]",
}

# Directories or files to exclude during sync (internal maintenance tools and personal scripts)
BLACKLIST: Set[str] = {
    # Skills (Internal/Local)
    "repo-auditor",
    "skill-system-audit",
    "skill-system-admin",
    "debt-manager",
    
    # Workflows (Internal/Local)
    "update-sync.md",
    "verify-loop.md",
    
    # Scripts
    "publish_agents.py",
    "audit_repo.py",
    "audit_structure.py",
    "SCRIPTS.md",
    
    # Folders & Personal
    "Vitals",
    "./vitals/",
    "personal/",
    "debug_scripts/",
    "archive",
    "tmp_",
    "temp_",
}

def sanitize_content(content: str, filename: str = "") -> str:
    # 1. Apply standard replacements
    content_sanitized: str = content
    for pattern, replacement in REPLACEMENTS.items():
        content_sanitized = re.sub(pattern, replacement, content_sanitized, flags=re.IGNORECASE)
    
    # 2. Prune lines containing blacklisted skills/items
    if filename != "verify_agents.py":
        lines: List[str] = content_sanitized.splitlines()
        sanitized_lines: List[Any] = [] # Use Any to bypass strict LiteralString append checks if they persist
        for line in lines:
            if any(item in line for item in BLACKLIST):
                # Special check to only prune if it's a mention in map/list, 
                # not if it's part of a different word (though repo-auditor is specific enough)
                continue
            sanitized_lines.append(line)
        
        return "\n".join(cast(List[str], sanitized_lines))
    return content_sanitized

def sync_root_files(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    src_files_rel: Set[str] = set()
    for file_obj in os.listdir(src_dir):
        file = cast(str, file_obj)
        if file in BLACKLIST:
            continue
        src_file = os.path.join(src_dir, file)
        if os.path.isfile(src_file) and file.endswith(('.md', '.json', '.yaml')):
            dest_file = os.path.join(dest_dir, file)
            src_files_rel.add(file)
            
            with open(src_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            sanitized = sanitize_content(content)
            
            already_exists = os.path.exists(dest_file)
            if already_exists:
                with open(dest_file, 'r', encoding='utf-8') as f:
                    existing_content = f.read()
                if existing_content == sanitized:
                    continue

            with open(dest_file, 'w', encoding='utf-8') as f:
                f.write(sanitized)
            print(f"{'Updated' if already_exists else 'Created'} (Root): {file}")

    if os.path.exists(dest_dir):
        for file in os.listdir(dest_dir):
            dest_file = os.path.join(dest_dir, file)
            if os.path.isfile(dest_file) and file.endswith(('.md', '.json', '.yaml')):
                if file not in src_files_rel:
                    os.remove(dest_file)
                    print(f"Retired (Deleted Root): {file}")


def sync_directory(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        print(f"Source directory {src_dir} does not exist. Skipping.")
        return

    # Track files to detect deletions
    src_files_rel: Set[str] = set()
    for root_obj, dirs_obj, files_obj in os.walk(src_dir):
        root = cast(str, root_obj)
        dirs = cast(List[str], dirs_obj)
        files = cast(List[str], files_obj)
        
        # Filter directories based on BLACKLIST in-place for os.walk
        filtered_dirs = [d for d in dirs if d not in BLACKLIST]
        dirs.clear()
        dirs.extend(filtered_dirs)
        
        rel_path = os.path.relpath(root, src_dir)
        target_path = os.path.join(dest_dir, rel_path)

        if not os.path.exists(target_path):
            os.makedirs(target_path)

        for file_obj in files:
            file = cast(str, file_obj)
            if file in BLACKLIST:
                continue
            if file.endswith(('.md', '.json', '.yaml', 'SKILL.md')):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(target_path, file)
                rel_file_path = os.path.normpath(os.path.join(rel_path, file))
                src_files_rel.add(rel_file_path)
                
                with open(src_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                sanitized = sanitize_content(content)
                
                # Only write if content changed to avoid unnecessary timestamp updates
                already_exists = os.path.exists(dest_file)
                if already_exists:
                    with open(dest_file, 'r', encoding='utf-8') as f:
                        existing_content = f.read()
                    if existing_content == sanitized:
                        continue

                with open(dest_file, 'w', encoding='utf-8') as f:
                    f.write(sanitized)
                print(f"{'Updated' if already_exists else 'Created'}: {rel_file_path}")

    # Mirroring: Remove files in destination that no longer exist in source
    if os.path.exists(dest_dir):
        for root_obj, _, files_obj in os.walk(dest_dir):
            root = cast(str, root_obj)
            files = cast(List[str], files_obj)
            for file_obj in files:
                file = cast(str, file_obj)
                if file.endswith(('.md', '.json', '.yaml', 'SKILL.md')):
                    dest_file = os.path.join(root, file)
                    rel_file_path = os.path.normpath(os.path.relpath(dest_file, dest_dir))
                    
                    if rel_file_path not in src_files_rel:
                        os.remove(dest_file)
                        print(f"Retired (Deleted): {rel_file_path}")
        
        # Cleanup empty directories
        for root, dirs, files in os.walk(dest_dir, topdown=False):
            if root == dest_dir: continue # Don't delete the base sync directory
            if not os.listdir(root):
                os.rmdir(root)
                print(f"Cleaned up empty directory: {os.path.relpath(root, dest_dir)}")

def sync_scripts():
    if not os.path.exists(SOURCE_SCRIPTS):
        return
    if not os.path.exists(TARGET_SCRIPTS):
        os.makedirs(TARGET_SCRIPTS)
    
    # We specifically want foundational scripts for the portable distribution. 
    # Personal or one-off maintenance scripts are EXCLUDED.
    scripts_to_sync = ["verify_agents.py"]
    
    for script_obj in scripts_to_sync:
        script = cast(str, script_obj)
        src = os.path.join(SOURCE_SCRIPTS, script)
        dest = os.path.join(TARGET_SCRIPTS, script)
        
        if os.path.exists(src):
            with open(src, 'r', encoding='utf-8') as f:
                content = f.read()
            
            sanitized = sanitize_content(content, script)
            
            # For verify_agents.py, we need to make sure BASE_DIR matches the portable relative structure
            if script == "verify_agents.py":
                sanitized = sanitized.replace('BASE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), ".agents")', 'BASE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), ".agents")') # Already correct relative to root/scripts/
            
            # Check if exists and same
            if os.path.exists(dest):
                with open(dest, 'r', encoding='utf-8') as f:
                    if f.read() == sanitized:
                        continue
            
            with open(dest, 'w', encoding='utf-8') as f:
                f.write(sanitized)
            print(f"Synced script: {script}")

def sanitize_explanations():
    if not os.path.exists(EXPLANATION_DIR):
        return
    
    for file in os.listdir(EXPLANATION_DIR):
        if file.endswith(".md"):
            file_path = os.path.join(EXPLANATION_DIR, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            sanitized = sanitize_content(content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(sanitized)
            print(f"Sanitized explanation: {file}")

def update_version(inc_type="patch"):
    if not os.path.exists(VERSION_FILE):
        initial_version = "1.0.0"
        with open(VERSION_FILE, 'w', encoding='utf-8') as f:
            f.write(initial_version)
        return initial_version

    with open(VERSION_FILE, 'r', encoding='utf-8') as f:
        version = f.read().strip()
    
    if inc_type == "none":
        return version

    parts = [int(p) for p in version.split('.')]
    if len(parts) == 3:
        if inc_type == "major":
            parts[0] += 1
            parts[1] = 0
            parts[2] = 0
        elif inc_type == "minor":
            parts[1] += 1
            parts[2] = 0
        elif inc_type == "patch":
            parts[2] += 1
        # If inc_type is something else (like None or unknown), we just return current
        else:
            return version
            
        new_version = '.'.join(map(str, parts))
        with open(VERSION_FILE, 'w', encoding='utf-8') as f:
            f.write(new_version)
        
        # Update README version marker
        if os.path.exists(r"portable brainvibing\README.md"):
            with open(r"portable brainvibing\README.md", 'r', encoding='utf-8') as f:
                readme_content = f.read()
            # Match ## 🏷️ Version\n1.0.0 ... and replace the version part only
            # Using a more robust match that doesn't eat trailing text
            new_readme = re.sub(r"(## 🏷️ Version\s*\n)(\d+\.\d+\.\d+)", rf"\g<1>{new_version}", readme_content)
            with open(r"portable brainvibing\README.md", 'w', encoding='utf-8') as f:
                f.write(new_readme)

        return new_version
    return version

def update_changelog(version, message, append_to_file=True):
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    header_marker = "adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)."
    
    if os.path.exists(CHANGELOG_FILE):
        with open(CHANGELOG_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = f"# Changelog\n\nAll notable changes to this project will be documented in this file.\nThe format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),\nand this project {header_marker}\n"

    if append_to_file:
        if not message.strip().startswith("###"):
            formatted_message = f"### Changed\n- {message}\n"
        else:
            formatted_message = message.strip() + "\n"
            
        log_entry = f"\n## [{version}] - {date_str}\n{formatted_message}"
        
        if header_marker in content:
            new_changelog_content = content.replace(header_marker, header_marker + "\n" + log_entry, 1)
        elif "# Changelog" in content:
            new_changelog_content = content.replace("# Changelog", "# Changelog\n" + log_entry, 1)
        else:
            new_changelog_content = "# Changelog\n" + log_entry + "\n" + content

        with open(CHANGELOG_FILE, 'w', encoding='utf-8') as f:
            f.write(new_changelog_content)
    else:
        new_changelog_content = content

    # Extraction of versions from CHANGELOG (Limit to 5 recent MAJOR/MINOR updates for docs)
    all_versions: List[Any] = re.findall(r"(## \[\d+\.\d+\.\d+\].*?)(?=\n## \[|\Z)", new_changelog_content, re.DOTALL)
    
    recent_changes_list: List[str] = []
    for version_text_obj in all_versions:
        version_text_str = cast(str, version_text_obj)
        # Check if version is Major or Minor (e.g. [1.2.0] or [2.0.0], not [1.2.3])
        if re.search(r"## \[\d+\.\d+\.0\]", version_text_str):
            recent_changes_list.append(version_text_str.replace("## [", "### [") + "\n")
    
    # Keep only the top 5 most recent major/minor updates (Manual for Pyre2)
    final_changes: List[str] = []
    for change in recent_changes_list:
        if len(final_changes) >= 5: break
        final_changes.append(change)
        
    recent_changes_content: str = "".join(final_changes).strip()
    
    # If no major/minor found in recent history, show a placeholder or the very latest even if patch
    if not recent_changes_content and all_versions:
        latest_version_text: str = cast(str, all_versions[0])
        recent_changes_content = latest_version_text.replace("## [", "### [").strip() + "\n*(Full history in CHANGELOG.md)*"

    # Targets for update: README.md and AGENTS.md
    update_targets = [
        r"portable brainvibing\README.md",
        r"portable brainvibing\AGENTS.md"
    ]

    for target_path in update_targets:
        if os.path.exists(target_path):
            with open(target_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Robust marker detection (supports with/without emoji, case-insensitive)
            marker_pattern = r"## (?:🔄 )?Recent Changes"
            # Pattern: Matches and captures the header and replaces everything up to the next separator/header
            # Separators: "---" OR "## " OR end of file
            changelog_section_pattern = rf"({marker_pattern}\s*\n)(.*?)(?=\n---|\n## |\Z)"
            
            if re.search(marker_pattern, content, flags=re.IGNORECASE):
                # Replace existing section content
                new_content = re.sub(changelog_section_pattern, rf"## 🔄 Recent Changes\n\n{recent_changes_content}\n", content, flags=re.DOTALL | re.IGNORECASE)
            else:
                # If section doesn't exist, append it at the end
                new_content = content + f"\n\n## 🔄 Recent Changes\n\n{recent_changes_content}\n"
            
            # Additional cleanup: Ensure only ONE "Recent Changes" section exists
            sections = re.split(marker_pattern, new_content, flags=re.IGNORECASE)
            if len(sections) > 2:
                # Reconstruct without slice to satisfy type checker (e.g. Pyre2)
                rest = "".join(sections[i] for i in range(2, len(sections)))
                new_content = sections[0] + f"## 🔄 Recent Changes\n\n{recent_changes_content}\n" + rest
            
            # Always sanitize the entire content of the target file
            new_content = sanitize_content(new_content)
            
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected changes and sanitized: {os.path.basename(target_path)}")

def detect_increment_type():
    """
    Detects the required increment type based on changes:
    - Minor: If a new Skill folder, Workflow file, or Rule file is added.
    - Patch: If existing files were modified or files were deleted.
    - None: If no changes were detected.
    """
    has_mods = False
    
    # 1. Check Root Files (in .agents root)
    src_root_files = [f for f in os.listdir(SOURCE_BASE) if os.path.isfile(os.path.join(SOURCE_BASE, f)) and f.endswith(('.md', '.json', '.yaml'))]
    dest_root_files = [f for f in os.listdir(TARGET_BASE) if os.path.isfile(os.path.join(TARGET_BASE, f)) and f.endswith(('.md', '.json', '.yaml'))] if os.path.exists(TARGET_BASE) else []
    
    # New root files -> Patch (since they are usually metadata/configs)
    if set(src_root_files) != set(dest_root_files):
        has_mods = True

    for file in src_root_files:
        src_f = os.path.join(SOURCE_BASE, file)
        dest_f = os.path.join(TARGET_BASE, file)
        if os.path.exists(dest_f):
            with open(src_f, 'r', encoding='utf-8') as f:
                src_c = f.read()
            with open(dest_f, 'r', encoding='utf-8') as f:
                dest_c = f.read()
            if sanitize_content(src_c) != dest_c:
                has_mods = True

    # 2. Check Subdirectories (skills, workflows, rules, templates, canons)
    for folder in ["skills", "workflows", "rules", "templates", "canons"]:
        src_path = os.path.join(SOURCE_BASE, folder)
        dest_path = os.path.join(TARGET_BASE, folder)
        
        if not os.path.exists(src_path):
            continue
            
        # Check for new items (Minor)
        src_items = {i for i in os.listdir(src_path) if i != ".gitkeep" and i not in BLACKLIST}
        dest_items = {i for i in os.listdir(dest_path) if i != ".gitkeep"} if os.path.exists(dest_path) else set()
        
        new_items = src_items - dest_items
        if new_items:
            # ONLY new skill folders (directories) trigger MINOR
            if folder == "skills":
                for item in new_items:
                    if os.path.isdir(os.path.join(src_path, item)):
                        return "minor"
            
            # New individual files in workflows, rules, etc. are now treated as PATCH
            has_mods = True

        # Check for modifications (Patch) or deletions
        if src_items != dest_items:
            has_mods = True

        for root, _, files in os.walk(src_path):
            for file in files:
                if file == ".gitkeep": continue
                if file.endswith(('.md', '.json', '.yaml', 'SKILL.md')):
                    src_file = os.path.join(root, file)
                    rel = os.path.relpath(src_file, src_path)
                    dest_file = os.path.join(dest_path, rel)
                    
                    if not os.path.exists(dest_file):
                        has_mods = True # New file deep in the tree
                        continue
                    
                    try:
                        with open(src_file, 'r', encoding='utf-8') as f:
                            src_c = f.read()
                        with open(dest_file, 'r', encoding='utf-8') as f:
                            dest_c = f.read()
                        
                        if sanitize_content(src_c) != dest_c:
                            has_mods = True
                    except Exception:
                        has_mods = True
                        
    return "patch" if has_mods else None

def main():
    # Usage: python publish_agents.py "Message" [patch|minor|major|auto]
    message = sys.argv[1].replace('\\n', '\n') if len(sys.argv) > 1 else "Automated agent synchronization and sanitization."
    requested_inc = sys.argv[2].lower() if len(sys.argv) > 2 else "auto"

    print(f"Detecting changes...")
    detected_inc = detect_increment_type()
    
    if requested_inc == "auto":
        inc_type = detected_inc
    else:
        inc_type = requested_inc

    if inc_type is None:
        print("No changes detected. Skipping synchronization.")
        return

    print(f"Starting synchronization (Version bump: {inc_type})")
    print(f"Message: {message}")
    
    # Sync root files (depth 0)
    sync_root_files(SOURCE_BASE, TARGET_BASE)
    
    for folder in ["skills", "workflows", "rules", "templates", "canons"]:
        src = os.path.join(SOURCE_BASE, folder)
        dest = os.path.join(TARGET_BASE, folder)
        sync_directory(src, dest)
    
    sync_scripts()
    sanitize_explanations()
    
    new_ver = update_version(inc_type)
    update_changelog(new_ver, message, append_to_file=(inc_type != "none"))
    
    print(f"\nDone! Updated to version {new_ver}")

if __name__ == "__main__":
    main()
