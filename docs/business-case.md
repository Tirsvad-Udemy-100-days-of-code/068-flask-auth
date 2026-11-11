# Business Case: Flask Auth (Day 68)

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Reviewed in RC-001: Go | pending |

---

## Executive Summary

Day 68 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" teaches user authentication in Flask: registering users, hashing and salting passwords, logging in with Flask-Login, flash messages and template-level authentication state. This project turns that lecture into a public learning reference: a README and a three-language wiki (English, Danish, Bahasa Malaysia) that explain each lecture step with a screenshot and say what was learned. No application code is delivered; the project holds documentation and project configuration only.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/` (plan first, review every artifact against its QC checklist, record each review as an `RC-*`). Quality attributes follow ISO/IEC 25010:2023. Documentation follows the framework's README template and wiki process (`framework/process/wiki.md`).

## Problem Statement

A course participant's notes on a lecture are scattered and lose value once the course is finished. Other course participants and GitHub readers who look for a worked example of Flask authentication find code without explanation, or explanation without the visual result of each step.

## Business Opportunity

A single repository can show what each lecture step produces (a screenshot) and what it teaches (a short explanation), in English and in two further languages, so the lecture can be revisited and shared.

## Objectives

1. Publish a README that walks through every Day 68 lecture step with a screenshot and instructions to set up a local `.venv`.
2. Publish a wiki in English, Danish and Bahasa Malaysia that explains what each step teaches.
3. Describe the repository on the git host with a description and topics.
4. Provide project configuration (`pyproject.toml`, Python `.gitignore`, `Doxyfile`) that a later coding phase can use unchanged.
5. Keep a traceable history: one branch and pull request per milestone.

## Scope

### In Scope

- README (framework template) for the Day 68 lecture steps, with screenshots.
- Wiki pages in `docs/wiki/` in English, Danish (`-da`) and Bahasa Malaysia (`-ms`), with screenshots and "what we gained" sections.
- Screenshots of each lecture step, captured from the lecture's end project run in a Docker container.
- Repository description and topics on the git host.
- `pyproject.toml` (Python 3.13 or newer, pytest), Python `.gitignore`, `Doxyfile`, documented `.venv` setup with `python -m pip install --upgrade pip`.
- A local opengrep scan before each push.

### Out of Scope

- Writing application source code or tests under `src/` and `tests/` (the folders are reserved for a later phase).
- Reproducing the lecture's video or course material beyond short descriptions and own screenshots.
- Publishing the course resource archive in the repository.

## Expected Benefits

### Tangible Benefits

- A README and a three-language wiki that a reader can follow without watching the lecture.
- One screenshot per lecture step as visual evidence.

### Intangible Benefits

- Consolidated learning of authentication, hashing and salting.
- A repository other participants can compare their solutions with.

## Strategic Alignment

The project supports the participant's learning goal in the bootcamp and the practice of the SQA and QC framework on a small, complete project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Lecture steps covered | All 7 steps in README and wiki | Count of steps with text and screenshot |
| 2 | Wiki languages | 3 (en, da, ms) with the same page set | `check-languages.sh` and page list |
| 3 | Repository metadata | Description and at least 5 topics set | Host API response |
| 4 | Review | Every artifact `Accepted` with a `Go` review | `RC-*` records |
| 5 | Security scan | 0 opengrep findings before each push | opengrep output |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The course resource link has expired | Screenshots cannot be captured from the end project | Stop and report; the user supplies the archive or chooses another source |
| The downloaded archive is untrusted | Malicious code runs | Extract into its own directory and run only inside a Docker container |
| A token leaks into the repository | Credential exposure | Tokens are read from `.env` outside the repository, never printed, never committed |
| Translations drift from English | Inconsistent wiki | English is authoritative; same page set; `check-languages.sh` |
| Screenshots show personal data | Privacy loss | Use test data only |

## Assumptions

- S01 is Product Owner, developer and reviewer.
- The Product Owner domain language is English, domain IT.
- The git host wiki is enabled and the organisation holds `TOKEN_FOR_GITEA_WIKI`.
- Docker is available on the host.

## Constraints

- Duration: the whole project is complete by 2026-11-16 (start 2026-11-11).
- Python 3.13 or newer; a local `.venv`; pytest for tests; constants in `constants.py` when code is written.
- Doxygen comments in any source code.
- Documents live under `docs/`; `src/` and `tests/` stay empty in this project.
- Browser captures run in a container, never on the host desktop.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| Author time for writing, translating and capturing screenshots. The assessment is qualitative because the project has no monetary cost or revenue. | A reusable reference for S01, S02 and S03 |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns the project, writes and reviews it |
| S02 | Reads and runs the README to compare solutions |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, documentation only, and the lecture content is already available.

---

[SA-001]: ./stakeholder-analysis.md
