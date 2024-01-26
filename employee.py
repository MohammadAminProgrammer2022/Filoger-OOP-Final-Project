'''
NOTE:
    The method add_movie() must return the 
    new movie object and it'll be saved on
    CinemaHall in movies dictionary.
    This will be done on main.py
'''

from person import *
from movie import *

class Employee(Person):
    emp_id = 1000
    movies={}
    def __init__(self, name=None, email=None, phone=None,  position=None):
        super().__init__(name, email, phone)
        self.position = position
        self.__employee_id = self.set_id()
    
    def __str__(self):
        return f"{super().__str__()} | Position: {self.position}"
    
    @property
    def employee_id(self):
        return self.__employee_id
    @employee_id.setter
    def employee_id(self, new_id):
        self.__employee_id = new_id
    
    @classmethod
    def set_id(cls):
        cls.emp_id += 1
        num = cls.emp_id
        return 'E' + str(num)
    
    def add_movie(self, film , year, start_time, end_time, date):
        movie_fetcher = MovieFetcher()
        new_movie = movie_fetcher.fetch_movie(film, year, start_time, end_time, date)
        if new_movie:
            Employee.movies[new_movie.id_] = new_movie
            return True, new_movie
        return False, "Not Found!"
    
    @classmethod
    def show_movies(cls):
        for item in cls.movies.values():
            print(item.title)


if __name__ == "__main__":
    e1 = Employee('ali','a@s.c', 9177895214,'p1')
    e2 = Employee('amir','am@s.c', 9177895215,'p12')
    e3 = Employee('amin','nm@s.c', 9171895215,'p123')

    e1.add_movie("oppenheimer", "2023",'12','16','2023-01-15')
    e3.add_movie("The holdovers", "2023",'12','16','2023-01-15')
    e2.add_movie("The holdovers", "2023",'12','16','2023-01-15')
    e1.show_movies()