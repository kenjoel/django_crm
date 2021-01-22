from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# This class represents a user and the permissions he/she is entitled to.
class User(AbstractUser):
    pass


# class condor will represent the leads or people monitored by an agent
class Condor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{first_name}"


# This class represents the agent and all the properties of an individual agent

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
