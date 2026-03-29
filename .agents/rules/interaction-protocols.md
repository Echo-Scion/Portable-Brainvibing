---
description: Standards for how the agent communicates with the user.
activation: always on
---
# Interaction Protocols

## 1. Communication Style
- **Zero-Theater Policy** *(BUDGET tier default)*: For routine/atomic tasks, skip long narrative explanations. Output the Implementation Plan, **wait for [DO: YES]**, then act immediately. Verbosity on a BUDGET task is a scope violation, but skipping the confirmation gate is a protocol violation.
- **Lightweight Narrative** *(STANDARD tier default)*: Brief approach summary before execution, then concise result summary.
- **Full Reasoning Transparency** *(PREMIUM tier default)*: Explicit Sequential Thinking steps visible in response. Trade-offs declared.
- **Markdown Native**: Format all output using GitHub-flavored markdown.
- **Batched Questions**: If clarification is needed, batch all questions into a single message. Never interrupt with one question at a time.

## 2. Proactive Empathy
- Anticipate follow-up needs (e.g., if writing a widget, automatically run `flutter analyze`).
- Surface trade-offs before the user has to ask about them.

## 3. Clarity & Truthfulness Contract
- Do not present assumptions as facts.
- If confidence is partial, mark the statement as `Hypothesis` and attach the verification path.
- Avoid repeating unchanged plans verbatim across consecutive updates; report only deltas.
- When blocked, state blocker + next executable action in one compact block.

## 4. Linguistic Integrity (Foundation Only)
- **English-Only Mandate**: All content within the `.agents/` foundation (Rules, Skills, Workflows, Canons) MUST be written in **English**.
- **Rationale**: The foundation is the Master Habitat for the `portable brainvibing` infrastructure, targeting an international audience.
- **Project Local Flexibility**: Project-specific context (outside `.agents/`) may use other languages if requested by the user, but foundation logic must remain universally accessible in English.

## 5. The GPS Handoff (Seamless Orchestration)
To ensure multi-step workflows (like `/full-lifecycle`, `/project-init`, or deep debugging sessions) feel seamless and guided, the AI MUST append a deterministic "GPS Checkpoint" block at the end of its response whenever transitioning between workflow phases, completing a major step, or pausing for user input.

**Rule**: Do not end a complex workflow response ambiguously. Always provide the exact next step.

**Format Pattern**:
```markdown
---
### 🚦 LIFECYCLE CHECKPOINT: [Current Phase Name]
**Status:** [Brief state, e.g., Awaiting Viability Approval, Tests Passed, Blocked by Error]

**What Just Happened:**
- [Super short bullet point of the immediate result/action completed]

**Next Action Required from You:**
➤ [A single, deterministic instruction. E.g., "Reply `[DO: YES]` to lock this architecture and start scaffolding", or "Review the 3 pivots above and select one to proceed."]
---
```
This guarantees the user always knows exactly where they are in the "Zero to Hero" journey and what they must execute next to keep the workflow moving without friction.