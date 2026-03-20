import os
import json
import hashlib
import re
from datetime import datetime

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_BASE = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

# Categories to scan
SCAN_DIRS = ["skills", "rules", "workflows", "canons", "templates"]

def calculate_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def extract_links(content):
    """
    Finds references like @skill-name, rule-name.md, or explicit depends_on metadata.
    """
    links = set()
    # Find @mentions
    mentions = re.findall(r'@([a-zA-Z0-9_-]+)', content)
    links.update(mentions)
    
    # Find file references in rules/canons
    file_refs = re.findall(r'([a-zA-Z0-9_-]+\.md)', content)
    for ref in file_refs:
        # Strip .md for consistency
        links.add(ref.replace(".md", ""))
        
    return list(links)

def build_graph():
    print("🧠 Building Knowledge Graph (Neural Mapping)...")
    
    # Load existing graph to check for changes (Merkle-style)
    old_graph = {}
    if os.path.exists(GRAPH_FILE):
        with open(GRAPH_FILE, 'r', encoding='utf-8') as f:
            old_graph = json.load(f).get("nodes", {})

    graph = {
        "generatedAt": datetime.now().isoformat() + "Z",
        "nodes": {},
        "inverted_index": {}
    }

    for folder in SCAN_DIRS:
        folder_path = os.path.join(SOURCE_BASE, folder)
        if not os.path.exists(folder_path): continue

        for root, _, files in os.walk(folder_path):
            for file in files:
                if not file.endswith((".md", ".json", "SKILL.md")) or file == ".gitkeep":
                    continue
                
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, SOURCE_BASE)
                node_id = os.path.basename(os.path.dirname(file_path)) if file == "SKILL.md" else file.replace(".md", "")
                
                current_hash = calculate_hash(file_path)
                
                # Logic: Only deep-scan if hash changed (Merkle Detection)
                links = []
                if node_id in old_graph and old_graph[node_id].get("hash") == current_hash:
                    links = old_graph[node_id].get("links_to", [])
                else:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        links = extract_links(content)
                        
                        # Build Inverted Index for keywords
                        words = re.findall(r'\b\w{4,}\b', content.lower())
                        for word in set(words):
                            if word not in graph["inverted_index"]:
                                graph["inverted_index"][word] = []
                            if node_id not in graph["inverted_index"][word]:
                                graph["inverted_index"][word].append(node_id)

                graph["nodes"][node_id] = {
                    "path": rel_path,
                    "hash": current_hash,
                    "links_to": links,
                    "type": folder
                }

    # Write the graph
    with open(GRAPH_FILE, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Knowledge Graph updated: {len(graph['nodes'])} nodes mapped.")

if __name__ == "__main__":
    build_graph()