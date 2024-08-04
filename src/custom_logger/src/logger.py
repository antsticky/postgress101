import logging
from typing import Literal

from custom_logger.src.loggers.dblogger import DbLogger
from custom_logger.src.data_models.extras import Extras

LOG_FORMAT = '[%(levelname)s] %(asctime)s | %(name)s - %(message)s'

def get_logger(name: str, logger_type: Literal['db_logger'], level: logging.ERROR | logging.WARNING | logging.INFO | logging.DEBUG, extras:dict | Extras = None, format: str =LOG_FORMAT) -> logging.Logger:
    def select_custom_logger():
        if logger_type == 'db_logger':
            return logging.setLoggerClass(DbLogger)
        
        raise ValueError('Invalid logger type')
    
    select_custom_logger()
    logging.basicConfig(level=level, format=format)
    
    logger = logging.getLogger(name=name)
    
    if isinstance(extras, Extras):
        logger.setExtras(extras=extras.model_dump())
    else:
        logger.setExtras(extras=extras)    
    
    logger.setLevel(level)
    
    return logger