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
            db_name: str,
            **_, # ignore extra params
            ):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name

    def __create__connection_string(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"

    def get_engine(self):
        try:
            print(self.__create__connection_string())
            print(type(self.__create__connection_string()))
            print("***************")
            print("befor 3 init")
            engine = create_engine(self.__create__connection_string())
            print("after 3 init")
            print("***************")
            import sys
            # sys.exit(1)
            engine.connect()
            sys.exit(1)
            return engine
        except OperationalError as e:
            raise DBConnectionError(
                message=f"Failed to connect {self.host}:{self.port}/{self.db_name}",
                reason=e,
            )
        import sys
        sys.exit(1)

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
