from datetime import datetime
from pydantic import BaseModel

#Create Pydantic models/schemas

class TaskBase(BaseModel):
    name: str
    ddl_time: datetime
    user_id: int
    

class TaskCreate(TaskBase):     # attributes that needed when create this task
    pass

    class Config:        # orm mode to used under related table query
        orm_mode = True      # to support models that map to ORM objects


class Task(TaskBase):       # attributes that needed to become a ORM objects, should be same as model table
    id:int
    create_time: datetime
    

    class Config:
        orm_mode = True



class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id:int
    has_tasks: list[TaskCreate] = []

    class Config:
        orm_mode = True