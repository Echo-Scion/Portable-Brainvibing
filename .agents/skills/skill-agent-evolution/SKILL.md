---
name: skill-agent-evolution
description: The specialized engine for self-improving agentic infrastructure. This skill monitors session history and MEMORY.md to identify repetitive patterns, promoting them into permanent Rules, Skills, or Workflows.
Recommended_Tier: Premium
compatibility: Optimized for Antigravity Tier-S standard.
---

## 🎯 Objective
To transform a static `.agents` directory into a dynamic, self-evolving "Outer Brain" that adapts to the user's specific coding habits, architectural preferences, and recurring tasks.

---

## 🛠️ Capabilities
1.  **Pattern Recognition**: Analyzes `MEMORY.md` across projects to find shared constraints or preferences.
2.  **Protocol Promotion**: Proposes moving a "Project Memory" (Level 2) into a "Global Rule" (Level 0) when it reaches a maturity threshold.
3.  **Workflow Synthesis**: Automatically generates new `.md` files in `workflows/` by recording manual multi-step sequences.
4.  **Redundancy Audit**: Identifies overlapping skills or rules and proposes consolidation (The "Entropy Guard").

---

## 📋 Activation Criteria
- Triggered manually via `@skill-agent-evolution`.
- Triggered automatically at the end of a major feature implementation to "Harvest Intelligence".
- Triggered during a `verify_agents.py` run to check for structural evolution opportunities.

---

## 🔄 Execution Loop: The Evolution Cycle

### Phase 1: Intake (Observation)
- Read current project's `context/00-overview/MEMORY.md`.
- Analyze recent session history for repetitive "User Hints" or manual corrections.

### Phase 2: Analysis (Reasoning)
- Compare local preferences against `.agents/rules/`.
- **Question**: "Is this a one-time preference or a new fundamental standard for this user?"
- **Question**: "Can this manual sequence of 5+ steps be simplified into a single slash command?"

### Phase 3: Proposal (Synthesis)
- Present a "Draft Update" to the user:
  - *"I've noticed you always ask for X. Should I make this a permanent rule?"*
  - *"We've performed this sync sequence 3 times today. Should I create a /quick-sync workflow?"*

### Phase 4: Implementation (The Change)
  - Create new `.md` files in `rules/`, `skills/`, or `workflows/`.
  - Update `workspace_map.md` to index the new intelligence.
  - Increment the system version in `CHANGELOG.md`.

---

## 🛡️ Guardrails (Evolution Safety)
- **Binary Oratory**: NEVER modify the global foundation without explicit "YES" from the user.
- **Rollback Registry**: Always log the previous state before an evolution to allow for easy reverts.
- **Sanitization**: Ensure no project-specific secrets or sensitive data are promoted to the Global Brain.

---

## 🏷️ Version
1.0.0 `initial_evolutionary_seed`