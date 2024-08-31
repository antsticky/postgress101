from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class ErrorTable(Base):
    __tablename__ = "logs_error_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    job_identifier = Column(String)
    error = Column(String)
    reason = Column(String)


class WarningTable(Base):
    __tablename__ = "logs_warning_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    job_identifier = Column(String)
    warning = Column(String)
    reason = Column(String)


class InfoTable(Base):
    __tablename__ = "logs_info_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    job_identifier = Column(String)
    info = Column(String)
    value = Column(Float)
