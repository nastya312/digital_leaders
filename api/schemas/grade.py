from pydantic import BaseModel, Field
import uuid
import datetime as datetime_dt


class GradeCreateUpdate(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str

    class Config:
        orm_mode = True
        from_attributes = True


class GradeRead(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str
    created_at: datetime_dt.datetime = Field(default_factory=datetime_dt.datetime.now)

    class Config:
        orm_mode = True
        from_attributes = True
