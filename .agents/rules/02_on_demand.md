---
description: Standardized Git workflow, commit messages, and branching strategy.
activation: always_on
glob: "*"
---
# Git Workflow & Conventional Commits

## 1. Commit Message Format
`<type>(<scope>): <description>`

## 2. Commit Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, missing semi-colons, etc.
- `refactor`: Refactoring production code
- `test`: Adding missing tests, refactoring tests
- `chore`: Updating build tasks, package manager configs, etc.

## 3. Branching Strategy
- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: New features
- `bugfix/*`: Bug fixes

## 4. Worktree Isolation (Parallel Development)
- **Concept**: For parallel sub-tasks or large feature refactors, use `git worktree add ../feature-branch feature-branch` to create a physically isolated workspace.
- **Benefit**: This prevents file locking issues and allows the AI to work on different parts of the project simultaneously without cross-contamination.
- **Cleanup**: Always use `git worktree remove` after the task is merged to maintain disk hygiene.

## 5. Rules
- Always pull before pushing.
- Rebase `develop` into your feature branch frequently.
- Keep commits atomic and descriptive.
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
---
description: Protocols for API communication, data integrity, and inter-service interaction.
activation: on_demand
---
# Connector & Interaction Protocols

## 1. Communication Standards
- Use JSON as the primary format for data exchange.
- Define clear API contracts between services.
- Implement versioning for all public APIs.

## 2. Interaction Protocols
- Ensure consistent response structures across all endpoints.
- Handle timeouts and retries for external service calls gracefully.
- Secure all inter-service communication using standard protocols (e.g., mTLS).

## 3. Data Integrity
- Validate all incoming data against predefined schemas.
- Ensure atomicity for complex multi-step operations.
- Implement idempotency for critical transactions.

## 4. Monitoring & Observability
- Export key metrics for system health monitoring.
- Implement distributed tracing for complex request flows.
- Ensure logs are structured and searchable.
---
description: Rules for using Context7 economically and managing token consumption.
activation: on_demand
---
# Context7 Economical Usage

## 1. Resource Management
- Minimize token consumption during context retrieval.
- Prioritize high-value information snippets over full-text reads.
- Reuse context objects efficiently to avoid redundant processing.

## 2. Query Optimization
- Use specific and targeted queries to filter relevant documentation.
- Cache common query results for faster subsequent access.
- Limit the depth of recursive context generation.

## 3. Cost Control
- Monitor usage patterns to identify potential inefficiencies.
- Use lower-tier models for non-critical context processing.
- Periodically review and purge outdated context data.

## 4. Integration Guidelines
- Integrate Context7 seamlessly with existing agent workflows.
- Ensure consistent data formatting for all retrieved context.
- Provide clear error messages when context retrieval fails.