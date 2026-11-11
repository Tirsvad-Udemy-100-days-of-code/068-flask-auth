"""Unit tests of the User entity."""

import dataclasses

import pytest

from flask_auth.domain.errors import InvalidRegistrationError
from flask_auth.domain.user import User
from tests.support import TEST_EMAIL, TEST_NAME


def test_user_is_created_with_given_values() -> None:
    user = User(id=None, name=TEST_NAME, email=TEST_EMAIL, password_hash="h")
    assert (user.id, user.name, user.email, user.password_hash) == (
        None,
        TEST_NAME,
        TEST_EMAIL,
        "h",
    )


def test_user_is_immutable() -> None:
    user = User(id=1, name=TEST_NAME, email=TEST_EMAIL, password_hash="h")
    with pytest.raises(dataclasses.FrozenInstanceError):
        user.name = "Other"  # type: ignore[misc]


@pytest.mark.parametrize("blank", ["", "   "])
@pytest.mark.parametrize("field", ["name", "email", "password_hash"])
def test_user_creation_rejects_blank_field(field: str, blank: str) -> None:
    values = {
        "name": TEST_NAME,
        "email": TEST_EMAIL,
        "password_hash": "h",
        field: blank,
    }
    with pytest.raises(InvalidRegistrationError):
        User(id=None, **values)
