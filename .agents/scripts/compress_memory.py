import os
import re
import shutil
from datetime import datetime

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
ARCHIVE_FILE = os.path.join(ARCHIVE_DIR, 'compressed_memory.md')

def compress_handoff():
    if not os.path.exists(HANDOFF_FILE):
        return False

    with open(HANDOFF_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for Offload entries to compress (anything between 3. Context Offloading and 4. Anti-Goals)
    offload_pattern = r'(## 3\. Context Offloading Entry.*?\n)(?=\n## 4\.|\n## \d+\.|$)'
    
    match = re.search(offload_pattern, content, re.DOTALL | re.IGNORECASE)
    if not match:
        return False

    offloaded_text = match.group(1).strip()
    
    # Check if it's already just the placeholder
        return False

    # Replace the offload content with a compressed placeholder
    new_handoff_content = re.sub(
        r'(## 3\. Context Offloading Entry\n).*?(?=\n## 4\.|\n## \d+\.|$)',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    if content == new_handoff_content:
         return False

    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
        
    
    mode = 'a' if os.path.exists(ARCHIVE_FILE) else 'w'
    with open(ARCHIVE_FILE, mode, encoding='utf-8') as f:

    # Rewrite handoff
    with open(HANDOFF_FILE, 'w', encoding='utf-8') as f:
        f.write(new_handoff_content)
        
    print(f"✅ Handoff memory successfully compressed.")
    return True

def compress_tasks():
    tasks_dir = os.path.join(BASE_DIR, 'workflows', 'tasks')
    if not os.path.exists(tasks_dir):
        return False
        
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)

    for file in os.listdir(tasks_dir):
        if not file.endswith('.md'): continue
        path = os.path.join(tasks_dir, file)
        
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Target status indicators meaning the task is done
        is_done = bool(re.search(r'Status:\s*\[x\]', content, re.IGNORECASE) or re.search(r'Status:\s*DONE', content, re.IGNORECASE))
        if is_done:
            dest = os.path.join(ARCHIVE_DIR, file)
            shutil.move(path, dest)
            print(f"✅ Archived completed task: {file}")
            

def compress_memory():
    print("🧹 Surgical Memory Compression starting...")
    handoff_compressed = compress_handoff()
    tasks_compressed = compress_tasks()
    
    if not handoff_compressed and not tasks_compressed:
        print("✅ No compressable context found. System memory is lean and efficient.")
    else:
        print(f"✅ Memory compression complete. Stale memories moved to {ARCHIVE_DIR}")

if __name__ == "__main__":
    compress_memory()