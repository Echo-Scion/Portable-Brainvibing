# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
import os
import re
from typing import Set, Dict, Any, List
import sys
import argparse
import json
from typing import List, Dict, Any, Optional

# Smart Root Discovery
def discover_roots():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # If we are in .agents/scripts, the .agents root is one level up
    if os.path.basename(current_dir) == "scripts" and os.path.basename(os.path.dirname(current_dir)) == ".agents":
        base_dir = os.path.dirname(current_dir)
    else:
        # Check if .agents exists in current dir
        if os.path.exists(".agents"):
            base_dir = os.path.abspath(".agents")
        else:
            base_dir = os.getcwd()
    return base_dir

BASE_DIR = discover_roots()
WORKFLOWS_DIR = os.path.join(BASE_DIR, "workflows")
SKILLS_DIR = os.path.join(BASE_DIR, "skills")
RULES_DIR = os.path.join(BASE_DIR, "rules")
CANONS_DIR = os.path.join(BASE_DIR, "canons")
FOUNDATION_PATH_MARKER = os.path.join(BASE_DIR, ".foundation_path")

class AuditResult:
    def __init__(self):
        self.errors: List[Dict[str, Optional[str]]] = []
        self.warnings: List[Dict[str, Optional[str]]] = []
        self.stats: Dict[str, int] = {"skills": 0, "rules": 0, "canons": 0}

    def add_error(self, category: str, message: str, file: Optional[str] = None):
        self.errors.append({"category": category, "message": message, "file": file})

    def add_warning(self, category: str, message: str, file: Optional[str] = None):
        self.warnings.append({"category": category, "message": message, "file": file})

def check_foundation_sync(res: AuditResult, verbose: bool = True):
    if not os.path.exists(FOUNDATION_PATH_MARKER):
        if verbose: print("[NOTE] No .foundation_path marker found. Skipping sync check.")
        return
    
    if verbose: print("\n--- FOUNDATION SYNC CHECK ---")
    
    try:
        with open(FOUNDATION_PATH_MARKER, "r", encoding="utf-8") as f:
            foundation_root = f.read().strip()
        foundation_agents = os.path.join(foundation_root, ".agents") if not (foundation_root.endswith(".agents") or os.path.basename(foundation_root) == ".agents") else foundation_root
        
        if not os.path.exists(foundation_agents):
            res.add_error("SYNC", f"Broken foundation link: {foundation_agents}")
            return
            
        if verbose: print(f"📌 Linked to Foundation: {foundation_root}")
        
        sync_folders = ["skills", "rules", "workflows", "canons"]
        for folder in sync_folders:
            local_folder = os.path.join(BASE_DIR, folder)
            found_folder = os.path.join(foundation_agents, folder)
            if not os.path.exists(found_folder): continue
            
            local_files = {f for r, d, files in os.walk(local_folder) for f in files if f.endswith(('.md', '.json', 'SKILL.md'))}
            found_files = {f for r, d, files in os.walk(found_folder) for f in files if f.endswith(('.md', '.json', 'SKILL.md'))}
            
            if local_files != found_files:
                diff_count = len(found_files - local_files)
                if diff_count > 0:
                    res.add_warning("SYNC", f"Folder {folder} is out of sync with foundation. Foundation has {diff_count} new/different items.")
                    if verbose: print(f"[SYNC] OUT-OF-SYNC ({folder}): Foundation has {diff_count} new/different items.")
                
        if verbose and len(res.warnings) > 0:
            print("👉 Run 'python .agents/scripts/deploy_foundation.py' to update your local agents.")
            
    except Exception as e:
        res.add_error("SYNC", f"Sync Check failed: {str(e)}")
        if verbose: print(f"[ERROR] Sync Check failed: {e}")

def check_mechanical_integrity(res: AuditResult, verbose: bool = True):
    if verbose: print("--- SCANNING FOR MECHANICAL INTEGRITY ERRORS ---")
    
    header_bug_pat = re.compile(r'^#+ [^#\n]+#+', re.MULTILINE)
    double_header_pat = re.compile(r'^#+ #+ ', re.MULTILINE)
    abs_path_pat = re.compile(r'[a-zA-Z]:\\[Uu]sers\\[a-zA-Z0-9_\-\.]+')
    
    for root, dirs, files in os.walk(BASE_DIR):
        if any(exc in root for exc in [".git", ".gemini", ".system_generated", "node_modules"]): continue
        for file in files:
            if not (file.endswith(".md") or file.endswith(".py")): continue
            
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, BASE_DIR)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                if file.endswith(".md"):
                    if header_bug_pat.search(content):
                        res.add_error("MECHANICAL", "Concatenated headers detected", rel_path)
                    if double_header_pat.search(content):
                        res.add_error("MECHANICAL", "Double headers (## ##) detected", rel_path)
                if file.endswith(".py") and abs_path_pat.search(content):
                    if file not in ["verify_agents.py", "publish_agents.py", "audit_repo.py"]:
                        res.add_error("MECHANICAL", "Absolute path detected in Python file", rel_path)
            except Exception as e:
                res.add_error("IO", f"Could not read file: {str(e)}", rel_path)

def check_links(res: AuditResult, verbose: bool = True):
    all_skills: Set[str] = set([str(d) for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))]) if os.path.exists(SKILLS_DIR) else set([])
    all_rules: Set[str] = set([])
    for d in [RULES_DIR, CANONS_DIR]:
        if os.path.exists(d):
            for r, dirs, files in os.walk(d):
                for f in files:
                    if f.endswith(".md"):
                        all_rules.add(f)
                        all_rules.add(os.path.relpath(os.path.join(r, f), d).replace("\\", "/"))
    
    if verbose: print("\n--- SCANNING FOR BROKEN LINKS ---")
    
    if not os.path.exists(WORKFLOWS_DIR):
        res.add_warning("LINK", "Workflows directory not found!")
        return

    rule_pattern = re.compile(r'@([a-zA-Z0-9_\-\./\\]+\.md)')
    skill_backtick_pattern = re.compile(r'`([a-z0-9\-]+)` skill')
    skill_mention_pattern = re.compile(r'@(?:skills/)?([a-zA-Z0-9\-_]+(?:\.md)?)')
    RULE_DIRS = {"rules", "common", "flutter", "web", "canons", "auth", "notifications", "ui-patterns"}

    for root, dirs, files in os.walk(WORKFLOWS_DIR):
        for file in files:
            if not file.endswith(".md"): continue
            
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, BASE_DIR)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                for r in rule_pattern.findall(content):
                    r_clean = r.split('`')[0].strip().replace("\\", "/")
                    if r_clean not in all_rules:
                        res.add_error("LINK", f"Broken rule reference: @{r_clean}", rel_path)
                        
                for s in skill_backtick_pattern.findall(content):
                    s_str = str(s)
                    if s_str not in all_skills and s_str != "context-manager":
                        res.add_error("LINK", f"Broken skill reference (backtick): `{s_str}`", rel_path)

                for s in skill_mention_pattern.findall(content):
                    s_str = str(s)
                    if s_str.endswith(".md") or s_str in ["param", "return", "type", "description"] or s_str in RULE_DIRS:
                        continue
                    if s_str not in all_skills:
                        res.add_error("LINK", f"Broken skill reference (@mention): @{s_str}", rel_path)

            except Exception as e:
                res.add_error("IO", f"Could not read file: {str(e)}", rel_path)
                    
def check_protocol_compliance(res: AuditResult, verbose: bool = True):
    if verbose: print("\n--- SCANNING FOR PROTOCOL COMPLIANCE ERRORS ---")
    
    # 1. Skill Tier Metadata
    if os.path.exists(SKILLS_DIR):
        for skill_name in os.listdir(SKILLS_DIR):
            skill_path = os.path.join(SKILLS_DIR, skill_name)
            if not os.path.isdir(skill_path): continue
            skill_md = os.path.join(skill_path, "SKILL.md")
            if os.path.exists(skill_md):
                try:
                    with open(skill_md, 'r', encoding='utf-8') as f:
                        content = f.read()
                    if "Recommended_Tier:" not in content:
                        res.add_error("PROTOCOL", "Missing Recommended_Tier", f"skills/{skill_name}/SKILL.md")
                    elif not any(tier in content for tier in ["Budget", "Standard", "Premium"]):
                        res.add_error("PROTOCOL", "Invalid Recommended_Tier (Must be Budget/Standard/Premium)", f"skills/{skill_name}/SKILL.md")
                except Exception as e:
                    res.add_error("IO", f"Could not read {skill_md}: {str(e)}")

    # 2. Rules Metadata
    if os.path.exists(RULES_DIR):
        for root, _, files in os.walk(RULES_DIR):
            for file in files:
                if not file.endswith(".md"): continue
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, RULES_DIR)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    if "description:" not in content or ("activation:" not in content.lower() and "trigger:" not in content.lower()):
                        res.add_error("PROTOCOL", "Incomplete YAML header", rel_path)
                except Exception as e:
                    res.add_error("IO", f"Could not read {file}: {str(e)}")

def run_audit(output_json: bool = False):
    res = AuditResult()
    verbose = not output_json
    
    if verbose: print("--- STARTING AUDIT ---")
    
    check_foundation_sync(res, verbose=verbose)
    check_mechanical_integrity(res, verbose=verbose)
    check_links(res, verbose=verbose)
    check_protocol_compliance(res, verbose=verbose)
    
    if output_json:
        print(json.dumps({
            "errors": res.errors,
            "warnings": res.warnings,
            "summary": {
                "total_errors": len(res.errors),
                "total_warnings": len(res.warnings)
            }
        }, indent=2))
    else:
        for err in res.errors:
            print(f"[ERROR] [{err['category']}] {err['message']} ({err['file'] or 'N/A'})")
        for wrn in res.warnings:
            print(f"[WARNING] [{wrn['category']}] {wrn['message']} ({wrn['file'] or 'N/A'})")
        
        total_errors = len(res.errors)
        if total_errors == 0:
            print("\n[PASS] ALL CHECKS PASSED: Workspace is mechanically sound and protocol compliant.")
        else:
            print(f"\n[FAIL] FAILED: Found {total_errors} integrity/compliance issues.")
    
    sys.exit(1 if len(res.errors) > 0 else 0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify workspace integrity and protocol compliance.")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format.")
    args = parser.parse_args()
    
    # Ensure stdout/stderr handle UTF-8 or at least escape properly
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

    run_audit(output_json=args.json)
