"""!
@file constants.py
@brief Constants shared by the application (no magic strings in the code).
"""

PASSWORD_HASH_METHOD = "pbkdf2:sha256"
PASSWORD_SALT_LENGTH = 8

DOWNLOAD_DIRECTORY = "static/files"
DOWNLOAD_FILENAME = "cheat_sheet.pdf"

DEFAULT_DATABASE_URI = "sqlite:///users.db"
DEFAULT_SECRET_KEY = "dev-only-change-me"  # Development default; set SECRET_KEY in production.

BLUEPRINT_NAME = "main"
ENDPOINT_HOME = "main.home"
ENDPOINT_LOGIN = "main.login"
ENDPOINT_SECRETS = "main.secrets"
LOGIN_ENDPOINT = ENDPOINT_LOGIN

FIELD_NAME = "name"
FIELD_EMAIL = "email"
FIELD_PASSWORD = "password"

TEMPLATE_INDEX = "index.html"
TEMPLATE_LOGIN = "login.html"
TEMPLATE_REGISTER = "register.html"
TEMPLATE_SECRETS = "secrets.html"

ENV_SECRET_KEY = "SECRET_KEY"
ENV_DATABASE_URI = "DATABASE_URI"

MSG_EMAIL_UNKNOWN = "That email does not exist, please try again."
MSG_PASSWORD_WRONG = "Password incorrect, please try again."
MSG_ALREADY_REGISTERED = "You've already signed up with that email, log in instead!"
