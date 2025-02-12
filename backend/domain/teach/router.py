from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from database import get_db
from domain.teach import crud, schema

from config import OPENAI_API_KEY
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

router = APIRouter(
    prefix="/api/teach"
)


@router.post("/create", status_code=status.HTTP_200_OK)
async def teach_create(teach_create: schema.TeachCreate, db: AsyncSession = Depends(get_db)):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 친절하고 정확한 교수안 작성 도우미입니다. 주어진 성취기준과 성취기준해설을 바탕으로 잘 구조화된 교수안을 작성해야 합니다. 교수안은 제목, 단원, 학습 목표, 도입, 전개, 정리로 구성됩니다."},
            {"role": "user", "content": f"단원 :{teach_create.unit} \n 성취기준: {teach_create.standard} \n 성취기준해설: {teach_create.commentary}\n 성취기준과, 성취기준해설을 보고 교수안의 제목, 단원, 학습목표와 도입, 전개, 정리를 작성해줘."},
            {"role": "assistant", "content": "제목, 단원\n 1. 학습 목표 설명\n2. 도입\n3. 전개\n4. 정리"}
        ]
    )

    result = completion.choices[0].message.content
    return {"content": result}

