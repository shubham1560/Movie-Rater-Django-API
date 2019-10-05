from django.contrib import admin
from .models import Movie, Rating, Te

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_on')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'movie', 'stars', 'created_on')
    # fields = ('movie',)


admin.site.register(Te)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
