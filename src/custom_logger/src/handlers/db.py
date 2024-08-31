import logging

from custom_logger.src.handlers.base import BaseLogHandler


class SpecialHandler(BaseLogHandler, logging.Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def emit(self, record):
        print(dir(record))
        print(record.levelname)
        print(record.processName)
        print(record.process)
        print(record.pathname)
        print(record.name)
        print(record.module)
        print(record.lineno)
        print(record.getMessage())
        
        structured_data = getattr(record, "structured_data", {})
        print(structured_data.get("my_key"))
        print()
        #self.sender.writeLog(record)
