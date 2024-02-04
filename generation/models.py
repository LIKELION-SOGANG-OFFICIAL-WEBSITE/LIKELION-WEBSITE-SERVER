from django.db import models

class Generation(models.Model):
    number = models.IntegerField()
    suffix = models.CharField(max_length=10)

    def __str__(self):
        return str(self.number) + self.suffix
