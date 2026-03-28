# Workspace Rules & Mandates: {project_name}

<!-- START FOUNDATION MANDATES -->
> **CRITICAL HABITAT NOTICE:** This directory is a satellite deployment of the Master Habitat. This file defines the **absolute operational constraints** for all agents operating within `{project_name}`. It is always-on and non-negotiable.

## 1. MANDATORY BOOTSTRAP (Session Resume)
- **Goal:** Immediately recover context, atomic task status, and architectural constraints.
- **CRITICAL**: Read `.agents/rules/core-guardrails.md` at the start of **every** task. This file contains the "Pre-Execution Firewall" (Binary Oratory), "Surgical Munching" protocols, and "Reasoning Standards" that are no longer hardcoded in this BIOS.
- For task-specific rules, execute `grep_search` on `.agents/rules/` to find domain-specific files.
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

---
*Mandate Version: 2.3.0 (Smart-Merge Gateway)*
<!-- END FOUNDATION MANDATES -->

## PROJECT-SPECIFIC MANDATES
<!-- Add your custom project rules here. They will be preserved during foundation updates. -->
