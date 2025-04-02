"""
Contains the actual functions to interact with the database
Used by API routes to create, read, update, and delete data
Separates the logic between the database and FastAPI endpoints
"""

from sqlalchemy.orm import Session
import models, schemas

# 1️⃣ Create a new person
def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(**person.model_dump())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person

# 2️⃣ Get all persons (with optional pagination)
def get_persons(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Person).offset(skip).limit(limit).all()

# 3️⃣ Get a single person by ID
def get_person(db: Session, person_id: int):
    return db.query(models.Person).filter(models.Person.person_id == person_id).first()

# 4️⃣ Create a bio for a person
def create_bio(db: Session, bio: schemas.BioCreate):
    db_bio = models.Bio(**bio.model_dump())
    db.add(db_bio)
    db.commit()
    db.refresh(db_bio)
    return db_bio

# 5️⃣ Get all bios
def get_bios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Bio).offset(skip).limit(limit).all()

# 6️⃣ Create a story for a person
def create_story(db: Session, story: schemas.StoryCreate):
    db_story = models.Story(**story.model_dump())
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story

# 7️⃣ Get all stories
def get_stories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Story).offset(skip).limit(limit).all()

# 8️⃣ Get a specific story
def get_story(db: Session, story_id: int):
    return db.query(models.Story).filter(models.Story.story_id == story_id).first()
