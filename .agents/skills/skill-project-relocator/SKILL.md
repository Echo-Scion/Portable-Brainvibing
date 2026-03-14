---
name: skill-project-relocator
description: Specialist in safely moving projects, particularly Flutter/Dart, with a focus on path integrity and deep cache clearing.
version: "1.0.0"
last_updated: "2026-03-14"
compatibility: Flutter/Dart (Windows/Unix)
Recommended_Tier: Budget
---

# Skill: Project Relocator (`@skill-project-relocator`)

Specialist in safely moving projects, especially Flutter/Dart, focusing on path integrity and thorough cache cleanup.

## <instructions>
Use this skill when asked to move a project or to diagnose errors after a project has been relocated.

### 1. EARLY CLEANUP
- **Action**: Run `flutter clean` in the source directory before performing the `move/copy` operation.
- **Action**: Use OS commands to delete folders that often cause issues:
  - `.dart_tool/`
  - `.idea/` (If it contains `workspace.xml` with absolute paths)
  - `build/`
  - `ios/.symlinks/` (Highly sensitive as it stores absolute paths to the Flutter SDK)
  - `pubspec.lock` (Optional, but helps regenerate dependency paths)

### 2. PATH & SYMLINK DETECTION
- **Check**: Look for `path` dependencies in `pubspec.yaml`. Calculate if those relative paths will still be valid in the new location.
- **Check**: Identify if the local `.agents/` folder is a Junction (Windows) or Symlink (Unix) to another location.
- **Report**: Notify the user if any dependencies might "break" after the relocation.

### 3. RESTORATION (Post-Move)
- **Action**: Reconnect broken symlinks (especially links to the global `.agents` foundation).
- **Action**: Run `flutter pub get` automatically after the files are moved.
- **Action**: Detect Melos usage (`melos.yaml`) and run `melos bootstrap` if necessary.

### 4. HANDLING COMMON ERRORS
- **Error "Broken Symlink"**: Delete the old symlink and recreate it using `mklink /j` (Windows) or `ln -s` (Unix).
- **Error "Invalid Flutter SDK Path"**: Usually in `ios/Flutter/Generated.xcconfig`. Solution: Delete the file and run `flutter pub get`.
- **Error "Package config not found"**: Delete `.dart_tool` and run `flutter pub get`.
</instructions>

## <available_resources>
- **Script**: `.agents/scripts/verify_agents.py` (Use to check the integrity of .agents links)
- **Tool**: `flutter clean`, `flutter pub get`, `melos bootstrap`
- **Shell**: `mklink /j` for directory links on Windows.
</available_resources>