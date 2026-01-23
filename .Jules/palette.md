# Palette's Journal

Critical learnings and UX insights.

## 2024-10-12 - Managing Focus in Single-Page Apps with innerHTML
**Learning:** When replacing content dynamically using `innerHTML`, the keyboard focus is lost, which disorients screen reader users. The application feels "broken" or unresponsive to them as they are not informed of the content change.
**Action:** Identify the primary heading of the new state, add `tabindex="-1"`, and programmatically set focus to it immediately after the DOM update to ensure a smooth, accessible transition.
