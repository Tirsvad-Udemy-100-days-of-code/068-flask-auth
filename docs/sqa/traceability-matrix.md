# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [4a5ddde] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | [RC-008] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-011] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006] | [RC-020] |
| [MIL-001] | MIL | en | it | [PP-001] | - | [RC-003] |
| [MIL-002] | MIL | en | it | [MIL-001] | - | [RC-004] |
| [MIL-003] | MIL | en | it | [MIL-002] | [MIL-004] | [RC-005] |
| [MIL-004] | MIL | en | it | [MIL-003], [BC-001] | [ADR-0001] | [RC-010] |
| [ADR-0001] | ADR | en | it | [MIL-004] | - | [RC-014] |
| [MIL-005] | MIL | en | it | [MIL-004] | [MIL-006] | [RC-016] |
| [MIL-006] | MIL | en | it | [MIL-005] | - | [RC-019] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [PP-001] | - | - | Covered |
| CN-002 | [MIL-002] | - | - | Covered |
| CN-003 | [MIL-003] | - | - | Covered |
| CN-004 | [MIL-001] | - | - | Covered |
| CN-005 | [MIL-001] | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| 1 | - | None found | - | Closed | - |

## Coverage Notes

Types with no instance yet have no row. `-` in Upstream means foundational, in Downstream that nothing is built on it yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-readme.md
[MIL-003]: ../milestones/mil-003-wiki.md
[MIL-004]: ../milestones/mil-004-flask-app.md
[ADR-0001]: ../adr/adr-0001-layered-structure-without-use-case-artifacts.md
[MIL-005]: ../milestones/mil-005-csrf-protection.md
[MIL-006]: ../milestones/mil-006-logout-post.md
[RC-001]: ./reviews/rc-001-bc.md
[RC-002]: ./reviews/rc-002-sa.md
[RC-003]: ./reviews/rc-003-mil-001.md
[RC-004]: ./reviews/rc-004-mil-002.md
[RC-005]: ./reviews/rc-005-mil-003.md
[RC-006]: ./reviews/rc-006-pp.md
[RC-008]: ./reviews/rc-008-bc.md
[RC-009]: ./reviews/rc-009-pp.md
[RC-010]: ./reviews/rc-010-mil-004.md
[RC-011]: ./reviews/rc-011-sa.md
[RC-014]: ./reviews/rc-014-adr-0001.md
[RC-016]: ./reviews/rc-016-mil-005.md
[RC-017]: ./reviews/rc-017-pp.md
[RC-019]: ./reviews/rc-019-mil-006.md
[RC-020]: ./reviews/rc-020-pp.md
[4a5ddde]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/4a5ddde2e1eacea3ee7b76655c4d51953e89c6fd
