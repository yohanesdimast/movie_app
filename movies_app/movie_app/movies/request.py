import requests

class MoviesAPI:
    BASE_URL = "https://api.themoviedb.org/3"
    HEADER = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MWM4Yzg4MGRjODA0NjA3MTNjYjdiNDYwZDcyNzVhZSIsInN1YiI6IjY1NjkzYjg1ZDM5OWU2MDBjNDBmODRiOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MAiPodXMvcUOZvCXDPc7jbiTh8ji3n_ONvCM8i5lIVI",
        }

    def genre_list(self):
        url = self.BASE_URL + '/genre/movie/list'
        raw_response = requests.get(url, headers=self.HEADER)
        response = raw_response.json()

        # can access the 'id' and 'name' of the genres
        return response['genres']

    def movies_by_genre(self, genre_id, page='1'):
        url = self.BASE_URL + f'/discover/movie?language=en-US&page={str(page)}&sort_by=popularity.desc&with_genres={str(genre_id)}'
        raw_response = requests.get(url, headers=self.HEADER)
        response = raw_response.json()

        return response['results'], response['total_pages']

    def movie_info(self, movie_id):
        url = self.BASE_URL + f'/movie/{movie_id}'
        raw_response = requests.get(url, headers=self.HEADER)
        response = raw_response.json()

        return response

    def movie_trailer(self, movie_id):
        url = self.BASE_URL + f'/movie/{movie_id}/videos'
        raw_response = requests.get(url, headers=self.HEADER)
        response = raw_response.json()
        
        trailer = []
        for video in response['results']:
            if video['site'] == 'YouTube' and video['type'] == 'Trailer' and video['official']:
                trailer.append(video)
        
        return trailer

    def movie_reviews(self, movie_id):
        url = self.BASE_URL + f'/movie/{movie_id}/reviews'
        raw_response = requests.get(url, headers=self.HEADER)
        response = raw_response.json()

        return response['results']

# genres = genre_list()
# for genre in genres:
#     print(genre['name'])

# movie_list = movies_by_genre(genre=28, page=1)
# for movie in movie_list:
#     print(movie['title'])

# print(movie_info(movie_id=670292))

# print(movie_trailer(movie_id=670292))

# reviews = movie_reviews(670292)
# for review in reviews:
#     print(review['author'])

