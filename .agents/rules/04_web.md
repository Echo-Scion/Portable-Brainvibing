---
description: Web Development Standards for frontend excellence, API safety, and Node.js logic.
activation: always_on
glob: "**/*.{ts,tsx,js,jsx,html,css}"
---
# Web Development Standards (Antigravity)

## 1. Backend & API (The "Defensive Shell" Principle)
- **Safety Gate**: Use `zod` or equivalent for strict input validation and schema parsing. Never trust raw request bodies.
- **Service Layer Pattern**: Decouple logic from Express/FastAPI routes. Use dedicated Service classes/functions for business logic.
- **Atomic Database Operations**: Use transactions for multi-step database writes to prevent partial data state.
- **API Documentation**: Provide comprehensive documentation for all endpoints (OpenAPI/Swagger).

## 2. Frontend (The "Component Harmony" Principle)
- **Type Safety**: Mandatory TypeScript for all React/Angular components.
- **State Management**: Use professional patterns (Redux Toolkit, Zustand, or TanStack Query) based on project complexity.
- **Atomic UI Components**: Keep components small (<150 lines) and focused on a single responsibility.
- **Responsiveness**: Build responsive and accessible user interfaces using modern CSS features.

## 3. Performance & Security
- **Static Analysis**: Enforce strict ESLint/Prettier rules before every commit.
- **Token Hygiene**: Use HttpOnly/Secure cookies for JWT storage. Never store secrets in `localStorage`.
- **Optimization**: Implement lazy loading for routes and heavy visual assets.
- **Vulnerability Protection**: Protect against common web vulnerabilities (XSS, CSRF, SQL Injection).

## 4. Dependency Management
- **Audit**: Regularly update libraries to include latest security fixes and audit performance impact.
- **Pruning**: Avoid over-reliance on large, monolithic frameworks; prefer modular, tree-shakable libraries.