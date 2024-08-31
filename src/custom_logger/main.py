import logging


from custom_logger.src.handlers.db import SpecialHandler
from custom_logger.src.handlers.std import ConsoleLogHandler

from custom_logger.src.logger import get_logger


def main():
    console_log_handler = ConsoleLogHandler(log_level=logging.DEBUG, log_format="[%(levelname)s] %(asctime)s | %(name)s - %(message)s")
    db_log_handler = SpecialHandler(log_level=logging.DEBUG)

    logger = get_logger(__name__, handlers=[console_log_handler, db_log_handler])

    logger.info("test msg1")
    logger.info("test msg2", extra={"structured_data": {"my_key": "value"}})
    logger.info("test msg3", extra={"structured_data": {"my_key": "value"}})

    # logger = get_logger(
    #     __name__,
    #     extras=DataModels.DBLoggerExtras(
    #         host="0.0.0.0",
    #         port=1234,
    #         user="root",
    #         password="password",
    #         db="test_db"),
    #     logger_type="db_logger",
    #     level=logging.DEBUG,
    # )
    # logger.info("This is an info message")


if __name__ == "__main__":
    main()
