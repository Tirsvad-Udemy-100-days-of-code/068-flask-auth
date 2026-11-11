"""!
@file extensions.py
@brief Flask extension instances, created once and bound to the app in the factory.
"""

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from flask_auth.constants import LOGIN_ENDPOINT

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = LOGIN_ENDPOINT
