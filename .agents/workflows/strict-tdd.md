---
description: Strict test-driven development cycle (RED-GREEN-REFACTOR).
---

# Strict TDD Workflow

Execute the following steps sequentially when instructed to use TDD.

## 0. CONTEXT RETRIEVAL (JIT)
- [ ] Verify Binary Oratory compliance. IF unsure, use `grep_search` on `@agent_protocols.md`.

- [ ] **1. Scaffold Interfaces**: Define types/interfaces or class/function skeletons without the actual implementation.
- [ ] **2. Write Failing Test (RED)**: Write a test that is *guaranteed to fail* because the code has not been implemented yet.
   - Test the happy path.
   - Test edge cases (null, empty, error boundaries).
- [ ] **3. Run Test**: Verify that the test actually fails (RED) with the appropriate error. If not executed, the TDD is invalid.
- [ ] **4. Implement Minimal Code (GREEN)**: Write as little code as possible just to make the failing test pass. Do not add features not covered by tests.
- [ ] **5. Run Test**: Verify that all tests now *pass* (GREEN).
- [ ] **6. Refactor (OPTIONAL)**: Load `@analytical_standards.md`. Improve code quality, extract constants, or optimize production code without changing logic (tests must remain green).
- [ ] **7. Repeat**: Perform for the next feature or function.

**ABSOLUTE RULE:** It is strictly forbidden to write implementation (business logic) BEFORE tests are created and verified to fail.