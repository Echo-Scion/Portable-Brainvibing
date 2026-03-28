---
trigger: glob
description: Flutter Hybrid Architecture guidelines regarding modularity and state management.
globs: *.dart
---

# Flutter Hybrid Architecture

## 1. Modular Structure
- Separate the application into clear layers: Data, Domain, and Presentation.
- Use a features-driven directory structure: `lib/src/features/[feature]/`.
- Isolate platform-specific logic using interfaces or conditional imports.
- Barrel exports: each feature exposes a single `[feature].dart` export file.

## 2. Navigation (go_router)
- Use `go_router` with `ShellRoute` for persistent bottom nav bars.
- Define all routes in a central `router.dart` using `GoRoute`.
- Implement auth guards via `redirect` callback: check auth state in `RouterNotifier`.
- Support deep linking by registering URL schemes in Android/iOS manifests.

## 3. Hybrid Patterns (Multi-Platform)
- **Cross-Platform Realtime Sync**: MANDATORY use of **Supabase Realtime Channels** to sync state instantly between Web (Next.js) and Mobile (Flutter) without polling.
- **Thread Isolation (60FPS Rule)**: For heavy data transformations (JSON parsing/Image processing), ALWAYS use `compute()` or `Isolate` on Mobile to keep the main UI thread free from jitters.
- **Web Shell Interop**: Use `dart:js_interop` for web shell communication and `Web Workers` for background heavy-lifting in Web environments.
- **Type-Safe Native Bridge**: Use **Pigeon** for native mobile APIs (Android/iOS) to prevent runtime type errors and IPC overhead.
- **Unified Logic Layer**: Maintain a shared Riverpod state layer, but isolate platform-specific implementation (e.g., File Storage vs LocalStorage) behind an interface.

## 4. Testing Strategy
- Unit tests for all Notifiers and Services (target ≥80% coverage).
- Widget tests for all critical user flows.
- Golden tests for UI regression: `flutter test --update-goldens` on design changes.
- Integration tests using `patrol` for E2E flows on device.