# Milestone 7: Styling with Bootstrap

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-007 |
| CrossReference | [BC-001], [MIL-006] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-023: Go | pending |

---

## Purpose

Decide whether the pages look finished: the application has only bare HTML, and S01 asked for CSS and Bootstrap. The lecture's end project uses Bootstrap; this milestone gives the application a consistent, responsive look without changing its behaviour.

## Deliverable

Bootstrap 5 loaded in `base.html`, a small own stylesheet in `presentation/static/css/`, restyled pages (navbar, home, register, login, secrets) and flash messages shown as alerts, with tests that the markup and the assets are present, and a visual check of every page in a browser.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Every page extends `base.html`, which loads the Bootstrap stylesheet and script and the own stylesheet | Test proves it | A page without styles |
| 2 | Any Bootstrap file loaded from a third-party host carries a pinned version and an `integrity` (SRI) attribute with `crossorigin` | Test proves it | Missing |
| 3 | The own stylesheet is served by the application with status 200 | Test proves it | 404 |
| 4 | Forms use Bootstrap form classes, each input has a label bound by `for`/`id`, and the hidden `csrf_token` field is kept | Test proves it | Label or token missing |
| 5 | Flash messages render as Bootstrap alerts with `role="alert"` | Test proves it | Plain text |
| 6 | Every behaviour covered by the existing 62 tests is unchanged; they all pass | All pass | Any failure |
| 7 | `pytest`, `ruff check`, `ruff format --check` and `mypy --strict` pass | All clean | Any failure |
| 8 | In the Browser pane, the home, register, login and secrets pages (and a flash message) render without console errors or failed asset requests, and at 375 px width there is no horizontal scroll | Seen and recorded | Errors or overflow |
| 9 | The code passes `QC-PY-001` (review recorded) | Go | No-Go |
| 10 | opengrep reports 0 blocking findings in CI on the pull request | 0 blocking | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-006] | The navbar logout form that the new navbar must keep |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 6 (working application) | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-16 — inside the project end date in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Load Bootstrap and the own stylesheet | In `base.html` load Bootstrap 5 (pinned version, SRI hash and `crossorigin` for the stylesheet and the script bundle) and `static/css/app.css` through `url_for('static', ...)`; build a responsive navbar that keeps the logout form with its CSRF token. | No | |
| 2 | Restyle the pages | Style `index`, `register`, `login` and `secrets` with Bootstrap components (container, card, form controls with bound labels, buttons); show flash messages as `alert` components with `role="alert"`. | No | |
| 3 | Test the markup and the assets | Add tests for the stylesheet and script tags with SRI, the own stylesheet served with 200, form classes and labels, the alert markup and the kept `csrf_token` field; adapt existing tests only where markup they matched changed. | No | |
| 4 | Check in a browser, document and review | Look at every page in the Browser pane at desktop and 375 px width and record what was seen; add a short styling note to the README; run ruff, mypy and pytest; review the code against `qc-programming-python.md` and record the `RC-*`. | No | |

## Open Issues

- Bootstrap is loaded from a CDN, as in the lecture, so the pages need network access to style correctly and the visitor's browser contacts that host. Vendoring the files into `static/` would remove the dependency at the cost of about 230 KB of third-party files in the repository; S01 may choose that instead before the milestone is accepted.
- The screenshots in the README and wiki come from the lecture's end project and are not retaken.

---

[BC-001]: ../business-case.md
[MIL-006]: ./mil-006-logout-post.md
