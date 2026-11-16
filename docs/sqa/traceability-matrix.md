# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-009] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [4a5ddde] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the row for MIL-009, the row for the wiki and the review records of the baseline; set the domain of BC-001 and PP-001 to education; added MIL-009 to the downstream links | pending |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | education | - | [SA-001], [PP-001], [MIL-009] | [RC-029] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-011] |
| [PP-001] | PP | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [MIL-006], [MIL-007], [MIL-008], [MIL-009] | [RC-030] |
| [MIL-001] | MIL | en | it | [PP-001] | - | [RC-003] |
| [MIL-002] | MIL | en | it | [MIL-001] | - | [RC-004] |
| [MIL-003] | MIL | en | it | [MIL-002] | [MIL-004] | [RC-005] |
| [MIL-004] | MIL | en | it | [MIL-003], [BC-001] | [ADR-0001] | [RC-010] |
| [ADR-0001] | ADR | en | it | [MIL-004] | - | [RC-014] |
| [MIL-005] | MIL | en | it | [MIL-004] | [MIL-006] | [RC-016] |
| [MIL-006] | MIL | en | it | [MIL-005] | [MIL-007] | [RC-019] |
| [MIL-007] | MIL | en | it | [MIL-006] | [MIL-008] | [RC-023] |
| [MIL-008] | MIL | en | it | [MIL-007] | [MIL-009] | [RC-026] |
| [MIL-009] | MIL | en | education | [MIL-008], [BC-001], [PP-001] | - | [RC-031] |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-003] | - | [RC-032], [RC-022], [RC-012], [RC-007] |

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

Types with no instance yet have no row. `-` in Upstream means foundational, in Downstream that nothing is built on it yet. The domain of BC-001, PP-001 and MIL-009 is `education` since MIL-009; the other documents keep the domain `it` they were accepted with (see the Open Issues of PP-001). The wiki row shows the domain of the project (a wiki is not an artifact with a `Domain` row). MIL-009 adds its row and the wiki row and changes no source, test, image or wiki file. The framework has no quality checklist for this matrix, so it has no review record of its own. The review records RC-029, RC-030, RC-031 and RC-032 are not rows themselves.

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
[MIL-007]: ../milestones/mil-007-styling.md
[MIL-008]: ../milestones/mil-008-lecture-look.md
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
[RC-023]: ./reviews/rc-023-mil-007.md
[RC-026]: ./reviews/rc-026-mil-008.md
[RC-027]: ./reviews/rc-027-pp.md
[RC-024]: ./reviews/rc-024-pp.md
[4a5ddde]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/4a5ddde2e1eacea3ee7b76655c4d51953e89c6fd
[MIL-009]: ../milestones/mil-009-framework-baseline.md
[RC-007]: ./reviews/rc-007-wiki.md
[RC-012]: ./reviews/rc-012-wiki.md
[RC-022]: ./reviews/rc-022-wiki-step-5.md
[RC-029]: ./reviews/rc-029-business-case-baseline.md
[RC-030]: ./reviews/rc-030-project-plan-baseline.md
[RC-031]: ./reviews/rc-031-milestone-009.md
[RC-032]: ./reviews/rc-032-wiki-baseline.md
