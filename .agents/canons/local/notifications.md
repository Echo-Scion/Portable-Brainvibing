# Canon: Notification Engine Standard

## 1. Overview
Standardized protocols for handling push, in-app, and email notifications.

## 2. Mandatory Rules
- **Idempotency:** All notification triggers must be idempotent.
- **Throttling:** Implement burst protection for push notifications.
- **Personalization:** Data objects for notifications must be pre-sanitized.

## 3. Implementation Logic
[Describe specific logic patterns here...]