from django.db import models
from djongo.models.fields import ObjectIdField, ArrayReferenceField

class User(models.Model):
    _id = ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Team(models.Model):
    _id = ObjectIdField()
    name = models.CharField(max_length=255)
    members = ArrayReferenceField(to=User, on_delete=models.CASCADE)

class Activity(models.Model):
    _id = ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    _id = ObjectIdField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    _id = ObjectIdField()
    name = models.CharField(max_length=255)
    description = models.TextField()
