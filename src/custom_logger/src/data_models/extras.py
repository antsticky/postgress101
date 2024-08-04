from pydantic import BaseModel


class Extras(BaseModel):
    pass


class TableName(BaseModel):
    info: str
    warning: str
    error: str


class DBLoggerExtras(Extras):
    host: str
    port: int
    user: str
    password: str
    db: str
    table_names: TableName
