"""!
@file extensions.py
@brief Flask extension instances, created once and bound to the app in the factory.
"""

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from flask_auth.constants import ENDPOINT_LOGIN


class Base(DeclarativeBase):
    """!
    @brief Typed declarative base of the database models.
    """


db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()
login_manager.login_view = ENDPOINT_LOGIN
