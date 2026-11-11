"""Fixtures for route-level tests: an app on an in-memory database and a client."""

from collections.abc import Iterator

import pytest
from flask import Flask
from flask.testing import FlaskClient
from werkzeug.test import TestResponse

from flask_auth import create_app
from flask_auth.constants import FIELD_EMAIL, FIELD_NAME, FIELD_PASSWORD, PATH_REGISTER
from flask_auth.infrastructure.extensions import db
from tests.support import (
    TEST_EMAIL,
    TEST_IN_MEMORY_DATABASE_URI,
    TEST_NAME,
    TEST_PASSWORD,
    TEST_SECRET_KEY,
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


def register(
    client: FlaskClient,
    email: str = TEST_EMAIL,
    name: str = TEST_NAME,
    password: str = TEST_PASSWORD,
) -> TestResponse:
    """Register a user through the form and return the response to the POST."""
    return client.post(
        PATH_REGISTER,
        data={FIELD_NAME: name, FIELD_EMAIL: email, FIELD_PASSWORD: password},
    )
