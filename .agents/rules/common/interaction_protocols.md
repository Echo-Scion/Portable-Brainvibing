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

## 5. Maintenance Operations

## 6. Mandatory Protocols
- **MainSystem Standard**: Follow `agent_protocols.md` for all Binary Oratory (DO/DON'T) loops and Early Model Selection.
- **Language Precision**: All AI-to-AI, System-to-Agent, and Prompt Guard instructions MUST be in English. Internal logic is strictly English-only.
- **Enforcement**: Plans failing the `@eval-engineer` scoring (score < 7) must be refined before user presentation.