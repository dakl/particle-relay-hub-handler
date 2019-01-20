import config
import logging


def setup_logging():
    if config.DEBUG:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(level=level)
