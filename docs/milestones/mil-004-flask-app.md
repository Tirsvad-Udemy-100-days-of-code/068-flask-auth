# Milestone 4: Flask authentication app

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [MIL-003] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-010: Go | pending |

---

## Purpose

Decide whether the repository contains a working Flask application that implements lecture steps 1 to 7 (register, download, hashing and salting, Flask-Login, flash messages, authentication state in templates), with tests, so the README and wiki describe code that the repository itself holds.

## Deliverable

A Flask application under `src/flask_auth/` (application factory, SQLite `User` model, routes, templates, static file) and pytest tests under `tests/`. Dependencies are declared in `pyproject.toml`; the README Run and Tests sections are updated.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pytest` passes in a fresh `.venv` on Python 3.13 | All pass | Any failure |
| 2 | Register stores a salted `pbkdf2:sha256` hash and never the plain password | Test proves it | Plain text stored |
| 3 | `/secrets` and `/download` redirect an anonymous visitor to `/login` | Test proves it | Reachable |
| 4 | Login with a wrong password or unknown email shows a flash message | Test proves it | No message |
| 5 | The home page navbar differs between logged in and logged out | Test proves it | Identical |
| 6 | Registering an existing email redirects to `/login` with a flash message | Test proves it | Duplicate created |
| 7 | Source follows `coding-conventions` and `clean-architecture` (constants in `constants.py`, Doxygen comments) | Reviewed | Not followed |
| 8 | The README states the real run and test commands | Yes | No |
| 9 | opengrep reports 0 findings on the branch | 0 findings | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | The wiki and README describe the steps this application implements |
| [BC-001] amended and accepted | The Business Case currently places application code out of scope |

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
| 1 | Scaffold application and dependencies | Add `src/flask_auth/` with an application factory, `constants.py`, configuration and the SQLAlchemy `User` model; declare Flask, Flask-Login, Flask-SQLAlchemy and Werkzeug in `pyproject.toml`; add a pytest fixture with an in-memory database. | No | |
| 2 | Register and greet (step 1) | `/register` form creates a `User` and shows `secrets.html` greeting the user by name; templates `base`, `register`, `secrets`. | No | |
| 3 | Hash and salt passwords (steps 3 and 4) | Store `generate_password_hash(method="pbkdf2:sha256", salt_length=8)`; never the plain password; test that the stored value differs from the input and that two hashes of one password differ. | No | |
| 4 | Log in, log out, protect routes (step 5) | Flask-Login `LoginManager` and `user_loader`; `/login`, `/logout`; `@login_required` on `/secrets` and `/download`. | No | |
| 5 | Download a file (step 2) | `/download` returns `static/files/cheat_sheet.pdf` with `send_from_directory()` for logged-in users; a small own placeholder PDF is used, not course material. | No | |
| 6 | Flash messages (step 6) | Flash on unknown email, wrong password and already-registered email, and show them in the login template. | No | |
| 7 | Authentication status in templates (step 7) | Navbar shows Login and Register when logged out and Logout when logged in, using `current_user.is_authenticated`. | No | |
| 8 | Update README and review code | Replace the "documentation only" text with real Run and Tests instructions; review the code against `qc-programming-*`; run opengrep. | No | |

---

[BC-001]: ../business-case.md
[MIL-003]: ./mil-003-wiki.md
