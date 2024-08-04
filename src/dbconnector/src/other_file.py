import logging

from dbconnector import get_db_logger

db_logger = get_db_logger(
    name=__name__,
    level=logging.DEBUG,
)


def src_fn():
    db_logger.info("Inside src fn")
    print("SRC FN was called")
