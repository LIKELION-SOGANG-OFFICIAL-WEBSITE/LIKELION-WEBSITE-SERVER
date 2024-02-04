from django.db import models
from generation.models import Generation

class Part(models.TextChoices):
    FRONT_END = 'FRONT-END'
    BACK_END = 'BACK-END'

class BabyLion(models.Model):
    name = models.CharField(max_length=20)
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class AdultLion(models.Model):
    name = models.CharField(max_length=20)
    generation = models.ForeignKey(Generation, on_delete=models.CASCADE)
    part = models.CharField(max_length=20, choices=Part.choices)
    emoji = models.FileField()

    def __str__(self):
        return self.name
