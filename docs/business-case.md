# Business Case: Flask Auth (Day 68)

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-009] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version<br>Reviewed in RC-001: Go | [4a5ddde] |
| 2026-11-11 | Deprecated | Jens Tirsvad Nielsen | S01 | Add the working Flask application to scope (objective 6)<br>Reviewed in RC-008: Go | [a7d60a0] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective 7, success criterion 6, a scope item, an out-of-scope item, a risk and two constraints for the baseline milestone MIL-009; set the PO domain to education; reviewed in autonomous mode, not independent<br>Reviewed in RC-029: Go | [01f769b] |

---

## Executive Summary

Day 68 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" teaches user authentication in Flask: registering users, hashing and salting passwords, logging in with Flask-Login, flash messages and template-level authentication state. This project turns that lecture into a public learning reference: a README and a three-language wiki (English, Danish, Bahasa Malaysia) that explain each lecture step with a screenshot and say what was learned. The project also delivers the working Flask application the lecture builds, with tests, so the documentation describes code the repository holds.

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
6. Deliver a working Flask authentication application (lecture steps 1 to 7) under `src/` with pytest tests under `tests/`.
7. Bring the finished project to the common baseline of the framework: the adopted framework release, a README that lists only the documents of the repository, project URL and licence metadata, the editor settings of the baseline, an `.env.example` in the framework's form that also lists the environment variables of the program, and a traceability matrix that covers the documents ([MIL-009]).

## Scope

### In Scope

- README (framework template) for the Day 68 lecture steps, with screenshots.
- Wiki pages in `docs/wiki/` in English, Danish (`-da`) and Bahasa Malaysia (`-ms`), with screenshots and "what we gained" sections.
- Screenshots of each lecture step, captured from the lecture's end project run in a Docker container.
- Repository description and topics on the git host.
- `pyproject.toml` (Python 3.13 or newer, pytest), Python `.gitignore`, `Doxyfile`, documented `.venv` setup with `python -m pip install --upgrade pip`.
- The Flask application for lecture steps 1 to 7 in `src/flask_auth/`, with pytest tests in `tests/`.
- A local opengrep scan before each push.
- The baseline milestone [MIL-009]: the framework release, the README without the private framework files in its appendix, project URL and licence metadata, `.editorconfig`, `.env.example`, an updated traceability matrix, review records and a review of the wiki. It changes no behaviour of the program.

### Out of Scope

- Reproducing the lecture's video or course material beyond short descriptions and own screenshots.
- Publishing the course resource archive in the repository.
- Any change to `src/`, `tests/`, `docs/images/` or the wiki pages in the baseline milestone [MIL-009]. That milestone starts the program on no public address, retakes no screenshot and runs the tests only.

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
| 6 | The baseline milestone is done (objective 7) | `framework/scripts/check-readme.sh`, `check-languages.sh` and `check-editorconfig.sh` exit with code 0, `python -m pytest` passes, 100 % of the continuous integration (CI) checks of the pull request of [MIL-009] pass | The script exit codes and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The course resource link has expired | Screenshots cannot be captured from the end project | Stop and report; the user supplies the archive or chooses another source |
| The downloaded archive is untrusted | Malicious code runs | Extract into its own directory and run only inside a Docker container |
| A token leaks into the repository | Credential exposure | Tokens are read from `.env` outside the repository, never printed, never committed |
| Translations drift from English | Inconsistent wiki | English is authoritative; same page set; `check-languages.sh` |
| Screenshots show personal data | Privacy loss | Use test data only |
| The documents of the baseline milestone [MIL-009] change documents that were accepted earlier, and an AI stand-in for S01 reviews them | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, `src/` and `tests/` are not changed, the tests run before and after, and the end-of-run summary lists the reviews for challenge |

## Assumptions

- S01 is Product Owner, developer and reviewer.
- The Product Owner (PO) language is English; the PO domain is education since [MIL-009] (it was information technology (IT) until then; the documents that [MIL-009] does not change keep the domain `it`, see the Open Issues of [PP-001]).
- The git host wiki is enabled and the organisation holds `TOKEN_FOR_GITEA_WIKI`.
- Docker is available on the host.

## Constraints

- Duration: the whole project is complete by 2026-11-16 (start 2026-11-11).
- The baseline milestone [MIL-009] starts 2026-11-16 and is finished within one week, by 2026-11-23, so the end date of the plan moves from 2026-11-16 to 2026-11-23. An AI stand-in for S01 reviews and accepts the changed documents.
- The program has no secret in the repository: the secret key and the database address are read from the environment variables `SECRET_KEY` and `DATABASE_URI` at run time, and `.env.example` holds empty placeholders only.
- Python 3.13 or newer; a local `.venv`; pytest for tests; constants in `constants.py` when code is written.
- Doxygen comments in any source code.
- Documents live under `docs/`; application code lives under `src/` and tests under `tests/`.
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

Proceed — the scope is small, and the lecture content is already available.

---

[SA-001]: ./stakeholder-analysis.md
[4a5ddde]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/4a5ddde2e1eacea3ee7b76655c4d51953e89c6fd
[a7d60a0]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/a7d60a0ff5f21fe76224c3663ba32f75a1af658e
[PP-001]: ./project-plan.md
[MIL-009]: ./milestones/mil-009-framework-baseline.md
[01f769b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/01f769b62ce2a651438d8817ad6d09d4241204a5
