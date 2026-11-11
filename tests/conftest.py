"""Shared pytest fixtures: an app with an in-memory database and a client."""

from collections.abc import Iterator

import pytest
from flask import Flask
from flask.testing import FlaskClient
from werkzeug.test import TestResponse

from flask_auth import create_app
from flask_auth.extensions import db

TEST_PASSWORD = "correct horse battery"


@pytest.fixture
def app() -> Iterator[Flask]:
    """App on a fresh in-memory SQLite database."""
    app = create_app(
        {
            "TESTING": True,
            "SECRET_KEY": "test",
            "SQLALCHEMY_DATABASE_URI": "sqlite://",
        }
    )
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """Test client with its own cookie jar."""
    return app.test_client()


def register(client: FlaskClient, email: str = "ada@example.com", name: str = "Ada") -> TestResponse:
    """!
    @brief Register a user through the form.
    @return The response to the POST.
    """
    return client.post(
        "/register",
        data={"name": name, "email": email, "password": TEST_PASSWORD},
    )
