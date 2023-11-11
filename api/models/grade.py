from models import Base
from sqlalchemy import Column, text, Text, sql, SmallInteger, UniqueConstraint, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import datetime


class Grade(Base):
    __tablename__ = 'grade'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                server_default=text("gen_random_uuid()"))
    name = Column(Text, nullable=False)

    created_at = Column(DateTime(True), nullable=False, server_default=sql.func.now(),
                        default=datetime.datetime.utcnow)

    task_type = relationship('TaskType', foreign_keys='[TaskType.minimal_grade_id]',
                        back_populates='minimal_grade')

    user = relationship('User', foreign_keys='[User.grade_id]',
                         back_populates='grade')

    __table_args__ = (
        UniqueConstraint('name', name='grade_name_constraint'),
    )