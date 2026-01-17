## 2026-01-17 - Focus Management in Vanilla JS SPAs
**Learning:** When replacing `innerHTML` to update views, focus is lost to the body, confusing screen reader users.
**Action:** Always add `tabindex="-1"` to the new view's heading and programmatically `.focus()` it after rendering.
