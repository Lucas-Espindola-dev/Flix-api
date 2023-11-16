from rest_framework import serializers
from movies.models import Movie


class MovieSerializers(serializers.ModelSerializer):
    model = Movie
    fields = '__all__'
