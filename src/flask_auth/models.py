"""!
@file models.py
@brief Database models.
"""

from flask_login import UserMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

from flask_auth.constants import PASSWORD_HASH_METHOD, PASSWORD_SALT_LENGTH
from flask_auth.extensions import db, login_manager


class User(UserMixin, db.Model):
    """!
    @brief A registered user. The password is stored only as a salted hash.
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    name: Mapped[str] = mapped_column(String(1000))

    @classmethod
    def create(cls, name: str, email: str, plain_password: str) -> "User":
        """!
        @brief Build a user whose password is hashed and salted.
        @param name Display name.
        @param email Unique login email.
        @param plain_password Password in clear text; never stored.
        @return A new, unsaved User.
        """
        hashed = generate_password_hash(
            plain_password,
            method=PASSWORD_HASH_METHOD,
            salt_length=PASSWORD_SALT_LENGTH,
        )
        return cls(name=name, email=email, password=hashed)

    def check_password(self, plain_password: str) -> bool:
        """!
        @brief Check a password against the stored hash.
        @param plain_password Password in clear text.
        @return True when it matches.
        """
        return check_password_hash(self.password, plain_password)


@login_manager.user_loader
def load_user(user_id: str) -> User | None:
    """!
    @brief Reload the user stored in the session.
    @param user_id The user id from the session cookie.
    @return The user, or None when it no longer exists.
    """
    return db.session.get(User, int(user_id))
