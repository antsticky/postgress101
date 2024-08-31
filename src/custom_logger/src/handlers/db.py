import logging

from custom_logger.src.handlers.base import BaseLogHandler
from custom_logger.src.data_models.extras import DBLoggerExtras

class SpecialHandler(BaseLogHandler, logging.Handler):
    def __init__(self, extra_params: DBLoggerExtras, *args, **kwargs):
        self.extra_params = extra_params
        super().__init__(*args, **kwargs)

    def emit(self, record):
        print(record.levelname)
        print(record.processName)
        print(record.process)
        print(record.pathname)
        print(record.name)
        print(record.module)
        print(record.lineno)
        print(record.getMessage())
        print(self.extra_params)
        
        structured_data = getattr(record, "structured_data", {})
        print(structured_data.get("my_key"))
        print()
        #self.sender.writeLog(record)
