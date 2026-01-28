## 2024-10-24 - Handling Focus in SPA-like HTML Updates
**Learning:** When using `innerHTML` to update the entire application state (SPA-like behavior in vanilla JS), keyboard focus is lost and resets to the `body` element. This disorients screen reader users and keyboard navigators.
**Action:** Always implement a manual focus management strategy. Add `tabindex="-1"` to the primary heading of the new view (e.g., `id="step-title"`) and programmatically set focus to it (`element.focus()`) immediately after rendering the new content.
