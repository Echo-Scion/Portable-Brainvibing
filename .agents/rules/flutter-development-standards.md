---
trigger: glob
description: Flutter Development Standards for widget composition, state, and performance.
globs: *.dart
---

# Flutter Development Standards (Antigravity)

## 1. Aesthetic-First Prototyping (The "Liquid Glass" Principle)
- **Premium Craftsmanship**: Every pixel and architecture choice must be intentional. Avoid basic implementations; optimize for both 60fps animations and low memory footprint.
- **Glassmorphism & Polish**: Leverage `ui-finish` to build beautiful visual frameworks (Liquid Glass) with micro-interactions early in the lifecycle.
- **Theme Consistency**: Strictly use project design tokens (`Theme.of(context)`) to maintain the Antigravity aesthetic.

## 2. Structural & UI Excellence
- **Visual State Mapping**: Every UI component MUST account for and implement all states: Loading, Empty, Success, Error, and Shimmer (using `Skeleton` or similar).
- **Accessibility (A11y)**: All code MUST be compliant with WCAG 2.1 AA standards. Use proper `Semantics` labels, ensure color contrast, and support keyboard/screen reader navigation.

## 3. Unidirectional Data Flow / UDF (The "One-Way Street" Principle)
- **Mandate**: All state MUST flow in one direction: **Model -> UI**. Events flow **UI -> Model**.
- **Riverpod 2.x**: Formalize logic in `AsyncNotifier` or `Notifier` to manage state predictably.
- **Reactive Mapping**: Every state change MUST be traceable through a central provider. This simplifies agent understanding of the codebase.

## 4. Widget Design
- Favor Composition over Inheritance.
- Use `const` whenever possible to optimize performance.
- Modularize UI components into small, reusable widgets (<150 lines per widget file).
- Never put business logic inside `build()` — extract to Notifiers or Services.

## 5. File & Naming Conventions
- Feature-driven structure: `lib/src/features/[feature_name]/`
  - `data/` — repositories, data sources, DTOs
  - `domain/` — models (Freezed), use cases
  - `presentation/` — widgets, providers, screens
- File names: `snake_case.dart`. Class names: `PascalCase`.
- Providers: `[featureName]Provider`, Notifiers: `[FeatureName]Notifier`.

## 6. Error Handling
- Use structured error handling (`AsyncValue.error`) in providers.
- Provide user-friendly error messages for common failure scenarios.
- Log critical errors with sufficient context for debugging.
- Never use empty `catch {}` blocks — at minimum, rethrow or log.

## 7. Performance Optimization
- **Speed Targets**: Target load times under 1.5 seconds and maintain consistent 60fps during transitions.
- Optimize build methods to avoid unnecessary rebuilds (`select()` over `watch()`).
- Use image caching (`cached_network_image`) for network assets.
- Use `ListView.builder` (never `ListView` with children) for dynamic lists.