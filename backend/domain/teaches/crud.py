from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from models import Teaches, Subjects, Sessions, Units, Standards, Commentaries


# 교수안 저장
async def create_teach(db: AsyncSession, response_json: dict):
    query = insert(Teaches).values(
        
    )



# 과목 조회
async def get_subjects_list(db: AsyncSession):
    query = select(Subjects).order_by(Subjects.title)
    result= await db.execute(query)
    return result.scalars().all()

# 과목 상세 조회
async def get_sission_list(db: AsyncSession, subject_id: int):
    query = select(Sessions).filter(Sessions.subject_id == subject_id).order_by(Sessions.id)
    result = await db.execute(query)
    return result.scalars().all()

# 단원 조회
async def get_unit_list(db: AsyncSession, session_id: int):
    query = select(Units).filter(Units.session_id == session_id).order_by(Units.id)
    result = await db.execute(query)
    return result.scalars().all()
#성취기준 조회
async def get_standard_list(db: AsyncSession, unit_id: int):
    query = select(Standards).filter(Standards.unit_id == unit_id).order_by(Standards.id)
    result = await db.execute(query)
    return result.scalars().all()

# 성취기준 해설 조회
async def get_comentary(db: AsyncSession, standard_id: int):
    query = select(Commentaries).filter(Commentaries.standard_id == standard_id)
    result = await db.execute(query)
    return result.scalars().first()