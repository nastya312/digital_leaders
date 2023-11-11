from enum import Enum

from pydantic import BaseModel, Field
import uuid
import datetime as datetime_dt


class PriorityEnum(Enum):
    HIGH = 0
    MIDDLE = 1
    LOW = 2


class TaskTypeRead(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str

    priority: PriorityEnum
    minimal_grade_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    duration: int = Field(default=90)

    created_at: datetime_dt.datetime = Field(default_factory=datetime_dt.datetime.now)

    class Config:
        orm_mode = True
        from_attributes = True


class TaskTypeCreateUpdate(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str

    priority: PriorityEnum
    minimal_grade_id: uuid.UUID = Field(default_factory=uuid.uuid4)

    class Config:
        orm_mode = True
        from_attributes = True