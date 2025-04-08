from djongo import models
from bson import ObjectId

class User(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    class Meta:
        db_table = 'users'

class Team(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    members = models.JSONField()
    class Meta:
        db_table = 'teams'

class Activity(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    class Meta:
        db_table = 'activity'

class Leaderboard(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'

class Workout(models.Model):
    _id = models.ObjectIdField(default=ObjectId, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duration = models.IntegerField()
    class Meta:
        db_table = 'workouts'