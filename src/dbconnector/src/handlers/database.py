from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker

from dbconnector.src.exceptions.database import DBConnectionError

class DBHandler:
    def __init__(
            self,
            user: str,
            password: str,
            host: str,
            port: int,
            db_name: str):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name

    def __create__connection_string(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"

    def get_engine(self):
        try:
            engine = create_engine(self.__create__connection_string())
            engine.connect()
            return engine
        except OperationalError as e:
            raise DBConnectionError(
                message=f"Failed to connect {self.host}:{self.port}/{self.db_name}",
                reason=e,
            )

    def check_if_table_exists(self, table_name: str, engine: Engine):
        try:
            metadata = MetaData()
            metadata.reflect(bind=engine, only=[table_name])
            return True
        except AttributeError:
            return False

    def create_table(self, table_model: str, engine: Engine):
        table_model.__table__.create(bind=engine, checkfirst=True)

    def insert_data(self, engine: Engine, data):
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(data)
        session.commit()