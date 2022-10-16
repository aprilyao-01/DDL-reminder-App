# All the crud methods in this file

from sqlalchemy.orm import Session
# allow to declare the type of the db parameters and have better type checks and completion in functions
import datetime

from . import models, schemas

# Insert user
def insert_user(db:Session, user: schemas.UserCreate):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Insert task
def insert_task(db:Session, task: schemas.TaskCreate):
    new_task = models.Task(**task.dict())
    new_task.create_time = datetime.datetime.now()
    print(datetime.datetime.now())
    print(new_task)
    db.add(new_task)        # add to db
    db.commit()             # commit changes
    db.refresh(new_task)    # refresh instance
    return new_task

# Read user by id
def select_user_by_id(db:Session, user_id: int):
    return db.query(models.User).get(user_id)

# Read user by email
def select_user_by_email(db:Session, user_email: str):
    return db.query(models.User).filter(models.User.email == user_email).first()

# Read task by id
def select_task_by_id(db:Session, task_id: int):
    return db.query(models.Task).get(task_id)

# Update user by id
def update_user_by_id(db: Session, user_id: int, modi_user: schemas.UserCreate):
    db_dept = db.query(models.User).get(user_id)
    db_dept.name = modi_user.name
    db_dept.email = modi_user.email
    db_dept.password = modi_user.password
    db.commit()
    return db_dept

# Update task by id
def update_task_by_id(db: Session, task_id: int, modi_task: schemas.TaskCreate):
    db_task = db.query(models.Task).get(task_id)
    db_task.name = modi_task.name
    db_task.ddl_time = modi_task.ddl_time
    db.commit()
    return db_task

# Delete user
def delete_user(db: Session, user: schemas.User):
    db.delete(user)
    db.commit()
    return

# Delete task
def delete_task(db: Session, task: schemas.Task):
    db.delete(task)
    db.commit()
    return