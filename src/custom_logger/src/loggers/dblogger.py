import logging

from custom_logger.src.data_models.extras import DBLoggerExtras
from dbconnector.src.handlers.database import DBHandler

class DbLogger(logging.Logger):
    def __init__(self, name: str, level=logging.INFO):
        print("init logger DB")
        super(DbLogger, self).__init__(name=name, level=level)

    def write_to_db(self, msg: str, table_name: str):
        print("----------------------------")
        print(f"Message: {msg}")
        print(table_name)
        print(self.extras.model_dump())
        
        connector = DBHandler(
            **self.extras.model_dump()
        )        
        
        connector.get_engine()
        
        print("----------------------------")
        

        
        # connector = DBHandler(
        #     user=os.getenv("DB_USER"),
        #     password=os.getenv("DB_PASSWORD"),
        #     host=os.getenv("DB_HOST"),
        #     port=os.getenv("DB_PORT"),
        #     db_name=os.getenv("DB_NAME"),
        # )
        # print("----------------------------")
        # print(f"Message: {msg}")
        # print(table_name)
        # print(self.extras)
        # print("----------------------------")

    def setExtras(self, extras: dict):
        self.extras = DBLoggerExtras(**extras)

    def info(self, msg: str, *args, **kwargs):
        self.write_to_db(msg=msg, table_name=self.extras.table_names.info)
        return super(DbLogger, self).info(
            f"{msg} - {self.extras.table_names.info}", *args, **kwargs
        )

    def warning(self, msg: str, *args, **kwargs):
        self.write_to_db(msg=msg, table_name=self.extras.table_names.warning)
        return super(DbLogger, self).warning(
            f"{msg} - {self.extras.table_names.warning}", *args, **kwargs
        )

    def error(self, msg: str, *args, **kwargs):
        self.write_to_db(msg=msg, table_name=self.extras.table_names.error)
        return super(DbLogger, self).error(
            f"{msg} - {self.extras.table_names.error}", *args, **kwargs
        )

    def debug(self, msg: str, *args, **kwargs):
        self.write_to_db(msg=msg, table_name=self.extras.table_names.error)
        return super(DbLogger, self).debug(
            f"{msg} - {self.extras.table_names.error}", *args, **kwargs
        )