from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.types import Date
from database import Base
from datetime import datetime


class Record(Base):
    __tablename__ = "Records"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    intro = Column(String(300), nullable=False)
    text = Column(Text, nullable=False)
    date = Column(Date, default=datetime.utcnow)
