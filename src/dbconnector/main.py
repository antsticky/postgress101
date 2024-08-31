import os
from dotenv import load_dotenv

from dbconnector.src.handlers.database import DBHandler

load_dotenv()


db_handler = DBHandler(
    host=os.environ.get("DB_HOST"),
    port=os.environ.get("DB_PORT"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    db_name=os.environ.get("DB_NAME"),
)

def main():
    try:
        engine = db_handler.get_engine()
        engine.connect()
    except Exception as e:
        print(e)
