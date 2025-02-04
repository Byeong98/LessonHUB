from datetime import timedelta, datetime

from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status
from passlib.hash import pbkdf2_sha256 as pwd_context

from database import get_db
from domain.users import crud, schema

router = APIRouter(
    prefix="/api/user",
)

# 회원가입
@router.post("/create", status_code=status.HTTP_204_NO_CONTENT)
def user_create(_user_create: schema.UserCreate, db: Session = Depends(get_db)):
    user = crud.get_existing_user(db, user_create=_user_create)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="이미 존재하는 사용자입니다.")
    else:
        crud.create_user(db=db, user_create=_user_create)

# 로그인
@router.post('/login',response_model=schema.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = crud.get_user(db, form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Incorrect username or password',
                            headers={"WWW-Authenticate": "Bearer"})
    data = {
        "sub": user.email,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    access_token = jwt.encode(data, SECRET_KEY , algorithm=ALGORITHM) # type: ignore

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "email": user.email
    }