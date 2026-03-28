---
description: Mandated reasoning depth and sequential thinking protocol per task tier.
activation: model decision
---
# Reasoning Protocols

## 1. Tier-Matched Depth
- **BUDGET**: Atomic tasks. **No Sequential Thinking.** Apply the Micro-Harness Protocol from `model-tier-protocol.md` — Scope Confirmation → Constraint Declaration → Execute → Self-Verify. Fail fast on scope creep.
- **STANDARD**: Standard coding. One lightweight planning pass (approach in ≤3 sentences + file list + 1-2 risks) before execution. Parallel tool calls are mandatory.
- **PREMIUM**: Architecture, deep debugging, audits. MUST use Sequential Thinking (minimum 3 steps). Find root causes, not symptoms.

## 2. BUDGET: Anti-Lazy Enforcement
To prevent BUDGET tasks from producing sloppy outputs, the agent MUST answer the following before any code/text modification:
- **What is the one change being made?** (If the answer cannot fit in 1 sentence, escalate to STANDARD.)
- **What constraint guarantees this change doesn't break anything adjacent?** (Justify atomicity.)

## 3. Sequential Thinking Mandate (Premium Tier)
When invoking Sequential Thinking:
1. State the problem hypothesis.
2. Break it into sub-problems.
3. Evaluate at least 2 alternative approaches.
4. Conclude with the chosen approach and its trade-offs.

## 4. Edge-Case Tax
Before finalizing any execution plan, list 2-3 potential failure modes or edge cases. This is mandatory for STANDARD and PREMIUM, optional for BUDGET.
