import os

from dotenv import load_dotenv

from custom_logger import DataModels, get_logger

load_dotenv()

extras = DataModels.DBLoggerExtras(
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


def get_db_logger(name, level):

    return get_logger(
        name=name,
        level=level,
        logger_type="db_logger",
        extras=extras)
