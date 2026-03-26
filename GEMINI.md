# Workspace Rules & Mandates

This file defines the absolute operational constraints for all agents in this workspace.

## 1. MANDATORY ANCHORING (Pattern 1)
- **Protocol:** Jangkarkan (Anchor) tugas ini pada aturan yang ada di `.agents/rules/00_always_on_core.md`.
- **Requirement:** Every task, regardless of complexity, MUST begin by acknowledging and applying the core protocols defined in the anchoring file.

## 2. REASONING TIER & RULE INGESTION
- **ALL TIERS (BUDGET, STANDARD, PREMIUM):**
    - The agent MUST ALWAYS read `.agents/rules/00_always_on_core.md` at the start of any task. No exceptions.
- **STANDARD & PREMIUM TIERS:**
    - In addition to the core rules, the agent MUST execute a `grep_search` on the `.agents/rules/` directory to identify and ingest any task-specific rules (e.g., Flutter-specific, Web-specific, or Security rules).
    - Use the results to refine the execution strategy before taking action.

## 3. SKILL & TRIGGER MAPPING
- **Resource:** Refer to `.agents/catalog.json` as the primary Trigger Map for specialized skills.
- **Protocol:** If a task description matches a skill's `id` or `description` keywords in the catalog, the agent MUST proactively recommend or activate that skill.

## 4. PROMPT ENGINEERING STANDARDS
- Adhere to the 10 Patterns of Prompt Engineering (Anchor, Constraint Stack, Persona Boundary, Failure Injection, Confidence Gate, Step Separator, Compression, Assumption Audit, Reframe Test, Specificity Ladder) when delegating to sub-agents or formulating complex reasoning steps.

---
*Mandate Version: 1.3.0 (Anchored, Rule-Enforced, Catalog-Mapped)*