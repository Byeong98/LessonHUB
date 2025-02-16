from datetime import timedelta, datetime

from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from passlib.hash import pbkdf2_sha256 as pwd_context

from database import get_db
from domain.users import crud, schema

router = APIRouter(
    prefix="/api/user",
)

# 회원가입
@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
async def user_create(_user_create: schema.UserCreate, db: AsyncSession = Depends(get_db)):
    # 이메일 중복 확인
    user = await crud.get_existing_user(db=db, email=_user_create.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="이미 존재하는 사용자입니다."
        )
    
    # 새로운 사용자 생성
    await crud.create_user(db=db, user_create=_user_create)

# 로그인
@router.post('/login',response_model=schema.Token)
async def login_for_access_token(form_data: schema.UserLogin ,db: AsyncSession = Depends(get_db)):
    if not form_data.username or not form_data.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Email 또는 Password를 입력해 주세요',
                            headers={"WWW-Authenticate": "Bearer"})

    # 사용자 조회
    user = await crud.get_user(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='사용자를 찾을 수 없습니다.',
                            headers={"WWW-Authenticate": "Bearer"})

    data = {
        "sub": user.email,
        "exp": datetime.utcnow() + timedelta(minutes=60)
    }
    access_token = jwt.encode(data, SECRET_KEY , algorithm=ALGORITHM) # type: ignore
    if not access_token:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Token encoding error")
    return {"access_token" : access_token, "token_type" : "bearer", "email": user.email}