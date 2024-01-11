# ############################## MANAGER CLASS ############################
# have a list of all the users
# have a list of all the employees
# ....
# ################################################################

from employee import *
class CinemaHall:
    def __init__(self, name, total_seats, movies_showing):
        self.name = name
        self.total_seats = total_seats
        self.movies_showing = movies_showing


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