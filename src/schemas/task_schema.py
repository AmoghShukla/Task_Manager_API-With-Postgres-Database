from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None


class TaskCreate(TaskBase):
    pass


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]

    model_config = ConfigDict(from_attributes=True)

class TaskDelete(BaseModel):
    id : int
    


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None