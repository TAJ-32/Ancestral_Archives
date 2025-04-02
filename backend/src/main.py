from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, db_config, schemas, crud

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=db_config.engine)

# Route to create a user
@app.post("/person/", response_model=schemas.UserResponse)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(db_config.get_db)):
    return crud.create_person(db, user)

# Route to get users
@app.get("/person/", response_model=list[schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(db_config.get_db)):
    return crud.get_persons(db, skip, limit)
