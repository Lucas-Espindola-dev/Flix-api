from django.http import JsonResponse
from genres.models import Genre
from rest_framework import generics


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = None
