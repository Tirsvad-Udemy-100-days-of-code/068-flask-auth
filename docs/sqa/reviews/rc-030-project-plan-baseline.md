# Review Record: PP-001 against QC-PP-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-030 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial review record; verdict Go (autonomous, not independent) | [01f769b] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / education
- Language reviewer: none (the stand-in reads English and knows the education domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Planning Assumptions give the start date 2026-11-11, the plan end and the constraint; the baseline window 2026-11-16 to 2026-11-23 and the move of the end date from 2026-11-16 are recorded with their source. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | The Gateway Schedule lists the nine gateways once each with document, decision date and owner; every document exists, including MIL-009. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | The decision dates of MIL-001 to MIL-008 are the target dates of their milestone documents (checked one by one: 2026-11-12, 13, 16, 16, 16, 16, 16 and 16); MIL-009 decides on 2026-11-23, its Target Date; the Planning Assumptions record the move of the end date. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every In Scope item of BC-001 to a gateway; a row for the baseline item was added in this change (the earlier items were already mapped). |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Dependencies state the chain MIL-001 to MIL-009 and that MIL-009 follows MIL-008; it is acyclic and agrees with the order of the dates. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies state that a No-Go moves every later gateway by the rework time and may move the end date, which S01 decides; the baseline adds a CI risk that says S01 decides after three failed rounds. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner S01 is a stakeholder ID of SA-001. The project has no governance document, so there is no RACI to contradict; no invented role names are used. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Each planning assumption names its source (a Business Case section, the Stakeholder Analysis or a decision of S01); the move of the end date is recorded with its reason, the baseline of the framework. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks give impact and mitigation for each risk; the CI risk of MIL-009 traces to success criterion 6 of BC-001. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues list the earlier point and add the domain of the unchanged documents, the open pull request #53 that the baseline does not close, the prompt log, the missing workflow file, the missing checklist for the traceability matrix, the milestones that were already on the host and the secret-free repository; the Purpose no longer says the plan has no deadline, so no statement contradicts another. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | The main deliverable of MIL-009 names the same items as its Deliverable section; the rows of the eight earlier gateways keep their text except the milestone column. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | The Stories column says `none` and gives the kind of task for every gateway, because every task is a plain task (no user story artifact exists, see ADR-0001). |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | The Gantt bar of the baseline uses the dates of the schedule table. The bars of the earlier gateways were not changed here (this is an optional criterion). |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Each gateway links its milestone on the git host (431, 432, 433, 445, 448, 454, 455 and 456 for the eight earlier gateways; the column held `not yet synced` or plain text and now holds the link); the milestone of MIL-009 is linked after the sync. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | PP-001 is the only Project Plan; its Version History records each change in its own row and only the latest row is Accepted. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table has `Language | en` and `Domain | education`; neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `education` is a row of the domain list of docs/artifact-registry.md. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The prose and the table cells are English; only file names, commands and IDs are code. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives the register `IT Executive English` for this type; the text is written for that reader. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The project has no dictionary (DICT), so there are no PO terms to check against. The added text uses the terms of the existing documents (lecture, requirement, milestone, gateway, baseline, framework) in one meaning each, found by reading. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are the framework's English ones. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `<name>.<language>.md` exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | The `Domain` row changed from `it` to `education` in this version (the language `en` is unchanged). The Version History row records the change and this review covers it. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reads English and knows the education domain and checked the terms; the check is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations added by this change are spelled out where they are first used (SQA, QC, CI, PO, IT, CSRF) or are established names (README). |

## Overall Verdict

Go — every Mandatory criterion of QC-PP-001 and QC-LANG-001 passes; the domain of the unchanged documents, pull request #53, the prompt log, the missing workflow file, the missing checklist for the traceability matrix and the milestones that were already on the host are recorded as Open Issues. Review of the whole document after the edits of this change.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No open action | S01 | 2026-11-23 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[01f769b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/01f769b62ce2a651438d8817ad6d09d4241204a5
