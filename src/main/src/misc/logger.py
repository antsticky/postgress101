import logging
import os

from dotenv import load_dotenv

from custom_logger.src.data_models.extras import DBLoggerExtras
from custom_logger.src.handlers.db import DBLogHandler
from custom_logger.src.handlers.std import ConsoleLogHandler

load_dotenv()


def get_log_handlers():
    console_log_handler = ConsoleLogHandler(
        log_level=logging.DEBUG,
        log_format="[%(levelname)s] %(asctime)s | %(name)s - %(message)s",
    )

    db_logger_extra_params = DBLoggerExtras(
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        db=os.environ.get("DB_NAME"),
        table_names={
            "info": "logs_info_table",
            "warning": "logs_warning_table",
            "error": "logs_error_table",
        },
    )
    db_log_handler = DBLogHandler(
        log_level=logging.DEBUG, db_handler_setup=db_logger_extra_params
    )

    return [console_log_handler, db_log_handler]
