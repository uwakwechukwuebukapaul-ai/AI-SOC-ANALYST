# Archive

Code moved out of the active app during the foundation cleanup (2026-07-31).
Nothing here is deleted — it's kept for reference and to avoid losing work.

- **web-refactor-wip/web/** — a parallel Flask-blueprint-style rebuild of the
  dashboard (routes/, templates/, static/). It was never wired up as the
  running app (the live entry point is `web_dashboard.py` at the repo root,
  per the README's own install instructions). It has some nice patterns
  (assign/status/note action routes) worth mining when we build out
  case actions on the live app — see PRODUCT_ROADMAP.md.
- **legacy/main.py** — original CLI-style entry point, superseded by
  `web_dashboard.py`.
- **legacy/backend/** — empty stub (`app.py` was 0 bytes), never used.
- **legacy/db-tools/** — one-off debug scripts (`incident_viewer.py`,
  `update_case.py`, `compare_db.py`, `add_evidence.py`) that pointed at
  `soc_incidents.db`, a stale database with only an `incidents` table.
  The live app uses `soc.db` (via `database/connection.py`), which has
  the full schema (cases, evidence, timeline, iocs, analyst_actions).
