from django.contrib import admin
from .models import FavMovies, GenresOfFavMovies

# Register your models here.
admin.site.register(FavMovies)
admin.site.register(GenresOfFavMovies)