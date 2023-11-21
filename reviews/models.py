from django.db import models
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=)
