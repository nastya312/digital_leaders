from models import Base
from sqlalchemy import Column, text, Text, sql, SmallInteger, UniqueConstraint, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
import datetime


class Location(Base):
    __tablename__ = 'location'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                server_default=text("gen_random_uuid()"))

    address = Column(Text, nullable=False)

    created_at = Column(DateTime(True), nullable=False, server_default=sql.func.now(),
                        default=datetime.datetime.utcnow)

    user = relationship('User', foreign_keys='[User.location_id]',
                         back_populates='location')

    __table_args__ = (
        UniqueConstraint('address', name='location_address_constraint'),
    )