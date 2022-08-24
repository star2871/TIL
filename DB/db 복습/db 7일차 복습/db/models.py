from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=30)

class Artist(models.Model):
    name = models.CharField(max_length=30)
    debut = models.DateField()