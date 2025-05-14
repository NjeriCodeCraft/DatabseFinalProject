from app.database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("SHOW TABLES")
print(cursor.fetchall())
cursor.close()
conn.close()