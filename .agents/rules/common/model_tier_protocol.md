---
description: Protocol for matching task complexity to the correct LLM model tier.
activation: always_on
---
# Model Tier Protocol

## 1. The Three Tiers

| Tier | Label | When to Use |
| :--- | :--- | :--- |
| **Tier 0** | `BUDGET` | Simple boilerplate, text transformations, minor styling fixes. |
| **Tier 1** | `STANDARD` | Standard feature implementation, unit tests, typical code changes. |
| **Tier 2** | `PREMIUM` | Complex architecture, deep audits, threat modeling, multi-system refactors. |

## 2. Mandatory Declaration
- Before any Tier-1+ task, the agent MUST declare: `[TIER: STANDARD]` or `[TIER: PREMIUM]` as the first line of its Binary Oratory pre-flight check.
- This declaration signals the reasoning depth to be applied.

## 3. Escalation Rules
- If a task initially classified as `STANDARD` reveals unexpected complexity mid-execution, PAUSE and re-declare as `PREMIUM` before continuing.
- Never downgrade during execution (do not start as `PREMIUM` and silently switch to `BUDGET` behavior).