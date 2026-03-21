# Canon: Authentication & Security Standard

## 1. Overview
Standardized approach for authentication and authorization within the project.

## 2. Mandatory Rules
- **Token Storage:** Never store JWTs in local storage; use HttpOnly cookies or secure secure-storage.
- **Error Handling:** Obfuscate auth errors (e.g., "Invalid credentials" rather than "User not found").
- **MFA:** Enable Multi-Factor Authentication for all administrative accounts.

## 3. Implementation Logic
[Describe specific logic patterns here...]