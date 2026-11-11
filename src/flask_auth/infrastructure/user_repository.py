"""!
@file user_repository.py
@brief SQLAlchemy implementation of the UserRepository port.
"""

from flask_sqlalchemy.session import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session

from flask_auth.domain.errors import EmailAlreadyRegisteredError
from flask_auth.domain.user import User
from flask_auth.infrastructure.models import UserRecord


def _to_domain(record: UserRecord) -> User:
    return User(
        id=record.id,
        name=record.name,
        email=record.email,
        password_hash=record.password,
    )


class SqlAlchemyUserRepository:
    """!
    @brief Stores users in a relational database through a SQLAlchemy session.
    """

    def __init__(self, session: scoped_session[Session]) -> None:
        """!
        @param session The session used for every query.
        """
        self._session = session

    def find_by_email(self, email: str) -> User | None:
        """!
        @brief Find a user by email.
        @return The user, or None.
        """
        record = self._session.execute(
            select(UserRecord).where(UserRecord.email == email)
        ).scalar()
        return None if record is None else _to_domain(record)

    def find_by_id(self, user_id: int) -> User | None:
        """!
        @brief Find a user by id.
        @return The user, or None.
        """
        record = self._session.get(UserRecord, user_id)
        return None if record is None else _to_domain(record)

    def add(self, user: User) -> User:
        """!
        @brief Store a new user.
        @return The stored user, with its id set.
        @throws EmailAlreadyRegisteredError When the unique email is taken, also
            when another request inserted it after the caller's lookup.
        """
        record = UserRecord(
            name=user.name, email=user.email, password=user.password_hash
        )
        self._session.add(record)
        try:
            self._session.commit()
        except IntegrityError as error:
            self._session.rollback()
            raise EmailAlreadyRegisteredError from error
        return _to_domain(record)
