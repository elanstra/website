## 2024-05-22 - [Manual Focus Management in Vanilla JS]
**Learning:** When using `innerHTML` to update content in a Single Page Application (SPA) style without a framework, keyboard focus is lost and reset to the body. This is disorienting for screen reader users.
**Action:** Always programmatically move focus to the new content container or heading after `innerHTML` updates. Use `tabindex="-1"` on the target element (like an `<h2>`) to make it focusable via JS but keep it out of the natural tab order. Pass a flag (e.g., `render(shouldFocus)`) to avoid stealing focus on initial page load.
