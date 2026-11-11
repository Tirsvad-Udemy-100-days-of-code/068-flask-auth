"""!
@file logging_setup.py
@brief Logging configuration for the running program.
"""

import logging

LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"


def configure_logging() -> None:
    """!
    @brief Send log records at INFO and above to stderr.
    """
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
