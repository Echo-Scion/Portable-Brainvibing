import os
import re

base_dir = r"E:\BINTANG\Project\.agents\skills"

def process_skills():
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path):
            new_name = item.replace('_', '-')
            new_path = os.path.join(base_dir, new_name)
            
            if new_name != item:
                os.rename(item_path, new_path)
                print(f"Renamed {item} to {new_name}")
            else:
                new_path = item_path
            
            skill_file = os.path.join(new_path, "SKILL.md")
            if os.path.exists(skill_file):
                with open(skill_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update name field
                content = re.sub(r'^name:\s*.*', f'name: {new_name}', content, count=1, flags=re.MULTILINE)
                
                # Add compatibility if not present
                if 'compatibility:' not in content:
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        # Append to frontmatter
                        if not parts[1].endswith('\n'):
                            parts[1] += '\n'
                        parts[1] += 'compatibility: Optimized for Antigravity (Google Deepmind Advanced Agentic Coding) and standard Markdown-based agent tooling.\n'
                        content = '---'.join(parts)
                
                with open(skill_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated SKILL.md frontmatter for {new_name}")

if __name__ == "__main__":
    process_skills()
