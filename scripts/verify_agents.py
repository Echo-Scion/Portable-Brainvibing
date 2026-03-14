import os
import re
import sys

# Use relative paths from script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), ".agents")
WORKFLOWS_DIR = os.path.join(BASE_DIR, "workflows")
SKILLS_DIR = os.path.join(BASE_DIR, "skills")
RULES_DIR = os.path.join(BASE_DIR, "rules")

class Counter:
    def __init__(self):
        self.val: int = 0
    def inc(self):
        self.val = self.val + 1

def get_all_skills() -> set[str]:
    if not os.path.exists(SKILLS_DIR):
        print("Skills directory not found!")
        return set()
    return {d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))}

def get_all_rules() -> set[str]:
    rules = set()
    if not os.path.exists(RULES_DIR):
        return rules
    for root, dirs, files in os.walk(RULES_DIR):
        for file in files:
            if file.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, file), RULES_DIR)
                rel_path = rel_path.replace("\\", "/")
                rules.add(rel_path)
    return rules

def check_mechanical_integrity() -> int:
    err_count = Counter()
    print("--- SCANNING FOR MECHANICAL INTEGRITY ERRORS ---")
    
    # Check for concatenated headers (e.g., ## Title## Subtitle or ### Header#)
    header_bug_pat = re.compile(r'^#+ [^#\n]+#+', re.MULTILINE)
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip dot-directories and specific excluded folders
        if any(exc in root for exc in [".git", ".gemini", ".system_generated"]): continue
        
        for file in files:
            if not file.endswith(".md"): continue
            
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # 1. Check for concatenated headers (e.g., # Title## Section)
                if header_bug_pat.search(content):
                    print(f"[BUG] CONCATENATED HEADERS in {os.path.relpath(filepath, BASE_DIR)}")
                    err_count.inc()

                # 2. Check for empty shell skills
                if "\\skills\\" in root.lower() or "/skills/" in root.lower():
                    if "resources/workflow.md" in content or "go read this file" in content.lower():
                        # Check if it also has actual instructions
                        if len(content) < 800: # Heuristic for shell
                            print(f"[BUG] EMPTY SHELL SKILL in {os.path.relpath(filepath, BASE_DIR)}")
                            err_count.inc()
            except Exception as e:
                print(f"[ERROR] Could not read {file}: {e}")
                err_count.inc()
                        
    return err_count.val

def check_links() -> int:
    all_skills: set[str] = get_all_skills()
    all_rules: set[str] = get_all_rules()
    err_count = Counter()
    
    print("\n--- SCANNING FOR BROKEN LINKS ---")
    
    if not os.path.exists(WORKFLOWS_DIR):
        print("Workflows directory not found!")
        return 1

    for root, dirs, files in os.walk(WORKFLOWS_DIR):
        for file in files:
            if not file.endswith(".md"): continue
            
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find @rule links
                rule_pattern = re.compile(r'@([a-zA-Z0-9_\-\./\\]+\.md)')
                for r in rule_pattern.findall(content):
                    r_clean = r.split('`')[0].strip().replace("\\", "/")
                    if r_clean not in all_rules:
                        print(f"[LINK] BROKEN RULE in {file}: @{r_clean}")
                        err_count.inc()
                        
                # Find skill references
                skill_pattern = re.compile(r'`([a-z0-9\-]+)` skill')
                for s in skill_pattern.findall(content):
                    if s not in all_skills and s != "context-manager": # context-manager is standard
                        print(f"[LINK] BROKEN SKILL in {file}: {s}")
                        err_count.inc()
            except Exception as e:
                print(f"[ERROR] Could not read {file}: {e}")
                err_count.inc()
                    
    return err_count.val

if __name__ == "__main__":
    m_errors = check_mechanical_integrity()
    l_errors = check_links()
    
    total = m_errors + l_errors
    if total == 0:
        print("\n✅ ALL CHECKS PASSED: Workspace is mechanically sound.")
        sys.exit(0)
    else:
        print(f"\n❌ FAILED: Found {total} integrity issues. Please fix before syncing.")
        sys.exit(1)