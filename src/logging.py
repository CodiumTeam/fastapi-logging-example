import logging

from .logging_filters import FastApiLoggingFilter

logging.basicConfig(format="%(levelname)s:  %(asctime)s - [%(context)s] - %(message)s")

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addFilter(FastApiLoggingFilter())

    return logger