import json
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
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": "당신은 친절하고 정확한 교수안 작성 도우미입니다. "
                "주어진 성취기준과 성취기준 해설을 바탕으로 잘 구조화된 교수안을 작성해야 합니다. "
                "교수안은 단원, 제목, 학습목표, 도입, 전개, 정리, 참고자료로 구성됩니다."
                "You are a helpful assistant designed to output JSON."
            },
            {
                "role": "user",
                "content": f"단원: {teach_create.unit}\n"
                f"성취기준: {teach_create.standard}\n"
                f"성취기준해설: {teach_create.commentary}\n"
                f"성취기준과 성취기준 해설을 보고 교수안을 작성해줘."
                "{단원: string... , 제목: string..., 학습목표: [string ...], 도입: [string ...], 전개: [string ...], 정리: [string ...], 참고자료: [string + URL ...] } "
            }
        ],
    )

    result = completion.choices[0].message.content
    if not result:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="교수안 제작 실패")

    parsed_json = json.loads(result)
    return parsed_json
