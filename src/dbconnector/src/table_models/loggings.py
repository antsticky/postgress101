import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float,PrimaryKeyConstraint, ForeignKey

import datetime
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import *
from sqlalchemy.exc import OperationalError
from sqlalchemy.engine import Engine

Base = declarative_base()


class ErrorTable(Base):
        __tablename__ = "error_table"
        id = Column(Integer, primary_key=True, autoincrement=True)
        timestamp = Column(DateTime(timezone=True), server_default=func.now())
        job_identifier = Column(String)
        error = Column(String)
        reason = Column(String)
    
class WarningTable(Base):
        __tablename__ = "warning_table"
        id = Column(Integer, primary_key=True, autoincrement=True)
        timestamp = Column(DateTime(timezone=True), server_default=func.now())
        job_identifier = Column(String)
        error = Column(String)
        reason = Column(String)
        
        
class InfoTable(Base):
        __tablename__ = "info_table"
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String)
        address = Column(String)
        latitude = Column(Float)
        
