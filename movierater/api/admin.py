from django.contrib import admin
from .models import Movie, Rating, Te

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_on', 'last_updated')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'stars', 'created_on', 'last_updated')
    # fields = ('movie',)


admin.site.register(Te)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
