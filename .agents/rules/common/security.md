---
description: Security best practices across projects (no secrets, input validation, authentication).
activation: always_on
---
# Security Best Practices

## 1. No Secrets in Code
- NEVER hardcode API keys, passwords, or tokens.
- Use `.env` files or environment variables.
- Add sensitive files to `.gitignore`.

## 2. Input Validation
- Always validate and sanitize user input on the server side.
- Use libraries like `zod` (Node.js) or built-in validators (Flutter).
- Prevent SQL Injection by using parameterized queries or ORMs.

## 3. Secure Configuration
- Disable debug modes in production.
- Use HTTPS for all communications.
- Set secure headers (HSTS, CSP, etc.).

## 4. Authentication & Authorization
- Use strong, industry-standard authentication (e.g., Supabase Auth, OAuth2).
- Follow the principle of least privilege for database roles.
- Verify JWTs on every protected request.