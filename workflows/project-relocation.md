---
description: Safe guide for moving projects (especially Flutter) to a new directory without path or cache errors.
---

# Workflow: Project Relocation (`/project-relocate`)

This workflow ensures the project is moved cleanly, handling relative dependencies, `.agents` symlinks, and Flutter/Dart caches that often cause errors after relocation.

## 0. PRE-FLIGHT CHECK
- [ ] Ensure no Flutter/Dart processes are running (Editor, Debugger, or Simulator).
- [ ] Identify the source directory (`SOURCE`) and the destination directory (`DEST`).
- [ ] Activate the `@skill-project-relocator` skill for automated cleanup.

---

## 1. CLEANUP (Source)
This step is crucial for Flutter to prevent bringing locked caches or absolute paths in build artifacts.
- [ ] Run `flutter clean` in the source directory.
- [ ] Manually delete the `.dart_tool/` folder if it still exists.
- [ ] Delete `pubspec.lock` (Optional, but recommended when moving between environments).
- [ ] Delete IDE folders: `.idea/` or `.vscode/` if they contain absolute paths (usually in `workspace.xml`).

---

## 2. ANALYSIS & PREPARATION
- [ ] Check `pubspec.yaml` for relative path dependencies (e.g., `path: ../packages/core`).
- [ ] If this is a Sub-project connected to the global `.agents` foundation via symlink (Junction), record the list of those symlinks.
- [ ] If this is a Melos monorepo, check `melos.yaml` for scope configuration.

---

## 3. EXECUTION (The Move)
- [ ] Move (or Copy then Delete) all folder contents to the new destination directory.
- [ ] **IMPORTANT**: Do not move the `build/`, `ios/.symlinks/`, or `android/.gradle/` folders if possible (let them be regenerated).

---

## 4. RE-LINKING & RE-CONFIG (Destination)
- [ ] If using the `.agents` Sub-project system:
  - Delete old broken symlinks in the new directory.
  - Re-run the `mklink /j` command to connect `.agents/skills`, `.agents/rules`, and `.agents/workflows` to the global foundation.
- [ ] Update `pubspec.yaml` if any relative paths have changed (e.g., folder level shift).

---

## 5. INITIALIZATION (Destination)
- [ ] Run `flutter pub get` in the new directory.
- [ ] If using Melos: Run `melos bootstrap`.
- [ ] Run `flutter pub run build_runner build --delete-conflicting-outputs` (if using code generation).

---

## 6. VALIDATION
- [ ] Run `flutter analyze` to ensure no import errors.
- [ ] Attempt to run the application (Emulator/Simulator) or run `flutter test`.

---

> [!TIP]
> "Pub get failed" errors after moving folders are usually caused by `.dart_tool/package_config.json` still storing old paths. Deleting the `.dart_tool` folder before `pub get` is the most effective solution.