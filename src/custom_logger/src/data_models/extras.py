from pydantic import BaseModel

class Extras(BaseModel):
    pass

class DBLoggerExtras(Extras):
    host: str