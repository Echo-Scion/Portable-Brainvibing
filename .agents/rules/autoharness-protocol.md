---
trigger: always_on
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

## 4. The Synthesis Loop (Iterative Refinement)
1. **Draft the Harness**: Write a quick script (Python/Bash) that defines `is_legal_action(action, state)` for the current task.
2. **Rejection Sampling**: Route your proposed solutions through this harness.
3. **Refine on Feedback**: If the harness fails (or if the environment rejects the action despite the harness), update the harness code using the error trace (Critic feedback). The harness must reach a 100% legal action verification rate.
4. **Execute**: Once the harness validates the action, safely execute the actual task.

## 5. Storage
Store reusable and generic harnesses in `.agents/canons/global/harnesses/` so other agents can reuse them across sessions.
