from pydantic import BaseModel, Field
import uuid
import datetime as datetime_dt


class LocationCreateUpdate(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    address: str

    class Config:
        orm_mode = True
        from_attributes = True


class LocationRead(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    address: str
    created_at: datetime_dt.datetime = Field(default_factory=datetime_dt.datetime.now)

    class Config:
        orm_mode = True
        from_attributes = True
