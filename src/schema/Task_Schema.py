from pydantic import BaseModel, Field, validator
from typing import Optional

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=5, max_length=300)

    @validator("title", "description")
    def clean(cls, v):
        v = v.strip()
        if not v:
            raise ValueError("Field cannot be empty")
        return v


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, min_length=5, max_length=300)

    @validator("title", "description")
    def clean(cls, v):
        if v is not None:
            v = v.strip()
            if not v:
                raise ValueError("Field cannot be empty")
        return v