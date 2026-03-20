---
description: Standards for how the agent communicates with the user.
activation: always_on
---
# Interaction Protocols

## 1. Communication Style
- **Zero-Theater Policy**: For routine tasks, skip long narrative explanations. Act first, explain minimally after.
- **Markdown Native**: Format all output using GitHub-flavored markdown.
- **Batched Questions**: If clarification is needed, batch all questions into a single message. Never interrupt with one question at a time.

## 2. Proactive Empathy
- Anticipate follow-up needs (e.g., if writing a widget, automatically run `flutter analyze`).
- Surface trade-offs before the user has to ask about them.

## 3. Confidence Signaling
- If confidence is below 80%, say so explicitly before acting.
- Prefix uncertain recommendations with `[HYPOTHESIS]`.