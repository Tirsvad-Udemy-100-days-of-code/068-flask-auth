"""!
@file user_repository.py
@brief Port: how the business rules store and find users.
"""

from typing import Protocol

from flask_auth.domain.user import User


class UserRepository(Protocol):
    """!
    @brief Storage of users, implemented by an outer layer.
    """

    def find_by_email(self, email: str) -> User | None:
        """!
        @brief Find a user by email.
        @return The user, or None.
        """
        ...

    def find_by_id(self, user_id: int) -> User | None:
        """!
        @brief Find a user by id.
        @return The user, or None.
        """
        ...

    def add(self, user: User) -> User:
        """!
        @brief Store a new user.
        @return The stored user, with its id set.
        @throws EmailAlreadyRegisteredError When the email is taken.
        """
        ...
