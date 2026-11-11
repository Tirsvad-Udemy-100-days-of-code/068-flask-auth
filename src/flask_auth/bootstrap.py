"""!
@file bootstrap.py
@brief Composition root: the one place that builds and wires the concrete parts.
"""

from collections.abc import Mapping
from typing import Any

from flask import Flask

from flask_auth.application.authenticate_user import AuthenticateUser
from flask_auth.application.get_user import GetUser
from flask_auth.application.register_user import RegisterUser
from flask_auth.infrastructure.config import build_config
from flask_auth.infrastructure.extensions import csrf, db, login_manager
from flask_auth.infrastructure.password_hasher import WerkzeugPasswordHasher
from flask_auth.infrastructure.user_repository import SqlAlchemyUserRepository
from flask_auth.presentation.login_adapter import register_user_loader
from flask_auth.presentation.routes import create_blueprint


def create_app(test_config: Mapping[str, Any] | None = None) -> Flask:
    """!
    @brief Application factory.
    @param test_config Optional settings that override the environment (tests).
    @return The configured Flask application.
    @throws MissingSecretKeyError When no secret key is configured.
    """
    app = Flask(__name__)
    app.config.from_mapping(build_config(test_config))

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    repository = SqlAlchemyUserRepository(db.session)
    hasher = WerkzeugPasswordHasher()
    register_user_loader(login_manager, GetUser(repository))
    app.register_blueprint(
        create_blueprint(
            RegisterUser(repository, hasher), AuthenticateUser(repository, hasher)
        )
    )
    with app.app_context():
        db.create_all()
    return app
