from pydantic import BaseModel, Field, validator, ConfigDict, model_validator, field_validator
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

class TaskDelete(BaseModel):
    id: int = Field(..., gt=0)

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None

    model_config = ConfigDict(extra="forbid")

    @field_validator("title", "description", mode="before")
    def clean_text(cls, v):
        if v is None:
            return v
        v = v.strip()
        if not v:
            raise ValueError("Field cannot be empty")
        return v

    @model_validator(mode="after")
    def at_least_one_field(self):
        if self.title is None and self.description is None:
            raise ValueError("At least one field must be provided")
        return self