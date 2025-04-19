"""
Define models (database tables)
Represents how data is stored in the database
Each class corresponds to a table
Basically builds the ORM structure so we can do things with the database using Python
"""

from django.db import models

class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()
    birth_date = models.DateField()
    country_origin = models.TextField()
    state_origin = models.TextField()
    city_origin = models.TextField()
    country_current = models.TextField()
    state_current = models.TextField()
    city_current = models.TextField()

class Bio(models.Model):
    bio = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Story(models.Model):
    story_name = models.TextField()
    story_text = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Country(models.Model):
    country_name = models.TextField()

class State(models.Model):
    state_name = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class City(models.Model):
    city_name = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class Religion(models.Model):
    religion_name = models.TextField()

class Race(models.Model):
    race_name = models.TextField()

class Ethnicity(models.Model):
    ethnicity_name = models.TextField()

class Gender(models.Model):
    gender_name = models.TextField()
