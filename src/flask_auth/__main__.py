"""!
@file __main__.py
@brief Run the development server: ``python -m flask_auth``.
"""

from flask_auth.bootstrap import create_app
from flask_auth.infrastructure.config import is_debug_enabled
from flask_auth.infrastructure.logging_setup import configure_logging


def main() -> None:
    """!
    @brief Start the server; debug mode only when FLASK_AUTH_DEBUG=1.
    """
    configure_logging()
    create_app().run(debug=is_debug_enabled())


if __name__ == "__main__":
    main()
