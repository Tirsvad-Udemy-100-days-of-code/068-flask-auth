"""!
@file __main__.py
@brief Run the development server: ``python -m flask_auth``.
"""

from flask_auth import create_app

if __name__ == "__main__":
    create_app().run(debug=True)
