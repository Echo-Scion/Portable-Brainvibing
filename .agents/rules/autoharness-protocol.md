---
description: Protocol for synthesizing and using verification harnesses before high-risk actions.
trigger: always_on
activation: model_decision
---

# Rule: AutoHarness Protocol

## 1. The Core Problem
Agents often fail not due to strategic blunders, but because of "illegal moves"—actions that violate strict environment rules, syntaxes, or state transitions (e.g., hallucinating a parameter, breaking JSON structure, violating a framework constraint).

## 2. Code-As-Harness Paradigm
Instead of relying purely on internal LLM simulation or "trying and hoping", the agent MUST proactively synthesize **Harness Scripts** to act as strict verifiers for its own proposed actions. The LLM completes itself by coding its own validation plumbing.

## 3. Harness Typology
When tackling a complex, rigid, or highly-constrained task, synthesize one of the following:

- **Harness-as-Action-Verifier**: A script that intercepts the agent's proposed action (e.g., a planned file modification, SQL query, or configuration change), validates it against constraints, and returns a strict `True`/`False` with a detailed error message before the action is executed on the real environment.
- **Harness-as-Action-Filter**: A script that computes and enumerates all *valid* actions in a given state, forcing the agent to rank or select only from a verified subset.
- **Harness-as-Policy**: For repetitive tasks or deterministic state transitions, synthesize a pure algorithmic script that executes the task without further LLM intervention.

## 4. The Synthesis Loop & Asymmetric Delegation (Antigravity IDE)
The concept of *Small Model Superiority* using *manual routing* relies on asymmetric delegation:
1. **Budget Model as The Scout & Harness-Writer**: If faced with a *Tier-1+ (Standard/Premium)* task, the Budget Model is **STRICTLY PROHIBITED** from touching the main *production* file. Its exclusive task is to: read the context, write `implementation_plan.md`, and create the *Harness* script (verifier/test).
2. **Handoff (Manual Model Switch)**: After the *Harness* is written, the Budget Model triggers a *Binary Oratory Auto-Abort* with the message: `[ABORT: HARNESS READY. PLEASE SWITCH TO PREMIUM MODEL THEN PROVIDE THE EXECUTION COMMAND]`.
3. **Premium Model as The Heavy Lifter**: The Premium Model takes over. Its only task is: Write the real code until the *Harness* script created by the Budget Model evaluates to `True / Pass`.  
4. **Identify Failure Taxonomy**: If the Harness rejects the action, categorize the rejection reason before trying again:
   - *Syntax Error*: (JSON format, YAML, Typo) ➔ Easily resolved by a small model.
   - *Logic/State Error*: (Calling a non-existent function, incorrect state) ➔ Requires reading extra files/context.
   - *System/Architecture Error*: (Violating RLS, Security Boundary) ➔ **High Risk Trigger**.
5. **Execute**: Once the harness validates the action, safely execute the actual task.

## 5. Storage
Store reusable and generic harnesses in `.agents/canons/global/harnesses/` so other agents can reuse them across sessions.

## 6. Mandatory Activation Triggers
AutoHarness is REQUIRED when any of the following is true:

- Operation can delete, overwrite, or migrate persistent state.
- Action depends on strict syntax/format constraints (YAML, JSON, schema, migrations).
- Previous attempt failed more than once for the same operation class.

If a trigger is present and no harness is used, the action must be blocked.

## 7. Harness Output Contract
Every harness run must emit:

1. `action_id`
2. `is_legal` (`True` or `False`)
3. `violated_rule` (or `none`)
4. `fix_hint`

Silent harness outcomes are non-compliant.