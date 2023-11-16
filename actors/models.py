from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'United States'),
    ('BRA', 'Brazil'),
    ('CUB', 'Cuba')
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, )

