from models import Base
from sqlalchemy import Column, text, Text, sql, SmallInteger, UniqueConstraint, ForeignKey, DateTime, Enum, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime
from sqlalchemy_utils.types.choice import ChoiceType

from sqlalchemy.orm import relationship

from models.grade import Grade
from schemas.task_type import PriorityEnum


class TaskType(Base):
    __tablename__ = 'task_type'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                server_default=text("gen_random_uuid()"))

    name = Column(Text, nullable=False)
    priority = Column(ChoiceType(PriorityEnum, impl=Integer()), nullable=False)
    duration = Column(SmallInteger, nullable=False, default=90)

    minimal_grade_id = Column(UUID(as_uuid=False), ForeignKey('grade.id'), nullable=False)
    minimal_grade = relationship('Grade', foreign_keys=[minimal_grade_id], back_populates='task_type')

    task = relationship('Task', foreign_keys='[Task.task_type_id]',
                         back_populates='task_type')

    created_at = Column(DateTime(True), nullable=False, server_default=sql.func.now(),
                        default=datetime.datetime.utcnow)