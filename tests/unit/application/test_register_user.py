"""Unit tests of the RegisterUser use case, with fake ports."""

import logging

import pytest

from flask_auth.application.register_user import RegisterUser
from flask_auth.domain.errors import (
    EmailAlreadyRegisteredError,
    InvalidRegistrationError,
)
from tests.support import TEST_EMAIL, TEST_NAME, TEST_PASSWORD
from tests.unit.fakes import FakePasswordHasher, InMemoryUserRepository


def make_use_case() -> tuple[RegisterUser, InMemoryUserRepository]:
    repository = InMemoryUserRepository()
    return RegisterUser(repository, FakePasswordHasher()), repository


def test_register_stores_user_with_hashed_password() -> None:
    use_case, repository = make_use_case()
    user = use_case.execute(TEST_NAME, TEST_EMAIL, TEST_PASSWORD)
    assert user.id is not None
    assert user.password_hash == FakePasswordHasher().hash(TEST_PASSWORD)
    assert user.password_hash != TEST_PASSWORD
    assert repository.find_by_email(TEST_EMAIL) == user


def test_register_raises_when_email_already_registered() -> None:
    use_case, repository = make_use_case()
    use_case.execute(TEST_NAME, TEST_EMAIL, TEST_PASSWORD)
    with pytest.raises(EmailAlreadyRegisteredError):
        use_case.execute(TEST_NAME, TEST_EMAIL, TEST_PASSWORD)
    assert repository.count() == 1


def test_register_raises_when_repository_reports_duplicate_after_lookup() -> None:
    use_case, repository = make_use_case()
    use_case.execute(TEST_NAME, TEST_EMAIL, TEST_PASSWORD)
    repository.lookups_hide_users = True
    with pytest.raises(EmailAlreadyRegisteredError):
        use_case.execute(TEST_NAME, TEST_EMAIL, TEST_PASSWORD)


@pytest.mark.parametrize(
    ("name", "email", "password"),
    [
        ("", TEST_EMAIL, TEST_PASSWORD),
        (TEST_NAME, "", TEST_PASSWORD),
        (TEST_NAME, TEST_EMAIL, ""),
        (TEST_NAME, TEST_EMAIL, "   "),
    ],
)
def test_register_rejects_empty_field(name: str, email: str, password: str) -> None:
    use_case, repository = make_use_case()
    with pytest.raises(InvalidRegistrationError):
        use_case.execute(name, email, password)
    assert repository.count() == 0


def test_register_logs_without_email_or_password(
    caplog: pytest.LogCaptureFixture,
) -> None:
    use_case, _ = make_use_case()
    with caplog.at_level(logging.INFO):
        use_case.execute(TEST_NAME, TEST_EMAIL, TEST_PASSWORD)
    assert caplog.records
    assert TEST_EMAIL not in caplog.text
    assert TEST_PASSWORD not in caplog.text
