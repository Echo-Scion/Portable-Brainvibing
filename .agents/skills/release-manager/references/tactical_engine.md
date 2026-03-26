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