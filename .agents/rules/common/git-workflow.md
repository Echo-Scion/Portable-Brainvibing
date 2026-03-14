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

## 4. Rules
- Always pull before pushing.
- Rebase `develop` into your feature branch frequently.
- Keep commits atomic and descriptive.