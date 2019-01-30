from django.db import models
import datetime

# Create your models here.
class Candidate(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    platform = models.TextField()

    def __str__(self):
        return self.lastname


class Position(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="vote")
    vote_datetime = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.candidate
