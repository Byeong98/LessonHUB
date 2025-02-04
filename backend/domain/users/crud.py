from datetime import datetime

from passlib.hash import pbkdf2_sha256 as pwd_context
from sqlalchemy.orm import Session
from domain.users.schema import UserCreate
from models import User

# 회원가입
def create_user(db: Session, user_create: UserCreate):
    db_user = User(email=user_create.email,
                    password=pwd_context.hash(user_create.password1),
                    create_at=datetime.now())
    db.add(db_user)
    db.commit()

# 회원가입시 중복 이메일 확인
def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(User.email == user_create.email).first()


def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()