## 2024-10-24 - Focus Management in DOM Replacements
**Learning:** Interactive elements that use `innerHTML` updates (like the Pizza Picker) destroy the currently focused element, causing focus to revert to the `body`. This disorients keyboard and screen reader users.
**Action:** Implement manual focus management: add `tabindex="-1"` to the new content's primary heading (conventionally `id="step-title"`) and programmatically set focus to it immediately after rendering.
