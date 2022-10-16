from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import  models, schemas, crud

#Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:            #make sure the db session is always closed after the request. Even if there was an exception while processing the request.
        db.close()

@app.get("/")
def test_get():
    return {"Hello world!"}

# add new user
@app.post("/user/", response_model=schemas.User)
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        exist_user = crud.select_user_by_email(db, user.email)
        if exist_user:
            raise HTTPException(status_code=400, detail="User exist")
        else:
            new_user = crud.insert_user(db, user)
    except ProgrammingError as e:          # catch all exception
        raise HTTPException(status_code=500, detail=str(e))
    return new_user

# add new task
@app.post("/task/", response_model=schemas.Task)
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    try:
        user = crud.select_user_by_id(db, task.user_id)
        if user is None:        # check if user exist
            raise HTTPException(status_code=404, detail="User not found, cannot insert")
        else:
            new_task = crud.insert_task(db, task)
    except ProgrammingError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return new_task

# get user's tasks according to user id
@app.get("/user/{user_id}", response_model=schemas.User)
def get_user_tasks(user_id: int, db: Session = Depends(get_db)):
    try:
        # user = crud.select_user_by_id(db, user_id)
        user=db.query(models.User).get(user_id)
        print(type(user))
        print(user.id, user.name, user.has_tasks)
        if user.has_tasks is None:
            print("true")
        else:
            print("false")
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
    except ProgrammingError as e:          # catch all exception
        raise HTTPException(status_code=500, detail=str(e))
    return user

# get task according to task id
@app.get("/task/{task_id}", response_model=schemas.Task)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    try:
        task = crud.select_task_by_id(db, task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="User not found")
    except ProgrammingError as e:          # catch all exception
        raise HTTPException(status_code=500, detail=str(e))
    return task


# update user information according to user id
@app.put("/user/{user_id}", response_model=schemas.User)
def update_user_by_id(user_id: int, modi_user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = crud.select_user_by_id(db, user_id)

        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        elif crud.select_user_by_email(db, modi_user.email) != db_user:
            raise HTTPException(status_code=400, detail="This email already linked with another account")
        else:
            crud.update_user_by_id(db, user_id, modi_user)
    except ProgrammingError as e:          # catch all exception
        raise HTTPException(status_code=500, detail=str(e))
    return db_user

# update task detail according to task id
@app.put("/task/{task_id}", response_model=schemas.Task)
def update_task_by_id(task_id: int, modi_task: schemas.TaskCreate, db: Session = Depends(get_db)):
    try:
        db_task = crud.select_task_by_id(db, task_id)
        db_user = crud.select_user_by_id(db, user_id=modi_task.user_id)
        if db_task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        elif db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            crud.update_task_by_id(db, task_id, modi_task)
    except ProgrammingError as e:          # catch all exception
        raise HTTPException(status_code=500, detail=str(e))
    return db_task


#delete user
@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = crud.select_user_by_id(db, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            crud.delete_user(db, user)
    except ProgrammingError as e:          # catch all exception
        raise HTTPException(status_code=500, detail=str(e))
    return {"Delete": "True"}

#delete task
@app.delete("/task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        task = crud.select_task_by_id(db, task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        else:
            crud.delete_task(db, task)
    except ProgrammingError as e:          # catch all exception
        raise HTTPException(status_code=500, detail=str(e))
    return {"Delete": "True"}