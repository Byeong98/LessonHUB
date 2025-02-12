from sqlalchemy import Column, Integer, String, Text, DateTime

from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    create_at = Column(DateTime, nullable=False)


