from statistics import mean
import requests

class Movie:
    def __init__(self, id_, title, runtime, rating, genre, director, actors, plot, start_time=None, end_time=None,date=None): #, showtimes, status, average_rating, feedback_list):
        self.id_ = id_
        self.title = title
        self.runtime = runtime
        self.rating = rating
        self.genre = genre
        self.director = director
        self.actors = actors
        self.plot = plot
        # employee | employee will modify these attributes below based on cinema planning and management
        # start time
        self.start_time = start_time
        # end time
        self.end_time = end_time
        # date
        self.date = date
        # rating - feedback
        self.usercinema_rating = {} # data saving structure => user_id : rate_number
        # rating average | This is a number between 0 - 100
        # self.average_rating = self.avg_rating(self.usercinema_rating)
        # user | user feed back
        self.comment = {} # data saving structure => user_id : string

    # def __str__(self):
    #     return f"ID: {self.id_}; Title: {self.title}; Runtime: {self.runtime}; Rating: {self.rating}; Genre: {self.genre}; Director: {self.director}; Actors: {self.actors}; Plot: {self.plot}; Show date: {self.date}; Start time: {self.start_time}, Comment: {self.comment.items()}"
    def __str__(self):
        return f"ID: {self.id_} * Title: {self.title} * Runtime: {self.runtime} * Rating: {self.rating} * Genre: {self.genre} * Director: {self.director} * Actors: {self.actors} * Plot: {self.plot} * Show date: {self.date} * Start time: {self.start_time} * User Cinema Comment: {self.comment} * User Cinema Rating: {self.usercinema_rating}"
    
    # @staticmethod
    # def avg_rating(data):
    #     print(f"value from ave_rating method: {data}, {len(data)}")
    #     if len(data) != 0:
    #         return mean(int(data.values()))
    
    def user_rate(self,phone, rate):
        self.usercinema_rating[phone] = rate
    
    def user_comment(self, phone, comment):
        self.comment[phone] = comment


class MovieFetcher:
    url = "https://www.omdbapi.com/?"

    @staticmethod
    def fetch_movie(film, year, start_time=None, end_time=None, date=None):
        film = film.replace(" ","+")
        params = {'t': film, 'y': year, 'apikey': '6610dc1a'}
        response = requests.get(MovieFetcher.url, params=params)
        try:
            if response.status_code == 200:
                movie_items = response.json()
            else:
                movie_items = {}
            if movie_items["Response"] == "True":
                obj_movie = Movie(
                    movie_items["imdbID"],
                    movie_items["Title"],
                    movie_items["Runtime"],
                    movie_items["imdbRating"],
                    movie_items["Genre"],
                    movie_items["Director"],
                    movie_items["Actors"],
                    movie_items["Plot"],
                    start_time,
                    end_time,
                    date
                )
                return obj_movie
        
            else:
                return None
        except Exception as e:
            print("API Error!")
            print(e)


if __name__ == '__main__':
    movie_fetcher = MovieFetcher()
    result = movie_fetcher.fetch_movie("oppenheimer", "2023")
    print (result)