from enum import Enum

from pydantic import BaseModel, Field
import fastapi_users
import uuid
import datetime as datetime_dt


class RoleEnum(Enum):
    MANAGER = 0
    EMPLOYEE = 1


class UserRead(fastapi_users.schemas.BaseUser[uuid.UUID]):
    first_name: str
    last_name: str
    patronymic: str = Field(default=None)
    created_at: datetime_dt.datetime

    role_id: RoleEnum = Field(default=RoleEnum.EMPLOYEE)
    grade_id: uuid.UUID | None = Field(default=None)
    location_id: uuid.UUID | None = Field(default=None)


class UserCreateUpdate(fastapi_users.schemas.BaseUserCreate):
    first_name: str
    last_name: str
    patronymic: str = Field(default=None)

    role_id: RoleEnum = Field(default=RoleEnum.EMPLOYEE)
    grade_id: uuid.UUID | None = Field(default=None)
    location_id: uuid.UUID | None = Field(default=None)
