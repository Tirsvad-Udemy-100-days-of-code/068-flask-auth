"""!
@file password_hasher.py
@brief Werkzeug implementation of the PasswordHasher port.
"""

from werkzeug.security import check_password_hash, generate_password_hash

from flask_auth.constants import PASSWORD_HASH_METHOD, PASSWORD_SALT_LENGTH


class WerkzeugPasswordHasher:
    """!
    @brief Salted password hashing with a configurable method and salt length.
    """

    def __init__(
        self,
        method: str = PASSWORD_HASH_METHOD,
        salt_length: int = PASSWORD_SALT_LENGTH,
    ) -> None:
        """!
        @param method Werkzeug hash method.
        @param salt_length Length of the random salt.
        """
        self._method = method
        self._salt_length = salt_length

    def hash(self, plain_password: str) -> str:
        """!
        @brief Hash a password with a fresh salt.
        @return The salted hash.
        """
        return generate_password_hash(
            plain_password, method=self._method, salt_length=self._salt_length
        )

    def verify(self, password_hash: str, plain_password: str) -> bool:
        """!
        @brief Check a password against a hash.
        @return True when it matches.
        """
        return check_password_hash(password_hash, plain_password)
