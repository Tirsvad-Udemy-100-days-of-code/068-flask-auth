# Milestone 6: Log out with POST

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-006 |
| CrossReference | [BC-001], [MIL-005] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-019: Go | pending |

---

## Purpose

Decide whether logging out is a protected POST instead of a GET. The lecture ends the session with `GET /logout`; a GET that changes state can be triggered from another site, for example by an image tag, and the CSRF protection of [MIL-005] cannot cover it. S01 asked for the change, which deliberately departs from the lecture's behaviour.

## Deliverable

`/logout` accepts POST only and is protected by the CSRF token; the navbar "Log Out" entry is a small form with a token and a button; tests, README and the Step 5 wiki pages describe the new behaviour.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `GET /logout` returns 405 and does not end the session | Test proves it | Session ended |
| 2 | `POST /logout` with a valid CSRF token ends the session and redirects to the home page | Test proves it | Not logged out |
| 3 | `POST /logout` without a valid token returns 400 and does not end the session | Test proves it | Logged out |
| 4 | The navbar of a logged-in user contains a form that posts to `/logout` with a hidden `csrf_token` field, and no link to `/logout` | Test proves it | Link remains |
| 5 | All existing tests still pass, adapted where they used `GET /logout` | All pass | Any failure |
| 6 | `pytest`, `ruff check`, `ruff format --check` and `mypy --strict` pass | All clean | Any failure |
| 7 | The code passes `QC-PY-001` (review recorded) | Go | No-Go |
| 8 | The README and the three Step 5 wiki pages say that logout is a POST and name the departure from the lecture; the wiki passes `QC-WIKI-001` | Yes | No |
| 9 | opengrep reports 0 blocking findings in CI on the pull request | 0 blocking | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-005] | The CSRF protection that this route relies on |

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
| 1 | Make logout a POST route | Register `/logout` with `methods=["POST"]` only; the CSRF protection of [MIL-005] covers it; the response redirects to the home page as before. | No | |
| 2 | Replace the navbar link with a form | In `base.html` replace the "Log Out" link with a form that posts to `/logout` with a hidden `csrf_token` field and a button. | No | |
| 3 | Test the new behaviour | Adapt the tests that used `GET /logout`; add tests for 405 on GET, 400 without a token, success with a token, and the navbar form. | No | |
| 4 | Update the documents and review | Update the README, the Step 5 wiki pages in English, Danish and Bahasa Malaysia, and the Home code table if needed; run ruff, mypy and pytest; record the code review and the wiki review. | No | |

## Open Issues

- None.

---

[BC-001]: ../business-case.md
[MIL-005]: ./mil-005-csrf-protection.md
