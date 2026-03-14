---
trigger: always_on (Budget Tier models)
description: Mandates deliberative reasoning for lightweight models (e.g., Gemini Flash) to prevent sproject_deltaw outputs.
---

# Reasoning Protocols (Deliberative Interrogation)

These protocols are MANDATORY when the system is operating in the **Budget (Flash)** tier or when deep analysis is requested.

## 1. Sequential Thinking Mandate
For any task tagged `[AUDIT]`, `[ANALYSIS]`, `[RESEARCH]`, or `[DEBUG]`, the agent MUST:
- Use the `sequential_thinking` tool with a minimum of **5 thoughts**.
- Each thought must explore a different dimension of the problem (Structural, Logical, Contextual, Edge Cases, Fix Strategy).

## 2. The Devil's Advocate Loop (The Skepticism Anchor)
Before presenting a final solution or analysis, the agent MUST perform a "Skepticism Check":
- **Query**: "What did I overlook? What if my primary assumption is wrong?"
- **Action**: Look for one reason why the proposed fix might FAIL or one instruction that was skipped during the scan.

## 3. Layered Auditing (The 3-Pass Rule)
Never provide an audit result in a single pass. Flash-tier models MUST perform 3 scans:
1. **Pass 1 (Surface)**: Syntax, formatting, header concatenation, naming conventions.
2. **Pass 2 (Context)**: Relationship between files, dead skill/rule references, logic flow contradictions.
3. **Pass 3 (Utility)**: Is the code/instruction actually actionable? If a skill is a "shell", it must be flagged.

## 4. Prompting for Depth
When using Flash-tier models:
- **Prioritize Verbs**: Use "Interrogate", "Dissect", "Critique" instead of "Analyze" or "Check".
- **Chain of Density**: If a response feels thin, the system automatically triggers a "Depth Recursive" call to expand on the top 3 critical findings.

## 5. Enforcement Gate
If an implementation plan is created by a Budget model and does not list any "Risks" or "Devil's Advocate" findings, it is considered **INVALID** and must be re-processed with a Skepticism Check.