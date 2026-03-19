---
description: Analytical standards for code review, ensuring structural integrity and proper documentation.
activation: always_on
---
# Analytical Standards (Experimental Engineering)

Logical and analytical standards for code review, ensuring structural integrity and proper documentation.

## 1. Principles of Lean Analysis
- **Trajectory over Deliberation**: Do not explain "what you are doing" for simple tasks. The code change or technical proposal is the answer.
- **Trajectory Logging**: Briefly state the resolution path (e.g., "Scanning canons -> UI patterns") instead of narrative deliberation.
- **Fact-Based Confidence**: If the answer is already in memory/initial context, output it immediately. Avoid artificial deliberation if technical data is already available.

## 2. Code Review Practices
- Prioritize logical correctness, security, and efficiency.
- Ensure core logic is covered by unit tests or verification scripts.
- Maintain high information density in every change log.
- **Surgical Edits**: Only modify the broken or requested parts. Respect existing project code style unless explicit refactoring is requested.

## 3. Logical Evaluation
- ALWAYS check for edge cases. Identify potential failures BEFORE writing success logic.
- Use guard clauses to reduce nesting and make code more readable for future AI (or human) passes.
- Avoid side effects in pure functions. Prioritize explicit types and return signatures.
- **Boundary Fortification (Defense-in-Depth)**: When fixing data integrity bugs, do not fix just one point. You MUST add *Guard Clauses* or validation at every system "boundary" the data passes through:
    1. **Entry Gate**: Validation on data entry (e.g., API Response parsing).
    2. **Storage Gate**: Validation in State Manager/Repository before storage.
    3. **Render Gate**: Validation at the Widget/UI level before display.

## 4. Structural Integrity & Documentation
- **Single Responsibility**: Ensure files remain focused on one primary responsibility (SRP).
- **Internal Referencing**: Use internal URI paths (e.g., `ref: .agents/rules/flutter/standards.md`) for precise context referencing in docs.
- **Living Knowledge**: Prioritize docstrings (in-code comments) for minor feature documentation over separate `.md` files that risk becoming stale.
- Document complex logic with clear comments and ensure documentation stays in sync with code changes.