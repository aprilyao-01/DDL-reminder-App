from fastapi import Depends, FastAPI

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