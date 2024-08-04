import logging

from custom_logger import performance_monitors as pm


from dbconnector import get_db_logger



db_logger = get_db_logger(
    name=__name__,
    level=logging.DEBUG,
)

@pm.time_logger(db_logger)
def src_fn():
    db_logger.info("Inside src fn")
    import time
    time.sleep(1)
