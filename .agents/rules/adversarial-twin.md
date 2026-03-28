---
description: Protocol for internal validation using a dual-agent structure (Builder vs. Breaker).
activation: mandatory for STANDARD and PREMIUM tiers; exempt for BUDGET (atomic scope too narrow to warrant a Breaker pass)
---

# Adversarial Twin Protocol

To achieve "Small Model Superiority", the agent MUST externalize its critical thinking by adopting an "Adversarial Twin" persona before finalizing any feature. 

## The Protocol
When a task is implemented but not yet verified:
1. **Context Switch**: The agent explicitly declares: `"Swapping to Breaker Persona."`
2. **The Goal of the Breaker**: The Breaker's ONLY objective is to find a flaw in the Builder's code. It must be highly pessimistic.
3. **Attack Vectors**:
   - What happens if the network drops mid-request?
   - What if a JSON field is `null` or missing?
   - Is there a race condition if the user double-taps?
   - Does this violate any architectural boundaries (e.g., UI directly calling DB)?
4. **Dynamic Harness Generation**: For the chosen attack vector, the Breaker must formulate a failing condition (or pseudo-unit test).
5. **Synthesis**: The Builder must then modify the original code until the Breaker's attack is neutralized.

*Never blindly trust the first draft of the code. Always let the Twin attack it first.*