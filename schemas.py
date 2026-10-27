from pydantic import BaseModel,Field

class Student(BaseModel):
    name: str = Field(min_length=2,max_length=100)
    course:str=Field(min_length=2,max_length=100)
    age:int=Field(ge=1,le=100)