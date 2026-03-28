import os
import json
import re
from datetime import datetime
from typing import List, Dict, Any

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_BASE = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
WORKSPACE_MAP = os.path.join(SOURCE_BASE, "workspace_map.md")
CATALOG_FILE = os.path.join(SOURCE_BASE, "catalog.json")

# Mapping folders to markers
MAPPINGS = {
    "rules": "RULES",
    "skills": "SKILLS",
    "canons": "CANONS",
    "workflows": "WORKFLOWS",
    "scripts": "SCRIPTS",
    "templates": "TEMPLATES"
}

# Blacklist for scanning
BLACKLIST = ["archive", "local", "tasks", "__pycache__", ".ipynb_checkpoints"]


def extract_description(file_path: str) -> str:
    """
    Extracts a description from a file (Markdown or Python).
    Optimized to skip trivial headers and repetitive metadata.
    """
    if not os.path.exists(file_path):
        return ""

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Markdown: Try Front Matter 'description'
            desc_match = re.search(r'^description:\s*(.*)', content, re.MULTILINE)
            if desc_match:
                return desc_match.group(1).strip()
            
            lines = content.splitlines()
            for line in lines:
                line = line.strip()
                if not line: continue
                
                # Python docstring or comment
                if file_path.endswith(".py"):
                    if line.startswith("#"):
                        desc = line.lstrip("# ").strip()
                        if desc.lower() not in file_path.lower(): return desc
                    if '"""' in line or "'''" in line:
                        desc = line.replace('"""', '').replace("'''", "").strip()
                        if desc: return desc
                
                # Markdown Header
                if line.startswith("# "):
                    desc = line.lstrip("# ").strip()
                    # Skip trivial headers (filename or generic labels)
                    base_name = os.path.basename(file_path).lower().split('.')[0]
                    if desc.lower() in [base_name, "workflow", "canon", "rule", "template", "skill"]:
                        continue
                    return desc
                    
                # First non-empty, non-header line as fallback (limit length)
                if not line.startswith(("#", "---", "import", "from", ">", "!", "[")):
                    res_line: str = line[:120].strip()
                    return res_line + ("..." if len(line) > 120 else "")
                    
    except Exception:
        pass
    return ""

def get_grouped_skills(skills_dir: str, catalog_data: Dict[str, Any]) -> List[str]:
    """
    Special logic for skills: Grouping in MD, but rich metadata in catalog.json.
    """
    categories = {
        "🏛️ Strategy, Architecture & Admin": ["architecture", "admin", "planning", "maintenance"],
        "🏗️ Backend, API & Database": ["backend", "api", "database"],
        "🎨 Data, UI & UX": ["logic", "ui", "ux", "flutter", "debugger"],
        "🛡️ Quality, Security & Audit": ["qa", "testing", "security", "audit", "chaos", "adversarial"],
        "📈 Marketing & Business (SaaS Growth)": ["business", "marketing", "saas", "strategy"],
        "📚 Knowledge & Optimization": ["utility", "research", "performance", "workflow"],
        "🔧 System & Operations": ["release", "devops", "ci/cd", "deploy", "path integrity"]
    }
    
    grouped: Dict[str, List[str]] = {cat: [] for cat in categories}
    grouped["Other"] = []
    
    skills_data = []
    
    skill_dirs = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])
    for skill_id in skill_dirs:
        skill_md = os.path.join(skills_dir, skill_id, "SKILL.md")
        
        # Extract rich metadata for catalog.json
        metadata = {"id": skill_id, "description": "", "tags": []}
        if os.path.exists(skill_md):
            with open(skill_md, 'r', encoding='utf-8') as f:
                content = f.read()
                desc_m = re.search(r'^description:\s*(.*)', content, re.MULTILINE)
                tags_m = re.search(r'^tags:\s*\[(.*?)\]', content, re.MULTILINE)
                
                metadata["description"] = desc_m.group(1).strip() if desc_m else extract_description(skill_md)
                metadata["tags"] = [t.strip(' "\'') for t in tags_m.group(1).split(',')] if tags_m else []

        skills_data.append(metadata)

        # In Workspace Map, we just list the skill ID
        display = f"- `{skill_id}`"
        
        assigned = False
        for cat, tags in categories.items():
            if any(tag in metadata["tags"] for tag in tags):
                grouped[cat].append(display)
                assigned = True
                break
        if not assigned: grouped["Other"].append(display)

    # Append to global catalog
    catalog_data["skills"].extend(skills_data)

    # Format for markdown (Clean and token-efficient)
    lines = []
    for cat, items in grouped.items():
        if items:
            lines.append(f"#### {cat}")
            lines.extend(sorted(items))
            lines.append("")
    return lines

def scan_directory(dir_name: str, catalog_data: Dict[str, Any]) -> List[str]:
    """
    Scans a directory recursively and returns clean markdown lines (paths only).
    Metadata is handled separately for catalog.json.
    """
    dir_path = os.path.join(SOURCE_BASE, dir_name)
    if not os.path.exists(dir_path):
        return []

    lines = []
    
    # Skills special handling (categorization)
    if dir_name == "skills":
        return get_grouped_skills(dir_path, catalog_data)

    # General recursive scan
    for root, dirs, files in os.walk(dir_path):
        # Filter blacklist
        dirs[:] = [d for d in dirs if d not in BLACKLIST]
        
        rel_root = os.path.relpath(root, dir_path)
        indent = "" if rel_root == "." else "  "
        
        if rel_root != ".":
            lines.append(f"{indent}- **{rel_root.replace(os.sep, '/').title()}**")
            indent += "  "

        for file in sorted(files):
            if file in BLACKLIST or file.startswith(".") or file == "SKILL.md":
                continue
            
            file_path = os.path.join(root, file)
            rel_file = os.path.relpath(file_path, dir_path).replace(os.sep, '/')
            
            # Workspace Map now only contains clean paths to save tokens (Lazy Loading)
            lines.append(f"{indent}- `{rel_file}`")

            # Rules special handling: extract metadata for catalog.json
            if dir_name == "rules" and file.endswith(".md"):
                metadata = {"id": rel_file, "description": "", "trigger": ""}
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        desc_m = re.search(r'^description:\s*(.*)', content, re.MULTILINE)
                        trigger_m = re.search(r'^trigger:\s*(.*)', content, re.MULTILINE)
                        
                        metadata["description"] = desc_m.group(1).strip() if desc_m else extract_description(file_path)
                        metadata["trigger"] = trigger_m.group(1).strip() if trigger_m else ""
                except Exception:
                    pass
                catalog_data["rules"].append(metadata)

    return lines


def update_map():
    workspace_root = os.path.abspath(os.path.join(SOURCE_BASE, ".."))
    project_name = os.path.basename(workspace_root)

    if not os.path.exists(WORKSPACE_MAP):
        # Create minimal dashboard
        header = (
            f"# WORKSPACE MAP: {project_name} (.agents)\n\n"
            "A high-level topography of the workspace. Metadata is stored in `catalog.json`.\n\n"
            "> [!IMPORTANT]\n"
            "> This document is a **LEAN INDEX**. \n"
            "> - **Lazy-Loading**: Refer to `catalog.json` for skill details and descriptions.\n\n"
        )
        with open(WORKSPACE_MAP, 'w', encoding='utf-8') as f:
            f.write(header)

    with open(WORKSPACE_MAP, 'r', encoding='utf-8') as f:
        content = f.read()

    catalog_data = {
        "generatedAt": datetime.now().isoformat() + "Z",
        "total": 0,
        "skills": [],
        "rules": []
    }

    for folder, marker in MAPPINGS.items():
        print(f"Mapping {folder}...")
        section_lines = scan_directory(folder, catalog_data)
        
        # Build block
        new_block = [f"<!-- {marker}_START -->", f"<!-- Auto-generated index -->"]
        new_block.extend(section_lines)
        new_block.append(f"<!-- {marker}_END -->")
        
        replacement = "\n".join(new_block)
        
        pattern = rf"<!-- {marker}_START -->.*?<!-- {marker}_END -->"
        if re.search(pattern, content, re.DOTALL):
            # Safe replacement immune to backslashes
            content = re.sub(pattern, lambda m: replacement, content, flags=re.DOTALL)
        else:
            # Append if marker not found
            content += f"\n## {folder.title()}\n{replacement}\n"

    # Write updated workspace_map.md
    with open(WORKSPACE_MAP, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Finalize catalog_data and write to catalog.json
    catalog_data["total"] = len(catalog_data["skills"]) + len(catalog_data["rules"])
    with open(CATALOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(catalog_data, f, indent=2, ensure_ascii=False)

    print(f"✅ Workspace map and catalog.json optimized.")

if __name__ == "__main__":
    update_map()