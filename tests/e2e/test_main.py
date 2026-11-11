"""Tests of the program entry point: debug is off unless asked for."""

import pytest

from flask_auth import __main__ as entry_point
from flask_auth.constants import ENV_DEBUG, ENV_DEBUG_ENABLED_VALUE


class RecordingApp:
    """Stand-in for the Flask app that records how run() was called."""

    def __init__(self) -> None:
        self.debug: bool | None = None

    def run(self, *, debug: bool) -> None:
        self.debug = debug


def run_main(monkeypatch: pytest.MonkeyPatch) -> RecordingApp:
    app = RecordingApp()
    monkeypatch.setattr(entry_point, "create_app", lambda: app)
    monkeypatch.setattr(entry_point, "configure_logging", lambda: None)
    entry_point.main()
    return app


def test_main_runs_without_debug_by_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(ENV_DEBUG, raising=False)
    assert run_main(monkeypatch).debug is False


def test_main_runs_with_debug_when_environment_variable_is_set(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv(ENV_DEBUG, ENV_DEBUG_ENABLED_VALUE)
    assert run_main(monkeypatch).debug is True
