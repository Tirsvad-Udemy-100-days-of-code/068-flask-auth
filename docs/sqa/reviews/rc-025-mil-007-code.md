# Review of MIL-007 source code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-025 |
| CrossReference | [MIL-007], [QC-PY-001], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the styling change in `src/flask_auth/` and `tests/` delivered under [MIL-007]
- Checklist used: [QC-PY-001]
- Scope: full checklist applied to the changed code (`bootstrap.py`, the five templates, `static/css/app.css`, `pyproject.toml`, `tests/`); the unchanged code keeps the result of [RC-015], [RC-018] and [RC-021]
- Language and domain: n/a (source code is not a PO-language artifact type)
- Language reviewer: none
- Mode: supervised (S01 asked for the styling in chat; the checklist was applied by the AI after the `python-developer` agent built it, and the tool results were re-run by the author)

## Tool evidence

Run in `.venv` (Python 3.13).

| Check | Result |
| --- | --- |
| `pytest` | 69 passed (the 62 existing tests plus 7 new in `tests/e2e/test_styling.py`) |
| `ruff check src tests` | All checks passed |
| `ruff format --check src tests` | 40 files already formatted |
| `mypy --strict src tests` | Success: no issues found in 40 source files |
| SRI hashes of Bootstrap 5.3.3 (CSS and bundle) | Recomputed from the files on jsDelivr; both match `base.html` |
| Browser pane check (criterion 8) | Home, register, login and secrets pages and a flash alert rendered with Bootstrap and the own CSS; no console errors, no failed asset requests; at 375 px no horizontal scroll and the navbar toggler opens; register, then logout through the navbar form, returned to the logged-out home page in a real browser |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | PEP 8 casing | Pass | |
| 2 | Names state purpose | Pass | `PATH_STYLESHEET`, `PATH_STATIC_DOWNLOAD`, `fetch_all_pages`. |
| 3 | Formatter and linter | Pass | Both clean. |
| 4 | Type annotations | Pass | `mypy --strict` clean. |
| 5 | No bare except | Pass | No try/except added. |
| 6 | No mutable defaults or shadowed builtins | Pass | |
| 7 | Context managers | Pass | Not affected. |
| 8 | Docstrings | Pass | New helper and tests carry docstrings. |
| 9 | Logging and secrets | Pass | No change. |
| 10 | Classes trace to a DCD; deviations recorded | Pass | No new class; layering stays in [ADR-0001]. |
| 11 | Tests | Pass | Tests for the stylesheet and script tags with SRI and `crossorigin`, the stylesheet served with 200, form classes and bound labels, the kept `csrf_token`, alerts with `role="alert"`, and that the download file is not served as a static file. |
| 12 | Strict type checker | Pass | Zero errors. |
| 13 | Dependencies pinned | Pass | No Python dependency change; Bootstrap is pinned to 5.3.3 with SRI. |
| 14 | One place per piece of knowledge | Pass | Paths come from `tests/support.py`. |
| 15 | Imports point inward | Pass | No import change. |
| 16 | SOLID | Pass | No logic added; only the Flask static settings changed. |
| 17 | Layered folders | Pass | Static files live under `presentation/static/`. |
| 18 | File and folder names | Pass | |

## Other points

- The Flask static folder is pinned to `presentation/static/css` so that `static/files/cheat_sheet.pdf` is not public; the download stays behind the login. `pyproject.toml` package-data includes `presentation/static/css/*`.
- Bootstrap comes from a CDN, as the lecture does; the pages need network access to look right (recorded in [MIL-007] Open Issues).
- OpenGrep was not run locally; CI runs it on the pull request (criterion 10 of [MIL-007]).

## Overall Verdict

Go — every Mandatory criterion of [QC-PY-001] passes. This closes criteria 1 to 9 of [MIL-007]; criterion 10 (opengrep) is checked in CI on the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Confirm opengrep reports no blocking finding in CI on the pull request | S01 | At the pull request |

---

[MIL-007]: ../../milestones/mil-007-styling.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[ADR-0001]: ../../adr/adr-0001-layered-structure-without-use-case-artifacts.md
[RC-015]: ./rc-015-mil-004-code-rereview.md
[RC-018]: ./rc-018-mil-005-code.md
[RC-021]: ./rc-021-mil-006-code.md
