"""!
@file ports.py
@brief Ports the use cases need from outside the business rules.
"""

from typing import Protocol


class PasswordHasher(Protocol):
    """!
    @brief Salted one-way hashing of passwords.
    """

    def hash(self, plain_password: str) -> str:
        """!
        @brief Hash a password.
        @return The salted hash.
        """
        ...

    def verify(self, password_hash: str, plain_password: str) -> bool:
        """!
        @brief Check a password against a hash.
        @return True when it matches.
        """
        ...
