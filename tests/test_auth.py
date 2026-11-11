"""Behaviour tests for registration, login, protected routes and flash messages."""

from flask import Flask
from flask.testing import FlaskClient
from sqlalchemy import select

from flask_auth.constants import (
    MSG_ALREADY_REGISTERED,
    MSG_EMAIL_UNKNOWN,
    MSG_PASSWORD_WRONG,
)
from flask_auth.extensions import db
from flask_auth.models import User
from tests.conftest import TEST_PASSWORD, register


def test_register_greets_user_by_name(client: FlaskClient) -> None:
    response = register(client, name="Ada")
    assert response.status_code == 302
    page = client.get("/secrets")
    assert b"Welcome, Ada!" in page.data


def test_register_stores_salted_hash_not_plain_password(
    app: Flask, client: FlaskClient
) -> None:
    register(client)
    with app.app_context():
        user = db.session.execute(select(User)).scalar_one()
        assert user.password != TEST_PASSWORD
        assert user.password.startswith("pbkdf2:sha256:")
        assert user.check_password(TEST_PASSWORD)


def test_same_password_hashes_differently_for_two_users(
    app: Flask, client: FlaskClient
) -> None:
    register(client, email="a@example.com")
    client.get("/logout")
    register(client, email="b@example.com")
    with app.app_context():
        hashes = db.session.execute(select(User.password)).scalars().all()
    assert len(set(hashes)) == 2


def test_anonymous_visitor_is_redirected_from_protected_routes(
    client: FlaskClient,
) -> None:
    for path in ("/secrets", "/download"):
        response = client.get(path)
        assert response.status_code == 302
        assert "/login" in response.headers["Location"]


def test_logged_in_user_can_download_file(client: FlaskClient) -> None:
    register(client)
    response = client.get("/download")
    assert response.status_code == 200
    assert response.data.startswith(b"%PDF")
    response.close()


def test_login_succeeds_and_logout_ends_session(client: FlaskClient) -> None:
    register(client)
    client.get("/logout")
    response = client.post(
        "/login", data={"email": "ada@example.com", "password": TEST_PASSWORD}
    )
    assert response.status_code == 302
    assert client.get("/secrets").status_code == 200
    client.get("/logout")
    assert client.get("/secrets").status_code == 302


def test_login_flashes_message_for_unknown_email(client: FlaskClient) -> None:
    response = client.post(
        "/login", data={"email": "nobody@example.com", "password": "x"}
    )
    assert MSG_EMAIL_UNKNOWN.encode() in response.data


def test_login_flashes_message_for_wrong_password(client: FlaskClient) -> None:
    register(client)
    client.get("/logout")
    response = client.post(
        "/login", data={"email": "ada@example.com", "password": "wrong"}
    )
    assert MSG_PASSWORD_WRONG.encode() in response.data


def test_register_existing_email_redirects_to_login_with_flash(
    app: Flask, client: FlaskClient
) -> None:
    register(client)
    client.get("/logout")
    response = register(client)
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]
    page = client.get("/login")
    assert MSG_ALREADY_REGISTERED.encode().replace(b"'", b"&#39;") in page.data
    with app.app_context():
        assert len(db.session.execute(select(User)).scalars().all()) == 1


def test_home_navbar_differs_when_logged_in(client: FlaskClient) -> None:
    logged_out = client.get("/").data
    assert b"Login" in logged_out and b"Register" in logged_out
    assert b"Log Out" not in logged_out
    register(client)
    logged_in = client.get("/").data
    assert b"Log Out" in logged_in
    assert b"Register" not in logged_in
    assert b"you are already logged in" in logged_in
