## 2026-01-29 - Focus Management in SPA-like Interactions
**Learning:** Updating content via `innerHTML` destroys the currently focused element, resetting focus to `body`. This disorients screen reader users who lose their place.
**Action:** When replacing substantial content, programmatically move focus to a relevant heading (e.g., `id="step-title"`) that has `tabindex="-1"` and `outline-none`.
