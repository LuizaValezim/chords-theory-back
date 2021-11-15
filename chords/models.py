from django.db import models
from django.contrib.postgres.fields import ArrayField

class Combinations(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    chords = ArrayField(models.CharField(max_length=40, blank=True))
    
    def __str__(self):
      return f'{self.id}. {self.title}. {self.chords}'  