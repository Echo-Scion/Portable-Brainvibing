# System Interrogation Framework (Research & Docs)

## 🏛️ Ingestion Workflow
1. **Identify**: pinpoint library name and exact version.
2. **Saturation**: Pull "Getting Started" and "API Reference" using MCP tools.
3. **Extraction**: Explain *how* and *why* before *what*.
4. **Stress Testing**: Generate 5 application-based validation tasks to verify understanding.

## ⚠️ Detailed Troubleshooting
| Symptom | Root Cause | Fix / Recovery |
| Version mismatch | Stale LLM training data | Use `read_url_content` on official changelogs. |
| Research generic | Domain not extracted | Re-read `BLUEPRINT.md` / `MEMORY.md` before searching. |
| API "Unknown Symbol" | Pre-2.0 or experimental | Check "Stability" section of official docs. |
| Documentation dense | Info overload | Use `mcp_context7_query-docs` for precision extraction. |

---
*Preserved from Portable Brainvibing Infrastructure*