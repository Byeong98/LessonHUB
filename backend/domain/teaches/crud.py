from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from models import *


# 교수안 저장
async def create_teach(db: AsyncSession,
                        response_json: dict,
                        current_user_id: int,
                        unit_id: int,
                        grade_id: int
                        ):
    query = insert(Teaches).values(
        grade_id=grade_id,
        subject=response_json['과목'],
        session=response_json['과목상세'],
        unit_id=unit_id,
        title=response_json['제목'],
        objective=",".join(response_json['학습목표']),
        intro=",".join(response_json['도입']),
        deployment=",".join(response_json['전개']),
        finish=",".join(response_json['정리']),
        create_at=datetime.now(),
        user_id=current_user_id,
    )
    await db.execute(query)
    await db.commit()

# 단일 값 조회
async def get_title(db: AsyncSession, model ,id: int):
    query = select(model).filter(model.id == id)
    result = await db.execute(query)
    return result.scalars().first()



# 학년 리스트 조회
async def get_grades_list(db: AsyncSession):
    query = select(Grades).order_by(Grades.id)
    result = await db.execute(query)
    return result.scalars().all()


# 과목 리스트 조회
async def get_subjects_list(db: AsyncSession):
    query = select(Subjects).order_by(Subjects.title)
    result = await db.execute(query)
    return result.scalars().all()

# 과목상세 리스트 조회
async def get_sission_list(db: AsyncSession, subject_id: int):
    query = select(Sessions).filter(Sessions.subject_id ==
                                    subject_id).order_by(Sessions.id)
    result = await db.execute(query)
    return result.scalars().all()

# 단원 리스트 조회
async def get_unit_list(db: AsyncSession, session_id: int):
    query = select(Units).filter(Units.session_id ==
                                session_id).order_by(Units.id)
    result = await db.execute(query)
    return result.scalars().all()

# 성취기준 리스트 조회
async def get_standard_list(db: AsyncSession, unit_id: int):
    query = select(Standards).filter(
        Standards.unit_id == unit_id).order_by(Standards.id)
    result = await db.execute(query)
    return result.scalars().all()

