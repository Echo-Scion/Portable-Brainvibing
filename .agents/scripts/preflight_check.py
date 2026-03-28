import os
import json
import re
import sys

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
CATALOG_FILE = os.path.join(BASE_DIR, 'catalog.json')

def load_valid_skills():
    if not os.path.exists(CATALOG_FILE):
        return set()
    with open(CATALOG_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return {skill['id'] for skill in data.get('skills', [])}

def get_all_valid_files():
    valid_files = set()
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            valid_files.add(file)
            # Add relative paths as well
            rel_path = os.path.relpath(os.path.join(root, file), BASE_DIR).replace('\\', '/')
            valid_files.add(rel_path)
    return valid_files

def run_preflight():
    print("🚀 Initiating Pre-Flight Diagnostic (Self-Healing Routing)...")
    
    valid_skills = load_valid_skills()
    valid_filenames = get_all_valid_files()
    
    scan_dirs = ["skills", "rules", "workflows", "canons", "templates"]
    files_to_scan = []
    
    if os.path.exists(os.path.join(BASE_DIR, "GEMINI.md")):
        files_to_scan.append(os.path.join(BASE_DIR, "GEMINI.md"))
        

    for d in scan_dirs:
        folder = os.path.join(BASE_DIR, d)
        if not os.path.exists(folder): continue
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith(".md"):
                    files_to_scan.append(os.path.join(root, file))

    errors = 0
    warnings = 0
    
    # Exceptions that are not broken links or exist at project root
    ignore_list = [
        "README.md", "LICENSE.md", "CONTRIBUTING.md", "example.md", "template.md",
        "BLUEPRINT.md", "MEMORY.md", "ROADMAP.md", "STYLE_GUIDE.md", "CHANGELOG.md", 
        "ARCHITECTURE.md", "TASK.md", "task-id.md", "model_tier_protocol.md", 
        "reasoning_protocols.md", "SESSION_HANDOFF.md", "PLAN.md", "WALKTHROUGH.md"
    ]
    
    for file_path in files_to_scan:
        rel_src_path = os.path.relpath(file_path, BASE_DIR)
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # 1. Check Skill Routing
        if rel_src_path == "GEMINI.md" or "rules" in rel_src_path:
            potential_skills = re.findall(r'`([a-z0-9]+-[a-z0-9-]+)`', content)
            for ps in set(potential_skills):
                # Ignore common hyphenated terms that aren't skills
                ignore_terms = ["fail-fast", "anti-goals", "no-sweetwords", "high-fidelity", "pre-flight", "session-handoff", "zero-trust", "multi-agent", "front-end", "back-end"]
                if ps not in valid_skills and ps not in ignore_terms and len(ps) > 5:
                    print(f"⚠️  [WARNING] Possible broken skill reference '{ps}' in {rel_src_path}")
                    warnings += 1

        # 2. Check explicitly formatted file references (.md)
        file_refs = re.findall(r'([a-zA-Z0-9_-]+\.md)', content)
        md_links = re.findall(r'\]\(([^)]+\.md)\)', content)
        
        all_refs = set(file_refs + [os.path.basename(p) for p in md_links])
        
        for ref in all_refs:
            if ref in ignore_list or ref.startswith("http") or "{" in ref:
                continue
            if ref not in valid_filenames and os.path.basename(ref) not in valid_filenames:
                print(f"❌ [ERROR] Broken file reference '{ref}' in {rel_src_path}")
                errors += 1

    if errors > 0:
        print(f"\n❌ Pre-Flight Failed: {errors} broken references, {warnings} warnings.")
        print("ACTION REQUIRED: Fix routing architecture before proceeding.")
        sys.exit(1)
    else:
        print(f"\n✅ Pre-Flight Passed: Routing architecture is structurally sound ({warnings} warnings).")
        sys.exit(0)

if __name__ == "__main__":
    import io
    # Ensure stdout/stderr handle UTF-8 on Windows
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    run_preflight()
