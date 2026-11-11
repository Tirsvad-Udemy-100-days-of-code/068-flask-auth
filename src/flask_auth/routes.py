"""!
@file routes.py
@brief HTTP routes for registration, login, the secret page and the download.
"""

from pathlib import Path

from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from flask_login import current_user, login_required, login_user, logout_user
from sqlalchemy import select
from werkzeug.wrappers import Response

from flask_auth.constants import (
    BLUEPRINT_NAME,
    DOWNLOAD_DIRECTORY,
    DOWNLOAD_FILENAME,
    ENDPOINT_HOME,
    ENDPOINT_LOGIN,
    ENDPOINT_SECRETS,
    FIELD_EMAIL,
    FIELD_NAME,
    FIELD_PASSWORD,
    MSG_ALREADY_REGISTERED,
    MSG_EMAIL_UNKNOWN,
    MSG_PASSWORD_WRONG,
    TEMPLATE_INDEX,
    TEMPLATE_LOGIN,
    TEMPLATE_REGISTER,
    TEMPLATE_SECRETS,
)
from flask_auth.extensions import db
from flask_auth.models import User

main = Blueprint(BLUEPRINT_NAME, __name__)


def _find_user_by_email(email: str) -> User | None:
    """!
    @brief Look a user up by email.
    @param email The email to search for.
    @return The user, or None.
    """
    return db.session.execute(select(User).where(User.email == email)).scalar()


@main.route("/")
def home() -> str:
    """!
    @brief Home page; the navbar depends on the authentication state.
    @return Rendered page.
    """
    return render_template(TEMPLATE_INDEX, logged_in=current_user.is_authenticated)


@main.route("/register", methods=["GET", "POST"])
def register() -> str | Response:
    """!
    @brief Register a user, log them in and send them to the secret page.
    @return The form (GET) or a redirect (POST).
    """
    if request.method == "POST":
        email = request.form[FIELD_EMAIL]
        if _find_user_by_email(email):
            flash(MSG_ALREADY_REGISTERED)
            return redirect(url_for(ENDPOINT_LOGIN))
        user = User.create(request.form[FIELD_NAME], email, request.form[FIELD_PASSWORD])
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for(ENDPOINT_SECRETS))
    return render_template(TEMPLATE_REGISTER, logged_in=current_user.is_authenticated)


@main.route("/login", methods=["GET", "POST"])
def login() -> str | Response:
    """!
    @brief Log a user in, or flash why that was not possible.
    @return The form or a redirect to the secret page.
    """
    if request.method == "POST":
        user = _find_user_by_email(request.form[FIELD_EMAIL])
        if user is None:
            flash(MSG_EMAIL_UNKNOWN)
        elif not user.check_password(request.form[FIELD_PASSWORD]):
            flash(MSG_PASSWORD_WRONG)
        else:
            login_user(user)
            return redirect(url_for(ENDPOINT_SECRETS))
    return render_template(TEMPLATE_LOGIN, logged_in=current_user.is_authenticated)


@main.route("/secrets")
@login_required
def secrets() -> str:
    """!
    @brief Page for logged-in users; greets them by name.
    @return Rendered page.
    """
    return render_template(TEMPLATE_SECRETS, name=current_user.name, logged_in=True)


@main.route("/logout")
def logout() -> Response:
    """!
    @brief End the session.
    @return Redirect to the home page.
    """
    logout_user()
    return redirect(url_for(ENDPOINT_HOME))


@main.route("/download")
@login_required
def download() -> Response:
    """!
    @brief Send the cheat sheet to a logged-in user.
    @return The file as a download response.
    """
    directory = Path(current_app.root_path) / DOWNLOAD_DIRECTORY
    return send_from_directory(directory, DOWNLOAD_FILENAME)
