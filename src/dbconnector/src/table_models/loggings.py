import datetime
import os

from sqlalchemy import (Column, DateTime, Float, ForeignKey, Integer, MetaData,
                        PrimaryKeyConstraint, Sequence, String, create_engine)
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker
from sqlalchemy.sql import *
from sqlalchemy.sql import func

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
