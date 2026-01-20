## 2024-05-22 - Single Page App Focus Management
**Learning:** `dominos.html` re-renders the entire `#app` innerHTML on state changes, destroying the currently focused element. This causes focus loss for screen reader/keyboard users.
**Action:** Future interactive improvements must implement manual focus management (e.g., `element.focus()`) after render cycles.
