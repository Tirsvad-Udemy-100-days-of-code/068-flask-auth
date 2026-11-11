# Milestone 8: Lecture look

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-008 |
| CrossReference | [BC-001], [MIL-007] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-026: Go | [6bd7fad] |

---

## Purpose

Decide whether the application looks like the screenshots in the README and the wiki. [MIL-007] styled the pages with plain Bootstrap cards, but the screenshots come from the lecture's end project: a full-screen dark gradient background, a centred white page title, dark translucent inputs with placeholders, and gradient buttons. S01 chose to change the CSS to match the screenshots rather than retake them.

## Deliverable

A restyled `base.html`, templates and `static/css/app.css` that reproduce the look of the screenshots on the home, register, login and secrets pages and on a flash message, with the behaviour, the CSRF fields and the accessibility of [MIL-007] kept, and a browser comparison of each page with its screenshot.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The page background is the dark red-to-blue gradient of the screenshots, filling the viewport below a light navbar | Seen in the Browser pane next to the screenshot | Plain or light background |
| 2 | The page title and text are white and centred, in a sans-serif face that matches the screenshots (Open Sans where installed, else a system sans-serif) | Seen and recorded | Mismatch |
| 3 | Inputs are dark translucent with a light border and a placeholder, the primary button is the blue gradient and the secondary button the light gradient, both full width in a column of about 300 px | Seen and recorded | Mismatch |
| 4 | The home page shows the title "Flask Authentication" with the Login and Register buttons; the register and login pages show "Register" and "Login" with the labels `Name`, `Email`, `Password` as placeholders; the secrets page shows "Welcome, {name}!" with the download link | Test proves the texts | Text missing |
| 5 | Every input keeps a label bound by `for`/`id` (visually hidden, not removed) and the hidden `csrf_token` field | Test proves it | Label or token missing |
| 6 | Flash messages stay `role="alert"` and are readable on the gradient (white text, contrast of at least 4.5:1) | Test proves the markup; contrast checked in the Browser pane | Unreadable |
| 7 | The navbar keeps the logout POST form and shows Home, Login and Register when logged out and Home and Log Out when logged in; the brand reads "Flask Authentication" | Test proves it | Link or form missing |
| 8 | No third-party file is added: no new external host, and the font is not loaded from a font service | Test proves the stylesheet links | New host |
| 9 | Every behaviour covered by the existing 69 tests is unchanged; they all pass, with markup-matching tests adapted only where the text changed | All pass | Any failure |
| 10 | `pytest`, `ruff check`, `ruff format --check` and `mypy --strict` pass | All clean | Any failure |
| 11 | In the Browser pane, home, register, login, secrets and a flash message render without console errors or failed asset requests, and at 375 px width there is no horizontal scroll | Seen and recorded | Errors or overflow |
| 12 | The code passes `QC-PY-001` (review recorded) | Go | No-Go |
| 13 | opengrep reports 0 blocking findings in CI on the pull request | 0 blocking | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-007] | The Bootstrap base, the own stylesheet and the markup tests that this milestone restyles |

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
| 1 | Restyle the base layout | In `base.html` and `app.css` give the body the dark gradient, keep the light navbar with the brand "Flask Authentication", and add the white centred typography, the dark translucent input style and the two gradient button styles, all without loading anything from a new host. | No | |
| 2 | Restyle the pages | Change `index`, `register`, `login` and `secrets` to the screenshot layout: centred 300 px column, placeholders with visually hidden labels bound by `for`/`id`, the texts of criterion 4, the `csrf_token` fields kept, flash messages readable on the gradient. | No | |
| 3 | Adapt and add tests | Adapt the tests that match changed text, and add tests for the visually hidden bound labels, the placeholders, the kept `csrf_token` field, the navbar for both states and that no new host is linked. | No | |
| 4 | Compare in a browser, document and review | Compare every page with its screenshot in the Browser pane at desktop and 375 px width and record what was seen; run ruff, mypy and pytest; update the styling note in the README; review the code against `qc-programming-python.md` and record the `RC-*`. | No | |

## Open Issues

- Open Sans is not loaded from a font service, because that would add a third-party host that the visitor's browser contacts and that cannot carry a subresource integrity hash. On a machine without Open Sans the page falls back to a system sans-serif, so it looks close to the screenshots but not identical. S01 may choose to vendor the font files into `static/css/` (about 50 KB) before the milestone is accepted.
- The screenshots show the navbar entries Home, Login, Register and Log Out at once, because the lecture's navbar is static. The application shows the entries that fit the login state, as in [MIL-007]; the screenshots are not retaken.
- The Bootstrap files still come from the content delivery network (CDN) decided in [MIL-007], with the subresource integrity (SRI) hashes of that milestone.

---

[BC-001]: ../business-case.md
[MIL-007]: ./mil-007-styling.md
[6bd7fad]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/6bd7fadcb36f5ce0d1961bf10340d61ea7ca4c98
