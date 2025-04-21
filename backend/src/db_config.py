import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from django.db import connection

DATABASE_URL = os.getenv("DATABASE_URL")

# FastAPI: SQLAlchemy Engine & Session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Django: Database connection (Django ORM already knows how to connect)
def get_django_connection():
    return connection