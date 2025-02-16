from pydantic import BaseModel
from pydantic import BaseModel, field_validator
from typing import List

class TeachCreate(BaseModel):
    grade_id: int
    subject_id: int
    section_id: int
    unit_id: int 
    standard_id: List[int]
    
    @field_validator('section_id', 'subject_id','grade_id', 'unit_id','standard_id')
    def validate_not_zero(cls, v):
        if not v:
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

# 교수안 목록 조회
class TeachList(BaseModel):
    id: int
    grade: str
    subject: str
    section: str
    unit: str
    title: str
    date: str

# 교수안 상세 조회
class TeachDetail(BaseModel):
    id: int
    grade: str
    subject: str
    section: str
    unit: str
    title: str
    objective: str
    intro: str
    deployment: str
    finish: str
    date: str

class TeachUpdate(BaseModel):
    teach_id: int
    objective: str
    intro: str
    deployment: str
    finish: str

class TeachID(BaseModel):
    id: int

#학년 조회
class Grades(BaseModel):
    id: int
    title: str

# 과목 조회
class Subjects(BaseModel):
    id: int
    title: str

# 과목 상세 조회
class Sections(BaseModel):
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