import logging

from custom_logger import get_logger
from dbconnector.src.other_file import src_fn

db_logger = get_logger(
    __name__,
    extras={
        "host": "localhost"},
    logger_type="db_logger",
    level=logging.DEBUG)


def main():

    src_fn()

    db_logger.warning("A warning message")
    db_logger.error("An error message")
    db_logger.critical("A critical message")
    db_logger.info("An info message")
    db_logger.debug("A debug message")

    print("EOD")
