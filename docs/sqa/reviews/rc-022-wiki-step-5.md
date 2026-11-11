# Review of the wiki (Step 5 logout note)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-022 |
| CrossReference | [QC-WIKI-001], [MIL-006] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [1b75359] |

---

## Artifact Under Review

- Instance reviewed: the wiki in `docs/wiki/` (no ID; documentation, not an artifact)
- Checklist used: [QC-WIKI-001]
- Scope: change review of the three `Step-5-Authenticate-With-Flask-Login` pages (en, da, ms), which gain one paragraph about POST-only logout; the other pages are unchanged since [RC-012]
- Language and domain: n/a (a wiki is not a PO-language artifact type)
- Language reviewer: none
- Mode: supervised (S01 accepted the plan in chat; the checklist was applied by the AI)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md` | Pass | Unchanged. |
| 2 | The sidebar starts with the title in bold, then one English list, `Home` first | Pass | Unchanged. |
| 3 | The page list links every English page and no dead link | Pass | Unchanged; the change adds no link. |
| 4 | `**Related**` only when related wikis exist | Pass | None, no section. |
| 5 | `**Languages**` is the last sidebar section | Pass | Unchanged. |
| 6 | The sidebar does not repeat the page list per language | Pass | Unchanged. |
| 7 | A generated sidebar names its generator | N-A | The sidebar is not generated. |
| 8 | A `Languages` line on each page | Pass | Unchanged. |
| 9 | English plus the PO language | Pass | English, Danish and Bahasa Malaysia. |
| 10 | Page sets are identical across languages | Pass | 8 English pages each exist in da and ms; 25 files in total. |
| 11 | Every page starts with the language line | Pass | Unchanged. |
| 12 | Non-English pages are named `<Page>-<code>.md` | Pass | Unchanged. |
| 13 | Code blocks, commands, file names and IDs stay in English | Pass | The added paragraph keeps `/logout`, `GET`, `POST` and `CSRF` in English. |
| 14 | The change was checked on the published wiki after the merge | Open | Cannot be checked before the merge; the published pages are checked after it. |
| 15 | A layout change is made in the generator and the checklist | Pass | No layout rule changed. |
| 16 | The wiki folder is flat | Pass | All files directly in `docs/wiki/`. |

## Overall Verdict

Go once criterion 14 is closed: every other Mandatory criterion passes, and criterion 14 can be checked only on the published wiki after the merge. Criterion 7 is N-A because no generator produces the sidebar.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the three Step 5 pages on the published wiki after the merge and record criterion 14 | S01 | After the merge |

---

[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[MIL-006]: ../../milestones/mil-006-logout-post.md
[RC-012]: ./rc-012-wiki.md
[1b75359]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/1b753595bc9d59fa84a8cc23dcb5e2a2ce4dfc47
