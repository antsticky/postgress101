from custom_logger.src.logger import get_logger
from main import get_log_handlers
from main.src.modules.other_file import src_fn

db_logger = get_logger(name=__name__, handlers=get_log_handlers())


def main():
    src_fn()

    db_logger.error(
        "Authentication need to be enabled",
        extra={
            "structured_data": {
                "job_identifier": "test_id",
                "error": "not implemented",
                "reason": "time",
            }
        },
    )
