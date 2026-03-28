import os
import json
import hashlib
import re
from datetime import datetime

# Configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_BASE = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
WORKSPACE_ROOT = os.path.abspath(os.path.join(SOURCE_BASE, ".."))
GRAPH_FILE = os.path.join(SOURCE_BASE, "knowledge_graph.json")

# Categories and folders to scan
SCAN_DIRS = ["skills", "rules", "workflows", "canons", "templates"]
# Specific files in .agents root or project root to include
EXTRA_FILES = [
    os.path.join(WORKSPACE_ROOT, "GEMINI.md"),
    os.path.join(WORKSPACE_ROOT, "README.md"),
    os.path.join(SOURCE_BASE, "workspace_map.md"),
    os.path.join(SOURCE_BASE, "DEPLOY_ME.md"),
    os.path.join(SOURCE_BASE, "LEARNINGS.md"),
    os.path.join(SOURCE_BASE, "session_handoff.md")
]

# Conceptual placeholders that are NOT files (Ignore List)
CONCEPTUAL_IGNORE = {
    "SKILL", "MEMORY", "ROADMAP", "ARCHITECTURE", "STYLE_GUIDE", "BLUEPRINT", "GEMINI", "RULES", "SKILLS",
    "Product_Hunt", "Waitlist", "Authentication", "Pre_Sales", "Waitlist", "Product_Roadmap",
    "User_Tracking", "Community_Building", "Partnerships", "CI_CD", "Demand_Testing",
    "Development_Plan", "AB_Testing", "Design_System", "Expansion_Strategy", "MVP_Scope",
    "Add_ons", "Unit_Testing", "Upsells", "Product_Led_Growth", "Integrations",
    "Customer_Interviews", "Niche_Selection", "Global_Expansion", "Market_Research",
    "Security", "Annual_Plans", "Social_Media", "Free_Trial", "Performance_Testing",
    "DevOps", "UX_Flows", "Hiring", "Tech_Stack", "User_Onboarding", "Subscriptions",
    "Feature_Prioritization", "Landing_Page", "Enterprise_Deals", "UI_Design", "Sales_Funnel",
    "Wireframes", "Monitoring", "Funnel_Analysis", "SEO_Wins", "Customer_Support",
    "Competitor_Analysis", "Beta_Testing", "Churn_Reduction", "Systems", "SaaS_Marketplaces",
    "APIs", "Prototype", "Integration_Testing", "Freemium_Model", "Email_Automation",
    "Exit_Strategy", "KPI_Dashboard", "Viral_Loops", "Opportunity_Mapping", "Checkout_Optimization",
    "Early_Adopters", "Content_Marketing", "Pricing_Strategy", "Frontend", "Cold_Email",
    "Influencer_Outreach", "Communities", "Cohort_Analysis", "Affiliate_Marketing",
    "Problem_Discovery", "Beta_Users", "Bug_Fixing", "Database", "Automation",
    "Referral_Programs", "Cloud_Hosting", "Public_Release", "Backend", "Feature_Adoption",
    "Landing_Page_Test", "Directories", "task-id", "Default", "freezed", "riverpod", "override",
    "ui_patterns", "auth", "state_management", "03_aesthetics_and_design_system", "template",
    "rules", "skills", "canons", "workflows", "scripts", "templates", "rule"
}

def calculate_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def extract_links(content):
    links = set()
    # Find @mentions
    mentions = re.findall(r'@([a-zA-Z0-9_-]+)', content)
    links.update(mentions)
    
    # Find file references in rules/canons/markdown
    file_refs = re.findall(r'([a-zA-Z0-9_-]+\.md)', content)
    for ref in file_refs:
        links.add(ref.replace(".md", ""))
        
    # Find bracket links [[link]]
    bracket_links = re.findall(r'\[\[(.*?)\]\]', content)
    for bl in bracket_links:
        links.add(bl.split('|')[0].strip())
        
    return list(links)

def build_graph():
    print("🧠 Building Knowledge Graph (Final Polish)...")
    
    graph = {
        "generatedAt": datetime.now().isoformat() + "Z",
        "nodes": {},
        "inverted_index": {},
        "broken_links": []
    }

    all_known_nodes = set()
    
    # 1. Map Extra Files
    for ef in EXTRA_FILES:
        if os.path.exists(ef):
            node_id = os.path.basename(ef).replace(".md", "")
            all_known_nodes.add(node_id)
            graph["nodes"][node_id] = {
                "path": os.path.relpath(ef, SOURCE_BASE).replace(os.sep, '/'),
                "hash": calculate_hash(ef),
                "links_to": [],
                "type": "infrastructure"
            }

    # 2. Scan Directories
    for folder in SCAN_DIRS:
        folder_path = os.path.join(SOURCE_BASE, folder)
        if not os.path.exists(folder_path): continue

        for root, _, files in os.walk(folder_path):
            for file in files:
                if not file.endswith((".md", ".json")) or file == ".gitkeep":
                    continue
                
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, SOURCE_BASE).replace(os.sep, '/')
                node_id = os.path.basename(os.path.dirname(file_path)) if file == "SKILL.md" else file.replace(".md", "")
                
                all_known_nodes.add(node_id)
                graph["nodes"][node_id] = {
                    "path": rel_path,
                    "hash": calculate_hash(file_path),
                    "links_to": [],
                    "type": folder
                }

    # 3. Deep Scan for Links
    for node_id, info in graph["nodes"].items():
        abs_path = os.path.join(SOURCE_BASE, info["path"])
        if not os.path.exists(abs_path): continue

        try:
            with open(abs_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                links = extract_links(content)
                
                valid_links = []
                for link in links:
                    if link in all_known_nodes:
                        valid_links.append(link)
                    elif link in CONCEPTUAL_IGNORE:
                        continue
                    else:
                        graph["broken_links"].append({"from": node_id, "to": link})
                
                graph["nodes"][node_id]["links_to"] = list(set(valid_links))
                
                # Inverted Index
                words = re.findall(r'\b\w{4,}\b', content.lower())
                for word in set(words):
                    if word not in graph["inverted_index"]:
                        graph["inverted_index"][word] = []
                    if node_id not in graph["inverted_index"][word]:
                        graph["inverted_index"][word].append(node_id)
        except: pass

    # 4. Finalize
    with open(GRAPH_FILE, 'w', encoding='utf-8') as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)
    
    broken_count = len(graph["broken_links"])
    print(f"✅ Knowledge Graph updated: {len(graph['nodes'])} nodes.")
    if broken_count > 0:
        print(f"⚠️  Detected {broken_count} broken links. See knowledge_graph.json")
    else:
        print("💎 Perfect Integrity: No broken links found.")

if __name__ == "__main__":
    build_graph()