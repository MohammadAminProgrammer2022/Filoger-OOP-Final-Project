# ############################## MANAGER CLASS ############################
# have a list of all the users
# have a list of all the employees
# ....
# ################################################################

import random

class CinemaHall:
    # class attributes
    all_users = {}
    all_employees = {}
    reserved_seats = [1, 2, 3, 4, 5, 6]
    availabel_movies = {} # save structure ==> {movie_id : movie_obj}
    
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        # self.movies_showing = movies_showing
    
    def __str__(self):
        pass
    
    def seat_number_generator(self):
        '''
            Recursive function which recevies total number of seats
            and returns an available seat number.
        '''
        rand_num = random.randint(1, self.total_seats)
        # print(rand_num)
        if rand_num not in CinemaHall.reserved_seats:
            CinemaHall.reserved_seats.append(rand_num)
            return
        else:
            self.seat_number_generator()
    
        

if __name__ == "__main__":
    c1 = CinemaHall('c1', 10)
    c1.seat_number_generator()
    print(c1.reserved_seats)