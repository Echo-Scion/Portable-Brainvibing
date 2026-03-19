---
description: Protocol for selecting and validating LLM model tiers based on task complexity.
activation: on_implementation_plan
---

# Model Tier Protocol (Tier-S)

This protocol ensures cost efficiency and output quality by matching task complexity with the appropriate LLM model tier (Budget, Standard, Premium).

## 1. Planning Logic
When generating an `Implementation Plan`, the agent MUST:
1.  **Lookup Skill Tiers**: Reference `.agents/catalog.json` or `workspace_map.md` to identify the `Recommended_Tier` for the active skills involved in the task.
2.  **Assign Tiers to Sub-tasks**:
    *   **Budget (Gemini Flash)**: Documentation (`tech-writer`), UI styling (`skill-ui-finish`), research (`skill-knowledge`), or basic boilerplate.
    *   **Standard**: Feature implementation, logic modeling (`skill-data-logic`), debugging (`flutter-debugger`), or testing (`skill-qa-engineer`).
3.  **Explicit Recommendation**: Every plan MUST include a `Model Recommendation` section.

## 2. Prompt Guard Integration
Before executing any task, the `Prompt Guard` MUST include the required Tier.
- **Format**:
  ```markdown
  Target: [Action]
  Tier: [Budget | Standard | Premium]
  Reason: [Why this tier is needed based on Skill metadata]
  ```

## 3. Enforcement & Guardrails
- **Flash Mandate**: If running on the **Budget** tier, the agent MUST activate `reasoning_protocols.md` to ensure depth.
- **Upgrade Warning**: If a task requires a **Premium** skill but is being executed on a **Budget** model, the agent MUST warn the user:
  > "⚠️ CAUTION: This task involves [Skill Name] (Premium). Current model (Budget) may produce sproject_deltaw or incomplete architecture. Consider upgrading for this step."

## 4. Automatic Escalation
If a task fails (build error or logic bug) on a lower tier:
1.  **First Failure**: Retry with deeper reasoning (Budget) or standard checks.
2.  **Second Failure**: The agent MUST recommend escalating the model tier for the next attempt.