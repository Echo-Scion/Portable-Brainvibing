import os
import re
import sys

# Use relative paths from script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
WORKFLOWS_DIR = os.path.join(BASE_DIR, "workflows")
SKILLS_DIR = os.path.join(BASE_DIR, "skills")
RULES_DIR = os.path.join(BASE_DIR, "rules")
CANONS_DIR = os.path.join(BASE_DIR, "canons")

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
    if os.path.exists(RULES_DIR):
        for root, dirs, files in os.walk(RULES_DIR):
            for file in files:
                if file.endswith(".md"):
                    rules.add(file)
                    
    if os.path.exists(CANONS_DIR):
        for root, dirs, files in os.walk(CANONS_DIR):
            for file in files:
                if file.endswith(".md"):
                    rules.add(file)
    return rules

def check_mechanical_integrity() -> int:
    err_count = Counter()
    print("--- SCANNING FOR MECHANICAL INTEGRITY ERRORS ---")
    
    # Check for concatenated headers (e.g., ## Title## Subtitle or ### Header#)
    header_bug_pat = re.compile(r'^#+ [^#\n]+#+', re.MULTILINE)
    # Check for double headers (e.g., ## ## Title)
    double_header_pat = re.compile(r'^#+ #+ ', re.MULTILINE)
    
    # Check for absolute paths (e.g., C:\Users\... or /home/user/...)
    # This is a bit sensitive, so we'll look for common patterns in scripts
    abs_path_pat = re.compile(r'[a-zA-Z]:\\[Uu]sers\\[a-zA-Z0-9_\-\.]+')
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip dot-directories and specific excluded folders
        if any(exc in root for exc in [".git", ".gemini", ".system_generated"]): continue
        
        for file in files:
            if not (file.endswith(".md") or file.endswith(".py")): continue
            
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # 1. Check for concatenated headers (e.g., # Title## Section)
                if file.endswith(".md") and header_bug_pat.search(content):
                    print(f"[BUG] CONCATENATED HEADERS in {os.path.relpath(filepath, BASE_DIR)}")
                    err_count.inc()

                # 2. Check for double headers (e.g., ## ## Title)
                if file.endswith(".md") and double_header_pat.search(content):
                    print(f"[BUG] DOUBLE HEADERS (## ##) in {os.path.relpath(filepath, BASE_DIR)}")
                    err_count.inc()

                # 3. Check for absolute paths in scripts
                if file.endswith(".py") and abs_path_pat.search(content):
                    # Exception for verify_agents.py itself and local-only scripts
                    if file not in ["verify_agents.py", "publish_agents.py", "audit_repo.py"]:
                        print(f"[BUG] ABSOLUTE PATH in {os.path.relpath(filepath, BASE_DIR)}")
                        err_count.inc()

                # 4. Check for empty shell skills
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
    
    # Common rule and canon directories to ignore in skill check
    RULE_DIRS = {"common", "flutter", "web", "canons", "auth", "notifications", "ui-patterns"}
    
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
                
                # 1. Find @rule links (e.g., @common/security.md)
                rule_pattern = re.compile(r'@([a-zA-Z0-9_\-\./\\]+\.md)')
                for r in rule_pattern.findall(content):
                    r_clean = r.split('`')[0].strip().replace("\\", "/")
                    if r_clean not in all_rules:
                        print(f"[LINK] BROKEN RULE in {file}: @{r_clean}")
                        err_count.inc()
                        
                # 2. Find skill references in backticks (e.g., `skill-name` skill)
                skill_backtick_pattern = re.compile(r'`([a-z0-9\-]+)` skill')
                for s in skill_backtick_pattern.findall(content):
                    if s not in all_skills and s != "context-manager": # context-manager is standard
                        print(f"[LINK] BROKEN SKILL (backtick) in {file}: {s}")
                        err_count.inc()

                # 3. Find skill mentions starting with @ (e.g., @skill-name or @skills/skill-name)
                # Allow underscores but ensure we skip rule links which end with .md
                skill_mention_pattern = re.compile(r'@(?:skills/)?([a-zA-Z0-9\-_]+(?:\.md)?)')
                for s in skill_mention_pattern.findall(content):
                    # Filter out non-skill mentions
                    if s.endswith(".md") or s in ["param", "return", "type", "description"]:
                        continue
                    
                    # Filter out rule directories
                    if s in RULE_DIRS:
                        continue
                    
                    # Ignore specific example/placeholder skills
                    if s in ["idea-planner", "freezed", "riverpod"]:
                        continue
                    
                    if s not in all_skills:
                        print(f"[LINK] BROKEN SKILL (@mention) in {file}: @{s}")
                        err_count.inc()

            except Exception as e:
                print(f"[ERROR] Could not read {file}: {e}")
                err_count.inc()
                    
    return err_count.val

def check_protocol_compliance() -> int:
    err_count = Counter()
    print("\n--- SCANNING FOR PROTOCOL COMPLIANCE ERRORS ---")
    
    # 1. Vibecode Limits & Logic Density
    # We check source files in the root project (outside .agents)
    # Since this script runs in .agents/scripts, we go up two levels to find the project root
    PROJECT_ROOT = os.path.dirname(BASE_DIR)
    
    source_exts = {".dart", ".ts", ".js", ".py", ".go", ".rs", ".kt", ".swift"}
    exclude_dirs = {".git", ".gemini", ".system_generated", "node_modules", "build", "dist", ".agents", "referensiagents"}

    for root, dirs, files in os.walk(PROJECT_ROOT):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if not any(file.endswith(ext) for ext in source_exts): continue
            
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                line_count = len(lines)
                rel_path = os.path.relpath(filepath, PROJECT_ROOT)
                
                # Critical Blocker (> 800 lines)
                if line_count > 800:
                    print(f"[BLOCKER] VIBECODE CRITICAL: {rel_path} has {line_count} lines (Max 800).")
                    err_count.inc()
                # Soft Cap (> 500 lines)
                elif line_count > 500:
                    print(f"[WARNING] VIBECODE SOFT CAP: {rel_path} has {line_count} lines (Recommended 500).")
                    # We don't increment err_count for warnings yet, but we could
                
                # Logic Density Heuristic (Complexity check)
                # Count keywords that imply high density: async, await, stream, provider, bloc, state, switch, case
                density_keywords = {"async", "await", "stream", "provider", "bloc", "state", "switch", "case", "useEffect", "useMemo"}
                content = "".join(lines)
                density_count = sum(1 for word in density_keywords if word in content)
                
                if density_count > 15 and line_count > 300:
                    print(f"[WARNING] LOGIC DENSITY CAP: {rel_path} is complex ({density_count} keywords) and > 300 lines.")
                    
            except Exception as e:
                print(f"[ERROR] Could not analyze {file}: {e}")

    # 2. Skill Tier Metadata
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
                        print(f"[COMPLIANCE] MISSING Recommended_Tier in {skill_name}/SKILL.md")
                        err_count.inc()
                    elif not any(tier in content for tier in ["Budget", "Standard", "Premium"]):
                        print(f"[COMPLIANCE] INVALID Recommended_Tier in {skill_name}/SKILL.md (Must be Budget/Standard/Premium)")
                        err_count.inc()
                        
                except Exception as e:
                    print(f"[ERROR] Could not read {skill_md}: {e}")
                    err_count.inc()

    # 3. Rules Metadata
    if os.path.exists(RULES_DIR):
        for root, _, files in os.walk(RULES_DIR):
            for file in files:
                if not file.endswith(".md"): continue
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Basic YAML header check
                    if "description:" not in content or "activation:" not in content.lower() and "trigger:" not in content.lower():
                        print(f"[COMPLIANCE] INCOMPLETE YAML HEADER in {os.path.relpath(filepath, RULES_DIR)}")
                        err_count.inc()
                        
                except Exception as e:
                    print(f"[ERROR] Could not read {file}: {e}")
                    err_count.inc()

    return err_count.val

if __name__ == "__main__":
    m_errors = check_mechanical_integrity()
    l_errors = check_links()
    p_errors = check_protocol_compliance()
    
    total = m_errors + l_errors + p_errors
    if total == 0:
        print("\n✅ ALL CHECKS PASSED: Workspace is mechanically sound and protocol compliant.")
        sys.exit(0)
    else:
        print(f"\n❌ FAILED: Found {total} integrity/compliance issues. Please fix before syncing.")
        sys.exit(1)
