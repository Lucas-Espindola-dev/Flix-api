from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieModelSerializer
from rest_framework.permissions import IsAuthenticated


class MoviesCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer


class MoviesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
