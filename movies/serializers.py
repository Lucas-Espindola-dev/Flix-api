from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_realise_date(self, value):
        if value.year < 1970:
            raise serializers.ValidationError('The realise date can not be before 1970.')
