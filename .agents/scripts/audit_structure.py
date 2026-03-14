import os
import re
import sys
from pathlib import Path

# Configuration
AGENTS_ROOT = Path(".agents")
SKILLS_DIR = AGENTS_ROOT / "skills"
WORKSPACE_MAP = AGENTS_ROOT / "workspace_map.md"
PORTABLE_AGENTS_MD = Path("portable brainvibing/AGENTS.md")
EXCLUDE_DIRS = {"archive"}

def get_actual_skills():
    """Returns a list of names for directories within .agents/skills/."""
    if not SKILLS_DIR.exists():
        return []
    # ONLY COUNT DIRECTORIES AS SKILLS, EXCLUDE INTERNAL SYSTEM DIRS
    return [d.name for d in SKILLS_DIR.iterdir() if d.is_dir() and d.name not in EXCLUDE_DIRS]

def get_documented_skills(file_path, actual_skills):
    """Checks which of the actual skills are explicitly mentioned in the markdown file."""
    if not file_path.exists():
        print(f"[WARNING] Documentation file not found: {file_path}")
        return []
    
    content = file_path.read_text(encoding='utf-8')
    documented = []
    for skill in actual_skills:
        # Match as a link [skill-name] or code `skill-name` or standalone in table | skill-name |
        if re.search(rf"[`\[]{re.escape(skill)}[`\]]", content) or \
           re.search(rf"(?:^|[|\-\n\r])\s*{re.escape(skill)}\s*(?:[|\-\n\r]|$)", content):
            documented.append(skill)
    
    return sorted(documented)

def audit_structure():
    print("--- Starting Structural Integrity Audit ---")
    actual_skills = sorted(get_actual_skills())
    documented_map = get_documented_skills(WORKSPACE_MAP, actual_skills)
    documented_agents_md = get_documented_skills(PORTABLE_AGENTS_MD, actual_skills)
    
    print(f"FileSystem: {len(actual_skills)} skills detected.")
    print(f"workspace_map.md: {len(documented_map)} skills documented.")
    print(f"AGENTS.md: {len(documented_agents_md)} skills documented.")
    
    issues = 0
    
    # Check Workspace Map
    # We only care if the ACTUAL skills are documented.
    missing_in_map = [s for s in actual_skills if s not in documented_map]
    if missing_in_map:
        print(f"\n[MAP MISSING] Documentation required in workspace_map.md for:")
        for s in missing_in_map: print(f"  - {s}")
        issues += len(missing_in_map)

    # Check AGENTS.md
    missing_in_agents = [s for s in actual_skills if s not in documented_agents_md]
    if missing_in_agents:
        print(f"\n[AGENTS MISSING] Documentation required in AGENTS.md for:")
        for s in missing_in_agents: print(f"  - {s}")
        issues += len(missing_in_agents)

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
