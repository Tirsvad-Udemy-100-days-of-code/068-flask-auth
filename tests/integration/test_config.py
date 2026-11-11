"""Tests of configuration: fail fast without a secret key, opt-in debug."""

import pytest

from flask_auth import create_app
from flask_auth.constants import (
    CONFIG_DATABASE_URI,
    CONFIG_SECRET_KEY,
    DEFAULT_DATABASE_URI,
    ENV_DATABASE_URI,
    ENV_DEBUG,
    ENV_DEBUG_ENABLED_VALUE,
    ENV_SECRET_KEY,
    MSG_SECRET_KEY_MISSING,
)
from flask_auth.infrastructure.config import (
    MissingSecretKeyError,
    build_config,
    is_debug_enabled,
)
from tests.support import TEST_SECRET_KEY


def test_build_config_fails_fast_without_secret_key(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv(ENV_SECRET_KEY, raising=False)
    with pytest.raises(MissingSecretKeyError, match=ENV_SECRET_KEY):
        build_config()


def test_build_config_fails_for_empty_secret_key(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(ENV_SECRET_KEY, "")
    with pytest.raises(MissingSecretKeyError, match=MSG_SECRET_KEY_MISSING):
        build_config()


def test_create_app_fails_fast_without_secret_key(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv(ENV_SECRET_KEY, raising=False)
    with pytest.raises(MissingSecretKeyError):
        create_app()


def test_build_config_reads_secret_key_and_database_from_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(ENV_SECRET_KEY, TEST_SECRET_KEY)
    monkeypatch.setenv(ENV_DATABASE_URI, "sqlite://")
    config = build_config()
    assert config[CONFIG_SECRET_KEY] == TEST_SECRET_KEY
    assert config[CONFIG_DATABASE_URI] == "sqlite://"


def test_build_config_uses_default_database_when_not_set(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv(ENV_DATABASE_URI, raising=False)
    config = build_config({CONFIG_SECRET_KEY: TEST_SECRET_KEY})
    assert config[CONFIG_DATABASE_URI] == DEFAULT_DATABASE_URI


def test_debug_is_off_by_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(ENV_DEBUG, raising=False)
    assert is_debug_enabled() is False


def test_debug_is_on_only_when_environment_variable_is_set(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(ENV_DEBUG, ENV_DEBUG_ENABLED_VALUE)
    assert is_debug_enabled() is True
    monkeypatch.setenv(ENV_DEBUG, "0")
    assert is_debug_enabled() is False
