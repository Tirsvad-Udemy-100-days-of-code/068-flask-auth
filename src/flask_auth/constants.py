"""!
@file constants.py
@brief Constants shared by the application (no magic strings in the code).
"""

PASSWORD_HASH_METHOD = "pbkdf2:sha256"
PASSWORD_SALT_LENGTH = 8

DOWNLOAD_DIRECTORY = "static/files"
DOWNLOAD_FILENAME = "cheat_sheet.pdf"

DEFAULT_DATABASE_URI = "sqlite:///users.db"

BLUEPRINT_NAME = "main"
ENDPOINT_HOME = "main.home"
ENDPOINT_LOGIN = "main.login"
ENDPOINT_SECRETS = "main.secrets"

PATH_HOME = "/"
PATH_REGISTER = "/register"
PATH_LOGIN = "/login"
PATH_SECRETS = "/secrets"
PATH_LOGOUT = "/logout"
PATH_DOWNLOAD = "/download"

FIELD_NAME = "name"
FIELD_EMAIL = "email"
FIELD_PASSWORD = "password"

TEMPLATE_INDEX = "index.html"
TEMPLATE_LOGIN = "login.html"
TEMPLATE_REGISTER = "register.html"
TEMPLATE_SECRETS = "secrets.html"

CONFIG_SECRET_KEY = "SECRET_KEY"
CONFIG_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"

ENV_SECRET_KEY = "SECRET_KEY"
ENV_DATABASE_URI = "DATABASE_URI"
ENV_DEBUG = "FLASK_AUTH_DEBUG"
ENV_DEBUG_ENABLED_VALUE = "1"

MSG_EMAIL_UNKNOWN = "That email does not exist, please try again."
MSG_PASSWORD_WRONG = "Password incorrect, please try again."
MSG_ALREADY_REGISTERED = "You've already signed up with that email, log in instead!"
MSG_FIELDS_REQUIRED = "Name, email and password are all required."
MSG_SECRET_KEY_MISSING = (
    "SECRET_KEY is not set. Set the SECRET_KEY environment variable "
    "to a long random value before starting the app."
)
