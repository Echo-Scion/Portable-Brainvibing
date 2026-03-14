# 📜 Scripts & Automation Index

This directory contains global utilities and automation scripts for the **Portable Brainvibing** infrastructure.

## 🛠️ Global Utility Scripts

| Script | Purpose | Availability |
| :--- | :--- | :--- |
| [verify_agents.py](file:///<ROOT>/.agents/scripts/verify_agents.py) | Scans for broken links/headers (Mechanical Audit). | **PORTABLE** |
| [audit_repo.py](file:///<ROOT>/.agents/scripts/audit_repo.py) | Advanced security/leak scanning (Owner Audit). | **LOCAL ONLY** |
| [publish_agents.py](file:///<ROOT>/.agents/scripts/publish_agents.py) | Sanitization & Versioning Engine (Sync Tool). | **LOCAL ONLY** |

## 🗄️ Archive
- `.agents/scripts/archive/`: Contains "one-off" or deprecated scripts (e.g., legacy migration tools like `tmp_rename_skills.py`). These are kept for reference but should not be used in active workflows.

## 📐 Organization Policy

1.  **Global Scripts**: Place in `.agents/scripts/`. These should be generic enough to run from the root.
2.  **Module Scripts**: Place in `/<module_name>/scripts/` (e.g., `echosystem/scripts/`).
3.  **Output Files**: Scripts should NEVER write persistent logs or reports to the root. Use a `logs/` folder or system-specific temp directories.
