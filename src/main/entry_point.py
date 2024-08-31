from main import get_log_handlers
from custom_logger.src.logger import get_logger

from main.src.modules.other_file import src_fn



def main():
    db_logger = get_logger(
        name=__name__,
        handlers=get_log_handlers()
    )
    
    db_logger.error("debug message", {"structured_data": {"job_identifier": "value", "error": "korte", "reason": "aaa"}})

    src_fn()

    print("EOD")
