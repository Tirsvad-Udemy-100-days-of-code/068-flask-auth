"""!
@file login_adapter.py
@brief Adapts the domain User to Flask-Login and reloads it from the session.
"""

from flask_login import LoginManager, UserMixin

from flask_auth.application.get_user import GetUser
from flask_auth.domain.user import User


class SessionUser(UserMixin):
    """!
    @brief Flask-Login view of a domain User.
    """

    def __init__(self, user: User) -> None:
        """!
        @param user The authenticated domain user.
        """
        self._user = user

    @property
    def name(self) -> str:
        """!
        @brief Display name of the user.
        """
        return self._user.name

    def get_id(self) -> str:
        """!
        @brief Identifier stored in the session cookie.
        @return The user id as text.
        """
        return str(self._user.id)


def register_user_loader(login_manager: LoginManager, get_user: GetUser) -> None:
    """!
    @brief Tell Flask-Login how to reload a user from the session.
    @param login_manager The login manager to configure.
    @param get_user Use case that finds a user by id.
    """

    @login_manager.user_loader
    def load_user(user_id: str) -> SessionUser | None:
        user = get_user.execute(int(user_id))
        return None if user is None else SessionUser(user)
