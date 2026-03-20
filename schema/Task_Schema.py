from pydantic import BaseModel

class Request(BaseModel):
    title : str
    description : str

class Response(BaseModel):
    id : int
    title : str
    description : str
