import logging

from custom_logger.src.data_models.extras import DBLoggerExtras
from custom_logger.src.data_models.tables import (ErrorTable, InfoTable,
                                                  WarningTable)
from custom_logger.src.handlers.base import BaseLogHandler
from dbconnector.src.handlers.database import DBHandler


class DBLogHandler(BaseLogHandler, logging.Handler):
    def __init__(
        self,
        db_handler_setup: DBLoggerExtras,
        structured_data_key="structured_data",
        *args,
        **kwargs
    ):
        self.__db_handler_setup = db_handler_setup
        self.default_table_name = self.__db_handler_setup.table_names.info
        self.default_message_type = InfoTable
        self.message_mapping = {
            "error": ErrorTable,
            "warning": WarningTable,
            "info": InfoTable,
        }

        self.structured_data_key = structured_data_key

        self.db_handler = DBHandler(
            user=db_handler_setup.user,
            password=db_handler_setup.password,
            host=db_handler_setup.host,
            port=db_handler_setup.port,
            db_name=db_handler_setup.db,
        )

        super().__init__(*args, **kwargs)

    def get_insert_data_model(self, log_level_name):
        # table_name = getattr(self.__db_handler_setup.table_names, log_level_name.lower(), self.default_table_name)
        log_data_model = self.message_mapping.get(
            log_level_name.lower(), self.default_message_type
        )
        return log_data_model

    def write_to_db(self, log_level_name, record, db_message):
        db_engine = self.db_handler.get_engine()
        log_data_model = self.get_insert_data_model(log_level_name)

        structured_message = log_data_model(**db_message)

        self.db_handler.create_table(
            table_model=log_data_model, engine=db_engine)
        self.db_handler.insert_data(engine=db_engine, data=structured_message)

    def emit(self, record):
        db_message = getattr(record, self.structured_data_key, False)

        if db_message:
            self.write_to_db(
                log_level_name=record.levelname,
                record=record,
                db_message=db_message)
