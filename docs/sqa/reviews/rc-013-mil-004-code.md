# Review of MIL-004 source code

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the source in `src/flask_auth/` and `tests/` delivered under [MIL-004] (commit a7d60a0)
- Checklist used: [QC-PY-001]
- Scope: full review, criteria 1 to 18
- Language and domain: n/a (source code is not a PO-language artifact type)
- Language reviewer: none
- Mode: supervised (S01 asked for the review in chat; the checklist was applied by the `python-developer` agent, and ruff and mypy results were re-run by the author)

## Tool evidence

Run in `.venv` (Python 3.13); ruff and mypy were installed for the review and are not declared in `pyproject.toml`.

| Check | Result |
| --- | --- |
| `pytest` | 10 passed |
| `ruff check src tests` (ruff defaults, no config committed) | All checks passed |
| `ruff format --check src tests` | 3 files would be reformatted: `constants.py`, `routes.py`, `tests/conftest.py` |
| `mypy --strict src tests` | 9 errors in 3 files: untyped `flask_login` (import, `UserMixin`, 3 decorators) and the `db.Model` base |

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | PEP 8 casing | Pass | snake_case modules, PascalCase classes, UPPER_SNAKE constants. |
| 2 | Names state purpose | Pass | No unexplained abbreviations. |
| 3 | Formatter and linter | Fail | Linter passes; the formatter flags 3 files and no ruff configuration is committed. |
| 4 | Type annotations | Pass | Every function and method is annotated; mypy reports no missing annotation in project code. |
| 5 | No bare except | Pass | No try/except in the code. |
| 6 | No mutable defaults or shadowed builtins | Pass | None found. |
| 7 | Context managers | Pass | No raw file, lock or connection handling. |
| 8 | Docstrings | Pass | Present on every module, class and function (Doxygen style). |
| 9 | Logging and secrets | Fail | `DEFAULT_SECRET_KEY` is a committed fallback used silently (`constants.py:13`, `__init__.py:29`); `debug=True` is hardcoded (`__main__.py:9`). No `print`, no logging. The criterion text names logs only, so a reviewer may rate it a minor note. |
| 10 | Classes trace to a DCD | Fail | No Design Class Diagram and no ADR exist; `User` and its operations trace to nothing. |
| 11 | Tests | Pass | 10 behaviour-named tests, in-memory database, no network, order independent. Gaps: no empty-field case, no direct `User.create` unit test, no `unit`/`integration`/`e2e` folders. |
| 12 | Strict type checker | Fail | 9 mypy errors, no justification or override committed. |
| 13 | Dependencies pinned | Fail | Lower bounds only; ruff and mypy are not declared. |
| 14 | One place per piece of knowledge | Fail | `LOGIN_ENDPOINT` duplicates `ENDPOINT_LOGIN`; the hash prefix and form field names are literals in tests. Minor. |
| 15 | Imports point inward | Fail | `models.py` is the only domain-like module and imports Flask-Login, Flask-SQLAlchemy and SQLAlchemy; hashing is inside the model. No framework-free business-rule module. |
| 16 | SOLID | Fail | `User` mixes persistence mapping, the session contract and password policy; route handlers mix HTTP, the duplicate-email rule, hashing and persistence; `db.session` is used directly. |
| 17 | Layered folders | Fail | `src/flask_auth/` is flat; no `domain`, `application`, `infrastructure` or `presentation` package and no ADR for a merged layer. `tests/` has no `unit`, `integration` or `e2e`. |
| 18 | File and folder names | Pass | English, no spaces, allowed characters. |

## Other defects

- The register route does not reject empty fields, and the find-then-insert on email can hit the unique constraint and return a 500 under a race.
- Function-local imports in `create_app` (`__init__.py:38-39`).

## Overall Verdict

No-Go — Mandatory criteria 3, 9, 10, 14, 15, 16 and 17 do not pass; Optional criteria 12 and 13 also fail. Criterion 7 of [MIL-004] (source follows `coding-conventions` and `clean-architecture`) is therefore not met, and neither is Go/No-Go criterion 9 until opengrep has run on the final code (it passed in CI on the pull request).

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Run `ruff format`; add `[tool.ruff]` and `[tool.mypy]` (strict, with a commented override for `flask_login`); declare ruff and mypy in the `dev` extra | S01 | Before re-review |
| Decide the structure: restructure into layers (a framework-free `domain` module for the user and hashing policy, ports for the repository and hasher, Flask and SQLAlchemy in outer packages, tests mirrored), or write an ADR that merges `application`, adapters and infrastructure for this tutorial app and keeps a small `domain` | S01 | Before re-review |
| Add a short DCD, or an ADR recording that the tutorial app has none | S01 | Before re-review |
| Remove the default secret key and fail fast when `SECRET_KEY` is unset outside tests; make `debug` opt-in through the environment | S01 | Before re-review |
| Pin the dependencies; reject empty register fields; handle the duplicate-email race | S01 | Before re-review |
| Re-review against [QC-PY-001] and record a new `RC-*` | S01 | After the fixes |

---

[MIL-004]: ../../milestones/mil-004-flask-app.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
