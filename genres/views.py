from genres.models import Genre
from rest_framework import generics
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from genres.permissions import GenrePermissionClass


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GenrePermissionClass)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
