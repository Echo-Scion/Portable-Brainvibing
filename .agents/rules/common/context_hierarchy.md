---
description: Core context hierarchy protocol defining how rules, skills, and memory resolve across the MainSystem.
activation: always_on
---
# Rule: Context Hierarchy & Inheritance

This rule defines how the agent must resolve and prioritize rules, skills, and memory across the "MainSystem" infrastructure.


## 1. Resolution Layers

The context is resolved in order of specificity (Specific overrides Global):

| Level | Name | Scope | Location |
| :--- | :--- | :--- | :--- |
| **0** | **Global Foundation** | General AI behavior & cross-project standards. | `.agents/rules/common/` |
| **1** | **Domain Canon** | Specialized domain logic (e.g., Auth, Finance, Games). | `.agents/canons/[domain]/` |
| **2** | **Project Specifics** | Active repo rules and context memory. | `MainSystem/context/` |

## 2. Priority Logic (Overriding)
- If a rule at **Level 2** conflicts with **Level 0**, the Level 2 rule **WINNER**.
- Level 0 serves as the **Default Fallback**. If a project lacks specific rules, Level 0 applies.
- **Skills**: Always check if a project-specific skill version exists before using the global version.

## 3. Initialization & Active Discovery
- **Active Discovery (Mandatory)**: At start, the agent MUST explicitly check for a `.agents/` folder at the current level or parent (`..`). 
- **Recursive Scan**: Read `workspace_map.md` to identify the active Level 2 project and its relationship to the global foundation.
- **Layer Loading**: Load rules in order: Level 0 → then augment with Level 1 → then override with Level 2.

## 4. Tiered Strictness (Opt-Out Logic)
- **Local Sovereignty**: A Level 2 project can explicitly "Opt-Out" of specific Level 0 rules to reduce overhead.
- **Implementation**: Define a `rule_overrides` section in the project-level `protocols.md` or metadata.
- **Example**: `rule_override: { binary_oratory: disable }`.

## 5. Documentation Strategy
- Keep Level 0 thin and high-density.
- Push implementation specificities down to Level 2.
- Always document "Hard Discovery" entry points (e.g., symlinks) if present.