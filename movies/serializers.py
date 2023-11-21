from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1970:
            raise serializers.ValidationError('The realise date can not be before 1970.')
        return value

    def validate_resume(self, value):
        if len(value) > 300:
            raise serializers.ValidationError('Resume must be smaller than 300 chars')
        return value
