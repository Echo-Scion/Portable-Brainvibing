import os
import re
import sys
from pathlib import Path

# Configuration - Relative to project root
AGENTS_ROOT = Path(".agents")
SKILLS_DIR = AGENTS_ROOT / "skills"
WORKSPACE_MAP = AGENTS_ROOT / "workspace_map.md"
FOUNDATION_PATH_MARKER = AGENTS_ROOT / ".foundation_path"
# Made this relative for universal use - looking at the file in the .agents folder
AGENTS_MD = AGENTS_ROOT / "AGENTS.md" 

def get_foundation_link():
    """Reads the foundation path if it exists."""
    if FOUNDATION_PATH_MARKER.exists():
        return FOUNDATION_PATH_MARKER.read_text(encoding='utf-8').strip()
    return None

def get_actual_skills():
    """Returns a list of names for directories within .agents/skills/."""
    if not SKILLS_DIR.exists():
        return []
    return [d.name for d in SKILLS_DIR.iterdir() if d.is_dir() and d.name not in EXCLUDE_DIRS]

def get_documented_skills(file_path, actual_skills):
    """Checks which of the actual skills are explicitly mentioned in the markdown file."""
    if not file_path.exists():
        return []
    
    content = file_path.read_text(encoding='utf-8')
    documented = []
    for skill in actual_skills:
        if re.search(rf"[`\[]{re.escape(skill)}[`\]]", content) or \
           re.search(rf"(?:^|[|\-\n\r])\s*{re.escape(skill)}\s*(?:[|\-\n\r]|$)", content):
            documented.append(skill)
    
    return sorted(documented)

def audit_structure():
    print("--- Starting Structural Integrity Audit ---")
    
    # 1. Foundation Link Audit
    foundation_link = get_foundation_link()
    if foundation_link:
        print(f"📌 Foundation Link: Verified -> {foundation_link}")
        if not os.path.exists(foundation_link):
            print(f"[ERROR] FOUNDATION PATH IS BROKEN: {foundation_link}")
            return 1
    else:
        # Check if we are in the foundation itself
            print("🏠 Root Foundation detected. Skipping link check.")
        else:
            print("[WARNING] ORPHANED PROJECT: No .foundation_path marker found.")

    actual_skills = sorted(get_actual_skills())
    documented_map = get_documented_skills(WORKSPACE_MAP, actual_skills)
    
    print(f"FileSystem: {len(actual_skills)} skills detected.")
    print(f"workspace_map.md: {len(documented_map)} skills documented.")
    
    issues = 0
    
    # Check Workspace Map (Primary requirement)
    missing_in_map = [s for s in actual_skills if s not in documented_map]
    if missing_in_map:
        print(f"\n[MAP MISSING] Documentation required in workspace_map.md for:")
        for s in missing_in_map: print(f"  - {s}")
        issues += len(missing_in_map)

    print(f"\n--- Audit Finished. Total Structural Discrepancies: {issues} ---")
    return issues

if __name__ == "__main__":
    issues = audit_structure()
    if issues > 0:
        print("\n[FAIL] Documentation is out of sync with filesystem!")
        sys.exit(1)
    else:
        print("\n[PASS] All documentation is synchronized.")
        sys.exit(0)