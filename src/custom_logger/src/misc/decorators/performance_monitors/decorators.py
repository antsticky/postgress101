from functools import wraps
from time import time


def time_logger(logger, *args, **kwargs):
    def timed(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start = time()
            result = f(*args, **kwargs)
            elapsed = time() - start
            
            logger.info("%s took %f seconds to finish" % (f.__name__, elapsed))
            
            return result
        return wrapper
    return timed