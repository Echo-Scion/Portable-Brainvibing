# Notifications Canon (FCM + Local)

This canon defines the standard push and local notification architecture.

## 1. Firebase Cloud Messaging (FCM) Lifecycle
- Request permissions on first launch (iOS requirement).
- Retrieve FCM Token via `FirebaseMessaging.instance.getToken()`.
- **CRITICAL**: Save the token to the database (`user_tokens` table) associated with the `user_id`.
- **CRITICAL**: On logout, you MUST delete the token from the database, otherwise previous users on the same device will receive notifications meant for the new user.

## 2. Background vs Foreground
- **Foreground**: FCM does *not* show a system banner by default while the app is open. Listen to `FirebaseMessaging.onMessage` and use `flutter_local_notifications` to show an in-app banner or local system notification.
- **Background/Terminated**: The OS handles the notification banner automatically.

## 3. Targeted Push (Backend)
- Do not trigger push messages directly from the Flutter client (security risk).
- Use a **Supabase Edge Function** or Node.js backend.
- The backend queries the `user_tokens` table for the target user and sends the payload to FCM HTTP v1 API.

## 4. Polling Strategy (Battery-Efficient Fallback)
- For extreme real-time apps where FCM delivery isn't guaranteed (e.g., Chinese OEMs aggressive battery management):
  - Do not use active WebSocket/Realtime if the app is in the background.
  - Implement WorkManager or Background Fetch to trigger a silent API check every 15 minutes.
  - Only fire a local notification if new data is found.

## 5. Navigation on Tap
Use `FirebaseMessaging.instance.getInitialMessage()` (app was terminated) and `FirebaseMessaging.onMessageOpenedApp` (app was in background). 
Map the payload `route` key to a `context.go(payload['route'])` call.