from sqlalchemy import MetaData, create_engine, text
import oracledb
from config import SQLALCHEMY_DATABASE_URL



# sync_engine = create_engine("oracle+oracledb://system:BMnpng98@localhost:1521/xe")

# with sync_engine.connect() as connection:
#         print(connection.scalar(text("SELECT 'Hello World' FROM dual"))) 

# connection = oracledb.connect(user="system", password="BMnpng98", dsn="localhost:1521/xe")

# cursor = connection.cursor()
# cursor.execute("""SELECT 'Hello World' FROM dual""")

# print(cursor.fetchall())


import asyncio
from sqlalchemy.ext.asyncio import create_async_engine

async_engine = create_async_engine("oracle+oracledb://system:BMnpng98@localhost:1521/xe")

async def async_query():
    async with async_engine.connect() as connection:
        result = await connection.execute(text("SELECT 'Hello World' FROM dual"))
        print(result.scalar())  

# 실행
asyncio.run(async_query())