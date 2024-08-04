import logging

from dbconnector.src.other_file import src_fn
from dbconnector import get_db_logger

db_logger = get_db_logger(
    name=__name__,
    level=logging.DEBUG)


def main():

    src_fn()

    db_logger.warning("A warning message")
    db_logger.error("An error message")
    db_logger.critical("A critical message")
    db_logger.info("An info message")
    db_logger.debug("A debug message")

    print("EOD")
