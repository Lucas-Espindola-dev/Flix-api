from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializers


class MoviesCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers


class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
