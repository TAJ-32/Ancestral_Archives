"""
Contains the actual functions to interact with the database
Used by API routes to create, read, update, and delete data
Separates the logic between the database and FastAPI endpoints
"""

from . import models, schemas
from django.db import transaction

# ----- PERSON -----
def create_person(person_data: schemas.PersonCreate) -> models.Person:
    with transaction.atomic():
        return models.Person.objects.create(**person_data.dict())

def get_all_people():
    return models.Person.objects.all()


# ----- BIO -----
def create_bio(bio_data: schemas.BioCreate) -> models.Bio:
    with transaction.atomic():
        return models.Bio.objects.create(**bio_data.dict())

def get_all_bios():
    return models.Bio.objects.all()


# ----- STORY -----
def create_story(story_data: schemas.StoryCreate) -> models.Story:
    with transaction.atomic():
        return models.Story.objects.create(**story_data.dict())

def get_all_stories():
    return models.Story.objects.all()


# ----- COUNTRY -----
def create_country(country_data: schemas.CountryCreate) -> models.Country:
    with transaction.atomic():
        return models.Country.objects.create(**country_data.dict())

def get_all_countries():
    return models.Country.objects.all()


# ----- STATE -----
def create_state(state_data: schemas.StateCreate) -> models.State:
    with transaction.atomic():
        return models.State.objects.create(**state_data.dict())

def get_all_states():
    return models.State.objects.all()


# ----- CITY -----
def create_city(city_data: schemas.CityCreate) -> models.City:
    with transaction.atomic():
        return models.City.objects.create(**city_data.dict())

def get_all_cities():
    return models.City.objects.all()


# ----- RELIGION -----
def create_religion(religion_data: schemas.ReligionCreate) -> models.Religion:
    with transaction.atomic():
        return models.Religion.objects.create(**religion_data.dict())

def get_all_religions():
    return models.Religion.objects.all()


# ----- RACE -----
def create_race(race_data: schemas.RaceCreate) -> models.Race:
    with transaction.atomic():
        return models.Race.objects.create(**race_data.dict())

def get_all_races():
    return models.Race.objects.all()


# ----- ETHNICITY -----
def create_ethnicity(ethnicity_data: schemas.EthnicityCreate) -> models.Ethnicity:
    with transaction.atomic():
        return models.Ethnicity.objects.create(**ethnicity_data.dict())

def get_all_ethnicities():
    return models.Ethnicity.objects.all()


# ----- GENDER -----
def create_gender(gender_data: schemas.GenderCreate) -> models.Gender:
    with transaction.atomic():
        return models.Gender.objects.create(**gender_data.dict())

def get_all_genders():
    return models.Gender.objects.all()


