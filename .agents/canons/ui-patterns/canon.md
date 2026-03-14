# UI Patterns Canon (Liquid Glass)

This canon defines the standard "Liquid Glass" premium UI aesthetic implementation.

## 1. The Material Stack Strategy
True glassmorphism requires three layers to avoid looking like a flat, dirty box:
- **Base Layer**: The underlying content (images, gradients, colorful scrolling lists) that provides light.
- **Blur Layer**: `BackdropFilter` with `ImageFilter.blur(sigmaX: 15, sigmaY: 15)` or higher.
- **Frosting Layer**: Semi-transparent surface tint (`Colors.white.withOpacity(0.05)` for dark mode, `0.2` for light mode).
- **Edge Highlight**: A 1px inside border using a `LinearGradient` (White opacity 0.3 top-left to Transparent bottom-right).

## 2. Design Tokens
Define all values centrally in a `ThemeExtension` or `AppStyle` class:
- `radius.small` (8px), `radius.medium` (16px), `radius.large` (24px)
- `spacing.p4` (4px) to `spacing.p32` (32px)
- `blur.subtle` (5 sigma), `blur.deep` (20 sigma + frost)

## 3. Typography
- **Code/Technical Surfaces**: `JetBrains Mono` or `Fira Code` for version numbers, IDs, code blocks.
- **Body/Display**: `Inter`, `Outfit`, or `SF Pro` for maximum legibility.
- Never let glass effects destroy text readability. If text sits on deep blur, ensure it has a slight `Shadow` or the glass tint is dark/light enough for contrast.

## 4. Micro-Interactions
- Add bounciness: Use `Curves.easeOutBack` or physics-based spring simulations for modal entrances and button presses.
- Touch feedback: `GestureDetector` that scales down the container slightly `Transform.scale(0.98)` on tap down, and returns to `1.0` on tap up/cancel.

## 5. Performance Limiters
- iOS renders blurs efficiently; older Android devices struggle.
- Consolidate blurs: Do not give every list item its own `BackdropFilter`. Instead, blur the app bar or bottom nav that sits *over* the scrolling list.
- Use `RepaintBoundary` around expensive blur stacks if they don't change often.