# CURD Operaton with FastAPI + PostgreSQL 

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from database import get_db_connection

app = FastAPI(title="Student Management API")


class Student(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    course: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=1, le=100)


@app.get("/students")
def get_students():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, name, course, age FROM students ORDER BY id"
            )
            rows = cursor.fetchall()

            return {
                "students": [
                    {
                        "id": row[0],
                        "name": row[1],
                        "course": row[2],
                        "age": row[3],
                    }
                    for row in rows
                ]
            }


@app.post("/students", status_code=201)
def add_student(student: Student):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO students (name, course, age)
                VALUES (%s, %s, %s)
                RETURNING id, name, course, age
                """,
                (student.name, student.course, student.age),
            )
            row = cursor.fetchone()

            return {
                "message": "Student added successfully",
                "student": {
                    "id": row[0],
                    "name": row[1],
                    "course": row[2],
                    "age": row[3],
                },
            }


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE students
                SET name = %s, course = %s, age = %s
                WHERE id = %s
                RETURNING id, name, course, age
                """,
                (student.name, student.course, student.age, student_id),
            )
            row = cursor.fetchone()

            if row is None:
                raise HTTPException(
                    status_code=404,
                    detail="Student not found",
                )

            return {
                "message": "Student updated successfully",
                "student": {
                    "id": row[0],
                    "name": row[1],
                    "course": row[2],
                    "age": row[3],
                },
            }


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM students
                WHERE id = %s
                RETURNING id
                """,
                (student_id,),
            )
            row = cursor.fetchone()

            if row is None:
                raise HTTPException(
                    status_code=404,
                    detail="Student not found",
                )

            return {
                "message": "Student deleted successfully",
                "student_id": row[0],
            }


@app.get("/students/{student_id}")
def get_student(student_id: int):
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, name, course, age
                FROM students
                WHERE id = %s
                """,
                (student_id,),
            )
            row = cursor.fetchone()

            if row is None:
                raise HTTPException(
                    status_code=404,
                    detail="Student not found",
                )

            return {
                "id": row[0],
                "name": row[1],
                "course": row[2],
                "age": row[3],
            }
