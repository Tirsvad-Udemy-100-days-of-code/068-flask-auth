"""Fixtures for route-level tests: an app on an in-memory database and a client."""

import re
from collections.abc import Iterator

import pytest
from flask import Flask
from flask.testing import FlaskClient
from werkzeug.test import TestResponse

from flask_auth import create_app
from flask_auth.constants import (
    FIELD_CSRF_TOKEN,
    FIELD_EMAIL,
    FIELD_NAME,
    FIELD_PASSWORD,
    PATH_LOGIN,
    PATH_REGISTER,
)
from flask_auth.infrastructure.extensions import db
from tests.support import (
    TEST_EMAIL,
    TEST_IN_MEMORY_DATABASE_URI,
    TEST_NAME,
    TEST_PASSWORD,
    TEST_SECRET_KEY,
)

CSRF_INPUT_PATTERN = re.compile(
    rf'<input type="hidden" name="{FIELD_CSRF_TOKEN}" value="([^"]+)"'
)


@pytest.fixture
def app() -> Iterator[Flask]:
    """App on a fresh in-memory SQLite database."""
    app = create_app(
        {
            "TESTING": True,
            "SECRET_KEY": TEST_SECRET_KEY,
            "SQLALCHEMY_DATABASE_URI": TEST_IN_MEMORY_DATABASE_URI,
        }
    )
    yield app
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """Test client with its own cookie jar."""
    return app.test_client()


def fetch_csrf_token(client: FlaskClient, path: str) -> str:
    """Read the hidden CSRF token from the form page at `path`."""
    page = client.get(path).get_data(as_text=True)
    match = CSRF_INPUT_PATTERN.search(page)
    assert match is not None, f"no {FIELD_CSRF_TOKEN} input on {path}"
    return match.group(1)


def register(
    client: FlaskClient,
    email: str = TEST_EMAIL,
    name: str = TEST_NAME,
    password: str = TEST_PASSWORD,
) -> TestResponse:
    """Register through the form, with its token; return the POST response."""
    return client.post(
        PATH_REGISTER,
        data={
            FIELD_NAME: name,
            FIELD_EMAIL: email,
            FIELD_PASSWORD: password,
            FIELD_CSRF_TOKEN: fetch_csrf_token(client, PATH_REGISTER),
        },
    )


def login(
    client: FlaskClient,
    email: str = TEST_EMAIL,
    password: str = TEST_PASSWORD,
) -> TestResponse:
    """Log in through the form, with the form's token; return the POST response."""
    return client.post(
        PATH_LOGIN,
        data={
            FIELD_EMAIL: email,
            FIELD_PASSWORD: password,
            FIELD_CSRF_TOKEN: fetch_csrf_token(client, PATH_LOGIN),
        },
    )
