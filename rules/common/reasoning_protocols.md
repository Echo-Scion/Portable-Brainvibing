---
trigger: always_on (Optimized for all Tiers)
description: Guidelines to balance reasoning depth with task complexity, preventing both sproject_deltaw outputs and token waste.
---

# Reasoning Protocols (High-Density Analysis)

These protocols replace long, unnecessary narrative ("Reasoning Theater") with tiered, high-density technical analysis.

## 1. Tiered Reasoning Depth (Zero-Theater Calibration)
- **Tier 0: Routine Execution (Direct)**: For simple fixes, boilerplate, and styling, skip reasoning tools. **Action**: Directly provide the `replace` or `write_file` proposal.
- **Tier 1: Logical Research (Trajectory)**: For feature implementations or medium refactors. **Action**: Briefly state the search/execution path (Trajectory Logging) before action.
- **Tier 2: Deep Analysis (Sequential Thinking)**: For architectural audits, complex debugging, or large migrations. **Action**: Use of the `sequential_thinking` tool is highly recommended for analytical depth (suggested 3-5 steps).

## 2. Failure Mode Analysis (L3 Analysis)
For complex tasks (Tier 2), take a moment to consider failure scenarios:
- **Check**: "Under what specific condition will this change break the existing system?"
- **Action**: Identify one concrete risk (e.g., circular dependency, schema mismatch) and address it before proceeding to execution.

## 3. High-Density Auditing (The Efficiency Rule)
When auditing, avoid multiple separate passes. Target **One-Pass Dense Ingestion**: Find 80% of issues in the first context read by combining syntax, context, and utility checks into a single report.

## 4. Precision Verbs & Chain of Density
- Use actionable verbs: "Scan", "Verify", "Identify", "Validate" to focus output on technical outcomes.
- If a response feels sproject_deltaw, pivot to a more granular tool (e.g., from `read_file` to `grep_search`) to gather additional technical facts.

## 5. Avoiding Redundant Commentary (Zero-Theater)
- Focus entirely on technical rationale and facts found.
- Avoid meta-communication about the thinking process (e.g., "I will carefully consider every possibility..."). Present facts and planned actions immediately.
- **Fact-Based Confidence**: If the solution is clear from the existing project context, provide the output or implementation directly without artificial deliberation.