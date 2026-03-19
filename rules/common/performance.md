---
trigger: always_on
description: Guidelines for optimizing application performance and context token usage.
---

# Performance & LLM Model Tiers (The Lean Protocol)

## 1. The Lean Protocol (Efficiency Standards)
- **Zero-Theater Policy**: For routine tasks (boilerplate, styling, fixes), skip long narrative explanations. Perform `replace` or `write_file` as soon as the strategy is understood.
- **Tiered Context Ingestion (L0-L2)**:
    - **L0 (Index-First)**: ALWAYS check `catalog.json` or `workspace_map.md` first to map dependencies.
    - **L1 (Header-Only)**: Use `read_file` with `end_line: 25` to see metadata/front matter before full ingestion.
    - **L2 (Surgical Read)**: Use `grep_search` with `context: 5` to read ONLY the relevant code block. Avoid full file reads unless refactoring the entire file.
- **Turn Minimization**: Prioritize parallel tool calls. Aim for **"One-Turn Execution"** for simple and clear directives.

## 2. LLM Model Tiers (Experimental Routing)
Optimizing cost and speed without sacrificing quality:
- **Budget**: Simple tasks, text transformations, or basic boilerplate. Follow reasoning protocols to prevent sproject_deltaw outputs.
- **Standard**: Standard coding tasks, feature implementations, and unit testing.
- **Premium**: Complex architecture design, deep debugging, or high-level reasoning requiring "Sequential Thinking."

## 3. Application Performance
- **Caching**: Use Redis or local caching for frequently accessed, slow-changing data.
- **Lazy Loading**: In Flutter, use `ListView.builder` for long lists.
- **Tree Shaking**: Ensure unused dependencies are removed from production builds.

## 4. Modularization & Context Integrity (Vibecode)
- **Modularity over Line Counts**: Prioritize Single Responsibility Principle (SRP). A file should be as long as necessary for logical integrity, but as short as possible to stay efficient within the AI context window.
- **Target Range**: Aim for **200–600 lines** per file for optimal context management.
- **Logical Cohesion**: Do not split files arbitrarily just to meet line count targets. If a feature or class requires more lines to stay cohesive, keep it together.
- **Refactoring Signals**: If a file exceeds **800-1000 lines**, consider it an experimental signal that the module might need decoupling for future AI context health.
- **Optimization**: Extract private widgets, helper classes, or providers into separate files when they represent distinct sub-responsibilities. Use barrel exports (`export 'file.dart';`) to maintain a clean public API.

## 5. Tooling & MCP Awareness
- **Pre-Flight Check**: Verify the status of active MCP servers (Dart, Supabase, GitHub, etc.). If a required server is missing, notify the USER before taking technical action.