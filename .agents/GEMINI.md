# Gemini CLI: Mandatory Protocol (`.agents`)

> **CRITICAL HABITAT NOTICE:** This directory (`.agents`) is the **Master Habitat (Development Source)**. The folder `portable brainvibing` is the target compilation (Export). DO NOT treat this directory as the portable system.

This file is a **foundational mandate** and takes absolute precedence over all other instructions.

## 1. MANDATORY BOOTSTRAP (Session Resume)
- **Goal:** Immediately recover context, atomic task status, and architectural constraints.

## 2. TRI-PILLAR ARCHITECTURE (The "OS" Foundation)
- **Rule:** The agent MUST strictly adhere to the three foundational pillars in this specific precedence order.
- **Pillar 1 (Canons):** `canons/` dictates The "What" — project identity, global standards, and local feature rules. (Local overrides Global).
- **Pillar 2 (Rules):** `rules/` dictates The "How" — agent behavioral constraints, economy, and operating protocols.
- **Pillar 3 (Skills):** `skills/` dictates The "Who" — specialized capability personas to invoke per task.
- **Precedence:** If a Conflict occurs: **LOCAL CANON > GLOBAL CANON > RULES > SKILLS**.
- **Goal:** Maintain an absolute, mechanically unambiguous chain of command for agent behavior.

## 3. SURGICAL MUNCHING (Surgical Reading Logic)
- **Rule:** Use `read_file` with `start_line` and `end_line` for all files > 100 lines.
- **Rule:** Never read a file in its entirety unless it is critical for a global refactor.
- **Goal:** Keep the "Main Context" window below 50%.

## 4. ATOMIC TASKING (Atomic Task Protocol)
- **Rule:** Only one task from `BLUEPRINT.md` may be "IN_PROGRESS" at a time.
- **Rule:** Each task MUST have a corresponding file in `workflows/tasks/task-id.md` (created from `templates/ATOMIC_TASK.template.md`).
- **Rule:** Every complex (Tier-1+) execution MUST incorporate explicit model tier matching and mandatory reasoning depth (see `model_tier_protocol.md` and `reasoning_protocols.md`).

## 5. AUTOMATED SYNC & GATEKEEPERS
- **Pre-Flight Rule:** Before any complex coding session, run `python scripts/preflight_check.py` to validate architecture routing.
- **Aesthetic Rule:** Before deploying UI changes, run `python evals/audit_aesthetics.py` to ensure premium fidelity.
- **Eviction Rule:** Periodically run `python scripts/compress_memory.py` to keep the operative memory lean.
- **Graph Rule:** After any change to `skills/`, `rules/`, or `canons/`, the agent MUST run `python scripts/build_graph.py`.

---

## NON-NEGOTIABLE ACTIVATIONS ⚡

These rules are ALWAYS active and CANNOT be bypassed. They are embedded here because they are the most commonly violated rules.

### Pre-Execution Firewall (Binary Oratory)
Before ANY task that writes, deletes, or deploys, the agent MUST declare:
1. **[TIER]**: `BUDGET` / `STANDARD` / `PREMIUM`
2. **[DO]** / **[DONT]**: Primary action + hard limits
3. **[CONFIRM]**: Wait for explicit user `[DO: YES]` before proceeding

### Absolute DONT List
- `[DONT]` Delete production databases or their contents.
- `[DONT]` Commit secrets, API keys, or credentials to any file.
- `[DONT]` Execute `rm -rf` or `Remove-Item -Recurse` without explicit confirmation.
- `[DONT]` Modify `GEMINI.md` or `rules/` without a Binary Oratory pre-flight.

### Anti-Hallucination
- Never invent file contents. If not read via `view_file`, assume contents are unknown.
- Never assume library APIs. Use Context7 or pub.dev first.

### Circuit Breaker
- If any tool call fails **3 times consecutively**, ABORT and call `notify_user`.

---

## SKILL ROUTING TABLE 🎯

> Consult `skills/_index.md` for the full routing table. Quick reference below:

| Task involves... | Invoke skill |
| :--- | :--- |
| Architecture, blueprints, PRD, system design | `project-architect` |
| AI agent loops, multi-agent, state machines | `agent-architect` |
| Flutter widget bug, layout, hot reload, dart inspector | `flutter-debugger` |
| Database schema, SQL migration, Supabase RLS | `db-expert` |
| API endpoint definition, data contracts | `api-contract` |
| Flutter UI polish, Liquid Glass, micro-interactions | `ui-finish` |
| Universal validation, security, QA, system audits, eval | `integrity-sentinel` |
| Chaos testing, fault injection, adversarial testing | `chaos-engineer` |
| Node.js memory leaks, backend bottlenecks | `backend-optimizer` |
| CI/CD, deploy, production readiness | `release-manager` |
| Managing `.agents/` system, new skills creation | `system-admin` |
| README, docs, tutorials writing | `tech-writer` |

---
*Protocol Version: 1.2.0 (Consolidated Rules, Skill Routing, Injection-First)*