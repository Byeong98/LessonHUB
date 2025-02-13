from models import *
from database import async_session
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

import json
import asyncio
import re

with open('teach_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
with open('commentary_data.json', 'r', encoding='utf-8') as f:
    commentary_data = json.load(f)


db = async_session()
# 과목별 단원 + 성취기준 저장


async def Validation_data(model, data):
    query = select(model).filter(model.title == data)
    result = await db.execute(query)
    return result.scalar()


async def add_data(model, data,):
    query = insert(model).values(title=data).returning(model.id)
    result = await db.execute(query)
    return result.scalar()


async def csreate_data(data):
    for subject, sessions in data.items():
        vaildate = await Validation_data(Subject, subject)
        if vaildate:
            print(f'{subject} 데이터 존제')
            break
        query = insert(Subject).values(title=subject).returning(Subject.id)
        result = await db.execute(query)
        await db.commit()
        subject_id = result.scalar()

        for session, units in sessions.items():
            query = insert(Session).values(
                title=session, subject_id=subject_id).returning(Session.id)
            result = await db.execute(query)
            await db.commit()
            session_id = result.scalar()

            for unit, standards in units.items():
                query = insert(Unit).values(
                    title=unit, session_id=session_id).returning(Unit.id)
                result = await db.execute(query)
                await db.commit()
                unit_id = result.scalar()

                for standard in standards:
                    query = insert(Standard).values(
                        title=standard, unit_id=unit_id)
                    await db.execute(query)
                    await db.commit()
    await db.close()


async def create_commentary(commentary_data):

    for commentary in commentary_data["commentary_data"]:
        match = re.search(r"\[(.*?)\]", commentary)
        if match:
            commentary_title = match.group(1)
            query = select(Standard).filter(
                Standard.title.like(f"[%{commentary_title}%]%"))
            result = await db.execute(query)
            standard = result.scalars().first()
            if standard:
                query = insert(Commentary).values(
                    title=commentary, standard_id=standard.id)
                await db.execute(query)
                await db.commit()
    await db.close()


# asyncio.run(csreate_data(data))
asyncio.run(create_commentary(commentary_data))
