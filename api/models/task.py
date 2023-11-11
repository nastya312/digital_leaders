from models import Base
from sqlalchemy import Column, text, Text, sql, SmallInteger, UniqueConstraint, ForeignKey, DateTime, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime
from sqlalchemy_utils.types.choice import ChoiceType

from sqlalchemy.orm import relationship

from models.point import Point
from models.task_type import TaskType
from models.user import User
from schemas.task import TaskStatusEnum


class Task(Base):
    __tablename__ = 'task'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                server_default=text("gen_random_uuid()"))

    task_type_id = Column(UUID(as_uuid=False), ForeignKey('task_type.id'), nullable=False)
    task_type = relationship('TaskType', foreign_keys=[task_type_id], back_populates='task')

    point_id = Column(UUID(as_uuid=False), ForeignKey('point.id'), nullable=False)
    point = relationship('Point', foreign_keys=[point_id], back_populates='task')

    executor_id = Column(UUID(as_uuid=False), ForeignKey('user.id'), nullable=True)
    executor = relationship('User', foreign_keys=[executor_id], back_populates='task')

    status = Column(ChoiceType(TaskStatusEnum, impl=Integer()), nullable=False)
    created_at = Column(DateTime(True), nullable=False, server_default=sql.func.now(), default=datetime.datetime.utcnow)

    __table_args__ = (
        UniqueConstraint('point_id', 'executor_id', 'task_type_id', name='unique_desc_date_user'),
    )
