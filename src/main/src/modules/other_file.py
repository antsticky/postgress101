import time

from custom_logger.src.logger import get_logger
from main import PerformanceLoggers as pm
from main import get_log_handlers

db_logger = get_logger(name=__name__, handlers=get_log_handlers())


@pm.memory_usage_logger(db_logger)
@pm.time_logger(db_logger)
def src_fn():
    db_logger.warning(
        "src_fn is just a dummy function",
        extra={
            "structured_data": {
                "job_identifier": "test_id",
                "warning": "src_fn",
                "reason": "dummy function",
            }
        },
    )

    time.sleep(1)
    large_string = "a" * 1024 * 1024 * 64
    time.sleep(1)

    return large_string
