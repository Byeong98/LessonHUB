from pydantic import BaseModel
from pydantic import BaseModel, field_validator, EmailStr
from pydantic_core.core_schema import FieldValidationInfo


# 회원가입 스키마
class UserCreate(BaseModel):
    email : EmailStr
    password1 : str
    password2 : str
    
    @field_validator('email', 'password1', 'password2')
    def validate_password1(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        if len(v) < 8:
            raise ValueError('비번호는 8자 이상으로 설정하세요.')
        return v
    
    @field_validator('password2')
    def password_match(cls, v, info: FieldValidationInfo):
        if 'password1' in info.data and v != info.data['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v

# 로그인 스키마
class Token(BaseModel):
    access_token: str
    token_type: str
    email: str

class UserLogin(BaseModel):
    username: EmailStr
    password: str