# Project Plan

## Metadata
| Key | Value |
| --- | --- |
| ID | PP-001 |
| CrossReference | [BC-001], [SA-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Reviewed in RC-006: Go | [4a5ddde] |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Add MIL-004 Flask application<br>Reviewed in RC-009: Go | pending |

---

## Purpose

Schedule the three phases that turn the Day 68 lecture into a README, a three-language wiki and a working Flask application. The plan has no fixed deadline in the Business Case; it keeps a short, documentation-only schedule.

## Planning Assumptions

- The plan starts 2026-11-11 and ends by 2026-11-16, the duration constraint in [BC-001] (Constraints).
- Each phase is one branch and one pull request that closes its issues (source: the request of S01).
- S01 owns and reviews every phase; in autonomous mode the AI acts as stand-in reviewer and records it (source: AGENTS.md, Modes).

## Gateway Schedule

| Gateway | Document | Window | Decision date | Owner | Stories | Main deliverable | Milestone |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project setup | [MIL-001] | 2026-11-11 to 2026-11-12 | 2026-11-12 | S01 | none (documentation tasks) | Repository metadata and configuration | not yet synced |
| README | [MIL-002] | 2026-11-12 to 2026-11-13 | 2026-11-13 | S01 | none (documentation tasks) | README with step screenshots | not yet synced |
| Wiki | [MIL-003] | 2026-11-13 to 2026-11-16 | 2026-11-16 | S01 | none (documentation tasks) | Wiki in en, da, ms | not yet synced |
| Flask app | [MIL-004] | 2026-11-12 to 2026-11-16 | 2026-11-16 | S01 | none (technical tasks) | Flask application with tests | not yet synced |

```plantuml
@startgantt
Project starts 2026-11-11
[Project setup] starts 2026-11-11 and ends 2026-11-12
[README] starts 2026-11-12 and ends 2026-11-13
[Wiki] starts 2026-11-13 and ends 2026-11-16
[Setup Go/No-Go] happens 2026-11-12
[README Go/No-Go] happens 2026-11-13
[Wiki Go/No-Go] happens 2026-11-16
[Flask app] starts 2026-11-12 and ends 2026-11-16
[Flask app Go/No-Go] happens 2026-11-16
@endgantt
```

## Scope Coverage

| Business Case scope item | Gateway |
| --- | --- |
| Repository description and topics; `pyproject.toml`, `.gitignore`, `Doxyfile` | [MIL-001] |
| README, screenshots, `.venv` instructions | [MIL-002] |
| Wiki in three languages | [MIL-003] |
| Flask application and tests | [MIL-004] |
| opengrep scan before push | All gateways |

## Dependencies

```
MIL-001 → MIL-002 → MIL-003
MIL-003 → MIL-004
```

A No-Go on a gateway moves every later gateway by the rework time and may move the end date of 2026-11-16; S01 decides any move of the end date.

## Plan Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The signed course archive link has expired (BC-001 risk 1) | Screenshots are blocked | Stop and report per the autonomous stop rules; S01 supplies the archive |
| Docker image build for the end project fails | Screenshots delayed | Fix on the same branch; stop after three failed rounds |

## Open Issues

- The course archive link in the request carries an expiry; its validity is checked in MIL-002 task 1.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[MIL-001]: ./milestones/mil-001-project-setup.md
[MIL-002]: ./milestones/mil-002-readme.md
[MIL-003]: ./milestones/mil-003-wiki.md
[MIL-004]: ./milestones/mil-004-flask-app.md
[4a5ddde]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/4a5ddde2e1eacea3ee7b76655c4d51953e89c6fd
