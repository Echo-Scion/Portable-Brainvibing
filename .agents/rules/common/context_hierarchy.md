---
description: Core context hierarchy protocol defining how rules, skills, and memory resolve across the workspace.
activation: always_on
---
# Rule: Plug & Play Context Hierarchy

This rule defines how the agent resolves and prioritizes rules, skills, and memory in a **Physical Residency** environment (Plug & Play).

## 1. Resolution Layers

The context is resolved in two or three layers depending on project type:

### Standard Project (Single Layer)
| Level | Name | Scope | Location |
| :--- | :--- | :--- | :--- |
| **0** | **Global Foundation** | General AI behavior & standards. | `.agents/rules/common/` |
| **1** | **Project Local** | Project-specific rules & memory. | `.agents/rules/local/` & `context/` |

### Monorepo Project (Double Lean Layer)
| Level | Name | Scope | Location |
| :--- | :--- | :--- | :--- |
| **0** | **Global Foundation** | General AI behavior & standards. | `.agents/rules/common/` |
| **1** | **Monorepo Root** | Shared infrastructure, DevOps, & Design. | `/context/` (Root) |
| **2** | **App Local** | Specific business logic & features. | `/apps/[app_name]/context/` |

## 2. Monorepo Context Distribution (Double Lean)

In a monorepo environment, context MUST be distributed to prevent "Context Bloat" and ensure app-specific isolation:

- **Root Context**: Reserved ONLY for global platform infrastructure, monorepo DevOps (e.g., Melos, Docker), and unified design systems.
- **App Context**: Every sub-app MUST maintain its own **Lean Context** folders (`00-overview`, `01-product`, `02-creative`, `03-tech`).
- **Distributed SaaS Mapping**: Detailed SaaS context (Idea, Planning, Development, etc.) is stored in the specific app's context directory, NOT the root.

## 3. Plug & Play Residency (Physical)

To ensure 100% IDE compatibility and symbol indexing (Antigravity IDE), this system uses **Physical Residency**:

- **No Symlinks/Junctions**: All rules and skills are physically copied into the project's `.agents/` folder.
- **Self-Contained**: Every project is a standalone "Intelligence Unit" that carries its own brain.
- **IDE Native**: Because files are local, `@` mentions and clickable file links work out-of-the-box.

## 3. Domain Canons (The Truth)

Beyond rules and behaviors, this system uses **Canons** (`canons/`) to store the "Static Truth" of the project:

- **Identity & Philosophy**: Foundational values and aesthetic standards (`canons/global/`).
- **Standard Logic**: Pre-approved architectural patterns for `auth/`, `notifications/`, etc.
- **Lazy-Loading**: The agent MUST lazy-load relevant `.md` files from the `canons/` directory based on the task domain to minimize context usage while maintaining high fidelity to standards.

## 4. Override Logic
- **Local Overrides Global**: If a rule exists in `.agents/rules/local/`, it automatically overrides the same rule in `.agents/rules/common/`.
- **Skill Priority**: The agent always checks for a local version of a skill in `.agents/skills/` before execution.

## 5. Initialization
- **Active Discovery**: At start, the agent checks for the `.agents/` folder in the project root.
- **Sync Status**: The agent verifies if the foundation metadata (`catalog.json`) matches the local skill files.