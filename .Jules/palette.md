## 2024-05-22 - Focus Management in Vanilla JS SPAs
**Learning:** Interactive elements that use `innerHTML` updates destroy the DOM and focus state, necessitating manual focus management to maintain accessibility.
**Action:** Always add `tabindex="-1"` to the new content's primary heading (conventionally `id="step-title"`) and programmatically set focus to it after rendering updates, but be careful not to steal focus on initial page load.
