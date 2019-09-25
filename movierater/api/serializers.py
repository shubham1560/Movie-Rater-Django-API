from rest_framework import serializers
from .models import Movie, Rating
# from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):
    # rating = RatingSerializer(many=True)

    class Meta:
        model = Movie
        # fields = ['id', 'title', 'description', 'rating']
        fields = ['id', 'title', 'description']


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['id', 'user', 'movie', 'stars']


class MovieFullSerializer(serializers.ModelSerializer):
    rating = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'rating']
        # fields = ['id', 'title', 'description']

