---
description: MainSystem Agent Protocols for workspace management, documentation, and interaction.
activation: always_on
---

# MainSystem Agent Protocols (Management & Behavior)

Guidelines for AI Agents to manage workspaces, documentation, and interact with the USER efficiently.

## 1. Context & Token Efficiency
- **Pre-Flight Check**: Every session MUST start by verifying the status of required MCP servers (e.g., `dart-mcp-server`, `supabase-mcp-server`) based on the project type. If a server is disabled but needed, notify the USER immediately.
- **Model Selection**: Every `implementation_plan.md` MUST include a model recommendation based on the Tiers defined in `performance.md`. Utilize the `@cost-optimizer` skill for precision.
- **Research Ceiling**: If research exceeds **5 turns** without a clear implementation path, the agent MUST stop, summarize findings, and ask the USER for a "Surgical Hint" to prevent token waste.
- **Efficiency Standards**: Always follow the **Vibecode Limit** and **Living Knowledge Protocol** as specified in `performance.md`.
- **Resources Strategy**: 
    - Consolidate core instructions directly into `SKILL.md` (< 100 lines) for speed.
    - Use `resources/` ONLY for large datasets (> 3000 tokens) or technical manuals.

## 2. Project Management SOP (Definition of Done)
- **Auto-Sync**: Proactively update project logs and `MEMORY.md` when features are completed.
- **Documentation Priority Matrix**:
    - **Level 1 (Architectural)**: `BLUEPRINT.md` & `MEMORY.md` MUST be updated for any structural or logic-flow changes.
    - **Level 2 (Feature)**: Relevant `context/` markdown files MUST be updated for new feature implementations.
    - **Level 3 (Maintenance)**: Inline docstrings and `CHANGELOG.md` are sufficient for bug fixes and refactors.
- **Context Integrity Protocol (Mandatory)**: Every code modification (via Skill or Workflow) is NOT complete until relevant documentation (based on the Matrix above) is updated.
- **Approval**: Always set `ShouldAutoProceed: false` on implementation plans to allow for manual USER review.

## 3. Mandatory Prompt Guard (Binary Oratory)
- **Universal Trigger**: Trigger the "Prompt Guard" check automatically before entering the `EXECUTION` phase of any non-trivial task.
- **English-Only Logic**: The guard MUST be written in English.
- **Format**: 
    "Target: [Short Goal].
    **[DO]**: [Direct Action]
    **[DON'T]**: [High-Risk Exception/Anti-pattern]
    Tier: [Model Tier].
    Confirm?"
- **Scoring**: Utilize `@eval-engineer` to score the guard before presentation.

## 4. Post-Mortem & Habit Adaptation
- **Failure Analysis**: If a task fails (e.g., build error, test failure, or USER rejection), the agent MUST run a "Post-Mortem Rule Check" to see if a specific rule in `.agents/rules/` was violated.
- **Tier Escalation**: If a task fails **twice** on Budget or Standard tiers, the Post-Mortem MUST recommend escalating to the **Premium Tier** for the next attempt.
- **Habit Promotion**: Analyze `MEMORY.md` every 5 features. If a specific "Correction" from the USER appears >3 times, the agent must propose a new permanent rule in `.agents/rules/local/`.
- **Integrity Check**: Run `python .agents/scripts/verify_agents.py` at the end of every infrastructure-related task to ensure no mechanical bugs (broken headers/links) were introduced.

## 5. Interaction & Standardization
- **English Only**: All underlying logic, AI-to-AI instructions, and Prompt Guard outputs MUST be in English. No secondary language translations allowed in system logic.
- **Transparency**: Provide concise change summaries after every major file modification.