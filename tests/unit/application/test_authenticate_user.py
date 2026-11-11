"""Unit tests of the AuthenticateUser use case, with fake ports."""

import logging

import pytest

from flask_auth.application.authenticate_user import AuthenticateUser
from flask_auth.application.get_user import GetUser
from flask_auth.application.register_user import RegisterUser
from flask_auth.domain.errors import UnknownEmailError, WrongPasswordError
from tests.support import (
    TEST_EMAIL,
    TEST_NAME,
    TEST_PASSWORD,
    TEST_UNKNOWN_EMAIL,
    TEST_WRONG_PASSWORD,
)
from tests.unit.fakes import FakePasswordHasher, InMemoryUserRepository


def make_use_case() -> tuple[AuthenticateUser, InMemoryUserRepository]:
    repository = InMemoryUserRepository()
    hasher = FakePasswordHasher()
    RegisterUser(repository, hasher).execute(TEST_NAME, TEST_EMAIL, TEST_PASSWORD)
    return AuthenticateUser(repository, hasher), repository


def test_authenticate_returns_user_for_correct_credentials() -> None:
    use_case, _ = make_use_case()
    assert use_case.execute(TEST_EMAIL, TEST_PASSWORD).email == TEST_EMAIL


def test_authenticate_raises_for_unknown_email() -> None:
    use_case, _ = make_use_case()
    with pytest.raises(UnknownEmailError):
        use_case.execute(TEST_UNKNOWN_EMAIL, TEST_PASSWORD)


def test_authenticate_raises_for_wrong_password() -> None:
    use_case, _ = make_use_case()
    with pytest.raises(WrongPasswordError):
        use_case.execute(TEST_EMAIL, TEST_WRONG_PASSWORD)


def test_authenticate_logs_failure_without_email_or_password(
    caplog: pytest.LogCaptureFixture,
) -> None:
    use_case, _ = make_use_case()
    with caplog.at_level(logging.INFO), pytest.raises(WrongPasswordError):
        use_case.execute(TEST_EMAIL, TEST_WRONG_PASSWORD)
    assert caplog.records
    assert TEST_EMAIL not in caplog.text
    assert TEST_WRONG_PASSWORD not in caplog.text


def test_get_user_finds_existing_and_returns_none_for_missing() -> None:
    _, repository = make_use_case()
    existing = repository.find_by_email(TEST_EMAIL)
    assert existing is not None
    assert existing.id is not None
    get_user = GetUser(repository)
    assert get_user.execute(existing.id) == existing
    assert get_user.execute(existing.id + 1) is None
