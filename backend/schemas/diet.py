from pydantic import BaseModel


class Entry(BaseModel):
    name:str
    ate:str
    time:str