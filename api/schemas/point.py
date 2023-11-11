from pydantic import BaseModel, Field
import uuid
import datetime as datetime_dt


class PointRead(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    address: str

    is_materials_delivered: bool = Field(default=False)
    date_of_connection_of_the_point: datetime_dt.datetime
    date_of_issue_of_the_last_card: datetime_dt.datetime

    number_of_approved_requests: int = Field(default=0)
    number_of_cards_issued: int = Field(default=0)

    created_at: datetime_dt.datetime = Field(default_factory=datetime_dt.datetime.now)

    class Config:
        orm_mode = True
        from_attributes = True


class PointCreateUpdate(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    address: str

    is_materials_delivered: bool = Field(default=False)
    date_of_connection_of_the_point: datetime_dt.datetime
    date_of_issue_of_the_last_card: datetime_dt.datetime

    number_of_approved_requests: int = Field(default=0)
    number_of_cards_issued: int = Field(default=0)

    class Config:
        orm_mode = True
        from_attributes = True