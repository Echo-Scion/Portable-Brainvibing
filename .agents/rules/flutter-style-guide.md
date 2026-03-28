---
trigger: glob
description: Dart and Flutter style guide, formatting, and naming conventions.
globs: *.dart
---

# Dart & Flutter Style Guide

## 1. Formatting & Linting
- Use `flutter format .` regularly.
- Follow `package:flutter_lints` or `package:very_good_analysis`.
- Avoid `relative` imports; use `package:` imports.

## 2. Naming Conventions
- `UpperCamelCase` for classes, enums, typedefs.
- `lowerCamelCase` for variables, properties, functions.
- `snake_case` for filenames and directory names.

## 3. Widget Architecture
- Keep build methods small and clean.
- Prefer `StatelessWidget` when possible.
- Use `const` constructors for performance.

## 4. State Management (Riverpod)
- Use `Provider` for constants.
- Use `AsyncNotifier` or `Notifier` for mutable state.
- Keep logic in Notifier classes, not UI.

## 5. Async Handling
- Use `await` instead of `.then()` for readability.
- Handle errors using `try-catch` or `AsyncValue.when`.
- Use `Future.wait` for parallel independent requests.