"""
Define models (database tables)
Represents how data is stored in the database
Each class corresponds to a table
Basically builds the ORM structure so we can do things with the database using Python
"""

from django.db import models

class Person(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    age = models.TextField(blank=True, null=True)
    birth_date = models.TextField(blank=True, null=True)
    country_origin = models.TextField(blank=True, null=True)
    state_origin = models.TextField(blank=True, null=True)
    city_origin = models.TextField(blank=True, null=True)
    country_current = models.TextField(blank=True, null=True)
    state_current = models.TextField(blank=True, null=True)
    city_current = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Bio(models.Model):
    bio = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name}"


class Story(models.Model):
    story_name = models.TextField()
    story_text = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name}"

class Country(models.Model):
    country_name = models.TextField()

    def __str__(self):
        return f"{self.country_name}"

class State(models.Model):
    state_name = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.state_name}"
    
class City(models.Model):
    city_name = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city_name}"

class Religion(models.Model):
    religion_name = models.TextField()

    def __str__(self):
        return f"{self.religion_name}"

class Race(models.Model):
    race_name = models.TextField()

    def __str__(self):
        return f"{self.race_name}"

class Ethnicity(models.Model):
    ethnicity_name = models.TextField()

    def __str__(self):
        return f"{self.ethnicity_name}"

class Gender(models.Model):
    gender_name = models.TextField()

    def __str__(self):
        return f"{self.gender_name}"
