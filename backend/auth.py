from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db

from config import SECRET_KEY, ALGORITHM
from jose import jwt, JWTError

from domain.users import crud

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user/login")

# 로그인 사용자 토큰 값 가져오기
async def get_current_user(token: Annotated [str, Depends(oauth2_scheme)], db: AsyncSession = Depends(get_db)):
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
