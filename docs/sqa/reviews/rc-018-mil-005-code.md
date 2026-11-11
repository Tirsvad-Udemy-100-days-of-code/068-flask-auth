# Review of MIL-005 source code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-018 |
| CrossReference | [MIL-005], [QC-PY-001], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the CSRF change in `src/flask_auth/` and `tests/` delivered under [MIL-005]
- Checklist used: [QC-PY-001]
- Scope: full checklist applied to the changed code (`bootstrap.py`, `constants.py`, `infrastructure/extensions.py`, two templates, `tests/e2e/`, `pyproject.toml`); the unchanged code keeps the result of [RC-015]
- Language and domain: n/a (source code is not a PO-language artifact type)
- Language reviewer: none
- Mode: supervised (S01 asked for the change in chat; the checklist was applied by the AI after the `python-developer` agent built it, and the tool results were re-run by the author)

## Tool evidence

Run in `.venv` (Python 3.13).

| Check | Result |
| --- | --- |
| `pytest` | 56 passed (the 48 existing tests plus 8 new ones) |
| `ruff check src tests` | All checks passed |
| `ruff format --check src tests` | 39 files already formatted |
| `mypy --strict src tests` | Success: no issues found in 39 source files |
| Import scan | no `flask_wtf` import in `domain` or `application`; the only import is in `infrastructure/extensions.py` |
| `WTF_CSRF_ENABLED`, route exemptions | none; CSRF is enabled in the test configuration too |
| Start of the app (by the developer agent) | `GET /register` contains `csrf_token`; `POST /register` and `POST /login` without a token return 400 |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | PEP 8 casing | Pass | `csrf`, `FIELD_CSRF_TOKEN`, `fetch_csrf_token`. |
| 2 | Names state purpose | Pass | |
| 3 | Formatter and linter | Pass | Both clean. |
| 4 | Type annotations | Pass | `mypy --strict` clean. |
| 5 | No bare except | Pass | No try/except added. |
| 6 | No mutable defaults or shadowed builtins | Pass | |
| 7 | Context managers | Pass | Not affected. |
| 8 | Docstrings | Pass | New helpers carry docstrings. |
| 9 | Logging and secrets | Pass | The token is not logged; `SECRET_KEY` stays required. |
| 10 | Classes trace to a DCD; deviations recorded | Pass | No new class; the layering decision stays in [ADR-0001]. |
| 11 | Tests | Pass | 8 new tests (hidden field on both pages; no, empty and wrong token on both POST routes); existing tests send the token through one helper. |
| 12 | Strict type checker | Pass | Zero errors. A commented `ignore_missing_imports` override covers `flask_wtf`, which ships no type marker. |
| 13 | Dependencies pinned | Pass | `Flask-WTF==1.3.0`; WTForms 3.3.2 comes in transitively and is constrained by that pin. |
| 14 | One place per piece of knowledge | Pass | The field name is `FIELD_CSRF_TOKEN` in `constants.py` and is used by the tests. The templates carry the literal name, as templates cannot import constants. |
| 15 | Imports point inward | Pass | See the import scan. |
| 16 | SOLID | Pass | The extension instance lives with the other extensions and is initialised only in the composition root. |
| 17 | Layered folders | Pass | No structure change. |
| 18 | File and folder names | Pass | |

## Other points

- `GET /logout` still ends the session without a token, as in the lecture; recorded as an open issue in [MIL-005].
- OpenGrep was not run locally; the CSRF rule findings on the two forms should clear, and CI confirms this on the pull request.
- Correction of [RC-015]: it said no `type: ignore` exists in the tests; one narrow `# type: ignore[misc]` exists in `tests/unit/domain/test_user.py`, in the test that assigns to a frozen dataclass on purpose. RC-015 is corrected in the same pull request.

## Overall Verdict

Go — every Mandatory criterion of [QC-PY-001] passes. This closes criterion 7 of [MIL-005]; criterion 8 (opengrep) is checked in CI on the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Confirm opengrep reports no blocking finding in CI on the pull request | S01 | At the pull request |

---

[MIL-005]: ../../milestones/mil-005-csrf-protection.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[ADR-0001]: ../../adr/adr-0001-layered-structure-without-use-case-artifacts.md
[RC-015]: ./rc-015-mil-004-code-rereview.md
