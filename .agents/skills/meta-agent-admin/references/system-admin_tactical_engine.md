# System Admin Tactical Engine

## 🏛️ Decision Tracking (MEMORY.md)
Record major architectural shifts using the format:
- **Date**: YYYY-MM-DD
- **Decision**: Summary of the change.
- **Rationale**: Why this choice was made.
- **Impact**: What this affects in the codebase.

## 🏗️ Creation Knowledge & Standards (100% Compliant)

### 1. Skill Construction (agentskills.io)
- **Frontmatter**: Strictly valid YAML (no double quotes on strings). `name` MUST match folder name exactly.
- **Naming**: Folder & Name MUST be `kebab-case` (1-64 chars, a-z, `-` only, no double `--`).
- **Satellite Directories**: STRICTLY use `scripts/` (executable code), `references/` (documentation), and `assets/` (templates/data). Avoid arbitrary folders like `resources/` or `examples/`.
- **Documentation**: Procedural instructions (Plan-Validate-Execute) instead of just descriptive.

### 2. Rule Construction (antigravity.google)
- **File**: `kebab-case.md` in `.agents/rules/`. (Removed numeric prefixes for cleaner `@mention` invocation).
- **Frontmatter**: Mandatory YAML:
  - `description`: Context-setting summary.
  - `activation`: `always_on`, `manual`, `model_decision`, or `glob`.
  - `glob`: (Required if activation is `glob`) Glob pattern (e.g., `*.dart`).
- **Structure**: Markdown content. Max 12k chars. Supports `@mentions`.
- **Grouping**: Multiple YAML blocks are allowed for grouped rules (e.g., `always-on-core.md`).

### 3. Workflow Construction (antigravity.google)
- **File**: `kebab-case.md` in `.agents/workflows/`.
- **Invocation**: Slash command `/filename`.
- **Frontmatter**: Mandatory YAML:
  - `description`: Summary of what it does.
- **Structure**:
  - `# Title`
  - `Description`
  - `Steps` (using `- [ ]` format for sequential tracking).
- **Features**: Supports nesting (call `/other-workflow`). Max 12k chars.

## 🔄 Habit-to-Rule Promotion
Analyze `MEMORY.md` every 5 features. If a user correction appears >3 times, propose a new global rule in `.agents/rules/`.

## ⚠️ Detailed Troubleshooting
| Symptom | Root Cause | Fix / Recovery |
| AI "forgets" decisions | MEMORY.md not in hierarchy | Ensure memory is linked in workspace_map.md. |
| Skill folder messy | Missing Tier-S folders | Scaffold references/ and scripts/ directories. |
| Decision drift | Inconsistent choices | Re-read "Canon" files before proposing new logic. |

---
*Preserved from Portable Brainvibing Infrastructure*