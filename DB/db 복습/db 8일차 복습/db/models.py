from django.db import models
class Genre(models.Model):
    name = models.CharField(max_length=30)


class Artist(models.Model):
    name = models.CharField(max_length=30)
    debut = models.DateField()


class Album(models.Model):
    name = models.CharField(max_length=30)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)