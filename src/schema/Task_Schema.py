from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title : str
    description : str

class TaskResponse(BaseModel):
    id : int
    title : str
    description : Optional[str]


class TaskUpdate(BaseModel):
    title : Optional[str]
    description : Optional[str]
