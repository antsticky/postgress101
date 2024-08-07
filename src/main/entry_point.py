print("\nSTAAAAAAART ENTRY POINT\n-----------------------")
import logging

print("Before imports")
# from main import get_db_logger
print("\nimport 1")
from main.src.modules.other_file import src_fn

# print("\nimport 2")
# print("START: get logger inside entry")
# db_logger = get_db_logger(name=__name__, level=logging.DEBUG)
# print("END: get logger inside entry")


def main():

    src_fn()

    # db_logger.warning("A warning message")
    # db_logger.error("An error message")
    # db_logger.critical("A critical message")
    # db_logger.info("An info message")
    # db_logger.debug("A debug message")

    print("EOD")
    
    
if __name__ == "__main__":
    main()
