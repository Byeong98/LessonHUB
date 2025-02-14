from models import *
from database import async_session
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

import json
import asyncio
import re

with open('teach_data/teach_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
with open('teach_data/commentary_data.json', 'r', encoding='utf-8') as f:
    commentary_data = json.load(f)


db = async_session()

async def Validation_data(model, data):
    query = select(model).filter(model.title == data)
    result = await db.execute(query)
    return result.scalar()


# 과목별 단원 + 성취기준 저장
async def csreate_data(data):
    for subject, sessions in data.items():
        vaildate = await Validation_data(Subjects, subject)
        if vaildate:
            print(f'{subject} 데이터 존제')
            break
        query = insert(Subjects).values(title=subject).returning(Subjects.id)
        result = await db.execute(query)
        await db.commit()
        subject_id = result.scalar()

        for session, units in sessions.items():
            query = insert(Sessions).values(
                title=session, subject_id=subject_id).returning(Sessions.id)
            result = await db.execute(query)
            await db.commit()
            session_id = result.scalar()

            for unit, standards in units.items():
                query = insert(Units).values(
                    title=unit, session_id=session_id).returning(Units.id)
                result = await db.execute(query)
                await db.commit()
                unit_id = result.scalar()

                for standard in standards:
                    query = insert(Standards).values(
                        title=standard, unit_id=unit_id)
                    await db.execute(query)
                    await db.commit()
    await db.close()


async def create_commentary(commentary_data):
    for commentary in commentary_data["commentary_data"]:
        match = re.search(r"\[(.*?)\]", commentary)
        if match:
            commentary_title = match.group(1)
            query = select(Standards).filter(
                Standards.title.like(f"[%{commentary_title}%]%"))
            result = await db.execute(query)
            standard = result.scalars().first()
            if standard:
                query = insert(Commentaries).values(
                    title=commentary, standard_id=standard.id)
                await db.execute(query)
                await db.commit()
    await db.close()
    

# 학년 데이터
grades = ["고등학교 1학년", "고등학교 2학년", "고등학교 3학년"]

# 학년 데이터 저장
async def create_grades(grades):
    for grade in grades:
        query = insert(Grades).values(title=grade)
        await db.execute(query)
        await db.commit()
    await db.close()


asyncio.run(csreate_data(data))
asyncio.run(create_commentary(commentary_data))
asyncio.run(create_grades(grades))
