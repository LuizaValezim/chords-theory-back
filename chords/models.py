from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    chords = ArrayField(models.CharField(max_length=40, blank=False))
    
    def __str__(self):
      return f"{self.tagTitle}"