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


def extract_description(file_path: str) -> str:
    """
    Extracts a description from a file (Markdown or Python).
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
            
            # Markdown/Python: Try first # Header or Docstring summary
            # Skip the first # header if it's just the filename
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
                    # If the header is just the filename, skip it
                    if desc.lower() in file_path.lower() or "workflow" in desc.lower() or "canon" in desc.lower():
                        continue
                    return desc
                # First non-empty, non-header line as fallback
                if not line.startswith(("#", "---", "import", "from")):
                    res_line: str = line[:100].strip()
                    return res_line + ("..." if len(line) > 100 else "")
                    
    except Exception:
        pass
    return ""

def scan_directory(dir_name: str) -> List[str]:
    """
    Scans a directory recursively and returns formatted markdown lines.
    """
    dir_path = os.path.join(SOURCE_BASE, dir_name)
    if not os.path.exists(dir_path):
        return []

    lines = []
    
    # Skills special handling (categorization)
    if dir_name == "skills":
        return get_grouped_skills(dir_path)

    # General recursive scan
    for root, dirs, files in os.walk(dir_path):
        # Filter blacklist (robust filtering for os.walk)
        filtered_dirs = [d for d in dirs if d not in BLACKLIST]
        dirs.clear()
        dirs.extend(filtered_dirs)
        
        rel_root = os.path.relpath(root, dir_path)
        indent = "" if rel_root == "." else "  "
        
        # Add subdirectory headers if not root
        if rel_root != ".":
            lines.append(f"{indent}- **{rel_root.replace(os.sep, '/').title()}**")
            indent += "  "

        for file in sorted(files):
            if file in BLACKLIST or file.startswith(".") or file == "SKILL.md":
                continue
            
            file_path = os.path.join(root, file)
            rel_file = os.path.relpath(file_path, dir_path).replace(os.sep, '/')
            
            desc = extract_description(file_path)
            desc_str = f" — {desc}" if desc else ""
            
            lines.append(f"{indent}- `{rel_file}`{desc_str}")

    return lines

def get_grouped_skills(skills_dir: str) -> List[str]:
    """
    Special logic for skills with categorization and tiers.
    Also updates catalog.json.
    """
    categories = {
        "🏛️ Strategy, Architecture & Admin": ["architecture", "admin", "planning", "maintenance"],
        "🏗️ Backend, API & Database": ["backend", "api", "database"],
        "🎨 Data, UI & UX": ["logic", "ui", "ux", "flutter", "debugger"],
        "🛡️ Quality, Security & Audit": ["qa", "testing", "security", "audit"],
        "📈 Marketing & Business (SaaS Growth)": ["business", "marketing"],
        "📚 Knowledge & Optimization": ["utility", "research", "performance", "workflow"]
    }
    
    grouped: Dict[str, List[str]] = {cat: [] for cat in categories}
    grouped["Other"] = []
    
    skills_data = []
    
    skill_dirs = sorted([d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))])
    for skill_id in skill_dirs:
        skill_md = os.path.join(skills_dir, skill_id, "SKILL.md")
        
        # Extract metadata for catalog.json
        metadata = {"name": skill_id, "description": "", "tier": "Standard", "tags": []}
        try:
            with open(skill_md, 'r', encoding='utf-8') as f:
                content = f.read()
                # Simple regex for description/tier/tags
                desc_m = re.search(r'^description:\s*(.*)', content, re.MULTILINE)
                tier_m = re.search(r'^(?:Recommended_Tier|tier):\s*(.*)', content, re.MULTILINE)
                tags_m = re.search(r'^tags:\s*\[(.*?)\]', content, re.MULTILINE)
                
                metadata["description"] = desc_m.group(1).strip() if desc_m else ""
                metadata["tier"] = tier_m.group(1).strip() if tier_m else "Standard"
                metadata["tags"] = [t.strip(' "\'') for t in tags_m.group(1).split(',')] if tags_m else []
                
                if not metadata["description"]:
                    h_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
                    metadata["description"] = h_match.group(1).strip() if h_match else ""
        except: pass

        # Catalog data
        skills_data.append({
            "id": skill_id,
            "description": metadata["description"],
            "tier": metadata["tier"],
            "tags": metadata["tags"]
        })

        # Map display
        tier_label = f"[{metadata['tier']}]"
        desc_text: str = str(metadata['description'])
        display = f"- `{skill_id}` {tier_label} — {desc_text.split('(')[0].strip()}"
        
        assigned = False
        for cat, tags in categories.items():
            if any(tag in metadata["tags"] for tag in tags):
                grouped[cat].append(display)
                assigned = True
                break
        if not assigned: grouped["Other"].append(display)

    # Update catalog.json
    catalog = {"generatedAt": datetime.now().isoformat() + "Z", "total": len(skills_data), "skills": skills_data}
    with open(CATALOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)

    # Format for markdown
    lines = []
    for cat, items in grouped.items():
        if items:
            lines.append(f"#### {cat}")
            lines.extend(sorted(items))
            lines.append("")
    return lines

def update_map():
    if not os.path.exists(WORKSPACE_MAP):
        print(f"Error: {WORKSPACE_MAP} not found.")
        return

    with open(WORKSPACE_MAP, 'r', encoding='utf-8') as f:
        content = f.read()

    for folder, marker in MAPPINGS.items():
        print(f"Mapping {folder}...")
        section_lines = scan_directory(folder)
        
        # Build block
        new_block = [f"<!-- {marker}_START -->", f"<!-- Auto-generated by update_catalog.py -->"]
        new_block.extend(section_lines)
        new_block.append(f"<!-- {marker}_END -->")
        
        replacement = "\n".join(new_block)
        # Escape backslashes for re.sub replacement string to avoid bad escape errors (e.g. \U)
        replacement = replacement.replace("\\", "\\\\")
        
        pattern = rf"<!-- {marker}_START -->.*?<!-- {marker}_END -->"
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(WORKSPACE_MAP, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Workspace map fully automated and updated.")

if __name__ == "__main__":
    update_map()