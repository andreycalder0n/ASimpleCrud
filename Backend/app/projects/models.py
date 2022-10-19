from unittest.util import _MAX_LENGTH
from venv import create
from turtle import title
from django.db import models

# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)