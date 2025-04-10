from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import MetaData
from config import SQLALCHEMY_ASYNC_DATABASE_URL

Base = declarative_base()

meta = MetaData()
async_engine = create_async_engine(SQLALCHEMY_ASYNC_DATABASE_URL)
async_session = async_sessionmaker(async_engine, autoflush=False, autocommit=False)

async def get_db():
	# 처음 실행시
    async with async_engine.begin() as conn:
        await conn.run_sync(meta.create_all)

    db = async_session()
    try:
        yield db
    finally:
        await db.close()

