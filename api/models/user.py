import datetime

from models import Base
from sqlalchemy import Column, text, Text, sql, SmallInteger, UniqueConstraint, ForeignKey, DateTime, Enum, Integer, \
    Boolean

from sqlalchemy.dialects.postgresql import UUID
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import relationship

from models.grade import Grade
from models.location import Location
from schemas.user import RoleEnum


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'user'

    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    patronymic = Column(Text, nullable=True)

    is_verified = Column(Boolean, default=True)

    role_id = Column(Enum(RoleEnum), nullable=False)

    grade_id = Column(UUID(as_uuid=False), ForeignKey('grade.id'), nullable=True)
    grade = relationship('Grade', foreign_keys=[grade_id], back_populates='user')

    location_id = Column(UUID(as_uuid=False), ForeignKey('location.id'), nullable=True)
    location = relationship('Location', foreign_keys=[location_id], back_populates='user')

    created_at = Column(DateTime(True), nullable=False, server_default=sql.func.now(), default=datetime.datetime.utcnow)

    task = relationship('Task', foreign_keys='[Task.executor_id]',
                         back_populates='executor')

    __table_args__ = (
        UniqueConstraint('email', name='user_email_constraint'),
    )