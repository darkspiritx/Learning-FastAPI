
from database import get_connection

try:
    connection = get_connection()
    print("PostgreSQL connected successfully!")

    connection.close()
    print("Connection closed.")

except Exception as error:
    print("Database connection failed:")
    print(error)
