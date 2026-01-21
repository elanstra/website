## 2024-05-22 - Focus Management in SPA
**Learning:** Re-rendering entire DOM via innerHTML destroys focus, confusing screen reader users.
**Action:** When replacing content, programmatically move focus to the new main heading using tabindex="-1".
