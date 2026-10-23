
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()

# Student data (temporary storage)
students = [
    {"id": 1, "name": "Mohit", "course": "BCA", "age": 21},
    {"id": 2, "name": "Rahul", "course": "BBA", "age": 22},
    {"id": 3, "name": "Priya", "course": "BCA", "age": 20}
]

class Student(BaseModel):
    name:str
    course:str
    age:int

# 1. Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}

#Get student
@app.get("/students")
def get_students():
    return{"student": students}

#Add student
@app.post("/students")
def add_student(student: Student):
    new_student={
        "id": len(students)+1,
        "name": student.name,
        "course":student.course,
        "age":student.age
    }
    students.append(new_student)
    return{
        "message": "Student added successfully",
        "student": new_student
}
#search STUDENT BY ID
@app.get("/students/{student_id}")
def get_student(student_id:int):
    for student in students:
        if student["id"]==student_id:
            return student
    raise HTTPException(
            status_code=404,
            detail="Student not found"
            )
#UPDATE STUDENT
@app.put("/students/{student_id}")
def update_student(student_id:int,student:Student):
    for existing_student in students:
        if existing_student["id"] == student_id:
            existing_student["name"]=student.name
            existing_student["course"]=student.course
            existing_student["age"]=student.age
            return{
                "message":"Student updated successfully",
                "student": existing_student
            }
            raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
#DELETE STUDENT
@app.delete("/studens/{student_id}")
def delete_student(student_id:int):
    for student in students:
        if student["id"]==student_id:
            students.remove(student)
            return {"message":"Student Data Deleted successfully"}
            raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )

