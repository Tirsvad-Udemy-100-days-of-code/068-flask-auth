"""Behaviour tests of registration, login, protected routes and flash messages."""

import pytest
from flask import Flask
from flask.testing import FlaskClient
from sqlalchemy import select

from flask_auth.constants import (
    FIELD_CSRF_TOKEN,
    FIELD_EMAIL,
    FIELD_NAME,
    FIELD_PASSWORD,
    MSG_ALREADY_REGISTERED,
    MSG_EMAIL_UNKNOWN,
    MSG_FIELDS_REQUIRED,
    MSG_PASSWORD_WRONG,
    PASSWORD_HASH_METHOD,
    PATH_DOWNLOAD,
    PATH_HOME,
    PATH_LOGIN,
    PATH_LOGOUT,
    PATH_REGISTER,
    PATH_SECRETS,
)
from flask_auth.infrastructure.extensions import db
from flask_auth.infrastructure.models import UserRecord
from tests.e2e.conftest import fetch_csrf_token, login, register
from tests.support import (
    TEST_EMAIL,
    TEST_NAME,
    TEST_OTHER_EMAIL,
    TEST_PASSWORD,
    TEST_UNKNOWN_EMAIL,
    TEST_WRONG_PASSWORD,
)


def escaped(message: str) -> bytes:
    """The message as Jinja renders it (apostrophes are HTML-escaped)."""
    return message.encode().replace(b"'", b"&#39;")


def test_register_greets_user_by_name(client: FlaskClient) -> None:
    response = register(client, name=TEST_NAME)
    assert response.status_code == 302
    page = client.get(PATH_SECRETS)
    assert f"Welcome, {TEST_NAME}!".encode() in page.data


def test_register_stores_salted_hash_not_plain_password(
    app: Flask, client: FlaskClient
) -> None:
    register(client)
    with app.app_context():
        record = db.session.execute(select(UserRecord)).scalar_one()
        assert record.password != TEST_PASSWORD
        assert record.password.startswith(f"{PASSWORD_HASH_METHOD}:")


def test_same_password_hashes_differently_for_two_users(
    app: Flask, client: FlaskClient
) -> None:
    register(client, email=TEST_EMAIL)
    client.get(PATH_LOGOUT)
    register(client, email=TEST_OTHER_EMAIL)
    with app.app_context():
        hashes = db.session.execute(select(UserRecord.password)).scalars().all()
    assert len(set(hashes)) == 2


@pytest.mark.parametrize("path", [PATH_SECRETS, PATH_DOWNLOAD])
def test_anonymous_visitor_is_redirected_from_protected_routes(
    client: FlaskClient, path: str
) -> None:
    response = client.get(path)
    assert response.status_code == 302
    assert PATH_LOGIN in response.headers["Location"]


def test_logged_in_user_can_download_file(client: FlaskClient) -> None:
    register(client)
    response = client.get(PATH_DOWNLOAD)
    assert response.status_code == 200
    assert response.data.startswith(b"%PDF")
    response.close()


def test_login_succeeds_and_logout_ends_session(client: FlaskClient) -> None:
    register(client)
    client.get(PATH_LOGOUT)
    response = login(client)
    assert response.status_code == 302
    assert client.get(PATH_SECRETS).status_code == 200
    client.get(PATH_LOGOUT)
    assert client.get(PATH_SECRETS).status_code == 302


def test_login_flashes_message_for_unknown_email(client: FlaskClient) -> None:
    response = login(client, email=TEST_UNKNOWN_EMAIL, password="x")
    assert MSG_EMAIL_UNKNOWN.encode() in response.data


def test_login_flashes_message_for_wrong_password(client: FlaskClient) -> None:
    register(client)
    client.get(PATH_LOGOUT)
    response = login(client, password=TEST_WRONG_PASSWORD)
    assert MSG_PASSWORD_WRONG.encode() in response.data


def test_register_existing_email_redirects_to_login_with_flash(
    app: Flask, client: FlaskClient
) -> None:
    register(client)
    client.get(PATH_LOGOUT)
    response = register(client)
    assert response.status_code == 302
    assert PATH_LOGIN in response.headers["Location"]
    page = client.get(PATH_LOGIN)
    assert escaped(MSG_ALREADY_REGISTERED) in page.data
    with app.app_context():
        assert len(db.session.execute(select(UserRecord)).scalars().all()) == 1


def test_home_navbar_differs_when_logged_in(client: FlaskClient) -> None:
    logged_out = client.get(PATH_HOME).data
    assert b"Login" in logged_out and b"Register" in logged_out
    assert b"Log Out" not in logged_out
    register(client)
    logged_in = client.get(PATH_HOME).data
    assert b"Log Out" in logged_in
    assert b"Register" not in logged_in
    assert b"you are already logged in" in logged_in


@pytest.mark.parametrize(
    ("name", "email", "password"),
    [
        ("", TEST_EMAIL, TEST_PASSWORD),
        (TEST_NAME, "", TEST_PASSWORD),
        (TEST_NAME, TEST_EMAIL, ""),
    ],
)
def test_register_rejects_empty_field_with_400_and_flash(
    app: Flask, client: FlaskClient, name: str, email: str, password: str
) -> None:
    response = register(client, email=email, name=name, password=password)
    assert response.status_code == 400
    assert MSG_FIELDS_REQUIRED.encode() in response.data
    assert client.get(PATH_SECRETS).status_code == 302
    with app.app_context():
        assert db.session.execute(select(UserRecord)).first() is None


@pytest.mark.parametrize("path", [PATH_REGISTER, PATH_LOGIN])
def test_form_pages_contain_hidden_csrf_token_field(
    client: FlaskClient, path: str
) -> None:
    page = client.get(path).get_data(as_text=True)
    assert f'<input type="hidden" name="{FIELD_CSRF_TOKEN}"' in page
    assert fetch_csrf_token(client, path)


@pytest.mark.parametrize("token", [None, "", "not-a-valid-token"])
def test_register_without_valid_csrf_token_returns_400_and_creates_no_user(
    app: Flask, client: FlaskClient, token: str | None
) -> None:
    data = {
        FIELD_NAME: TEST_NAME,
        FIELD_EMAIL: TEST_EMAIL,
        FIELD_PASSWORD: TEST_PASSWORD,
    }
    if token is not None:
        data[FIELD_CSRF_TOKEN] = token
    response = client.post(PATH_REGISTER, data=data)
    assert response.status_code == 400
    assert client.get(PATH_SECRETS).status_code == 302
    with app.app_context():
        assert db.session.execute(select(UserRecord)).first() is None


@pytest.mark.parametrize("token", [None, "", "not-a-valid-token"])
def test_login_without_valid_csrf_token_returns_400_and_does_not_log_in(
    client: FlaskClient, token: str | None
) -> None:
    register(client)
    client.get(PATH_LOGOUT)
    data = {FIELD_EMAIL: TEST_EMAIL, FIELD_PASSWORD: TEST_PASSWORD}
    if token is not None:
        data[FIELD_CSRF_TOKEN] = token
    response = client.post(PATH_LOGIN, data=data)
    assert response.status_code == 400
    assert client.get(PATH_SECRETS).status_code == 302
