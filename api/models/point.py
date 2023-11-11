from models import Base
from sqlalchemy import Column, text, Text, sql, SmallInteger, UniqueConstraint, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import datetime


class Point(Base):
    __tablename__ = 'point'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                server_default=text("gen_random_uuid()"))

    address = Column(Text, nullable=False)

    is_materials_delivered = Column(Boolean, nullable=False, default=False)
    date_of_connection_of_the_point = Column(DateTime(True), nullable=False)
    date_of_issue_of_the_last_card = Column(DateTime(True), nullable=False)

    number_of_approved_requests = Column(SmallInteger, nullable=False, default=0)
    number_of_cards_issued = Column(SmallInteger, nullable=False, default=0)

    created_at = Column(DateTime(True), nullable=False, server_default=sql.func.now(),
                        default=datetime.datetime.utcnow)

    task = relationship('Task', foreign_keys='[Task.point_id]',
                         back_populates='point')


    __table_args__ = (
        UniqueConstraint('address', name='point_address_constraint'),
    )