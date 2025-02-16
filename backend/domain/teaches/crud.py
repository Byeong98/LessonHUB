from datetime import datetime

from sqlalchemy.orm import selectinload
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
        section=response_json['과목상세'],
        unit_id=unit_id,
        title=response_json['제목'],
        objective=",".join(response_json['학습목표']),
        intro=",".join(response_json['도입']),
        deployment=",".join(response_json['전개']),
        finish=",".join(response_json['정리']),
        create_at=datetime.now(),
        user_id=current_user_id,
    ).returning(Teaches.id)
    result = await db.execute(query)
    await db.commit()

    return result.scalar()

# 교수안 목록 조회
async def get_teach_list(db: AsyncSession, id: int):
    query = (
        select(Teaches)
        .options(selectinload(Teaches.grade), selectinload(Teaches.unit)) 
        .filter(Teaches.user_id == id)
        .order_by(Teaches.id.desc())
    )
    result = await db.execute(query)
    return result.scalars().all()

# 교수안 조회 
async def get_teach_detail(db: AsyncSession, id: int):
    query = select(Teaches).options(selectinload(Teaches.grade), selectinload(Teaches.unit)).filter(Teaches.id == id)
    result = await db.execute(query)
    return result.scalar()

# 단일 값 조회
async def get_title(db: AsyncSession, model, id: int):
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


async def get_filter_list(db: AsyncSession, model, filter_field: str, id: int):
    filter_column = getattr(model, filter_field)
    query = select(model).filter(filter_column == id).order_by(model.id)
    result = await db.execute(query)
    return result.scalars().all()
