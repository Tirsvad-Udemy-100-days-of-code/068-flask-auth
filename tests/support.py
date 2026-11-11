"""Test data shared by several test modules."""

TEST_NAME = "Ada"
TEST_EMAIL = "ada@example.com"
TEST_OTHER_EMAIL = "bob@example.com"
TEST_UNKNOWN_EMAIL = "nobody@example.com"
TEST_PASSWORD = "correct horse battery"
TEST_WRONG_PASSWORD = "not-the-right-one"
TEST_SECRET_KEY = "test-secret-key"
TEST_IN_MEMORY_DATABASE_URI = "sqlite://"
PATH_STYLESHEET = "/static/css/app.css"
PATH_STATIC_DOWNLOAD = "/static/files/cheat_sheet.pdf"
BRAND_TEXT = "Flask Authentication"
ALLOWED_ASSET_HOST = "cdn.jsdelivr.net"
HIDDEN_LABEL_CLASS = "visually-hidden"
FIELD_PLACEHOLDERS = {"name": "Name", "email": "Email", "password": "Password"}


def heading_pattern(text: str) -> str:
    """Regex that matches the page's single h1 with exactly `text`."""
    return rf"<h1[^>]*>\s*{text}\s*</h1>"


def label_pattern(field: str) -> str:
    """Regex for the visually hidden label bound to the input `field`."""
    return rf'<label for="{field}" class="[^"]*{HIDDEN_LABEL_CLASS}[^"]*">'
