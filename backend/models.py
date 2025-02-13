from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# User 모델
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    create_at = Column(DateTime, nullable=False)

    teaches = relationship("Teach", back_populates="user")


# 교수안 모델
class Teach(Base):
    __tablename__ = "teach"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)  # 과목
    session = Column(String, nullable=False)  # 과목 상세 (예: 국어, 수학 ...)
    unit_id = Column(Integer, ForeignKey("unit.id"), nullable=False)  # 단원
    title = Column(String, nullable=False)  # 제목
    intro = Column(Text, nullable=False)  # 도입
    deployment = Column(Text, nullable=False)  # 전개
    conclusion = Column(Text, nullable=False)  # 정리
    create_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="teaches")
    unit = relationship("Unit", back_populates="teaches")


# 과목 모델
class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    sessions = relationship("Session", back_populates="subject")

# 과목 상세 (예: 국어, 수학 ...)
class Session(Base):
    __tablename__ = "session"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    subject_id = Column(Integer, ForeignKey("subject.id"), nullable=False)

    subject = relationship("Subject", back_populates="sessions")
    units = relationship("Unit", back_populates="session")


# 단원 모델
class Unit(Base):
    __tablename__ = "unit"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    session_id = Column(Integer, ForeignKey("session.id"), nullable=False)

    session = relationship("Session", back_populates="units")
    standards = relationship("Standard", back_populates="unit")


# 성취기준 모델
class Standard(Base):
    __tablename__ = "standard"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    unit_id = Column(Integer, ForeignKey("unit.id"), nullable=False)

    unit = relationship("Unit", back_populates="standards")
    commentaries = relationship("Commentary", back_populates="standard")


# 성취기준해설 모델
class Commentary(Base):
    __tablename__ = "commentary"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    standard_id = Column(Integer, ForeignKey("standard.id"), nullable=False)

    standard = relationship("Standard", back_populates="commentaries")
