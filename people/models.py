from django.db import models

class Part(models.TextChoices):
    FRONT = 'FRONT'
    BACK = 'BACK'

class BabyLion(models.Model):
    name = models.CharField(max_length=20)
    generation = models.IntegerField()


    def __str__(self):
        return self.name;

class AdultLion(models.Model):
    name = models.CharField(max_length=20)
    generation = models.IntegerField()
    part = models.CharField(max_length=20, choices=Part.choices)
    emoji_url = models.FileField()

    def __str__(self):
        return self.name;
