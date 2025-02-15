from pydantic import BaseModel
from pydantic import BaseModel, field_validator
from typing import List

class TeachCreate(BaseModel):
    grade_id: int
    subject_id: int
    session_id: int
    unit_id: int 
    standard_id: List[int]
    
    @field_validator('session_id', 'subject_id','grade_id', 'unit_id','standard_id')
    def validate_not_zero(cls, v):
        if not v:
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class Grades(BaseModel):
    id: int
    title: str

# 과목 조회
class Subjects(BaseModel):
    id: int
    title: str

# 과목 상세 조회
class Sessions(BaseModel):
    id: int
    title: str

# 단원 조회
class Units(BaseModel):
    id: int
    title: str

# 성취기준 조회
class Standards(BaseModel):
    id: int
    title: str