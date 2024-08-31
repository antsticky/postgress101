from main import PerformanceLoggers as pm

from main import get_log_handlers
from custom_logger.src.logger import get_logger


db_logger = get_logger(
    name=__name__,
    handlers=get_log_handlers()
)


@pm.memory_usage_logger(db_logger)
@pm.time_logger(db_logger)
def src_fn():
    db_logger.error("debug message", {"structured_data": {"job_identifier": "value", "error": "korte", "reason": "aaa"}})
    import time

    time.sleep(1)

    large_string = "a" * 1024 * 1024 * 64
