from pydantic import BaseModel
from typing import Optional
from datetime import date

# User Models
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    user_id: int
    created_at: str

# Task Models
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    status: Optional[str] = "pending"
    priority: Optional[str] = "medium"
    due_date: Optional[date] = None
    user_id: int

class TaskInDB(TaskCreate):
    task_id: int
    created_at: str