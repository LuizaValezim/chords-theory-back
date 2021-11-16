from django.db import models

class Combinations(models.Model):
    id = models.AutoField(primary_key=True)
    chords = models.CharField(max_length=20)
    
    def __str__(self):
      return f'{self.id}. {self.chords}'  