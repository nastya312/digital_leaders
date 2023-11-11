from enum import Enum

from pydantic import BaseModel, Field
import uuid
import datetime as datetime_dt


class TaskStatusEnum(Enum):
    CREATED = 0
    IN_PROGRESS = 1
    DONE = 2


class TaskRead(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    task_type_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    point_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    executor_id: uuid.UUID = Field(default_factory=uuid.uuid4)

    status: TaskStatusEnum = Field(default=TaskStatusEnum.CREATED)
    created_at: datetime_dt.datetime = Field(default_factory=datetime_dt.datetime.now)

    class Config:
        orm_mode = True
        from_attributes = True


class TaskCreateUpdate(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    task_type_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    point_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    executor_id: uuid.UUID = Field(default_factory=uuid.uuid4)

    status: TaskStatusEnum = Field(default=TaskStatusEnum.CREATED)

    class Config:
        orm_mode = True
        from_attributes = True