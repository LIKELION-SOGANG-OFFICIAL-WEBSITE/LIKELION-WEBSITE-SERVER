from django.db import models

class Visit(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date_time)

