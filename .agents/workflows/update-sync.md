---
description: Workflow to sanitize and sync local foundation updates to the portable version.
---

# Workflow: Update Sync (`/update-sync`)

Run this workflow when you have made updates to the core `_foundation/.agents` logic and want to sync those changes to the `portable brainvibing` repository for public distribution.

## 0. PRE-FLIGHT
- [ ] Verify Binary Oratory compliance via `@agent_protocols.md`.
- [ ] Ensure all local changes in the `_foundation` workspace are conceptually sound.
- [ ] Run `/verify-loop` to mechanically validate `.agents` integrity.

## 1. SANITIZATION & SYNC
- [ ] Run the synchronization script: `python .agents/scripts/publish_agents.py "Your commit message here" [auto/patch/minor/major]`.
- [ ] *Rationale*: This script automatically strips hardcoded local paths, prunes blacklisted private tools (like `audit_repo.py`), and increments the version in `CHANGELOG.md`.

## 2. VERIFY PORTABLE VERSION
- [ ] Run `python "portable brainvibing/.agents/scripts/verify_agents.py"` to guarantee the sanitized payload did not break any links.

## 3. FINALIZE & PUSH
- [ ] Provide a summary of the exported files.
- [ ] Instruct the user to commit and push the `portable brainvibing` folder to GitHub.