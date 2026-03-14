---
description: Automated loop to verify code quality, tests, and infrastructure integrity before committing.
---

# Workflow: Verify Loop (`/verify-loop`)

Run this workflow before creating a Pull Request or pushing major changes. It guarantees code health and infrastructure stability.

## 0. PRE-FLIGHT
- [ ] Verify Binary Oratory compliance via `@agent_protocols.md`.

## 1. STATIC ANALYSIS
- [ ] Run `flutter analyze` or `npm run lint` depending on the environment.
- [ ] Fix any warnings or errors automatically.

## 2. AUTOMATED TESTING
- [ ] Activate `@skill-qa-engineer`.
- [ ] Run the full test suite (`flutter test` or `npm test`).
- [ ] If tests fail, diagnose and fix them immediately. Do not proceed until green.

## 3. INFRASTRUCTURE AUDIT
- [ ] Activate `@skill-system-audit` to check for leaked secrets or logic drift.
- [ ] Run `python .agents/scripts/verify_agents.py` to guarantee `.agents` link integrity and protocol compliance.

## 4. FINAL REPORT
- [ ] Generate a markdown summary of the verification results.
- [ ] Only recommend `git commit` if all stages pass perfectly.