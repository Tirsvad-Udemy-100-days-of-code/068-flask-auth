"""Integration tests of the SQLAlchemy repository on in-memory SQLite."""

from collections.abc import Iterator

import pytest
from flask import Flask

from flask_auth import create_app
from flask_auth.domain.errors import EmailAlreadyRegisteredError
from flask_auth.domain.user import User
from flask_auth.infrastructure.extensions import db
from flask_auth.infrastructure.user_repository import SqlAlchemyUserRepository
from tests.support import (
    TEST_EMAIL,
    TEST_IN_MEMORY_DATABASE_URI,
    TEST_NAME,
    TEST_SECRET_KEY,
)


@pytest.fixture
def repository() -> Iterator[SqlAlchemyUserRepository]:
    app: Flask = create_app(
        {
            "TESTING": True,
            "SECRET_KEY": TEST_SECRET_KEY,
            "SQLALCHEMY_DATABASE_URI": TEST_IN_MEMORY_DATABASE_URI,
        }
    )
    with app.app_context():
        yield SqlAlchemyUserRepository(db.session)
        db.session.remove()
        db.drop_all()


def new_user(email: str = TEST_EMAIL) -> User:
    return User(id=None, name=TEST_NAME, email=email, password_hash="hash")


def test_add_returns_user_with_id_and_it_can_be_found(
    repository: SqlAlchemyUserRepository,
) -> None:
    stored = repository.add(new_user())
    assert stored.id is not None
    assert repository.find_by_email(TEST_EMAIL) == stored
    assert repository.find_by_id(stored.id) == stored


def test_find_returns_none_when_user_is_missing(
    repository: SqlAlchemyUserRepository,
) -> None:
    assert repository.find_by_email(TEST_EMAIL) is None
    assert repository.find_by_id(1) is None


def test_add_maps_unique_email_violation_to_domain_error(
    repository: SqlAlchemyUserRepository,
) -> None:
    repository.add(new_user())
    with pytest.raises(EmailAlreadyRegisteredError):
        repository.add(new_user())


def test_repository_is_usable_after_duplicate_email_error(
    repository: SqlAlchemyUserRepository,
) -> None:
    repository.add(new_user())
    with pytest.raises(EmailAlreadyRegisteredError):
        repository.add(new_user())
    other = repository.add(new_user("other@example.com"))
    assert other.id is not None
