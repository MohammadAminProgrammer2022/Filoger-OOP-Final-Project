from person import *
from movie import *


class Employee(Person):
    emp_id = 1000
    movies={}
    def __init__(self, position):
        self.position = position
        self.__employee_id = self.set_id()
    
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
    
    def add_movie(self, film , year):
        movie_fetcher = MovieFetcher()
        new_movie = movie_fetcher.fetch_movie(film, year)
        if new_movie.id_ in Employee.movies:
            print(f"{film} is exist.")
        else:
            Employee.movies[new_movie.id_] = new_movie
            print (f"{film} added")            
    
    @classmethod
    def shoe_movies (cls):
        for item in cls.movies.values():
            print(item.title)


if __name__ == "__main__":
    e1 = Employee('p1')
    print(e1.employee_id)
    
    e2 = Employee('p2')
    print(e2.employee_id)
    
    e3 = Employee('p3')
    print(e3.employee_id)

    e1.add_movie("oppenheimer", "2023")
    e3.add_movie("The holdovers", "2023")
    e2.add_movie("The holdovers", "2023")
    e1.shoe_movies()