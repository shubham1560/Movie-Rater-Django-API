# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, MovieFullSerializer
# Create your views here.


def first(request):
    return HttpResponse("Well" + str(request))


def api(request):
    return HttpResponse("Api" + str(request))


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    # serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return MovieFullSerializer
        return MovieSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
