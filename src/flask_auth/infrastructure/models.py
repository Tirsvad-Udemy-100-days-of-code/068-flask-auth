"""!
@file models.py
@brief Database mapping of the user table.
"""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from flask_auth.infrastructure.extensions import Base


class UserRecord(Base):
    """!
    @brief One row of the user table; the domain User is mapped to and from it.
    """

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(200))
    name: Mapped[str] = mapped_column(String(1000))
