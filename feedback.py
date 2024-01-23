from user import *
from movie import *
from cinema_hall import *

class Feedback:
    def __init__(self, phone, movie_id, cinemausers, cinemaMovies):
        self.phone = phone
        self.movie_id = movie_id
        self.cineamusers = cinemausers
        self.cinemaMovies = cinemaMovies
    
    def add_rc(self):
        try:
            for ph, obj in self.cineamusers:
                if ph == self.phone:
                    for res_obj in obj.reservations.values():
                        if res_obj.movie_id == self.movie_id:
                            rating, comment = input ("Enter This Info (rating (1 - 10) | comment) use ',' to seperate: ").split(',')
                            for m_id, movie_obj in self.cinemaMovies:
                                if m_id == self.movie_id:
                                    movie_obj.user_rate(self.phone, rating)
                                    movie_obj.user_comment(self.phone, comment)
        except Exception as e:
            print(e)