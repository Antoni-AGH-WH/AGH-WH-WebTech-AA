from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

    class Config:
        schema_extra = {"example": {"first_name": "Jerzetta","last_name": "Kłosińska",}}

class Student(BaseModel):
    id: int
    real_id: int
    first_name: str
    last_name: str

class StudentUpdateSchema(BaseModel):
    id: int
    first_name: str
    last_name: str

def ID_maker(a):
    ID = ""
    for i in range(a):
        ID = ID + str(random.randint(0,9))
    ID = int(ID)
    return ID


STUDENTS = {}

@app.get("/students")
async def get_students():
    return STUDENTS

@app.post("/students")
async def create_student(student: StudentCreateSchema):
    id = len(STUDENTS) + 1
    real_id = ID_maker(2)
    new_student = Student(**student.dict(), id=id, real_id = real_id)
    STUDENTS[id] = new_student
    return new_student

@app.get("/STUDENTS/<id>")
async def find_student_by_id(item_id: int):
    if item_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"Student ID": STUDENTS[item_id]}

@app.post("/STUDENTS")
async def modify_student(item_id: int, first_name:str, last_name: str):
    if item_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Student not found")
    new_student = StudentUpdateSchema(first_name = first_name, last_name = last_name, id=item_id)
    STUDENTS[item_id] = new_student
    return {"Student ID:", STUDENTS[item_id]}

#uvicorn KOD:app --reload