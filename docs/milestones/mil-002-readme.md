# Milestone 2: README

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Reviewed in RC-004: Go | [4a5ddde] |

---

## Purpose

Decide whether the README explains the Day 68 lecture to a newcomer: every lecture step with its screenshot, and how to set up and run a local `.venv`.

## Deliverable

`README.md` built from the framework template, and the step screenshots under `docs/images/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The README follows the framework template and `check-readme.sh` passes | Passes | Fails |
| 2 | Each of the 7 lecture steps has a heading, a short explanation and a screenshot | 7 of 7 | Fewer |
| 3 | The README documents creating and using `.venv` and `python -m pip install --upgrade pip` | Present | Missing |
| 4 | The README says how to run the tests and states that the project has no runtime dependencies | Present | Missing |
| 5 | Screenshots show test data only and no credentials | Yes | No |
| 6 | opengrep reports 0 findings on the branch | 0 findings | Findings |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Configuration and repository metadata the README refers to |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-13 — inside the short, documentation-only schedule in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture lecture step screenshots | Download the course resource archive into its own empty directory, run it only inside a Docker container with test data, and capture one screenshot per lecture step with the built-in browser. Stop and report if the signed archive link has expired. Browser work stays off the host desktop, as the framework requires. | No | |
| 2 | Write README lecture walkthrough | Write the README from the framework template: the 7 steps (register and greet, download, encryption and hashing theory, hashing and salting with Werkzeug, Flask-Login, flash messages, authentication status in templates), each with its screenshot. | No | |
| 3 | Document venv, run and tests | Add Requirements, Setup, Run and Tests sections: create `.venv`, upgrade pip with `python -m pip install --upgrade pip`, run pytest, and state that there are no runtime dependencies. Serves S02. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-project-setup.md
[4a5ddde]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/4a5ddde2e1eacea3ee7b76655c4d51953e89c6fd
