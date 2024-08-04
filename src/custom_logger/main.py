import logging

from custom_logger import DataModels, get_logger


def main():
    logger = get_logger(
        __name__,
        extras=DataModels.DBLoggerExtras(host="0.0.0.0"),
        logger_type="db_logger",
        level=logging.DEBUG,
    )
    logger.info("This is an info message")


if __name__ == "__main__":
    main()
