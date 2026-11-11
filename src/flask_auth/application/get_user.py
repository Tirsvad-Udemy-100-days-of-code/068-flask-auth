"""!
@file get_user.py
@brief Use case: reload a user from the id kept in the session.
"""

from flask_auth.domain.user import User
from flask_auth.domain.user_repository import UserRepository


class GetUser:
    """!
    @brief Finds a user by id.
    """

    def __init__(self, repository: UserRepository) -> None:
        """!
        @param repository Where users are stored.
        """
        self._repository = repository

    def execute(self, user_id: int) -> User | None:
        """!
        @brief Find a user.
        @return The user, or None when it no longer exists.
        """
        return self._repository.find_by_id(user_id)
