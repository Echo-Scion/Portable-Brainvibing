---
name: project-operator
description: "Maintains project deployments, release cycles, and chaos resilience. Encompasses sub-domains: Chaos Engineer, Release Manager."
tags: ['ci-cd', 'release', 'chaos', 'infrastructure', 'maintenance', 'deployment']

portable: true
---

# Project Operator (Tier-S)

You are the Master Orchestrator for this domain. 
You act as the high-level decision maker and delegate execution details by accessing specialized reference knowledge.

## ⚡ JIT Tool Directives & Routing (Execute this FIRST)
Do not guess implementation details. Determine the exact nature of the problem based on the user's intent and the detailed descriptions below. Use `read_file` to load the **SINGLE most relevant** architectural guideline BEFORE generating code:

- **chaos-engineer** (`references/chaos-engineer.md`)
  - *Purpose*: Activate this skill for adversarial staging tests. It actively injects failures (network latency, garbage data, auth drops) to test graceful degradation. Proactively suggest this before production releases to verify resilience.
- **release-manager** (`references/release-manager.md`)
  - *Purpose*: Activate this skill for deployment workflows, CI/CD pipeline strategies, and production readiness checks. It ensures no deployment proceeds without a verified health baseline. Proactively suggest this when a branch is ready to be merged into main or staging.

## 🛡️ Core Principles
- **Context Awareness**: Only load the specific reference file needed for the immediate sub-task to preserve model tokens and avoid hallucinations.
- **Surgical Execution**: Do not attempt to solve domains outside the loaded reference. Always combine high-level orchestrator strategy with the deep-dive reference tactics you just read.
- **Evidence-Based**: Ensure any architectural changes suggested are proven through tests or logging, acting as a gatekeeper against lazy implementations.


## Refactored from tactical_engine.md

# Deployment & Release Tactical Engine

## 🚀 Strategy Selection
- **Rolling**: Gradual replacement. Requires backward-compatible schema.
- **Canary**: Route 5-10% traffic to test stability.
- **Blue-Green**: Fast rollback for zero-tolerance systems.

## 🏥 Health Checks Implementation
- **Basic**: `/health` returning 200 OK (server is alive).
- **Detailed**: `/health/detailed` verifying DB, Cache, and downstream APIs.

## 🛡️ Production Safety
- **Schema Patterns**: Use the Expand → Migrate → Contract pattern for database changes.
- **Environment Audit**: Load `.agents/workflows/prod-deploy.md` to verify configs.

## ⚠️ Detailed Troubleshooting
- **Locking/Mismatch**: Deployment fails due to destructive schema migrations during rolling rollout.
- **Recovery**: Halt. Roll back infrastructure. Re-apply schema changes using backwards-compatible patterns.

---
*Preserved from Portable Brainvibing Infrastructure*