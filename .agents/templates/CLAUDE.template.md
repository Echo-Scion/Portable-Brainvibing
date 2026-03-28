# Claude Instructions: {project_name}

<!-- START FOUNDATION MANDATES -->
> **CRITICAL HABITAT NOTICE:** This directory is a satellite deployment of the Master Habitat. This file defines the **absolute operational constraints** for all agents operating within `{project_name}`. It is always-on and non-negotiable.

## 1. MANDATORY BOOTSTRAP (Session Resume)
- **Goal:** Immediately recover context, atomic task status, and architectural constraints.
- **CRITICAL**: Read `.agents/rules/core-guardrails.md` at the start of **every** task. This file contains the "Pre-Execution Firewall" (Binary Oratory), "Surgical Munching" protocols, and "Reasoning Standards" that are no longer hardcoded in this BIOS.
- For task-specific rules, execute search on `.agents/rules/` to find domain-specific files.
- **ANTI-AFFIRMATION MANDATE**: Never simply agree with or affirm the user's ideas/code. You must proactively find flaws, logical gaps, missed edge cases, or scalability issues. Treat every initial idea as flawed until proven otherwise. You MUST provide exactly 3 specific points of criticism along with 3 corresponding actionable solutions before proceeding.

## 2. ABSOLUTE [DONT] LIST
- `[DONT]` Delete production databases or their contents.
- `[DONT]` Commit secrets, API keys, or credentials to any file.
- `[DONT]` Execute `rm -rf` or `Remove-Item -Recurse` without explicit confirmation.
- `[DONT]` Modify `GEMINI.md` or `rules/` without a Binary Oratory pre-flight.

## 3. SKILL ROUTING TABLE
> Full routing in `.agents/workspace_map.md` or `catalog.json`.

| Task involves... | Invoke skill |
| :--- | :--- |
| Architecture, blueprints, PRD | `project-architect` |
| AI agent loops, multi-agent | `agent-architect` |
| Flutter widget bug, layout | `flutter-debugger` |
| Database schema, RLS, migration | `db-expert` |
| API endpoint, data contracts | `api-contract` |
| Flutter UI polish, Liquid Glass | `ui-finish` |
| Security, QA, audits, eval | `integrity-sentinel` |
| Node.js bottlenecks, backend | `backend-optimizer` |
| CI/CD, deploy, prod readiness | `release-manager` |
| New skills, `.agents/` system | `system-admin` |
| README, docs, tutorials | `tech-writer` |
| Context pruning, token economy | `context-manager` |
| SaaS idea validation, viability | `saas-viability` |
| SaaS growth, acquisition, retention | `saas-growth` |

## 4. THREE-TIER REASONING MODEL
- **BUDGET**: Atomic, single-file, deterministic (use Haiku/fast model)
- **STANDARD**: Multi-file, cross-module (use Sonnet/standard model)
- **PREMIUM**: Architecture, security, complex reasoning (use Opus/premium model + extended thinking)

See `.agents/rules/tier-execution-protocol.md` for tier determination logic.

## 5. CONTEXT HIERARCHY (4-Pillar System)
When working with projects using this foundation:

```
context/
├── 00_Strategy/    # Business goals, monetization
├── 01_Product/     # Features, roadmap
├── 02_Creative/    # Design, UX, style
└── 03_Tech/        # Architecture, API, data models
```

Core files: `BLUEPRINT.md`, `ROADMAP.md`, `STYLE_GUIDE.md`, `ARCHITECTURE.md`

## 6. SURGICAL MUNCHING (Context Economy)
- Read only what's needed (lazy-load from `workspace_map.md`)
- Use search on `.agents/rules/` for domain-specific guidance
- Check `.agents/LEARNINGS.md` before PREMIUM tasks
- Read `session_handoff.md` Section 4 before script execution

## 7. CRITICAL FILES

### Always Read First
- `.agents/rules/core-guardrails.md` - Core protocols, reasoning standards
- `.agents/workspace_map.md` - Orchestration entry point
- `GEMINI.md` - Workspace mandates (if exists)

### Never Modify Without Binary Oratory
- `GEMINI.md`
- Anything in `.agents/rules/`
- `workspace_map.md`

## 8. SYNCHRONIZATION SCRIPTS

Located in `.agents/scripts/`:

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `verify_agents.py` | Structural integrity check | Before publishing changes |
| `update_catalog.py` | Rebuild catalog.json index | After adding/removing skills |
| `build_graph.py` | Update knowledge graph | After structural changes |
| `publish_agents.py` | Sync to portable brainvibing | Before git push |
| `deploy_foundation.py` | Deploy foundation to project | Setting up new project |

Run verification before any .agents/ changes:
```bash
python .agents/scripts/verify_agents.py
```

## 9. SPECIAL PROTOCOLS

### Circuit Breaker
If any operation fails 3x consecutively → ABORT and request human intervention

### Evidence Mandate
PREMIUM tasks only complete when verified through:
- Empirical reproduction
- Test execution
- Explicit output validation

### Edge-Case Tax
Before finalizing features, document 2-3 failure modes and their handling

### Assumption Audit
For PREMIUM tasks, list every technical assumption before proceeding

---
*Mandate Version: 2.4.0 (Multi-AI Gateway)*
<!-- END FOUNDATION MANDATES -->

## PROJECT-SPECIFIC INSTRUCTIONS
<!-- Add your custom Claude instructions here. They will be preserved during foundation updates. -->
