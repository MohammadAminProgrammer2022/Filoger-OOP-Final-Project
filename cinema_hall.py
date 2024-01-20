# ############################## MANAGER CLASS ############################
# have a list of all the users
# have a list of all the employees
# ....
# ################################################################


from employee import *

class CinemaHall:
    # class attributes
    all_users = {}
    all_employees = {}
    reserved_seats = []
    number_seat = 0
    availabel_movies = {} # save structure ==> {movie_id : movie_obj}
    test = 12
    
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats

    
    def __str__(self):
        return f"Cinema name: {self.name}, Total seats: {self.total_seats}"
    
    def seat_number_generator(self):
        CinemaHall.number_seat += 1
        if self.total_seats == len(CinemaHall.reserved_seats):
            return None
        CinemaHall.reserved_seats.append(CinemaHall.number_seat)
        return CinemaHall.number_seat
        

if __name__ == "__main__":
    c1 = CinemaHall('c1', 100)
    u = c1.seat_number_generator()
    print(u)