"""Tests that every page loads Bootstrap with SRI and uses its markup."""

import re

import pytest
from flask.testing import FlaskClient

from flask_auth.constants import (
    FIELD_CSRF_TOKEN,
    FIELD_EMAIL,
    FIELD_NAME,
    FIELD_PASSWORD,
    MSG_PASSWORD_WRONG,
    PATH_HOME,
    PATH_LOGIN,
    PATH_LOGOUT,
    PATH_REGISTER,
)
from tests.e2e.conftest import fetch_all_pages, login, logout, register
from tests.support import PATH_STATIC_DOWNLOAD, PATH_STYLESHEET, TEST_WRONG_PASSWORD

BOOTSTRAP_VERSION = "5.3.3"
BOOTSTRAP_CSS_URL = (
    f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/css/"
    "bootstrap.min.css"
)
BOOTSTRAP_JS_URL = (
    f"https://cdn.jsdelivr.net/npm/bootstrap@{BOOTSTRAP_VERSION}/dist/js/"
    "bootstrap.bundle.min.js"
)
SRI_ATTRIBUTE_PATTERN = r'integrity="sha384-[A-Za-z0-9+/]+=*" crossorigin="anonymous"'
STYLESHEET_TAG_PATTERN = re.compile(
    rf'<link rel="stylesheet" href="{re.escape(BOOTSTRAP_CSS_URL)}" '
    rf"{SRI_ATTRIBUTE_PATTERN}>"
)
SCRIPT_TAG_PATTERN = re.compile(
    rf'<script src="{re.escape(BOOTSTRAP_JS_URL)}" {SRI_ATTRIBUTE_PATTERN}></script>'
)
VIEWPORT_META = '<meta name="viewport" content="width=device-width, initial-scale=1">'
ALERT_PATTERN = re.compile(r'<div class="alert[^"]*" role="alert">([^<]+)</div>')
FORM_FIELDS = {
    PATH_REGISTER: [FIELD_NAME, FIELD_EMAIL, FIELD_PASSWORD],
    PATH_LOGIN: [FIELD_EMAIL, FIELD_PASSWORD],
}


def test_every_page_loads_bootstrap_with_pinned_version_and_sri(
    client: FlaskClient,
) -> None:
    for label, page in fetch_all_pages(client).items():
        assert STYLESHEET_TAG_PATTERN.search(page), f"stylesheet tag on {label}"
        assert SCRIPT_TAG_PATTERN.search(page), f"script tag on {label}"
        assert VIEWPORT_META in page, f"viewport meta on {label}"
        assert PATH_STYLESHEET in page, f"own stylesheet link on {label}"


def test_own_stylesheet_is_served_with_status_200(client: FlaskClient) -> None:
    response = client.get(PATH_STYLESHEET)
    assert response.status_code == 200
    assert response.mimetype == "text/css"
    response.close()


def test_download_file_is_not_served_as_public_static_file(
    client: FlaskClient,
) -> None:
    response = client.get(PATH_STATIC_DOWNLOAD)
    assert response.status_code == 404
    response.close()


@pytest.mark.parametrize("path", [PATH_REGISTER, PATH_LOGIN])
def test_form_fields_have_labels_bound_to_inputs_and_form_control_class(
    client: FlaskClient, path: str
) -> None:
    page = client.get(path).get_data(as_text=True)
    for field in FORM_FIELDS[path]:
        assert re.search(rf'<label for="{field}" class="form-label">', page)
        assert re.search(
            rf'<input [^>]*id="{field}"[^>]*name="{field}"[^>]*class="form-control"',
            page,
        )
    assert f'<input type="hidden" name="{FIELD_CSRF_TOKEN}"' in page


def test_flash_message_renders_as_alert_with_role(client: FlaskClient) -> None:
    register(client)
    logout(client)
    page = login(client, password=TEST_WRONG_PASSWORD).get_data(as_text=True)
    match = ALERT_PATTERN.search(page)
    assert match is not None
    assert match.group(1) == MSG_PASSWORD_WRONG


def test_logged_in_navbar_keeps_logout_form_inside_responsive_navbar(
    client: FlaskClient,
) -> None:
    register(client)
    page = client.get(PATH_HOME).get_data(as_text=True)
    assert "navbar navbar-expand-lg" in page
    assert f'<form action="{PATH_LOGOUT}" method="post">' in page
    assert f'<input type="hidden" name="{FIELD_CSRF_TOKEN}"' in page
    assert f'href="{PATH_LOGOUT}"' not in page
