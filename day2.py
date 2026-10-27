# # CURD Operaton with FastAPI + PostgreSQL

# from database import get_connection
# from pydantic import BaseModel
# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# class Student(BaseModel):
#     name:str
#     course:str
#     age:int

# @app.get("/students")
# def get_students():
#     connection = get_connection()

#     try:
#         cursor = connection.cursor()

#         cursor.execute(
#             "SELECT id, name, course, age FROM students ORDER BY id"
#         )

#         rows = cursor.fetchall()

#         students = []
#         for row in rows:
#             students.append({
#                 "id": row[0],
#                 "name": row[1],
#                 "course": row[2],
#                 "age": row[3]
#             })

#         cursor.close()

#         return {"students": students}

#     finally:
#         connection.close()


# @app.post("/students", status_code=201)
# def add_student(student: Student):
#     connection = get_connection()

#     try:
#         cursor = connection.cursor()

#         cursor.execute(
#             """
#             INSERT INTO students (name, course, age)
#             VALUES (%s, %s, %s)
#             RETURNING id, name, course, age
#             """,
#             (student.name, student.course, student.age)
#         )

#         row = cursor.fetchone()
#         connection.commit()
#         cursor.close()

#         return {
#             "message": "Student added successfully",
#             "student": {
#                 "id": row[0],
#                 "name": row[1],
#                 "course": row[2],
#                 "age": row[3]
#             }
#         }

#     except Exception:
#         connection.rollback()
#         raise

#     finally:
#         connection.close()

# @app.put("/students/{student_id}")
# def update_student(student_id:int,student:Student):
#     connection=get_connection()

#     try:
#         cursor=connection.cursor()

#         cursor.execute(
#             """
#             UPDATE students
#             SET name =%s,course=%s,age=%s
#             WHERE id  = %s
#             RETURNING id,name,course,age
#             """,
#             (student.name,student.course,student.age,student_id)
#         )
#         row = cursor.fetchone()

#         if row is None:
#             raise HTTPException(
#             status_code=404,
#             detail="Student None Found!!!",
#         )
#         connection.commit()
#         cursor.close()

#         return{
#         "message":"Student Updated Successfully",
#         "student":{
#             "id": row[0],
#             "name":row[1],
#             "course":row[2],
#             "age":row[3]   
#             }
#         }
#     except Exception:
#         connection.rollback()
#         raise
#     finally:
#         connection.close()

# @app.delete("/students/{student_id}")
# def delete_student(student_id:int):
#     connection = get_connection()
#     try:
#         cursor=connection.cursor()
#         cursor.execute(
#             """
#             DELETE From students
#             WHERE id=%s
#             RETURNING id
#             """,
#             (student_id,)
#         )
#         row=cursor.fetchone()
#         if row is None:
#             raise HTTPException(
#             status_code=404,
#             detail="Student Not Found"
#         )
#         connection.commit()
#         cursor.close()
#         return {
#         "message":"Student Deleted Successfully!!!",
#         "id": row[0]
#         }
#     except Exception:
#         connection.rollback()
#         raise
#     finally:
#         connection.close()

# @app.get("/students/{student_id}")
# def get_student(student_id:int):
#     connection=get_connection()

#     try:
#         cursor=connection.cursor()

#         cursor.execute(
#         """
#         SELECT id ,name,course,age
#         FROM students
#         WHERE id = %s
#         """,
#         (student_id,)
#         )
#         row=cursor.fetchone()
#         if row is None:

#             raise HTTPException(
#                 status_code=404,
#                 detail="Student Not Found"
#             )
#         cursor.close()
#         return {
#             "id" :row[0],
#             "name":row[1],
#             "course":row[2],
#             "age":row[3]

#         }
#     finally:
#         connection.close()