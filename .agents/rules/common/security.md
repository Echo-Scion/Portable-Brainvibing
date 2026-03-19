---
description: Security best practices across projects (no secrets, input validation, authentication).
activation: always_on
---
# Security Best Practices

## 1. No Secrets in Code or Context
- NEVER hardcode API keys, passwords, or tokens in source code.
- **Strict Context Isolation**: The agent is FORBIDDEN from writing API keys, secrets, or credentials into `MEMORY.md`, `BLUEPRINT.md`, or any file within the `context/` directory during debugging or documentation.
- Use `.env` files or environment variables exclusively for secrets.
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

## 5. MiniClaw Security Principles (Local Agentic Safety)
- **Least Agency**: Only grant agents the minimum permissions required for the current task. Avoid granting broad shell access if specific tool calls suffice.
- **Manual Audit**: ALWAYS manually audit third-party skills, hooks, or MCP configurations before integration. Look for hidden prompt injections or credential exfiltration patterns.
- **Access Isolation**: Prefer local, SSH-only (mosh/tmux) persistent sessions for agent execution. Limit external channel access (Telegram/Discord bots) to non-critical monitoring tasks only.
- **Ephemeral Context**: Do not allow sensitive user data to persist in `MEMORY.md` or logs. Wipe session context if accidental leak occurs.