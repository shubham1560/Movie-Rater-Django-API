# from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, MovieFullSerializer
from rest_framework.response import Response
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication


def first(request):
    return HttpResponse("Well" + str(request))


def api(request):
    return HttpResponse("Api" + str(request))


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    authentication_classes = (TokenAuthentication, )
    # serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return MovieFullSerializer
        return MovieSerializer

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        # print(pk)
        # print(request.data)
        movie = Movie.objects.get(id=pk)
        # user = User.objects.get(id=1)
        user = request.user
        print(user)
        # user = request.user
        result = []
        actiondata = ""
        if 'stars' in request.data:
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

            # result = []
        # result = [{"title": movie.title, "description": movie.description}]
        # for y in a:
        #     z = {"title": "", "description": "", "id":""}
        #     z["description"] = y.description
        #     z["title"] = y.title
        #     z["id"] = y.id
        #     result.append(z)
        # print(result)
        # print(a)
        response = {"rating": result, "action": actiondata}
        return Response(response, status=status.HTTP_200_OK)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
