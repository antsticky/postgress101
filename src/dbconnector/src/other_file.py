import logging

from custom_logger import performance_monitors as pm
from dbconnector import get_db_logger

db_logger = get_db_logger(
    name=__name__,
    level=logging.DEBUG,
)


@pm.memory_usage_logger(db_logger)
@pm.time_logger(db_logger)
def src_fn():
    db_logger.debug("Inside src fn")
    import time

    time.sleep(1)

    large_string = "a" * 1024 * 1024 * 64
