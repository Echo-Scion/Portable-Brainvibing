---
trigger: always_on
description: Guidelines for optimizing application performance and context token usage.
---

# Performance & LLM Model Tiers

## 1. LLM Model Tiers

Optimizing for cost and speed while maintaining quality:

- **Budget**: Use for simple tasks, text transformations, or basic boilerplate generation. **MANDATORY**: Models in this tier MUST follow the deliberative reasoning steps in [reasoning_protocols.md](rules/common/reasoning_protocols.md) to prevent sproject_deltaw outputs.
- **Budget Tradeoff**: If on Budget Tier, trade speed for depth by using Multi-Step Thinking / Sequential Thinking.
- **Standard**: Use for standard coding tasks, feature implementations, and unit testing. (e.g., Gemini Pro Low models).
- **Premium**: Use for complex architecture design, deep debugging, or high-level reasoning. (e.g., Gemini Pro High models).

## 2. Application Performance
- **Caching**: Use Redis or local caching for frequently accessed, slow-changing data.
- **Lazy Loading**: In Flutter, use `ListView.builder` for long lists.
- **Tree Shaking**: Ensure unused dependencies are removed from production builds.

## 3. Context Optimization
- **Vibecode Limit**: Keep files between 200-500 lines for precise navigation via `@context-manager`.
- **Logic Density Cap**: For high-complexity logic (e.g., nested state management, multiple async streams), the Soft Cap is reduced to **300 lines**.
- **Turn Minimization**: AI MUST prioritize parallel tool calls for independent tasks. Aim for a **"One-Turn Research"** goal for simple queries.
- **MCI Protocol**: Use the `@context-manager` skill for monorepo context isolation to prevent token bloat.
- **Living Knowledge**: Prioritize "living" documentation within the code (docstrings/comments) and global rules (`.agents/rules/`) over creating new `.md` context files for minor features.
- Use `view_file_outline` before reading large files.
- Minimize the use of full file reads to preserve token quota.
- Aim for high information density in prompts and logs.

## 4. Vibecode Limits (AI-Friendly Code Structure)
> [!IMPORTANT]
> **The Golden Rule**: Avoid files > 500 lines. This is a technical boundary to prevent AI from experiencing "Logic Drift" or getting "Lost in the Middle".

- **Soft Cap**: Target **200–500 lines** per source code file.
  - Files > 500 lines MUST be refactored/split if new logic is required.
  - Files > 800 lines are considered a **CRITICAL BLOCKER**. Agents are prohibited from adding new logic to these files without splitting them first.
- **Modularization**: Extract private widgets, move providers to separate files, and use barrel exports (`exports.dart` or `index.ts`) so AI only loads necessary symbols.

## 5. Tooling & MCP Management
- **MCP Pre-Flight Check**: AI MUST verify active tools at the start of each session. If a project requires specific tooling (e.g., Flutter requires `dart-mcp-server`) but the server is not in the active tool list, AI MUST warn the USER immediately before proceeding.