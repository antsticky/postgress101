import os
from dotenv import load_dotenv

from dbconnector.src.handlers.database import DBHandler
from dbconnector.src.exceptions.database import DBConnectionError

load_dotenv()


def main():
    connector = DBHandler(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        db_name=os.getenv("DB_NAME"))

    try:
        connector.get_engine()

    except DBConnectionError as e:
        print(e.message)
        print(e.reason)
