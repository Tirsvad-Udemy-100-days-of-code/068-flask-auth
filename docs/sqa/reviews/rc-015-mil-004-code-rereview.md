# Review of MIL-004 source code (re-review)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [MIL-004], [QC-PY-001], [RC-013], [ADR-0001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [4fb9219] |

---

## Artifact Under Review

- Instance reviewed: the source in `src/flask_auth/` and `tests/` after the fixes for [RC-013]
- Checklist used: [QC-PY-001]
- Scope: full re-review, criteria 1 to 18
- Language and domain: n/a (source code is not a PO-language artifact type)
- Language reviewer: none
- Mode: supervised (S01 asked in chat to fix the findings of RC-013; the checklist was applied by the AI, and the tool results were re-run by the author)

## Tool evidence

Run in `.venv` (Python 3.13) by the author after the fix.

| Check | Result |
| --- | --- |
| `pytest` | 48 passed |
| `ruff check src tests` | All checks passed |
| `ruff format --check src tests` | 39 files already formatted |
| `mypy --strict src tests` | Success: no issues found in 39 source files |
| Import scan | `domain` imports only `dataclasses`, `typing` and itself; `application` imports only `domain` and itself |
| `type: ignore`, `print(`, bare `except:` | no `print(` or bare `except:`; no `type: ignore` in `src/`; one `# type: ignore[misc]` in `tests/unit/domain/test_user.py` (the test that assigns to a frozen dataclass on purpose) |
| Start of `python -m flask_auth` (by the developer agent) | debug off; `/` and `/register` returned 200 |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | PEP 8 casing | Pass | Unchanged from RC-013. |
| 2 | Names state purpose | Pass | Use cases and ports named for what they do. |
| 3 | Formatter and linter | Pass | `ruff` configured in `pyproject.toml`; check and format both clean. |
| 4 | Type annotations | Pass | `mypy --strict` clean. |
| 5 | No bare except | Pass | `IntegrityError` is caught narrowly and mapped to `EmailAlreadyRegisteredError`. |
| 6 | No mutable defaults or shadowed builtins | Pass | None found. |
| 7 | Context managers | Pass | No raw file, lock or connection handling. |
| 8 | Docstrings | Pass | Present. |
| 9 | Logging and secrets | Pass | No default secret key (the app raises `MissingSecretKeyError` without one); debug only with `FLASK_AUTH_DEBUG=1`; `logging` used for auth events, logging the user id only (two tests assert this). |
| 10 | Classes trace to a DCD; deviations recorded | Pass | No DCD; the deviation and the design classes are recorded in [ADR-0001]. |
| 11 | Tests | Pass | 48 tests in `unit`, `integration`, `e2e`; fakes for the unit tests, in-memory database, no network. |
| 12 | Strict type checker | Pass | Zero errors; no `type: ignore` in `src/` and one narrow, intentional one in a test (see Tool evidence); the two override blocks in `pyproject.toml` carry comments. |
| 13 | Dependencies pinned | Pass | Runtime and dev dependencies pinned with `==`; ruff and mypy declared in `dev`. |
| 14 | One place per piece of knowledge | Pass | `LOGIN_ENDPOINT` and `DEFAULT_SECRET_KEY` removed; messages, endpoints, fields and templates are constants; tests use the constants. |
| 15 | Imports point inward | Pass | Import scan above; no framework import in `domain` or `application`. |
| 16 | SOLID | Pass | Use cases have one job and receive a repository and a hasher through their constructors; `bootstrap.py` is the only place that builds the implementations. |
| 17 | Layered folders | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/flask_auth/`; `unit`, `integration`, `e2e` under `tests/`. |
| 18 | File and folder names | Pass | English, no spaces. |

## Other points

- Domain objects reach the presentation layer without data transfer objects; recorded as a deviation in [ADR-0001].
- Importing any `flask_auth` module loads Flask, because `flask_auth/__init__.py` re-exports `create_app`. The layers themselves do not import Flask.
- The pinned versions are the ones installed in `.venv`; no packaging build was run to check `package-data`.
- Defects from RC-013 now fixed: empty register fields return 400; the duplicate-email race is mapped to a flash message.
- opengrep was not run locally; it runs in CI on the pull request.

## Overall Verdict

Go — every Mandatory criterion of [QC-PY-001] passes, and so do the Optional ones. This closes criterion 7 of [MIL-004]; criterion 9 (opengrep) is checked in CI on the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Confirm opengrep passes in CI on the pull request | S01 | At the pull request |

---

[MIL-004]: ../../milestones/mil-004-flask-app.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[RC-013]: ./rc-013-mil-004-code.md
[ADR-0001]: ../../adr/adr-0001-layered-structure-without-use-case-artifacts.md
[4fb9219]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/4fb9219b59820b5533ef7aa278fd36cd436b097e
