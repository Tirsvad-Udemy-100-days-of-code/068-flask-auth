"""!
@file register_user.py
@brief Use case: register a new user.
"""

import logging

from flask_auth.application.ports import PasswordHasher
from flask_auth.domain.errors import (
    EmailAlreadyRegisteredError,
    InvalidRegistrationError,
)
from flask_auth.domain.user import User
from flask_auth.domain.user_repository import UserRepository

logger = logging.getLogger(__name__)


class RegisterUser:
    """!
    @brief Creates a user with a hashed password.
    """

    def __init__(self, repository: UserRepository, hasher: PasswordHasher) -> None:
        """!
        @param repository Where users are stored.
        @param hasher How passwords are hashed.
        """
        self._repository = repository
        self._hasher = hasher

    def execute(self, name: str, email: str, plain_password: str) -> User:
        """!
        @brief Register a user.
        @return The stored user.
        @throws InvalidRegistrationError When a field is empty.
        @throws EmailAlreadyRegisteredError When the email is taken.
        """
        try:
            stored = self._register(name, email, plain_password)
        except InvalidRegistrationError:
            logger.warning("Registration rejected: empty field")
            raise
        except EmailAlreadyRegisteredError:
            logger.warning("Registration rejected: email already registered")
            raise
        logger.info("User registered: id=%s", stored.id)
        return stored

    def _register(self, name: str, email: str, plain_password: str) -> User:
        if not plain_password.strip():
            raise InvalidRegistrationError
        if self._repository.find_by_email(email) is not None:
            raise EmailAlreadyRegisteredError
        user = User(
            id=None,
            name=name,
            email=email,
            password_hash=self._hasher.hash(plain_password),
        )
        return self._repository.add(user)
