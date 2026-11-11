"""!
@file routes.py
@brief HTTP routes for registration, login, the secret page and the download.
"""

from pathlib import Path

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.wrappers import Response

from flask_auth.application.authenticate_user import AuthenticateUser
from flask_auth.application.register_user import RegisterUser
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
    MSG_FIELDS_REQUIRED,
    MSG_PASSWORD_WRONG,
    PATH_DOWNLOAD,
    PATH_HOME,
    PATH_LOGIN,
    PATH_LOGOUT,
    PATH_REGISTER,
    PATH_SECRETS,
    TEMPLATE_INDEX,
    TEMPLATE_LOGIN,
    TEMPLATE_REGISTER,
    TEMPLATE_SECRETS,
)
from flask_auth.domain.errors import (
    EmailAlreadyRegisteredError,
    InvalidRegistrationError,
    UnknownEmailError,
    WrongPasswordError,
)
from flask_auth.presentation.login_adapter import SessionUser

HTTP_BAD_REQUEST = 400

# The flash message shown for each domain error.
ERROR_MESSAGES: dict[type[Exception], str] = {
    EmailAlreadyRegisteredError: MSG_ALREADY_REGISTERED,
    UnknownEmailError: MSG_EMAIL_UNKNOWN,
    WrongPasswordError: MSG_PASSWORD_WRONG,
    InvalidRegistrationError: MSG_FIELDS_REQUIRED,
}


def create_blueprint(
    register_user: RegisterUser, authenticate_user: AuthenticateUser
) -> Blueprint:
    """!
    @brief Build the blueprint around the given use cases.
    @param register_user Use case that registers a user.
    @param authenticate_user Use case that checks credentials.
    @return The blueprint with all routes.
    """
    main = Blueprint(BLUEPRINT_NAME, __name__, template_folder="templates")
    download_directory = Path(main.root_path) / DOWNLOAD_DIRECTORY

    @main.route(PATH_HOME)
    def home() -> str:
        return render_template(TEMPLATE_INDEX, logged_in=current_user.is_authenticated)

    @main.route(PATH_REGISTER, methods=["GET", "POST"])
    def register() -> str | Response | tuple[str, int]:
        if request.method == "POST":
            try:
                user = register_user.execute(
                    request.form.get(FIELD_NAME, ""),
                    request.form.get(FIELD_EMAIL, ""),
                    request.form.get(FIELD_PASSWORD, ""),
                )
            except EmailAlreadyRegisteredError as error:
                flash(ERROR_MESSAGES[type(error)])
                return redirect(url_for(ENDPOINT_LOGIN))
            except InvalidRegistrationError as error:
                flash(ERROR_MESSAGES[type(error)])
                page = render_template(TEMPLATE_REGISTER, logged_in=False)
                return page, HTTP_BAD_REQUEST
            login_user(SessionUser(user))
            return redirect(url_for(ENDPOINT_SECRETS))
        return render_template(
            TEMPLATE_REGISTER, logged_in=current_user.is_authenticated
        )

    @main.route(PATH_LOGIN, methods=["GET", "POST"])
    def login() -> str | Response:
        if request.method == "POST":
            try:
                user = authenticate_user.execute(
                    request.form.get(FIELD_EMAIL, ""),
                    request.form.get(FIELD_PASSWORD, ""),
                )
            except (UnknownEmailError, WrongPasswordError) as error:
                flash(ERROR_MESSAGES[type(error)])
            else:
                login_user(SessionUser(user))
                return redirect(url_for(ENDPOINT_SECRETS))
        return render_template(TEMPLATE_LOGIN, logged_in=current_user.is_authenticated)

    @main.route(PATH_SECRETS)
    @login_required
    def secrets() -> str:
        return render_template(TEMPLATE_SECRETS, name=current_user.name, logged_in=True)

    @main.route(PATH_LOGOUT)
    def logout() -> Response:
        logout_user()
        return redirect(url_for(ENDPOINT_HOME))

    @main.route(PATH_DOWNLOAD)
    @login_required
    def download() -> Response:
        return send_from_directory(download_directory, DOWNLOAD_FILENAME)

    return main
