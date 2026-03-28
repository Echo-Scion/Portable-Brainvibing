# System Audit Tactical Engine

## 🛡️ Multi-Layer Audit Steps
1. **Security Scan**: `grep_search` for common secret patterns (sk-, gcp-, etc).
2. **Path Scan**: Find absolute drive letters (e.g., `C:\`) and genericize them to relative paths or `C:\Users\USER\AndroidStudioProjects\_foundation`.
3. **Mechanical Verification**: Run `python .agents/scripts/verify_agents.py` to check markdown formatting, headers, and links.

## 🧪 Vibe-Code Deconstruction
Treat AI-generated prototypes (Replit, Bolt, Lovable, v0) as hostile until audited:
- **Folder Cleanup**: Move flat files into standard feature folders.
- **Mock-to-Real**: Replace mock Supabase calls with native project services.
- **Theming**: Refactor heavy wrapper themes (FlutterFlow) into native Dart `ThemeData`.

## ⚠️ Detailed Troubleshooting
| Symptom | Root Cause | Fix / Recovery |
| Leaked Path | Literal tool output usage | Use `relpath` in scripts or manually genericize. |
| Broken Link | File moved without map update | Update `workspace_map.md` and re-run verifier. |
| Skill Selection Loop | Overlapping skill defs | Consolidate duplicate skills. |

---
*Preserved from Portable Brainvibing Infrastructure*