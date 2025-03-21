from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# User 모델
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    create_at = Column(DateTime, nullable=False)

    teaches = relationship("Teaches", back_populates="user")


# 교수안 모델
class Teaches(Base):
    __tablename__ = "teaches"

    id = Column(Integer, primary_key=True)
    grade_id = Column(Integer, ForeignKey("grades.id"), nullable=False)  # 학년
    subject = Column(String(100), nullable=False)  # 과목
    section = Column(String(100), nullable=False)  # 과목 상세 (예: 국어, 수학 ...)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)  # 단원
    title = Column(String(255), nullable=False)  # 제목
    objective = Column(Text, nullable=False)  # 학습목표
    intro = Column(Text, nullable=False)  # 도입
    deployment = Column(Text, nullable=False)  # 전개
    finish = Column(Text, nullable=False)  # 정리
    ai_url = Column(Text, nullable=False)  # AI URL
    create_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("Users", back_populates="teaches")
    unit = relationship("Units", back_populates="teach_list")
    grade = relationship("Grades", back_populates="teach_list")


class Grades(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)

    teach_list = relationship("Teaches", back_populates="grade")


# 과목 모델
class Subjects(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)

    sections = relationship("Sections", back_populates="subject")

# 과목 상세 (예: 국어, 수학 ...)
class Sections(Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)

    subject = relationship("Subjects", back_populates="sections")
    units = relationship("Units", back_populates="section")


# 단원 모델
class Units(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=False)

    section = relationship("Sections", back_populates="units")
    standards = relationship("Standards", back_populates="unit")
    teach_list = relationship("Teaches", back_populates="unit")

# 성취기준 모델
class Standards(Base):
    __tablename__ = "standards"

    id = Column(Integer, primary_key=True)
    title = Column(String(4000), nullable=False)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)

    unit = relationship("Units", back_populates="standards")
    commentaries = relationship("Commentaries", back_populates="standard")


# 성취기준해설 모델
class Commentaries(Base):
    __tablename__ = "commentaries"

    id = Column(Integer, primary_key=True)
    title = Column(String(4000), nullable=False)
    standard_id = Column(Integer, ForeignKey("standards.id"), nullable=False)

    standard = relationship("Standards", back_populates="commentaries")


class Aiurls(Base):
    __tablename__ = "ai_urls"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    content = Column(String(4000), nullable=False)
    url = Column(String(255), nullable=False)