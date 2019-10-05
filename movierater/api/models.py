from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import MaxValueValidator, MinValueValidator
import random, string


class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=360)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def average_rating(self):
        sum1 = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum1 += rating.stars
        if ratings:
            average_rating = sum1/len(ratings)
        else:
            average_rating = 0
        return average_rating


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_on = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'movie'), )
        index_together = (('user', 'movie'), )


class Te(models.Model):
    name = models.CharField(max_length=30)
    id = models.BigAutoField(primary_key=True)
    created_on = models.DateTimeField(auto_now=True)
