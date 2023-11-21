from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all()
    )


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
