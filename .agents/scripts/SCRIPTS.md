# ?? Scripts & Automation Index

This directory contains global utilities and automation scripts for the **Portable Brainvibing** infrastructure.

## ??? Global Utility Scripts (Portable)

| Script | Purpose | Availability |
| :--- | :--- | :--- |
| [verify_agents.py](file:///<ROOT>/.agents/scripts/verify_agents.py) | Scans for broken links/headers (Mechanical Audit). | **PORTABLE** |
| [audit_repo.py](file:///<ROOT>/.agents/scripts/audit_repo.py) | Advanced security/leak scanning (Owner Audit). | **PORTABLE** |
| [audit_structure.md](file:///<ROOT>/.agents/scripts/audit_structure.py) | Structural compliance validator. | **PORTABLE** |

## ?? Organization Policy

1.  **Global Scripts**: Place in .agents/scripts/. These should be generic enough to run from any project project's root.
2.  **Output Files**: Scripts should NEVER write persistent logs or reports to the root. Use a logs/ folder or system-specific temp directories.
