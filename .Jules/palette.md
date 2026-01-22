## 2024-05-23 - Focus Management in Single Page Apps
**Learning:** Interactive elements that use `innerHTML` updates destroy the active element, resetting focus to the body. This disorients keyboard and screen reader users.
**Action:** When replacing large DOM sections, manually manage focus by adding `tabindex="-1"` to the new container/heading and calling `.focus()` immediately after rendering.
