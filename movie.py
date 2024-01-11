import requests

class Movie:
    def __init__(self, id_, title, runtime, rating): #, showtimes, status, average_rating, feedback_list):
        self.id_ = id_
        self.title = title
        self.runtime = runtime
        self.rating = rating
        '''self.showtimes = showtimes
        self.status = status
        self.average_rating = average_rating
        self.feedback_list = feedback_list'''

    def __str__(self):
        return f"{self.id_}, {self.title}, {self.runtime}, {self.rating}"
    #, {self.showtimes}, {self.status}, {self.average_rating}, {self.feedback_list}\n"

class MovieFetcher:
    url = "https://www.omdbapi.com/?"

    @staticmethod
    def fetch_movie(film, year):
        film = film.replace(" ","+")
        params = {'t': film, 'y': year, 'apikey': '6610dc1a'}
        response = requests.get(MovieFetcher.url, params=params)
        if response.status_code == 200:
            movie_items = response.json()
        else:
            movie_items = {}
        if movie_items["Response"] == "True":
            obj_movie = Movie(
                movie_items["imdbID"],
                movie_items["Title"],
                movie_items["Runtime"],
                movie_items["imdbRating"]
            )
            return obj_movie
        else:
            return "Movie not found!"


if __name__ == '__main__':
    movie_fetcher = MovieFetcher()
    result = movie_fetcher.fetch_movie("oppenheimer", "2023")
    print (result)