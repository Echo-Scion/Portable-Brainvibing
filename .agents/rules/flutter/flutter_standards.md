---
description: Flutter Development Standards for widget composition, state, and performance.
activation: always_on
glob: "**/*.dart"
---

# Flutter Development Standards

## 1. Widget Design
- Favor Composition over Inheritance.
- Use `const` whenever possible to optimize performance.
- Modularize UI components into small, reusable widgets (<150 lines per widget file).
- Never put business logic inside `build()` — extract to Notifiers or Services.

## 2. State Management (Riverpod 2.x)
- Use `@riverpod` codegen annotation for all new providers (run `dart run build_runner watch`).
- Keep business logic in `AsyncNotifier` / `Notifier`, away from UI layer.
- Never use `ref.read` inside `build()` — use `ref.watch` for reactive state.
- Ensure all state transitions are predictable and traceable via copyWith.

## 3. File & Naming Conventions
- Feature-driven structure: `lib/src/features/[feature_name]/`
  - `data/` — repositories, data sources, DTOs
  - `domain/` — models (Freezed), use cases
  - `presentation/` — widgets, providers, screens
- File names: `snake_case.dart`. Class names: `PascalCase`.
- Providers: `[featureName]Provider`, Notifiers: `[FeatureName]Notifier`.

## 4. Error Handling
- Use structured error handling (`AsyncValue.error`) in providers.
- Provide user-friendly error messages for common failure scenarios.
- Log critical errors with sufficient context for debugging.
- Never use empty `catch {}` blocks — at minimum, rethrow or log.

## 5. Performance Optimization
- Optimize build methods to avoid unnecessary rebuilds (`select()` over `watch()`).
- Use image caching (`cached_network_image`) for network assets.
- Minimize the use of heavy third-party dependencies.
- Use `ListView.builder` (never `ListView` with children) for dynamic lists.