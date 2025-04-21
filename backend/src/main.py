from typing import List
from fastapi import FastAPI, HTTPException
import django
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Setup Django ORM
django.setup()

from . import crud, schemas

app = FastAPI()

@app.get("/people", response_model=List[schemas.Person])
def list_people():
    people = crud.get_all_people()
    return people

@app.post("/people", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate):
    try:
        return crud.create_person(person)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
