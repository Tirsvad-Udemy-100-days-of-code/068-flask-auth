"""Tests that every page loads Bootstrap with SRI and uses its markup."""

import re
from urllib.parse import urlparse

import pytest
from flask.testing import FlaskClient

from flask_auth.constants import (
    FIELD_CSRF_TOKEN,
    FIELD_EMAIL,
    FIELD_NAME,
    FIELD_PASSWORD,
    MSG_PASSWORD_WRONG,
    PATH_DOWNLOAD,
    PATH_HOME,
    PATH_LOGIN,
    PATH_LOGOUT,
    PATH_REGISTER,
    PATH_SECRETS,
)
from tests.e2e.conftest import fetch_all_pages, login, logout, register
from tests.support import (
    ALLOWED_ASSET_HOST,
    BRAND_TEXT,
    FIELD_PLACEHOLDERS,
    PATH_STATIC_DOWNLOAD,
    PATH_STYLESHEET,
    TEST_NAME,
    TEST_WRONG_PASSWORD,
    heading_pattern,
    label_pattern,
)

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
ASSET_URL_PATTERN = re.compile(r'<(?:link|script)[^>]*\b(?:href|src)="([^"]+)"')
BRAND_PATTERN = re.compile(rf'<a class="navbar-brand"[^>]*>{BRAND_TEXT}</a>')
NAV_LINK_HREFS_LOGGED_OUT = [PATH_HOME, PATH_LOGIN, PATH_REGISTER]
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
        assert re.search(label_pattern(field), page)
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
    assert BRAND_PATTERN.search(page)
    assert f'href="{PATH_LOGIN}"' not in page
    assert f'href="{PATH_REGISTER}"' not in page


def test_logged_out_navbar_links_home_login_and_register_with_brand(
    client: FlaskClient,
) -> None:
    page = client.get(PATH_HOME).get_data(as_text=True)
    assert BRAND_PATTERN.search(page)
    for href in NAV_LINK_HREFS_LOGGED_OUT:
        assert f'class="nav-link" href="{href}"' in page
    assert f'action="{PATH_LOGOUT}"' not in page


@pytest.mark.parametrize("path", [PATH_REGISTER, PATH_LOGIN])
def test_inputs_have_placeholders_and_hidden_csrf_token(
    client: FlaskClient, path: str
) -> None:
    page = client.get(path).get_data(as_text=True)
    for field in FORM_FIELDS[path]:
        assert f'placeholder="{FIELD_PLACEHOLDERS[field]}"' in page
    assert f'<input type="hidden" name="{FIELD_CSRF_TOKEN}"' in page


def test_page_headings_and_actions_follow_the_lecture_texts(
    client: FlaskClient,
) -> None:
    pages = fetch_all_pages(client)
    expected = {
        "home": [BRAND_TEXT, f'href="{PATH_LOGIN}"', f'href="{PATH_REGISTER}"'],
        "register": ["Register", "Sign me up."],
        "login": ["Login", "Let me in."],
        "secrets": [f"Welcome, {TEST_NAME}!", f'href="{PATH_DOWNLOAD}"'],
    }
    for label, texts in expected.items():
        assert re.search(heading_pattern(re.escape(texts[0])), pages[label]), label
        for text in texts[1:]:
            assert text in pages[label], f"{text} on {label}"
    assert "(you are already logged in)" in pages["home-logged-in"]
    assert f'href="{PATH_SECRETS}"' in pages["home-logged-in"]
    assert "Download Your File" in pages["secrets"]


def test_pages_link_assets_only_from_the_bootstrap_cdn_host(
    client: FlaskClient,
) -> None:
    for label, page in fetch_all_pages(client).items():
        for url in ASSET_URL_PATTERN.findall(page):
            host = urlparse(url).netloc
            assert host in ("", ALLOWED_ASSET_HOST), f"{url} on {label}"
