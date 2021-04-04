from django.db import models
from django.conf import settings


class MoviePost(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    released = models.BooleanField(default=True)
    tagline = models.CharField(max_length=256)
    vote_avg = models.FloatField()
    vote_cnt = models.IntegerField()

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=128)
    posts = models.CharField(models.ForeignKey(MoviePost))

    def __str__(self):
        return self.name

#Spoken Language
class Language(models.Model):
    name = models.CharField(max_length=32)
    posts = models.CharField(models.ForeignKey(MoviePost))

    def __str__(self):
        return self.name