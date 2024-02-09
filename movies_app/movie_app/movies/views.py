from django.shortcuts import render
from .request import MoviesAPI
import json
from .models import FavMovies, GenresOfFavMovies

# Create your views here.
def index(request):
    contents = MoviesAPI().genre_list()

    return render(request, 'movies/index.html', {'genres': contents})

def movie_list(request, genre_id, genre_name):
    get_page = request.GET.get('page')
    if get_page == None:
        get_page = 1

    contents = MoviesAPI().movies_by_genre(genre_id=genre_id, page=get_page)
    
    if int(get_page) <= 1:
        has_prev = False
    else:
        has_prev = True
    if int(get_page) == int(contents[1]):
        has_next = False
    else:
        has_next = True
    prev_page = int(get_page) - 1
    next_page = int(get_page) + 1
    
    paginate = {
        'page_now': get_page,
        'has_next': has_next,
        'has_prev': has_prev,
        'next_page': next_page,
        'prev_page': prev_page,
    }
    
    return render(request, 'movies/movie_list.html', {'genre_name': genre_name, 'movies': contents[0], 'paginate': paginate})

def movie_info(request, movie_id):
    contents = MoviesAPI().movie_info(movie_id)
    trailer = MoviesAPI().movie_trailer(movie_id)

    if request.method == "POST":
        id = request.POST.get('id', '')
        title = request.POST.get('title', '')
        tagline = request.POST.get('tagline', '')
        genre_raw = request.POST.get('genres', '')
        poster = request.POST.get('poster', '')
        overview = request.POST.get('overview', '')
        runtime = request.POST.get('runtime', '')
        date = request.POST.get('date', '')

        fav_movie = FavMovies(title=title, 
                              id=id,
                              tagline=tagline, 
                              poster_path=poster, 
                              overview=overview,
                              runtime=runtime,
                              date=date)
        fav_movie.save()

        genre_raw = genre_raw.replace("\'","\"")
        genres = json.loads(genre_raw)
        for genre in genres:
            movie_genre = GenresOfFavMovies(genre_id=genre['id'], genre_name=genre['name'])
            movie_genre.save()
            fav_movie.genres.add(movie_genre)


    return render(request, 'movies/movie_info.html', {'info': contents, 'movie_id': movie_id, 'trailer': trailer[0]})

def movie_reviews(request, movie_id):
    contents = MoviesAPI().movie_reviews(movie_id)

    return render(request, 'movies/movie_reviews.html', {'reviews': contents})

def movie_favorites(request):
    contents = FavMovies.objects.all()
    print(contents)

    return render(request, 'movies/movie_favorites.html', {'movies': contents})