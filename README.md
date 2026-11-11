<!-- README from framework/templates/README-template.md -->

# 🚀 Flask Auth (Day 68)

A walkthrough of Day 68 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp": user authentication in Flask. It is written for course participants who want to compare solutions and for visitors looking for ideas. This repository holds documentation and project configuration only; it has no runtime dependencies.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The lecture builds a small Flask site where people register, log in, see a secret page and download a file. The screenshots below come from the lecture's end project, run in a Docker container with test data only.

| Folder | Purpose |
| --- | --- |
| `src/` | Reserved for source code; empty, because this project does not program the lecture |
| `tests/` | Reserved for pytest tests; empty for the same reason |
| `docs/` | Project documents, the step screenshots (`docs/images/`) and the wiki (`docs/wiki/`) |

The [wiki][wiki] explains what each lecture step taught, in English, Danish and Bahasa Malaysia.

### Lecture steps

#### 1. Register new users and greet them

The `/register` form takes a name, an email and a password, creates a `User` and saves it in `users.db`. The user is then sent straight to `secrets.html`, whose `h1` greets them by name.

![Register form](docs/images/step-01a-register-form.png)
![Secrets page greeting the user](docs/images/step-01b-secrets-greeting.png)

#### 2. Download a file

The "Download Your File" link calls `GET /download`, which uses Flask's `send_from_directory()` to return `static/files/cheat_sheet.pdf`.

![The download link](docs/images/step-02a-download-link.png)
![Response of /download](docs/images/step-02b-download-response.png)

#### 3. Encryption, hashing and password attacks (theory)

Plain text storage is unsafe. Encryption needs a key and can be reversed with it; a hash is one way. Hackers use hash tables and dictionary attacks against common passwords, so a long, complex password and a salt matter. The illustration shows the same password hashing to the same value, and two salted hashes that differ.

![Hashing versus salting](docs/images/step-03-hashing-vs-salting.png)

#### 4. Hash and salt passwords with Werkzeug

`generate_password_hash()` with `method="pbkdf2:sha256"` and `salt_length=8` hashes and salts the password before it is stored. The database never holds the password itself.

![Hashed password in the database](docs/images/step-04-hashed-password-in-db.png)

#### 5. Authenticate users with Flask-Login

Flask-Login needs a `LoginManager`, a `user_loader` callback and a `User` that uses `UserMixin`. `login_user()` logs a user in after registering or logging in, `@login_required` protects `/secrets` and `/download`, and `check_password_hash()` verifies the password. `/logout` ends the session.

![Secrets requires login](docs/images/step-05a-secrets-requires-login.png)
![Login form](docs/images/step-05b-login-form.png)
![Successful login](docs/images/step-05c-login-success.png)

#### 6. Flash messages

`flash()` gives feedback once: the email does not exist, the password is wrong, or the email is already registered. The login template shows each message in a `<p>` tag.

![Unknown email](docs/images/step-06a-flash-unknown-email.png)
![Wrong password](docs/images/step-06b-flash-wrong-password.png)
![Already registered](docs/images/step-06c-flash-already-registered.png)

#### 7. Pass the authentication status to templates

Routes pass `logged_in=current_user.is_authenticated` to the templates. `base.html` and `index.html` hide Login and Register for a logged-in user, and the home page adds "(you are already logged in)".

![Home page, logged out](docs/images/step-07a-home-logged-out.png)
![Home page, logged in](docs/images/step-07b-home-logged-in.png)

## 📋 Requirements

- Python 3.13 or newer.
- `venv`, to keep the project's packages apart from the system Python.
- pytest, only to run the (empty) test suite.
- Doxygen, only to generate documentation of source code that a later phase may add (`Doxyfile`).

## 🛠️ Setup

Create and use a local `.venv`, then upgrade `pip`:

```bash
python -m venv .venv
source .venv/bin/activate        # Linux and macOS
.venv\Scripts\activate           # Windows (PowerShell or cmd)
python -m pip install --upgrade pip
python -m pip install pytest
```

The project has no runtime dependencies. To run the lecture's own end project, install its packages in the same `.venv`. On Python 3.13 use `SQLAlchemy>=2.0.36`, because the pinned `2.0.25` fails to import:

```bash
python -m pip install Flask==3.0.0 Werkzeug==3.0.0 Flask_Login==0.6.3 flask_sqlalchemy==3.1.1 "SQLAlchemy>=2.0.36"
```

## ▶️ Run

This repository does not contain the application. Read the steps above, or open the [wiki][wiki]. The end project is the course's own download; with its packages installed (see Setup) it starts with `python main.py` and serves `http://127.0.0.1:5000`.

## 🧪 Tests

```bash
python -m pytest
```

There are no tests yet, so pytest reports that no tests were collected (exit code 5).

## 📄 License

GNU Affero General Public License v3.0, see [LICENSE](LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth
[wiki]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/wiki
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
