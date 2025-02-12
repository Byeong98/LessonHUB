from pydantic import BaseModel
from pydantic import BaseModel, field_validator

class TeachCreate(BaseModel):
    grade: str
    unit: str 
    standard: str 
    commentary: str

    @field_validator('grade', 'unit', 'standard', 'commentary')
    def validate_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 혀옹되지 않습니다.')
        return v