from employee import *

class Reservation:
    res_id = 1000
    def __init__(self, movie_id, start_time, date, phone_number, seat_number):
        self.movie_id = movie_id
        self.start_time = start_time
        self.date = date
        self.phone_number = phone_number
        self.seat_number = seat_number
        self.reserve_id = self.set_id()
        self.movie_name = self.movie_title
    
    def __str__(self):
        return f"Movie:{self.movie_name} Start time: {self.start_time} Date: {self.date} Seat number: {self.seat_number} "
    
    @staticmethod
    def movie_title (movie_id):
        movie_name = Employee.movies[movie_id]['Title']
        return movie_name

    @classmethod
    def set_id(cls):
        cls.res_id += 1
        num = cls.res_id
        return 'Res' + str(num)


if __name__ == "__main__":
    res = Reservation(1, 2, 4, 6, 9)