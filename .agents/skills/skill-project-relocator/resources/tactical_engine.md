# Project Relocation Tactical Engine

## 🧹 Early Cleanup Actions
- Run `flutter clean` in source.
- Delete ephemeral/absolute-path folders:
  - `.dart_tool/`, `.idea/`, `build/`.
  - `ios/.symlinks/` (Highly sensitive).
  - `android/.gradle/` (Prevents daemon path mismatch across drives).
  - `windows/flutter/ephemeral/` (Clears Windows build artifacts).
  - `pubspec.lock` (Forces fresh path resolution for dependencies).

## 🔗 Path & Symlink Restoration
- Reconnect broken Junctions (Windows) or Symlinks (Unix).
- Run `flutter pub get` and `melos bootstrap` (if applicable).
- Reconnect links to global `.agents` foundation.

## ⚠️ Common Error Recovery
- **Broken Symlink**: Recreate using `mklink /j` (Win) or `ln -s` (Unix).
- **Invalid SDK Path**: Delete `ios/Flutter/Generated.xcconfig` -> `pub get`.
- **Package config missing**: Delete `.dart_tool` -> `pub get`.

---
*Preserved from Portable Brainvibing Infrastructure*