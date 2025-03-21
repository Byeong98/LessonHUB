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
with open("teach_data/ai_url.json", 'r', encoding='utf-8') as f:
    ai_url = json.load(f)

db = async_session()


async def Validation_data(model, data):
    query = select(model).filter(model.title == data)
    result = await db.execute(query)
    return result.scalar()


# 과목별 단원 + 성취기준 저장
async def csreate_data(data):
    for subject, sections in data.items():
        vaildate = await Validation_data(Subjects, subject)
        if vaildate:
            print(f'{subject} 데이터 존제')
            break
        query = insert(Subjects).values(title=subject).returning(Subjects.id)
        result = await db.execute(query)
        await db.commit()
        subject_id = result.scalar()

        for section, units in sections.items():
            query = insert(Sections).values(
                title=section, subject_id=subject_id).returning(Sections.id)
            result = await db.execute(query)
            await db.commit()
            section_id = result.scalar()

            for unit, standards in units.items():
                query = insert(Units).values(
                    title=unit, section_id=section_id).returning(Units.id)
                result = await db.execute(query)
                await db.commit()
                unit_id = result.scalar()

                for standard in standards:
                    query = insert(Standards).values(
                        title=standard, unit_id=unit_id)
                    await db.execute(query)
                    await db.commit()
    await db.close()
    print("교수안 데이터")


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
    print("해설 데이터")


# 학년 데이터
grades = ["고등학교 1학년", "고등학교 2학년", "고등학교 3학년"]

# 학년 데이터 저장


async def create_grades(grades):
    for grade in grades:
        query = insert(Grades).values(title=grade)
        await db.execute(query)
        await db.commit()
    await db.close()
    print("학년 데이터")


async def create_ai_url(ai_url):
    for ai_url in ai_url["ai_url"]:
        query = insert(Aiurls).values(
            name=ai_url["이름"],
            url=ai_url["url"],
            content=ai_url["설명"]
        )
        await db.execute(query)
        await db.commit()
    await db.close()
    print("ai 데이터")


asyncio.run(csreate_data(data))
asyncio.run(create_commentary(commentary_data))
asyncio.run(create_grades(grades))
asyncio.run(create_ai_url(ai_url))
