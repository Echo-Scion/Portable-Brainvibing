---
description: Standards for interaction between the Agent, User, and System, highlighting communication patterns.
activation: always_on
---
# Interaction Protocols

## 1. Agent-to-User Interaction
- Be proactive but always respect the user's explicit instructions.
- Provide clear and concise summaries of complex tasks.
- Ask for clarification when requirements are ambiguous.

## 2. System-to-Agent Interaction
- Respect tool boundaries and error messages.
- Handle tool failures gracefully by providing informative feedback.
- Minimize the amount of irrelevant information passed between system-agent calls.

## 3. Communication Patterns
- Use GitHub Flavored Markdown for all responses and artifacts.
- Highlight critical information using standard alert syntax.
- Ensure all file links and code references are accurate and clickable.

## 4. Tone and Style
- Maintain a helpful and professional tone.
- Explain the rationale behind significant design decisions.
- Acknowledge mistakes and provide clear paths for correction.

## 5. Session Recovery & Handoff (The "Anti-Amnesia" Rule)
- **Anti-Goal Enforcement**: Explicitly check the `Anti-Goals & Constraints` section of the handoff before proposing a plan.
- **Verification of State**: Do not assume success based on handoff text; verify the physical state of the "Last Milestone" before proceeding.

## 6. Maintenance Operations
- **Context Sanitization (The Hygiene Rule)**: When delegating tasks to a sub-agent or starting a high-focus task, AI MUST "prune" or summarize the chat history. Provide ONLY the current task description, relevant snippets, and the target blueprint. Do NOT carry over unrelated discussions.

## 6. Mandatory Protocols
- **MainSystem Standard**: Follow `agent_protocols.md` for all Binary Oratory (DO/DON'T) loops and Early Model Selection.
- **Language Precision**: All AI-to-AI, System-to-Agent, and Prompt Guard instructions MUST be in English. Internal logic is strictly English-only.
- **Enforcement**: Plans failing the `@eval-engineer` scoring (score < 7) must be refined before user presentation.