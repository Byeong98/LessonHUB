from datetime import datetime

# from database import database
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select
from passlib.hash import pbkdf2_sha256 as pwd_context

from domain.users.schema import UserCreate
from models import Users

# 회원가입
async def create_user(db: AsyncSession, user_create: UserCreate):
    query = insert(Users).values(
        email=user_create.email,
        password=pwd_context.hash(user_create.password1),
        create_at=datetime.now()
    )
    await db.execute(query)
    await db.commit()

# 이메일 중복 확인
async def get_existing_user(db: AsyncSession, email: str):
    query = select(Users).where(Users.email == email)
    result = await db.execute(query)
    return result.scalar()

async def get_user(db: AsyncSession, email: str):
    query = select(Users).filter(Users.email == email)
    result = await db.execute(query)
    return result.scalar()