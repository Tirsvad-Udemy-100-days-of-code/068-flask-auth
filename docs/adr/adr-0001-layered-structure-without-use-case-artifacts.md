# ADR-0001: Layered structure; no Design Class Diagram for the tutorial app

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [MIL-004], [RC-013] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-11 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-014: Go | [4fb9219] |

Allowed Status values: `Proposed`, `Accepted`, `Rejected`, `Deprecated`, `Superseded by ADR-NNNN`.

---

## Context

[RC-013] found that the first version of the Flask application was one flat package in which the `User` class mixed the database mapping, the Flask-Login session contract and password hashing, and that no Design Class Diagram (DCD) exists for it (criteria 10, 15, 16 and 17 of QC-PY-001).

The framework requires a DCD to trace to a use case (`UC`), and a use case to trace to the Business Case. The project plan records that the tasks of [MIL-004] are technical tasks that need no use case, because the application re-implements a fixed tutorial. Writing a use case, domain model, system sequence diagrams and operation contracts only to feed one DCD would cost more than the application it describes.

Options considered:

1. Keep the flat package and accept the failed criteria. Rejected: the failures are real defects (a domain object that imports the web framework, an ORM session used in route code).
2. Restructure into the four clean-architecture layers and add the full chain `UC`, `DM`, `SSD`, `OC`, `SD`, `DCD`. Rejected as disproportionate for a seven-step tutorial.
3. Restructure into the four layers and record the design classes in this ADR, as a recorded deviation from the DCD requirement.

## Decision

The application is organised in the `domain`, `application`, `infrastructure` and `presentation` packages under `src/flask_auth/`, with `bootstrap.py` as the composition root, and this ADR is the recorded deviation from the DCD requirement: it lists the design classes below instead of a DCD.

| Layer | Classes and operations |
| --- | --- |
| `domain` | `User` (frozen dataclass: `id`, `name`, `email`, `password_hash`; rejects blank fields); errors `DomainError`, `EmailAlreadyRegisteredError`, `UnknownEmailError`, `WrongPasswordError`, `InvalidRegistrationError`; port `UserRepository` (`find_by_email`, `find_by_id`, `add`) |
| `application` | port `PasswordHasher` (`hash`, `verify`); use cases `RegisterUser.execute`, `AuthenticateUser.execute`, `GetUser.execute` |
| `infrastructure` | `UserRecord` (SQLAlchemy table `user`); `SqlAlchemyUserRepository` implements `UserRepository`; `WerkzeugPasswordHasher` implements `PasswordHasher`; `build_config`, `is_debug_enabled`, `MissingSecretKeyError`; `configure_logging` |
| `presentation` | `create_blueprint` (routes `/`, `/register`, `/login`, `/secrets`, `/logout`, `/download`); `SessionUser` (Flask-Login adapter around `User`); `register_user_loader` |

Imports point inward: `domain` imports nothing from the other layers or from a framework, `application` imports only `domain`, and `infrastructure` and `presentation` import inward. Domain objects reach the presentation layer without data transfer objects, because `SessionUser` is the only consumer; this is a second recorded deviation from the `clean-architecture` skill.

## Consequences

**Positive:**

- The business rules (a user needs a name, an email and a hash; an email is registered once; a password must match) are testable without Flask or a database, and the unit tests use fakes.
- The framework, the database and the hashing library are replaceable at the outer layers.
- Security: the secret key has no default and the app fails fast without it; debug is opt-in.

**Negative:**

- More files and indirection than a tutorial strictly needs.
- No DCD or use-case chain exists, so a reader cannot follow these classes to a use case; the mapping from lecture steps to code is kept in the wiki and README instead.
- If the project later adds real use cases, this ADR must be superseded by a DCD that traces to them.

## Affected Artifacts

- [MIL-004] — criterion 7 (source follows `coding-conventions` and `clean-architecture`) is met through this decision.
- [RC-013] — the review whose No-Go findings this decision resolves.

---

[MIL-004]: ../milestones/mil-004-flask-app.md
[RC-013]: ../sqa/reviews/rc-013-mil-004-code.md
[4fb9219]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/commit/4fb9219b59820b5533ef7aa278fd36cd436b097e
