import os
import re
import sys

# Path relative to the script location
script_dir = os.path.dirname(os.path.abspath(__file__))
# If script is in .agents/skills, the actual skills are in the same dir
skills_dir = script_dir

# Skills already migrated or that need special handling (Local Only)
skipped_skills = {
    "skill-creator", 
    "skill-stocktake",
}

def migrate_skill(skill_path):
    skill_name = os.path.basename(skill_path)
    if skill_name in skipped_skills:
        print(f"Skipping {skill_name}: Listed in exclusion list.")
        return

    skill_md_path = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(skill_md_path):
        return

    with open(skill_md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if "Tier-S standard" in content:
        print(f"Skipping {skill_name}: Already Tier-S.")
        return

    print(f"Migrating {skill_name}...")

    # Update yaml frontmatter
    content = re.sub(r'compatibility:\s*Antigravity Support', r'compatibility: Optimized for Antigravity Tier-S standard.', content)

    # Extract Title (e.g. # Accessibility Auditor)
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else skill_name.replace('-', ' ').title()

    # Split frontmatter from body
    parts = re.split(r'^(#\s+.*?)$', content, maxsplit=1, flags=re.MULTILINE)
    if len(parts) < 3:
        print(f"Could not parse body for {skill_name}, skipping.")
        return
    frontmatter = parts[0]
    body = parts[1] + parts[2]

    # Extract Workflow Resources (Persona & Context -> Troubleshooting)
    # Typically: `## Persona & Context` ... up to `## Troubleshooting`
    match_workflow = re.search(r'(##\s+Persona\s+&\s+Context.*?)(\n##\s+Troubleshooting)', body, re.DOTALL)
    
    if match_workflow:
        workflow_content = match_workflow.group(1).strip()
    else:
        # Fallback if no troubleshooting
        match_workflow2 = re.search(r'(##\s+Persona\s+&\s+Context.*)', body, re.DOTALL)
        workflow_content = match_workflow2.group(1).strip() if match_workflow2 else ""

    match_trouble = re.search(r'(##\s+Troubleshooting.*?)(?=\n##\s|$)', body, re.DOTALL)
    trouble_content = match_trouble.group(1).strip() if match_trouble else "## Troubleshooting\n\nNo troubleshooting provided yet."

    if not workflow_content:
        # If it doesn't match the standard Antigravity Legacy layout, we skip or extract all
        workflow_content = body

    # Write resources
    res_dir = os.path.join(skill_path, "resources")
    os.makedirs(res_dir, exist_ok=True)
    
    with open(os.path.join(res_dir, "workflow.md"), 'w', encoding='utf-8') as f:
        f.write(workflow_content)
        
    with open(os.path.join(res_dir, "troubleshooting_table.md"), 'w', encoding='utf-8') as f:
        f.write(trouble_content)

    # Generate new SKILL.md body
    new_body = f"""# {title}

You are an Elite Agent operating exactly parameter limits defined in your root resources.

## ## Critical: Strategy & Workflow Loading
Before executing tasks or providing suggestions, you MUST read the core engineering guidelines:
1. **Reference Resource**: `resources/workflow.md`
2. **Goal**: Internalize your precise Persona, Context, Critical Validations, and Workflow Patterns. Ensure all outputs strictly align with these instructions.

## ## Execution Workflow
1. **Context Loading**: Understand the core intent from the User request.
2. **Strategy Blueprinting**: Map the request against your predefined workflow parameters.
3. **Execution**: Perform the precise steps defined in your resources.
4. **Validation**: Check against the Critical Validations constraints before finalizing your output.
5. **Quality Gate**: Assure formatting and tone strictly follow the Persona definition.

## ## Troubleshooting
If you encounter constraints, roadblocks, or unexpected system behavior, consult `resources/troubleshooting_table.md` for exact recovery protocols.
"""

    new_skill_md = frontmatter + new_body
    
    # Save new SKILL.md
    with open(skill_md_path, 'w', encoding='utf-8') as f:
        f.write(new_skill_md)

    print(f"Successfully migrated {skill_name}.")

for item in os.listdir(skills_dir):
    full_path = os.path.join(skills_dir, item)
    if os.path.isdir(full_path) and not item.startswith("."):
        try:
            migrate_skill(full_path)
        except Exception as e:
            print(f"Error migrating {item}: {e}")

print("\nMigration Script Finished.")
