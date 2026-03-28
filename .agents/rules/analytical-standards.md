---
trigger: model_decision
description: Standards for analytical rigor and evidence-based decision making.
---

# Analytical Standards

## 1. Evidence-Based Decisions
- All architectural recommendations MUST cite specific file paths or code patterns as evidence.
- Do not recommend patterns that contradict what already exists in the codebase.

## 2. Causal Enforcement (The "No-Fix" Policy)
- **Iron Law**: No code modifications are permitted until the root cause of an issue is isolated and a hypothesis is verified.
- **Protocol**: If a bug is reported, the agent MUST first demonstrate the failure (via test or reproduction script) and trace the data flow before proposing a fix.
- **Circuit Breaker**: If three consecutive fix attempts fail, the agent MUST stop and return to the research phase to re-evaluate the core hypothesis.

## 3. Value-Density Analysis (Scope Guard)
- **MVC Principle**: Prioritize Minimum Viable Complexity. Always seek the simplest implementation that fulfills the core requirement.
- **Scope Critique**: Before finalizing a plan, the agent MUST critique the proposed scope for "feature bloat." 
- **Filtering Modes**:
    - *Reduction*: Identify and remove 10-20% of non-essential complexity.
    - *Selective Expansion*: Only expand scope if it adds 10x value to the user experience.
    - *Hold*: Strictly adhere to the original blueprint without "just-in-case" additions.

## 4. Structural Critique (The 5 Questions)
When auditing or designing a system, apply these lenses:
1. **Why does this exist?** (Root cause, not surface observation)
2. **Is this the correct abstraction?** (Is this layer necessary?)
3. **What breaks if this is removed?** (Coupling analysis)
4. **What adversary could exploit this?** (Threat modeling)
5. **Does intent match behavior?** (Verify the system does what the docs claim)

## 3. Anti-Halucination Guard
- Never invent file contents. If a file has not been read via `view_file`, assume its contents are unknown.
- Never assume library APIs. If unsure, use Context7 or pub.dev search first.