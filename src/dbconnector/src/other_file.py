import logging
from custom_logger import get_logger

db_logger = get_logger(name=__name__, logger_type='db_logger', extras={"host": "localhost"}, level=logging.DEBUG)

def src_fn():
    db_logger.info("Inside src fn")
    print("SRC FN was called")