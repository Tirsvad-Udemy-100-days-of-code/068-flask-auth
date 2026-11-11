"""!
@file __init__.py
@brief Flask authentication walkthrough (Udemy 100 Days of Code, day 68).
"""

import os
from collections.abc import Mapping
from typing import Any

from flask import Flask

from flask_auth.constants import (
    DEFAULT_DATABASE_URI,
    DEFAULT_SECRET_KEY,
    ENV_DATABASE_URI,
    ENV_SECRET_KEY,
)
from flask_auth.extensions import db, login_manager


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    """!
    @brief Application factory.
    @param test_config Optional settings that override the defaults (used in tests).
    @return The configured Flask application.
    """
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get(ENV_SECRET_KEY, DEFAULT_SECRET_KEY),
        SQLALCHEMY_DATABASE_URI=os.environ.get(ENV_DATABASE_URI, DEFAULT_DATABASE_URI),
    )
    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    login_manager.init_app(app)

    from flask_auth import models  # noqa: F401  (registers the user loader)
    from flask_auth.routes import main

    app.register_blueprint(main)
    with app.app_context():
        db.create_all()
    return app
