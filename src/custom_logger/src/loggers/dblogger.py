import logging

from custom_logger.src.data_models.extras import DBLoggerExtras


class DbLogger(logging.Logger):
    def __init__(self, name: str, level=logging.INFO):
        super(DbLogger, self).__init__(name=name, level=level)

    def write_to_db(self, msg: str, table_name: str):
        print("----------------------------")
        print(f"Message: {msg}")
        print(table_name)
        print(self.extras)
        print("----------------------------")

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
