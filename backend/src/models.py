"""
Define models (database tables)
Represents how data is stored in the database
Each class corresponds to a table
Basically builds the ORM structure so we can do things with the database using Python
"""

from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from db_config import Base  # Assuming database.py sets up SQLAlchemy's Base

class Person(Base):
    __tablename__ = "person"

    person_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    age = Column(Integer)
    birth_date = Column(Date)
    country_origin = Column(Text)
    state_origin = Column(Text)
    city_origin = Column(Text)
    country_current = Column(Text)
    state_current = Column(Text)
    city_current = Column(Text)

    bio = relationship("Bio", back_populates="person", cascade="all, delete")
    stories = relationship("Story", back_populates="person", cascade="all, delete")


class Bio(Base):
    __tablename__ = "bio"

    bio_id = Column(Integer, primary_key=True, index=True)
    bio = Column(Text, nullable=False)
    person_id = Column(Integer, ForeignKey("person.person_id", ondelete="CASCADE"))

    person = relationship("Person", back_populates="bio")


class Story(Base):
    __tablename__ = "story"

    story_id = Column(Integer, primary_key=True, index=True)
    story_name = Column(Text, nullable=False)
    story_text = Column(Text, nullable=False)
    person_id = Column(Integer, ForeignKey("person.person_id", ondelete="CASCADE"))

    person = relationship("Person", back_populates="stories")


class Country(Base):
    __tablename__ = "country"

    country_id = Column(Integer, primary_key=True, index=True)
    country_name = Column(Text, nullable=False)


class State(Base):
    __tablename__ = "state"

    state_id = Column(Integer, primary_key=True, index=True)
    state_name = Column(Text, nullable=False)
    country_id = Column(Integer, ForeignKey("country.country_id", ondelete="CASCADE"))


class City(Base):
    __tablename__ = "city"

    city_id = Column(Integer, primary_key=True, index=True)
    city_name = Column(Text, nullable=False)
    country_id = Column(Integer, ForeignKey("country.country_id", ondelete="CASCADE"))
    state_id = Column(Integer, ForeignKey("state.state_id", ondelete="CASCADE"))


class Religion(Base):
    __tablename__ = "religion"

    religion_id = Column(Integer, primary_key=True, index=True)
    religion_name = Column(Text, nullable=False)


class Race(Base):
    __tablename__ = "race"

    race_id = Column(Integer, primary_key=True, index=True)
    race_name = Column(Text, nullable=False)


class Ethnicity(Base):
    __tablename__ = "ethnicity"

    ethnicity_id = Column(Integer, primary_key=True, index=True)
    ethnicity_name = Column(Text, nullable=False)


class Gender(Base):
    __tablename__ = "gender"

    gender_id = Column(Integer, primary_key=True, index=True)
    gender_name = Column(Text, nullable=False)
