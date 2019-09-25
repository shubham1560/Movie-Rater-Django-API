# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, MovieFullSerializer
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import action


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

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        response = {'message': "it's working"}
        return Response(response, status=status.HTTP_200_OK)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
