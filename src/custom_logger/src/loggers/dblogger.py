import logging

from custom_logger.src.data_models.extras import DBLoggerExtras


class DbLogger(logging.Logger):
    def __init__(self, name: str, level=logging.INFO):
        super(DbLogger, self).__init__(name=name, level=level)

    def setExtras(self, extras: dict):
        self.extras = DBLoggerExtras(**extras)

    def info(self, msg: str, *args, **kwargs):
        return super(DbLogger, self).info(msg)
