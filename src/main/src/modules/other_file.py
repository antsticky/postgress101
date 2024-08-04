import logging

from main import PerformanceLoggers as pm
from main import get_db_logger

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
    print(large_string.replace("a", "") + "large_string")
