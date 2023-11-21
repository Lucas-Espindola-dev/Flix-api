from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all()
    )
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all()
    )


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
