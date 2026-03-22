---
description: Checklist for reviewing source code quality and security before committing (Code Review).
---

# Code Review Workflow

Before accepting or approving code changes (`git diff --name-only HEAD`), perform a check on each modified file based on the following criteria:

## 0. CONTEXT RETRIEVAL (JIT)
- [ ] Verify Binary Oratory compliance. IF unsure, use `grep_search` on `@00_always_on_core.md`.
- [ ] Invoke `@context-manager` to properly map code relations.

## Steps

- [ ] **Step 1:** Load `@01_always_on_context.md` for logical checking baseline.
- [ ] **Step 2:** Check for **CRITICAL Security** violations (Block commit immediately):
  - Hardcoded credentials, API keys, JWT secrets, or tokens.
  - SQL injection vulnerabilities (use of string concatenation in queries).
  - XSS vulnerabilities (rendering HTML without sanitization).
  - Missing or weak input validation on client/server-side.
  - Path traversal risks (reading files based on direct user input).
- [ ] **Step 3:** Check for **HIGH Code Quality** violations (Block commit if too many):
  - Functions > 50 lines (request extraction into smaller functions).
  - Files > 800 lines (request splitting into separate modules).
  - Nesting depth logic > 4 levels (use early returns / guard clauses).
  - *Silent fail*: Missing error handling (empty catch blocks).
  - Leftover `console.log` from debugging or unclear `TODO/FIXME` items.
- [ ] **Step 4:** Provide **MEDIUM Best Practices** suggestions:
  - Variable mutation present (prioritize immutable patterns / data copying).
  - No unit tests for newly added logic/functions.
  - Missing JSDoc/docstrings for public functions or external APIs.

After the review, generate a clear report containing Severity (CRITICAL/HIGH/MEDIUM), file location & line number, problem description, and direct improvement suggestions. NEVER approve code that violates CRITICAL Security points!