from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ...


class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review
    serializer_class = ...
