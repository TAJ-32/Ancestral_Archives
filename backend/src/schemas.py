"""
This validates data to ensure API requests access the data properly
    - Controls what data is returned from the API to users
And serializes the data to convert db objects into JSON 
"""

from pydantic import BaseModel


from pydantic import BaseModel
from typing import Optional, List
from datetime import date

"""
We have to make the base models for every table here
because this will define how it is sent and receied via API
The models.py file defines how data is stored in the database
So it seems like we are doing it twice but it serves different purposes
"""
class PersonBase(BaseModel):
    first_name: str
    last_name: str
    age: Optional[int] = None
    birth_date: Optional[date] = None
    country_origin: Optional[str] = None
    state_origin: Optional[str] = None
    city_origin: Optional[str] = None
    country_current: Optional[str] = None
    state_current: Optional[str] = None
    city_current: Optional[str] = None


class PersonCreate(PersonBase):
    pass  # Used for creating a new person


class PersonResponse(PersonBase):
    person_id: int

    class Config:
        from_attributes = True


class BioBase(BaseModel):
    bio: str


class BioCreate(BioBase):
    person_id: int


class BioResponse(BioBase):
    bio_id: int
    person_id: int

    class Config:
        from_attributes = True


class StoryBase(BaseModel):
    story_name: str
    story_text: str


class StoryCreate(StoryBase):
    person_id: int


class StoryResponse(StoryBase):
    story_id: int
    person_id: int

    class Config:
        from_attributes = True


class CountryBase(BaseModel):
    country_name: str


class CountryCreate(CountryBase):
    pass


class CountryResponse(CountryBase):
    country_id: int

    class Config:
        from_attributes = True
