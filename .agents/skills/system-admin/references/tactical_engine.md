# System Admin Tactical Engine

## 🏛️ Decision Tracking (MEMORY.md)
Record major architectural shifts using the format:
- **Date**: YYYY-MM-DD
- **Decision**: Summary of the change.
- **Rationale**: Why this choice was made.
- **Impact**: What this affects in the codebase.

## 🧠 Skill Construction Standards
- **Atomic SKILL.md**: Consolidated brain (< 100-150 lines).
- **Satellite Folders**: Use `scripts/`, `examples/`, and `references/` only for heavy assets.
- **Naming**: Folder MUST be `kebab-case`. Main file MUST be `SKILL.md`.

## 🔄 Habit-to-Rule Promotion
Analyze `MEMORY.md` every 5 features. If a user correction appears >3 times, propose a new global rule in `.agents/rules/`.

## ⚠️ Detailed Troubleshooting
| Symptom | Root Cause | Fix / Recovery |
| AI "forgets" decisions | MEMORY.md not in hierarchy | Ensure memory is linked in workspace_map.md. |
| Skill folder messy | Missing Tier-S folders | Scaffold references/ and scripts/ directories. |
| Decision drift | Inconsistent choices | Re-read "Canon" files before proposing new logic. |

---
*Preserved from Portable Brainvibing Infrastructure*