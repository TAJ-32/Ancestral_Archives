"""  
Set up the connection to the db and configure SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
