# # CURD Operaton with FastAPI + PostgreSQL + ERROR HANDLING

# import logging
# import psycopg
# from fastapi import Request
# from fastapi.responses import JSONResponse
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, Field
# from database import get_db_connection


# app = FastAPI(title="Student Management API")


# class Student(BaseModel):
#     name: str = Field(min_length=2, max_length=100)
#     course: str = Field(min_length=2, max_length=100)
#     age: int = Field(ge=1, le=100)


# @app.get("/students")
# def get_students():
#     with get_db_connection() as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "SELECT id, name, course, age FROM students ORDER BY id"
#             )
#             rows = cursor.fetchall()

#             return {
#                 "students": [
#                     {
#                         "id": row[0],
#                         "name": row[1],
#                         "course": row[2],
#                         "age": row[3],
#                     }
#                     for row in rows
#                 ]
#             }


# @app.post("/students", status_code=201)
# def add_student(student: Student):
#     with get_db_connection() as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """
#                 INSERT INTO students (name, course, age)
#                 VALUES (%s, %s, %s)
#                 RETURNING id, name, course, age
#                 """,
#                 (student.name, student.course, student.age),
#             )
#             row = cursor.fetchone()

#             return {
#                 "message": "Student added successfully",
#                 "student": {
#                     "id": row[0],
#                     "name": row[1],
#                     "course": row[2],
#                     "age": row[3],
#                 },
#             }


# @app.put("/students/{student_id}")
# def update_student(student_id: int, student: Student):
#     with get_db_connection() as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """
#                 UPDATE students
#                 SET name = %s, course = %s, age = %s
#                 WHERE id = %s
#                 RETURNING id, name, course, age
#                 """,
#                 (student.name, student.course, student.age, student_id),
#             )
#             row = cursor.fetchone()

#             if row is None:
#                 raise HTTPException(
#                     status_code=404,
#                     detail="Student not found",
#                 )

#             return {
#                 "message": "Student updated successfully",
#                 "student": {
#                     "id": row[0],
#                     "name": row[1],
#                     "course": row[2],
#                     "age": row[3],
#                 },
#             }


# @app.delete("/students/{student_id}")
# def delete_student(student_id: int):
#     with get_db_connection() as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """
#                 DELETE FROM students
#                 WHERE id = %s
#                 RETURNING id
#                 """,
#                 (student_id,),
#             )
#             row = cursor.fetchone()

#             if row is None:
#                 raise HTTPException(
#                     status_code=404,
#                     detail="Student not found",
#                 )

#             return {
#                 "message": "Student deleted successfully",
#                 "student_id": row[0],
#             }


# @app.get("/students/{student_id}")
# def get_student(student_id: int):
#     with get_db_connection() as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """
#                 SELECT id, name, course, age
#                 FROM students
#                 WHERE id = %s
#                 """,
#                 (student_id,),
#             )
#             row = cursor.fetchone()

#             if row is None:
#                 raise HTTPException(
#                     status_code=404,
#                     detail="Student not found",
#                 )

#             return {
#                 "id": row[0],
#                 "name": row[1],
#                 "course": row[2],
#                 "age": row[3],
#             }

# logging.basicConfig(level=logging.ERROR)
# logger =logging.getLogger(__name__)

# @app.exception_handler(psycopg.Error)
# async def database_error_handler(
#     request: Request,
#     exc: psycopg.Error,
# ):
#     logger.error(
#     "Database error on %s %s",
#     request.method,
#     request.url.path,
#     exc_info=(type(exc), exc,exc.__traceback__),
#     )
#     return  JSONResponse(
#         status_code=500,
#         content={
#             "detail":" A DATABASE ERROR OCCURRED. PLEASE TRY AGAIN LATER"
#         },
# )
# # for check error handling working or not(this is temporary)
# # @app.get("/test-db-error")
# # def test_db_error():
# #     raise psycopg.OperationalError("temporary test error")
