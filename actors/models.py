from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100)

