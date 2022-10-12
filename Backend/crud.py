# All the crud methods in this file

from sqlalchemy.orm import Session
# allow to declare the type of the db parameters and have better type checks and completion in functions

from . import models, schemas

# Create a task
# def insert_task(db: Session, department: schemas.DepartmentCreate):
    