import logging

from custom_logger.src.handlers.base import BaseLogHandler


class ConsoleLogHandler(BaseLogHandler, logging.StreamHandler):
    def __init__(self, log_format, *args, **kwargs):
        self.log_format = log_format
        super().__init__(*args, **kwargs)
