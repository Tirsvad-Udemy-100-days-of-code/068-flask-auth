"""Fakes of the application ports, for tests without a database or a framework."""

from dataclasses import replace

from flask_auth.domain.errors import EmailAlreadyRegisteredError
from flask_auth.domain.user import User

FAKE_HASH_PREFIX = "hashed:"


class FakePasswordHasher:
    """Reversible fake hash, so tests can see what was hashed."""

    def hash(self, plain_password: str) -> str:
        return FAKE_HASH_PREFIX + plain_password

    def verify(self, password_hash: str, plain_password: str) -> bool:
        return password_hash == self.hash(plain_password)


class InMemoryUserRepository:
    """User repository that keeps users in a dict."""

    def __init__(self) -> None:
        self._users: dict[int, User] = {}
        self.lookups_hide_users = False

    def find_by_email(self, email: str) -> User | None:
        if self.lookups_hide_users:
            return None
        return next((u for u in self._users.values() if u.email == email), None)

    def find_by_id(self, user_id: int) -> User | None:
        return self._users.get(user_id)

    def add(self, user: User) -> User:
        if any(u.email == user.email for u in self._users.values()):
            raise EmailAlreadyRegisteredError
        stored = replace(user, id=len(self._users) + 1)
        assert stored.id is not None
        self._users[stored.id] = stored
        return stored

    def count(self) -> int:
        return len(self._users)
