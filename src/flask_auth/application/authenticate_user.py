"""!
@file authenticate_user.py
@brief Use case: check an email and password.
"""

import logging

from flask_auth.application.ports import PasswordHasher
from flask_auth.domain.errors import UnknownEmailError, WrongPasswordError
from flask_auth.domain.user import User
from flask_auth.domain.user_repository import UserRepository

logger = logging.getLogger(__name__)


class AuthenticateUser:
    """!
    @brief Verifies credentials.
    """

    def __init__(self, repository: UserRepository, hasher: PasswordHasher) -> None:
        """!
        @param repository Where users are stored.
        @param hasher How passwords are checked.
        """
        self._repository = repository
        self._hasher = hasher

    def execute(self, email: str, plain_password: str) -> User:
        """!
        @brief Authenticate a user.
        @return The user whose credentials match.
        @throws UnknownEmailError When no user has the email.
        @throws WrongPasswordError When the password does not match.
        """
        user = self._repository.find_by_email(email)
        if user is None:
            logger.warning("Login failed: unknown email")
            raise UnknownEmailError
        if not self._hasher.verify(user.password_hash, plain_password):
            logger.warning("Login failed: wrong password for user id=%s", user.id)
            raise WrongPasswordError
        logger.info("Login succeeded: user id=%s", user.id)
        return user
