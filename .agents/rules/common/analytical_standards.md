---
description: Standards for analytical rigor and evidence-based decision making.
activation: always_on
---
# Analytical Standards

## 1. Evidence-Based Decisions
- All architectural recommendations MUST cite specific file paths or code patterns as evidence.
- Do not recommend patterns that contradict what already exists in the codebase.

## 2. Structural Critique (The 5 Questions)
When auditing or designing a system, apply these lenses:
1. **Why does this exist?** (Root cause, not surface observation)
2. **Is this the correct abstraction?** (Is this layer necessary?)
3. **What breaks if this is removed?** (Coupling analysis)
4. **What adversary could exploit this?** (Threat modeling)
5. **Does intent match behavior?** (Verify the system does what the docs claim)

## 3. Anti-Halucination Guard
- Never invent file contents. If a file has not been read via `view_file`, assume its contents are unknown.
- Never assume library APIs. If unsure, use Context7 or pub.dev search first.