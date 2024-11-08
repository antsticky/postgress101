from functools import wraps
from time import time

import psutil


def time_logger(logger, *args, **kwargs):
    def timed(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start = time()
            result = f(*args, **kwargs)
            elapsed = time() - start

            logger.info(
                "%s took %f seconds to finish" % (f.__name__, elapsed),
                extra={
                    "structured_data": {
                        "job_identifier": f"{f.__name__}",
                        "info": "elapsed_time",
                        "value": elapsed,
                    }
                },
            )

            return result

        return wrapper

    return timed


def memory_usage_logger(logger, *args, **kwargs):
    def memory_usage(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            process = psutil.Process()

            before_memory = process.memory_info().rss
            return_value = f(*args, **kwargs)
            after_memory = process.memory_info().rss

            logger.info(
                f"{f.__name__} used {after_memory - before_memory} bytes memory",
                extra={
                    "structured_data": {
                        "job_identifier": f"{f.__name__}",
                        "info": "used_memory",
                        "value": after_memory -
                        before_memory,
                    }},
            )

            return return_value

        return wrapper

    return memory_usage
