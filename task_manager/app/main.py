from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from .database import get_db_connection
from .models import UserCreate, UserInDB, TaskCreate, TaskInDB
from typing import List
import mysql.connector

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# User CRUD Operations
@app.post("/users/", response_model=UserInDB)
async def create_user(user: UserCreate):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)"
    cursor.execute(query, (user.username, user.email, user.password))
    conn.commit()
    
    user_id = cursor.lastrowid
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    new_user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return new_user

@app.get("/users/{user_id}", response_model=UserInDB)
async def read_user(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Task CRUD Operations
@app.post("/tasks/", response_model=TaskInDB)
async def create_task(task: TaskCreate):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """INSERT INTO tasks 
               (title, description, status, priority, due_date, user_id) 
               VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(query, (
        task.title, 
        task.description, 
        task.status, 
        task.priority, 
        task.due_date, 
        task.user_id
    ))
    conn.commit()
    
    task_id = cursor.lastrowid
    cursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
    new_task = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return new_task

@app.get("/tasks/{task_id}", response_model=TaskInDB)
async def read_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
    task = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.get("/users/{user_id}/tasks", response_model=List[TaskInDB])
async def read_user_tasks(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM tasks WHERE user_id = %s", (user_id,))
    tasks = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return tasks

@app.put("/tasks/{task_id}", response_model=TaskInDB)
async def update_task(task_id: int, task: TaskCreate):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """UPDATE tasks SET 
               title = %s, 
               description = %s, 
               status = %s, 
               priority = %s, 
               due_date = %s 
               WHERE task_id = %s"""
    cursor.execute(query, (
        task.title, 
        task.description, 
        task.status, 
        task.priority, 
        task.due_date, 
        task_id
    ))
    conn.commit()
    
    cursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
    updated_task = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
    conn.commit()
    
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    
    cursor.close()
    conn.close()
    return {"message": "Task deleted successfully"}