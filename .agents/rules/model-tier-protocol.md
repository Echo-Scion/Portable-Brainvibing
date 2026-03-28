---
trigger: always_on
description: Protocol for matching task complexity to the correct LLM model tier, with forced reasoning and token constraints per tier.
---

# Model Tier Protocol

## 0. Tier Classification Heuristics (Read First)

> **Auto-Router**: Before choosing a tier, answer these questions in order. Stop at the first match.

| Question | Yes → Tier |
| :--- | :--- |
| Can I describe the full change in 1 sentence and it touches only 1 file? | `BUDGET` |
| Does the change require reading state from >1 file to understand impact? | `STANDARD` |
| Does it touch auth, RLS, global config, or cross-system architecture? | `PREMIUM` |
| Am I unsure which tier applies? | Escalate to `STANDARD`, declare why. |

**Golden Rule**: When defaulting to `STANDARD`, you MUST explicitly state which heuristic forced it. Silent default to STANDARD is a protocol violation.

> **Anti-Deliberation Clause**: If you need to *read a file to determine* whether the task qualifies as BUDGET, the task is already STANDARD. BUDGET classification must be immediately obvious from the task description alone — no investigation required.

---

## 1. The Three Tiers (Calibrated)

| Tier | Label | Practical Scope | When to Use |
| :--- | :--- | :--- | :--- |
| **Tier 0** | `BUDGET` | **Atomic / Stylistic** | Documentation, log updates, formatting, minor CSS/styling, single-file bug fixes (localized logic), basic boilerplate generation, basic unit test additions. |
| **Tier 1** | `STANDARD` | **Integrative / Feature** | Multi-file feature implementation, domain-specific state management, complex bug fixes spanning multiple modules, registry maintenance (`catalog.json`, `workspace_map.md`). |
| **Tier 2** | `PREMIUM` | **Architectural / Risky** | Global system refactors, security/Auth/RLS logic changes, high-risk infrastructure updates, deep performance bottleneck resolution. |

## 2. Infrastructure Special Note
- **Don't Over-Classify**: Modifying files inside `.agents/` is NOT automatically `PREMIUM`.
- If the change is purely about keeping the registry/map up to date, use `STANDARD`.
- If the change modifies the *logic* of how agents operate (e.g., changing `core-guardrails.md`), use `PREMIUM`.

## 3. Mandatory Declaration
- Before any Tier-1+ task, the agent MUST declare: `[TIER: STANDARD]` or `[TIER: PREMIUM]` as the first line of its Binary Oratory pre-flight check.
- **BUDGET tasks** DO NOT require Binary Oratory pre-flight. Execute directly with token-minimal I/O.

## 4. Forced Intelligence Per Tier (Capability Harness)

The following constraints are **mandatory per tier**, not optional. They prevent lazy or "sloppy" outputs at each level.

### BUDGET: Micro-Harness Protocol
Even simple tasks MUST satisfy the following Lightweight Validation Gate before output is accepted:
1. **Scope Confirmation** (1 sentence): State what the task is in plain English. No more, no less.
2. **Constraint Declaration** (1-3 bullets): What CANNOT be changed or broken. Serves as a self-injected guardrail.
3. **Zero-Theater Execution**: Perform the action immediately. No preamble, no narrative justification.
4. **Self-Verification Micro-Check**: After execution, confirm the output satisfies the original scope (e.g., "File updated. Key: X changed to Y. No other lines modified.").
- **Token Ceiling**: BUDGET tasks MUST NOT read more than 1 file in full. Use `grep_search` for targeted extraction.
- **Prohibited Actions in BUDGET**: No Sequential Thinking calls, no multi-file reads, no architectural scope expansion.

### STANDARD: Lightweight Planning Gate
Before any execution:
1. State the implementation approach in ≤3 sentences.
2. List files to be touched.
3. Identify 1-2 risk points.

Then execute in parallel where possible (Turn Minimization).

After implementation, **before marking as done**: apply the Adversarial Twin Protocol (`adversarial-twin.md`). Declare `"Swapping to Breaker Persona."` and run at least 1 attack vector against the output.

### PREMIUM: Full Sequential Thinking Mandate
See `reasoning-protocols.md` for the full protocol. Sequential Thinking with minimum 3 thought steps is **mandatory, not optional**.

## 5. Escalation & Transition Rules
- **Escalation**: If a task initially classified as `STANDARD` reveals unexpected complexity mid-execution (e.g., a simple script tweak breaks the entire graph), PAUSE and re-declare as `PREMIUM`.
- **BUDGET → STANDARD Escalation Trigger**: If a "single-file fix" requires understanding of state shared across >2 files, escalate to `STANDARD`.
- **Downgrade (Phase-Based)**: Permitted ONLY between distinct implementation phases (e.g., move to `STANDARD` for UI after a `PREMIUM` architecture phase).
- **No Silent Downgrades**: All tier changes MUST be explicitly declared.

## 6. Token Economy Rules Per Tier
| Tier | Max File Reads | Preferred Read Mode | Parallel Tool Calls |
| :--- | :--- | :--- | :--- |
| `BUDGET` | 1 (targeted grep preferred) | `grep_search` > `view_file` (header only) | Allowed |
| `STANDARD` | 3-5 (surgical sections) | `view_file` with line range | Mandatory for independent steps |
| `PREMIUM` | Unlimited (justified) | Full reads when necessary | Mandatory |