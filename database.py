
import psycopg

def get_connection():
    connection = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="student_db",
        user="postgres",
        password="2909"
    )
    return connection
