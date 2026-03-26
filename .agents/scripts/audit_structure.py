# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
import os
import re
import sys
import argparse
import json
from pathlib import Path
from typing import List, Dict, Any

# Smart Root Discovery
def discover_agents_root() -> Path:
    current_dir = Path(__file__).resolve().parent
    # If we are in .agents/scripts, the .agents root is one level up
    if current_dir.name == "scripts" and current_dir.parent.name == ".agents":
        return current_dir.parent
    
    # Otherwise check if .agents exists in cwd
    local_agents = Path(".agents")
    if local_agents.exists() and local_agents.is_dir():
        return local_agents
    
    # If we are already inside .agents (but not in scripts)
    if Path("scripts").exists() and Path("workspace_map.md").exists():
        return Path(".")
        
    return Path(".agents") # Fallback

AGENTS_ROOT = discover_agents_root()
SKILLS_DIR = AGENTS_ROOT / "skills"
WORKSPACE_MAP = AGENTS_ROOT / "workspace_map.md"
FOUNDATION_PATH_MARKER = AGENTS_ROOT / ".foundation_path"
EXCLUDE_DIRS = ['__pycache__', 'node_modules']

def get_foundation_link() -> str | None:
    if FOUNDATION_PATH_MARKER.exists():
        return FOUNDATION_PATH_MARKER.read_text(encoding='utf-8').strip()
    return None

def get_actual_skills() -> List[str]:
    if not SKILLS_DIR.exists(): return []
    return [d.name for d in SKILLS_DIR.iterdir() if d.is_dir() and d.name not in EXCLUDE_DIRS]

def get_documented_skills(file_path: Path, actual_skills: List[str]) -> List[str]:
    if not file_path.exists(): return []
    content = file_path.read_text(encoding='utf-8')
    documented = []
    for skill in actual_skills:
        if re.search(rf"[`\[]{re.escape(skill)}[`\]]", content) or \
           re.search(rf"(?:^|[|\-\n\r])\s*{re.escape(skill)}\s*(?:[|\-\n\r]|$)", content):
            documented.append(skill)
    return sorted(documented)

def audit_structure(output_json: bool = False) -> int:
    results: Dict[str, Any] = {
        "errors": [],
        "warnings": [],
        "summary": {"actual_skills": 0, "documented_skills": 0}
    }
    
    if not output_json: print("--- Starting Structural Integrity Audit ---")
    
    foundation_link = get_foundation_link()
    if foundation_link:
        if not os.path.exists(foundation_link):
            results["errors"].append({"category": "STRUCTURE", "message": f"Broken foundation link: {foundation_link}"})
    else:
            results["warnings"].append({"category": "STRUCTURE", "message": "Orphaned project: No foundation path link found."})

    actual_skills = sorted(get_actual_skills())
    documented_map = get_documented_skills(WORKSPACE_MAP, actual_skills)
    
    results["summary"]["actual_skills"] = len(actual_skills)
    results["summary"]["documented_skills"] = len(documented_map)

    missing_in_map = [s for s in actual_skills if s not in documented_map]
    for s in missing_in_map:
        results["errors"].append({"category": "DOCUMENTATION", "message": f"Skill '{s}' missing from workspace_map.md", "skill": s})

    if output_json:
        print(json.dumps(results, indent=2))
    else:
        if foundation_link: print(f"📌 Foundation Link: Verified -> {foundation_link}")
        print(f"FileSystem: {len(actual_skills)} skills detected.")
        print(f"workspace_map.md: {len(documented_map)} skills documented.")
        
        for err in results["errors"]:
            print(f"[FAIL] {err['message'] or 'Unknown Error'}")
        for wrn in results["warnings"]:
            print(f"[WARN] {wrn['message'] or 'Unknown Warning'}")
            
        if len(results["errors"]) == 0:
            print("\n[PASS] All documentation is synchronized.")
        else:
            print(f"\n[FAIL] Audit Finished. Total Errors: {len(results['errors'])}")

    return len(results["errors"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit structural integrity.")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format.")
    args = parser.parse_args()
    
    # Ensure stdout/stderr handle UTF-8 on Windows
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

    issues = audit_structure(output_json=args.json)
    sys.exit(1 if issues > 0 else 0)