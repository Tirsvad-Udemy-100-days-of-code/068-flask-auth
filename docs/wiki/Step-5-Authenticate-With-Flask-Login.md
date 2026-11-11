**English** · [Dansk](Step-5-Authenticate-With-Flask-Login-da) · [Bahasa Malaysia](Step-5-Authenticate-With-Flask-Login-ms)

# Step 5: Authenticate users with Flask-Login

## What the lecture asked

Only logged-in users may see `/secrets` and download the file. Configure Flask-Login, log the user in when they register, protect `/secrets` and `/download`, and write the `/login` and `/logout` routes.

## What we built

A `LoginManager` with a `user_loader` callback, a `User` that uses `UserMixin`, `login_user()` after register and login, `@login_required` on the protected routes, `check_password_hash()` to verify the password and `logout_user()` for `/logout`.

```python
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route("/secrets")
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)
```

In this repository `/logout` accepts POST only. The navbar "Log Out" entry is a small form that carries the CSRF token, and `GET /logout` returns 405. This departs from the lecture, where logout is a plain link, because a GET that changes state can be triggered from another site.

## What it looks like

![/secrets without logging in is refused](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-05a-secrets-requires-login.png)

![The login form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-05b-login-form.png)

![After a successful login](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/068-flask-auth/raw/branch/main/docs/images/step-05c-login-success.png)

## What we gained

- Flask-Login keeps track of who is logged in between requests.
- A `user_loader` turns the stored user id into a `User`.
- `@login_required` protects a route with one line.
- `check_password_hash()` compares a typed password with the stored hash without ever decoding it.

Previous step: [Hash and salt passwords with Werkzeug](Step-4-Hash-And-Salt-With-Werkzeug) · Next step: [Flash messages](Step-6-Flash-Messages) · [Back to the overview](Home)
