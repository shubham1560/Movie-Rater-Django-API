# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, MovieFullSerializer, UserSerializer
from rest_framework.response import Response
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication


def first(request):
    return HttpResponse("Well" + str(request))


def api(request):
    return HttpResponse("Api" + str(request))


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    authentication_classes = (TokenAuthentication, )
    # serializer_class = MovieSerializer
    # permission_classes = (IsAuthenticated, )  # even with allowed any, this will be shown only to the logged in user

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return MovieFullSerializer
        return MovieSerializer

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        movie = Movie.objects.get(id=pk)
        user = request.user
        print(user)
        result = []
        actiondata = ""
        if 'stars' in request.data:
            print(request)
            stars = request.data['stars']
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                actiondata = "updation"
            except:
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                actiondata = "Creation"
            serializer = RatingSerializer(rating, many=False)
            result = serializer.data
        response = {"rating": result, "action": actiondata}
        return Response(response, status=status.HTTP_200_OK)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
