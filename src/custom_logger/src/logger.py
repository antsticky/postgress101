import logging


LOG_FORMAT = "[%(levelname)s] %(asctime)s | %(name)s - %(message)s"


def get_logger(name, handlers):
    logger = logging.getLogger(name=name)
    logger.setLevel(logging.DEBUG)
    
    for handler in handlers:
        handler.setLevel(handler.log_level)
        
        if hasattr(handler, 'log_format'):
            formatter = logging.Formatter(handler.log_format)    
            handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return logger
