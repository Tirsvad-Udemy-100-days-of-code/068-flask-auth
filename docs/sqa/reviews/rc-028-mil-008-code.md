# Review of MIL-008 source code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-028 |
| CrossReference | [MIL-008], [QC-PY-001], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the restyle to the lecture look in `src/flask_auth/` and `tests/` delivered under [MIL-008]
- Checklist used: [QC-PY-001]
- Scope: full checklist applied to the changed code (the five templates, `static/css/app.css`, `tests/support.py`, `tests/e2e/test_styling.py`); the unchanged code keeps the result of [RC-015], [RC-018], [RC-021] and [RC-025]
- Language and domain: n/a (source code is not a PO-language artifact type)
- Language reviewer: none
- Mode: supervised (S01 chose the restyle and accepted the plan in chat; the checklist was applied by the AI after the `python-developer` agent built it, and the tool results were re-run by the author)

## Tool evidence

Run in `.venv` (Python 3.13).

| Check | Result |
| --- | --- |
| `pytest` | 74 passed (the 69 existing tests plus 5 new in `tests/e2e/test_styling.py`) |
| `ruff check src tests` | All checks passed |
| `ruff format --check src tests` | 40 files already formatted |
| `mypy --strict src tests` | Success: no issues found in 40 source files |
| Bootstrap tags | Unchanged; SRI hashes as verified in [RC-025] |
| Browser pane comparison (criteria 1 to 3, 11) | Home, register, login (with a flash message) and secrets pages compared with the screenshots: dark gradient, centred column, dark inputs with placeholders, blue and light gradient buttons all match; the font is the Open Sans stack with a system fallback (the check machine has no Open Sans, so letterforms differ slightly, as the milestone's Open Issues say); flash text is white on the gradient; no console errors; at 375 px no horizontal scroll (home and secrets measured, login and register use the same column); register, login failure and secrets worked with the CSRF fields in a real browser |

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
| 11 | Tests | Pass | Tests for the visually hidden bound labels, placeholders, `csrf_token`, the navbar in both login states with the brand text, the page headings and actions, and that every link and script is relative or on `cdn.jsdelivr.net`. |
| 12 | Strict type checker | Pass | Zero errors. |
| 13 | Dependencies pinned | Pass | No dependency change; no new external host. |
| 14 | One place per piece of knowledge | Pass | Paths come from `tests/support.py`. |
| 15 | Imports point inward | Pass | No import change. |
| 16 | SOLID | Pass | No logic changed; only templates, CSS and tests. |
| 17 | Layered folders | Pass | Templates and CSS stay under `presentation/`. |
| 18 | File and folder names | Pass | |

## Other points

- The flash message class changed from `alert-warning` to `flash-message` (white text, no box); the markup keeps `class="alert ..."` and `role="alert"`.
- The "Your file is ready." line was removed from the secrets page to match the screenshot.
- OpenGrep was not run locally; CI runs it on the pull request (criterion 13 of [MIL-008]).

## Overall Verdict

Go — every Mandatory criterion of [QC-PY-001] passes. This closes criteria 1 to 12 of [MIL-008]; criterion 13 (opengrep) is checked in CI on the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Confirm opengrep reports no blocking finding in CI on the pull request | S01 | At the pull request |

---

[MIL-008]: ../../milestones/mil-008-lecture-look.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[ADR-0001]: ../../adr/adr-0001-layered-structure-without-use-case-artifacts.md
[RC-015]: ./rc-015-mil-004-code-rereview.md
[RC-018]: ./rc-018-mil-005-code.md
[RC-021]: ./rc-021-mil-006-code.md
[RC-025]: ./rc-025-mil-007-code.md
