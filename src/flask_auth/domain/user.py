"""!
@file user.py
@brief The User entity.
"""

from dataclasses import dataclass

from flask_auth.domain.errors import InvalidRegistrationError


@dataclass(frozen=True, slots=True)
class User:
    """!
    @brief A registered user. Holds only a password hash, never the password.
    """

    id: int | None
    name: str
    email: str
    password_hash: str

    def __post_init__(self) -> None:
        """!
        @brief Reject a user with an empty name, email or password hash.
        @throws InvalidRegistrationError When one of those fields is blank.
        """
        values = (self.name, self.email, self.password_hash)
        if not all(value.strip() for value in values):
            raise InvalidRegistrationError
