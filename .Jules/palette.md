## 2024-05-22 - SPA Focus Management in Vanilla JS
**Learning:** Interactive elements using `innerHTML` updates require manual focus management to maintain accessibility. Without it, focus resets to the body, confusing screen reader and keyboard users.
**Action:** Always add `tabindex="-1"` to the new content's primary heading (e.g., `id="step-title"`) and programmatically set focus to it after rendering.
