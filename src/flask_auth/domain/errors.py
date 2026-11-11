"""!
@file errors.py
@brief Errors raised by the business rules.
"""


class DomainError(Exception):
    """!
    @brief Base class of every error the business rules raise.
    """


class EmailAlreadyRegisteredError(DomainError):
    """!
    @brief A user with that email already exists.
    """


class UnknownEmailError(DomainError):
    """!
    @brief No user has that email.
    """


class WrongPasswordError(DomainError):
    """!
    @brief The password does not match the stored hash.
    """


class InvalidRegistrationError(DomainError):
    """!
    @brief A required registration field is empty.
    """
