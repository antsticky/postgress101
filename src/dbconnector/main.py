import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float,PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import *
from sqlalchemy.exc import OperationalError
from sqlalchemy.engine import Engine

DB_HOST = 'localhost'
DB_PORT = 5432
DB_USER = 'postgres'
DB_PASSWORD = 'S3cret'
DB_NAME = 'citizix_db'

class DBConnectionError(Exception):
      def __init__(self, message, reason):
            self.message = message
            self.reason = reason

class DBHandler:
      def __init__(self, user: str, password: str, host: str, port: int, db_name: str):
            self.user = user
            self.password = password
            self.host = host
            self.port = port
            self.db_name = db_name
            
      def __create__connection_string(self) -> str:
            return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}'
      
      def get_engine(self):
            try:
                  engine = create_engine(self.__create__connection_string())
                  engine.connect()
                  return engine
            except OperationalError as e:
                  raise DBConnectionError(message=f"Failed to connect {self.host}:{self.port}/{self.db_name}", reason=e)

      def check_if_table_exists(self, table_name: str, engine: Engine):
            try:
                  metadata = MetaData()
                  metadata.reflect(bind=engine, only=[table_name])
                  return True
            except AttributeError as e:
                  return False
            
            

def main():
      connector = DBHandler(
            user = DB_USER,
            password = DB_PASSWORD,
            host = DB_HOST,
            port = DB_PORT,
            db_name = DB_NAME
      )
      
      try:
            engine = connector.get_engine()
            
            
            
            
      except DBConnectionError as e:
            print(e.message)
            print(e.reason)
      
      
      # try:
      #       engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
      #       engine.connect()
      # except OperationalError as e:
      #       print("cannot connect")
      #       print(e)


      # metadata = sqlalchemy.MetaData(bind=engine)
      # metadata.reflect(only=['test_table'])

      # print(metadata.tables)

            # Base = declarative_base()
            # class PointsOfInterest(Base):
            #       __tablename__ = "points_of_interest"
            #       poi_id = Column(Integer, primary_key=True)
            #       name = Column(String)
            #       address = Column(String)
            #       latitude = Column(Float)

            # PointsOfInterest.__table__.create(bind=engine, checkfirst=True)


# Variable_tableName = "mytable"

# engine = create_engine("sqlite:///myexample.db")  # Access the DB Engine
# if not engine.dialect.has_table(engine, Variable_tableName):  # If table don't exist, Create.
#     metadata = MetaData(engine)
#     # Create a table with the appropriate Columns
#     Table(Variable_tableName, metadata,
#           Column('Id', Integer, primary_key=True, nullable=False), 
#           Column('Date', Date), Column('Country', String),
#           Column('Brand', String), Column('Price', Float),
#     )
#     # Implement the creation
#     metadata.create_all()