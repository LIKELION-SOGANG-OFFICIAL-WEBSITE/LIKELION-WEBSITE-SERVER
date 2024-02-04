from django.db import models

class VisitType(models.TextChoices):
    TODAY = 'TODAY'
    TOTAL = 'TOTAL'

class Visit(models.Model):
    visit_type = models.CharField(max_length=20, choices=VisitType.choices)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.visit_type

