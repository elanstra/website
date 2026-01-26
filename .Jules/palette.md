## 2024-05-22 - Focus Management in Vanilla JS SPAs
**Learning:** Vanilla JS updates via `innerHTML` destroy the DOM, causing focus loss. Explicit focus management is required to maintain context for assistive technology.
**Action:** Identify dynamic content updates and programmatically move focus to the new content container or heading, ensuring `tabindex="-1"` is applied.
