from django.db import models

# Create your models here.
class GenresOfFavMovies(models.Model):
    genre_id = models.CharField(max_length=200)
    genre_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.genre_name


class FavMovies(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    genres = models.ManyToManyField(GenresOfFavMovies)
    poster_path = models.TextField()
    overview = models.TextField()
    runtime = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title
