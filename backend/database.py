from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import MetaData
from config import SQLALCHEMY_ASYNC_DATABASE_URL
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

meta = MetaData()
async_engine = create_async_engine(SQLALCHEMY_ASYNC_DATABASE_URL, echo=True)

# 비동기 세션 생성
async_session = sessionmaker(
    bind=async_engine, class_=AsyncSession, autoflush=False, autocommit=False, expire_on_commit=False
)


async def get_db():
	# 처음 실행시
    # async with async_engine.begin() as conn:
    #     await conn.run_sync(meta.create_all)

    db = async_session()
    try:
        yield db
    finally:
        db.close()

