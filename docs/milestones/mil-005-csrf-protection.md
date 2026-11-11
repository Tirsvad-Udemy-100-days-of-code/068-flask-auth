# Milestone 5: CSRF protection

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [MIL-004] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-016: Go | pending |

---

## Purpose

Decide whether the register and login forms are protected against cross-site request forgery (CSRF), so a third-party page cannot submit them on behalf of a visitor. The lecture's end project has no such protection; the OpenGrep scan flagged the forms (CI run of pull request 30), and S01 asked for it.

## Deliverable

Flask-WTF `CSRFProtect` enabled in the application, a CSRF token in the register and login forms, and tests that show a POST without a valid token is refused. The README states the protection.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `POST /register` and `POST /login` without a CSRF token return 400 and change nothing | Test proves it | Accepted |
| 2 | `POST /register` and `POST /login` with the token from the form behave as before | Test proves it | Broken |
| 3 | The register and login pages contain a hidden `csrf_token` field | Test proves it | Missing |
| 4 | The 48 existing tests still pass, adapted to send the token | All pass | Any failure |
| 5 | `pytest`, `ruff check`, `ruff format --check` and `mypy --strict` pass | All clean | Any failure |
| 6 | The new dependency is pinned in `pyproject.toml` and the layering of [ADR-0001] holds (no Flask-WTF import in `domain` or `application`) | Yes | No |
| 7 | The code passes `QC-PY-001` (re-review recorded) | Go | No-Go |
| 8 | opengrep reports 0 blocking findings in CI on the pull request | 0 blocking | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] | The application whose forms are protected |

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
| 1 | Enable CSRF protection | Add a pinned Flask-WTF dependency and enable `CSRFProtect` in the composition root (`bootstrap.py`) and the infrastructure extensions; keep Flask-WTF out of `domain` and `application`. A request without a valid token to a POST route returns 400. | No | |
| 2 | Add the token to the forms | Add a hidden `csrf_token` field to `register.html` and `login.html`. | No | |
| 3 | Test the protection | Adapt the e2e tests to fetch the token from the form and send it; add tests for a missing token, a wrong token and the hidden field; keep CSRF enabled in the test configuration. | No | |
| 4 | Document and review | State the protection in the README, run ruff, mypy and pytest, review the code against `qc-programming-python.md` and record the `RC-*`. | No | |

## Open Issues

- `GET /logout` ends the session, as in the lecture. A GET that changes state can still be triggered cross-site; changing it to POST alters the lecture's behaviour and is left to S01 to decide, outside this milestone.

---

[BC-001]: ../business-case.md
[MIL-004]: ./mil-004-flask-app.md
[ADR-0001]: ../adr/adr-0001-layered-structure-without-use-case-artifacts.md
