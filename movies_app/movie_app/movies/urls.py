from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('genre/<genre_id>/<genre_name>', views.movie_list, name='movies'),
    path('movie/<movie_id>/', views.movie_info, name='info'),
    path('movie/reviews/<movie_id>', views.movie_reviews, name='reviews'),
    path('favorites/', views.movie_favorites, name='favorite'),
    
]
