import logging
from typing import Literal

from custom_logger.src.data_models.extras import Extras
from custom_logger.src.loggers.dblogger import DbLogger

LOG_FORMAT = "[%(levelname)s] %(asctime)s | %(name)s - %(message)s"


def get_logger(
    name: str,
    logger_type: Literal["db_logger"],
    level: logging.ERROR | logging.WARNING | logging.INFO | logging.DEBUG,
    extras: dict | Extras = None,
    format: str = LOG_FORMAT,
) -> logging.Logger:
    def select_custom_logger():
        if logger_type == "db_logger":
            return logging.setLoggerClass(DbLogger)

        raise ValueError("Invalid logger type")

    def set_extras(logger):
        if isinstance(extras, Extras):
            logger.setExtras(extras=extras.model_dump())
        if isinstance(extras, dict):
            logger.setExtras(extras=extras)

    select_custom_logger()
    logging.basicConfig(level=level, format=format)
    logger = logging.getLogger(name=name)
    set_extras(logger)

    logger.setLevel(level)

    return logger
