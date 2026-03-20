---
description: Flutter Development Standards for widget composition, state, and performance.
activation: always_on
glob: "**/*.dart"
---

# Flutter Development Standards (Antigravity)

## 1. Aesthetic-First Prototyping (The "Liquid Glass" Principle)
- **Visuals-First**: Never model complex business logic if the UI isn't high-fidelity yet. Use placeholders to "feel" the vibe first.
- **Glassmorphism & Polish**: Leverage `skill-ui-finish` to build beautiful visual frameworks (Liquid Glass) with micro-interactions early in the lifecycle.
- **Theme Consistency**: Strictly use project design tokens (`Theme.of(context)`) to maintain the Antigravity aesthetic.

## 2. Unidirectional Data Flow / UDF (The "One-Way Street" Principle)
- **Mandate**: All state MUST flow in one direction: **Model -> UI**. Events flow **UI -> Model**.
- **Riverpod 2.x**: Formalize logic in `AsyncNotifier` or `Notifier` to manage state predictably.
- **Reactive Mapping**: Every state change MUST be traceable through a central provider. This simplifies agent understanding of the codebase.

## 3. Widget Design
- Favor Composition over Inheritance.
- Use `const` whenever possible to optimize performance.
- Modularize UI components into small, reusable widgets (<150 lines per widget file).
- Never put business logic inside `build()` — extract to Notifiers or Services.

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