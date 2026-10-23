from database import get_connection
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

class Student(BaseModel):
    name:str
    course:str
    age:int

@app.get("/students")
def get_students():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id, name, course, age FROM students ORDER BY id"
        )

        rows = cursor.fetchall()

        students = []
        for row in rows:
            students.append({
                "id": row[0],
                "name": row[1],
                "course": row[2],
                "age": row[3]
            })

        cursor.close()

        return {"students": students}

    finally:
        connection.close()

@app.post("/students",status_code=201)
def add_student(student:Student):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO students (name,course,age)
            value (%s,%s,%s)
            RETURING id,name,course,age
            
            """,
            (student.name,student.course,student.age)
        )
        row = cursor.fetchone()
        connection.commit()

        cursor.close()

        return {
            "message":"Student added successfully",
            "student": {
                "id":row[0],
                "name":row[1],
                "course":row[2],
                "age":row[3]
            }
        }
    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
