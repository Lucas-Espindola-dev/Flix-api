from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieModelSerializer


class MoviesCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
