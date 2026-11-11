"""!
@file config.py
@brief Application settings, read from the environment.
"""

import os
from collections.abc import Mapping
from typing import Any

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


class MissingSecretKeyError(RuntimeError):
    """!
    @brief No secret key is configured; the app refuses to start.
    """


def build_config(overrides: Mapping[str, Any] | None = None) -> dict[str, Any]:
    """!
    @brief Build the Flask settings from the environment and optional overrides.
    @param overrides Settings that win over the environment (used in tests).
    @return The settings.
    @throws MissingSecretKeyError When no secret key is set anywhere.
    """
    config: dict[str, Any] = {
        CONFIG_DATABASE_URI: os.environ.get(ENV_DATABASE_URI, DEFAULT_DATABASE_URI),
    }
    secret_key = os.environ.get(ENV_SECRET_KEY)
    if secret_key:
        config[CONFIG_SECRET_KEY] = secret_key
    if overrides:
        config.update(overrides)
    if not config.get(CONFIG_SECRET_KEY):
        raise MissingSecretKeyError(MSG_SECRET_KEY_MISSING)
    return config


def is_debug_enabled() -> bool:
    """!
    @brief Tell whether the debug server is switched on; off unless asked for.
    @return True only when the debug environment variable is "1".
    """
    return os.environ.get(ENV_DEBUG) == ENV_DEBUG_ENABLED_VALUE
