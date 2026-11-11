**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Flask Auth: Day 68, authentication

This wiki explains what each lecture step of Day 68 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" taught us. The lecture builds a Flask site where people register, log in, see a secret page and download a file. The screenshots come from the lecture's end project, run in a Docker container with test data.

## Run it

This repository holds documentation only. To follow along, create a local `.venv`, upgrade pip and install the lecture's packages (the full instructions are in the [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth)):

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install Flask==3.0.0 Werkzeug==3.0.0 Flask_Login==0.6.3 flask_sqlalchemy==3.1.1 "SQLAlchemy>=2.0.36"
```

## The seven steps

1. [Step 1: Register new users and greet them](Step-1-Register-And-Greet)
2. [Step 2: Download a file](Step-2-Download-A-File)
3. [Step 3: Encryption, hashing and password attacks](Step-3-Encryption-And-Hashing)
4. [Step 4: Hash and salt passwords with Werkzeug](Step-4-Hash-And-Salt-With-Werkzeug)
5. [Step 5: Authenticate users with Flask-Login](Step-5-Authenticate-With-Flask-Login)
6. [Step 6: Flash messages](Step-6-Flash-Messages)
7. [Step 7: Pass the authentication status to templates](Step-7-Authentication-Status-In-Templates)

## What we gained overall

- Registering users and greeting them by name.
- Serving a file with `send_from_directory()`.
- Why passwords are hashed and salted, and how Werkzeug does it.
- Flask-Login for sessions, protected routes and logout.
- Flash messages for feedback and template variables for the login state.
