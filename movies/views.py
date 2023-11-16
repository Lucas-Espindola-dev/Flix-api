from rest_framework import generics
from movies.models import Movie


class MoviesCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = None
