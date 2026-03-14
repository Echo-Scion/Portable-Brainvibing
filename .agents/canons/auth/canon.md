# Authentication Canon (Supabase + Firebase Auth)

This canon defines the standard auth patterns for Flutter applications in the MainSystem.

## 1. Auth Provider Pattern
- Use **Firebase Auth** for Social Logins (Google, Apple, Phone OTP) — it has stronger native integrations.
- Use **Supabase Auth** for pure Email/Password if Firebase is not used.
- If using both: Firebase mints the JWT, then exchange it for a Supabase session using a Custom JWT.

## 2. Token Management
- **Never** store tokens in `SharedPreferences`.
- Always use `flutter_secure_storage` for JWTs and Refresh Tokens.
- Implement an interceptor (`dio` or `http`) to automatically inject the Bearer token and handle 401s (trigger session refresh).

## 3. State Management (Riverpod)
- Create `auth_provider.dart` with an `AsyncNotifier<UserModel?>`.
- State transitions:
  - `const AsyncLoading()` during startup check
  - `AsyncData(null)` for unauthenticated (guest)
  - `AsyncData(UserModel)` for authenticated
- Expose a `logout()` method that clears secure storage and resets state.

## 4. Routing Guards (go_router)
Protect screens using `redirect` in `GoRouter`:
```dart
redirect: (context, state) {
  final authState = ref.watch(authProvider);
  final isGoingToLogin = state.uri.path == '/login';
  
  if (authState.isLoading) return null; // wait
  
  if (authState.value == null && !isGoingToLogin) {
    return '/login'; // force login
  }
  
  if (authState.value != null && isGoingToLogin) {
    return '/dashboard'; // already logged in
  }
  
  return null; // no redirect
}
```

## 5. Security (RLS)
- If using Supabase, **Row Level Security (RLS)** is mandatory.
- Example policy: `auth.uid() = user_id`.
- Never trust the client to filter its own data.