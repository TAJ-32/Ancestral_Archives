"""
This validates data to ensure API requests access the data properly
    - Controls what data is returned from the API to users
And serializes the data to convert db objects into JSON 
"""

from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# ---------- PERSON ----------
class PersonBase(BaseModel):
    first_name: str
    last_name: str
    age: int
    birth_date: date
    country_origin: str
    state_origin: str
    city_origin: str
    country_current: str
    state_current: str
    city_current: str

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int  # Assuming Django default ID field is used

    class Config:
        orm_mode = True


# ---------- BIO ----------
class BioBase(BaseModel):
    bio: str
    person_id: int

class BioCreate(BioBase):
    pass

class Bio(BioBase):
    id: int

    class Config:
        orm_mode = True


# ---------- STORY ----------
class StoryBase(BaseModel):
    story_name: str
    story_text: str
    person_id: int

class StoryCreate(StoryBase):
    pass

class Story(StoryBase):
    id: int

    class Config:
        orm_mode = True


# ---------- COUNTRY ----------
class CountryBase(BaseModel):
    country_name: str

class CountryCreate(CountryBase):
    pass

class Country(CountryBase):
    id: int

    class Config:
        orm_mode = True


# ---------- STATE ----------
class StateBase(BaseModel):
    state_name: str
    country_id: int

class StateCreate(StateBase):
    pass

class State(StateBase):
    id: int

    class Config:
        orm_mode = True


# ---------- CITY ----------
class CityBase(BaseModel):
    city_name: str
    country_id: int
    state_id: int

class CityCreate(CityBase):
    pass

class City(CityBase):
    id: int

    class Config:
        orm_mode = True


# ---------- RELIGION ----------
class ReligionBase(BaseModel):
    religion_name: str

class ReligionCreate(ReligionBase):
    pass

class Religion(ReligionBase):
    id: int

    class Config:
        orm_mode = True


# ---------- RACE ----------
class RaceBase(BaseModel):
    race_name: str

class RaceCreate(RaceBase):
    pass

class Race(RaceBase):
    id: int

    class Config:
        orm_mode = True


# ---------- ETHNICITY ----------
class EthnicityBase(BaseModel):
    ethnicity_name: str

class EthnicityCreate(EthnicityBase):
    pass

class Ethnicity(EthnicityBase):
    id: int

    class Config:
        orm_mode = True


# ---------- GENDER ----------
class GenderBase(BaseModel):
    gender_name: str

class GenderCreate(GenderBase):
    pass

class Gender(GenderBase):
    id: int

    class Config:
        orm_mode = True
