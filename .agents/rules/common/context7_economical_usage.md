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