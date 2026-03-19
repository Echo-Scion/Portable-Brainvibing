---
description: Squash repository history into a single initial commit while preserving the current file state.
---

# Workflow: Repository Squash (`/repo-squash`)

This workflow resets the entire history of a repository to a single "initial commit", effectively squashing all past activity. This is useful for cleaning up a development history before a public release or resetting a project's "soul" without losing files.

> [!CAUTION]
> **DESTRUCTIVE ACTION**: This will irreversibly delete all commit history, tags, and branches. Ensure you have a backup of the original repository before proceeding.

## Steps

1. **Create Orphan Branch**
   // turbo
   - *Rationale*: This creates a new branch that has no parent commits, starting a fresh history.

2. **Stage All Files**
   // turbo
   - Run: `git add -A`

3. **Create Initial Commit**
   // turbo
   - Run: `git commit -m "initial commit: MainSystem Global Foundation"`

4. **Replace Main Branch**
   // turbo
   - Run: `git branch -D main`
   - Run: `git branch -m main`

5. **Force Push to Remote**
   // turbo
   - Run: `git push origin main --force`
   - *Warning*: This overwrites the history on the remote server.

> [!NOTE]
> After running this, collaborating members will need to perform a `git fetch` and `git reset --hard origin/main` to align with the new history.