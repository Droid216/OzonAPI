import datetime

from sqlalchemy import Column, Integer, String, Enum, Date, ForeignKey, Sequence, Numeric, Boolean, MetaData
from sqlalchemy.orm import relationship, declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class User(Base):
    __tablename__ = 'users'

