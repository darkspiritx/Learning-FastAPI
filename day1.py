
from fastapi import FastAPI

app = FastAPI()

# Student data (temporary storage)
students = [
    {"id": 1, "name": "Mohit", "course": "BCA", "age": 21},
    {"id": 2, "name": "Rahul", "course": "BBA", "age": 22},
    {"id": 3, "name": "Priya", "course": "BCA", "age": 20}
]


# 1. Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


# 2. Get all students
@app.get("/students")
def get_students():
    return {"students": students}


# 3. Get one student by ID (Path Parameter)
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}


# 4. Filter students by course (Query Parameter)
@app.get("/search")
def search_students(course: str):
    result = []

    for student in students:
        if student["course"].lower() == course.lower():
            result.append(student)

    return {"students": result}
