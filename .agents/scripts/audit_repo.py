import os
import re
import sys
from pathlib import Path

# Configuration
SECRET_PATTERNS = [
    r"(?:api_key|secret|password|token|credential)\s*[:=]\s*['\"][a-zA-Z0-9_\-]{16,}['\"]",
    r"sk-[a-zA-Z0-9]{20,}",  # OpenAI
    r"sb_publishable_[a-zA-Z0-9]{20,}",  # Supabase
    r"xox[bpgs]-[a-zA-Z0-9\-]{10,}",  # Slack
]

PATH_PATTERNS = [
    r"[a-zA-Z]:\\[^ \n\r\"']+",  # Windows absolute paths
    r"/(?:Users|home)/[^ \n\r\"']+",  # Unix absolute paths (suspicious)
]

FILE_LINK_PATTERN = r"file:///([^ \n\r\"'>#]+)"

EXTENSIONS_TO_SCAN = {'.md', '.txt', '.py', '.js', '.ts', '.yaml', '.yml', '.json'}
EXCLUDE_DIRS = {'.git', '.agent', '.agents', 'node_modules', 'dist', 'build', '.gemini'}

def audit_repo(root_dir):
    print(f"--- Starting Repository Audit at {root_dir} ---")
    issues_found = 0
    root_path = Path(root_dir)

    for path in root_path.rglob('*'):
        if any(exclude in path.parts for exclude in EXCLUDE_DIRS):
            continue
        
        if path.is_file():
            # 1. Check for exposed .env files
            if path.name == ".env" or path.name.endswith(".env.local"):
                print(f"[CRITICAL] Exposed env file found: {path.relative_to(root_path)}")
                issues_found += 1

            if path.suffix in EXTENSIONS_TO_SCAN:
                try:
                    content = path.read_text(encoding='utf-8', errors='ignore')
                    lines = content.splitlines()

                    for i, line in enumerate(lines, 1):
                        # 2. Hardcoded Secrets
                        for pattern in SECRET_PATTERNS:
                            if re.search(pattern, line, re.IGNORECASE):
                                # Mask the secret for display
                                print(f"[SECURITY] Possible secret in {path.relative_to(root_path)}:L{i}")
                                issues_found += 1

                        # 3. Absolute Paths
                        for pattern in PATH_PATTERNS:
                            if re.search(pattern, line):
                                # Exception for known safe absolute paths if any, but usually better to genericize
                                print(f"[SANITY] Absolute path found in {path.relative_to(root_path)}:L{i} -> {re.search(pattern, line).group()}")
                                issues_found += 1

                        # 4. Broken File Links
                        links = re.findall(FILE_LINK_PATTERN, line)
                        for link in links:
                            # Handle <ROOT> placeholder
                            resolved_link = link.replace("<ROOT>", ".").replace("%3CROOT%3E", ".")
                            
                            # Try to resolve
                            link_path = Path(resolved_link)
                            if not link_path.exists():
                                # Check if it's relative to project root
                                if not (root_path / resolved_link).exists():
                                    print(f"[INTEGRITY] Broken file link in {path.relative_to(root_path)}:L{i} -> {link}")
                                    issues_found += 1
                except Exception as e:
                    print(f"[ERROR] Could not read {path}: {e}")

    print(f"\n--- Audit Finished. Issues Found: {issues_found} ---")
    return issues_found

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    issues = audit_repo(target)
    if issues > 0:
        sys.exit(1)
    else:
        sys.exit(0)
