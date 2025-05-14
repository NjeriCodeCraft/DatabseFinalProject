import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='task_manager',
            user='root',
            password='2002@November'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None