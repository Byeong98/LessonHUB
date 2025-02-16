from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db

from config import SECRET_KEY, ALGORITHM
from jose import jwt, JWTError

from domain.users import crud


from fastapi import Request

async def get_token_from_header(request: Request):
    authorization: str = request.headers.get("Authorization")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = authorization.split(" ")[1]  # 'Bearer '를 제거하고 토큰만 가져오기
    return token

# 로그인 사용자 토큰 값 가져오기
async def get_current_user(token: Annotated[str, Depends(get_token_from_header)], db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")
        if not user_email:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # 사용자 정보 조회 
    user = await crud.get_user(db , email=user_email)
    if not user:
        raise credentials_exception
    return user
