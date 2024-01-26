import json
from user import *
from employee import *
from movie import *
from cinema_hall import *
from feedback import *
from reservation import *

c_name = input("Enter Your Cinema Name: ")

def number_of_seats():
    '''A recursive function with try-except error handler.'''
    try:
        total_seats = int(input("Enter total seats(MUST BE INTEGER): "))
        return total_seats
    except ValueError as e:
        print(f"Error: {e}\nTry again!")
        return number_of_seats()

def default_movies():
    print("MOVIE Recommendation: ")
    with open('movies.json', 'r') as file_:
        file_json = json.load(file_)
    for movie in file_json:
        print(movie['Title'], movie['Year'])

def phone_number_validator():
    '''A recursive function with try-except error handler.'''
    try:
        phone = input("Enter Phone Number: ")
        p_int = int(phone)
        return phone
    except ValueError as e:
        print(f"Error: {e}\nNot a Phone Number!\nTry again!")
        return phone_number_validator()

total_seats = number_of_seats()
cinema = CinemaHall(c_name, total_seats)

while True:
    cmd = input('new employee: n-e / new user: n-u / add movie: add-m / available movies: a-m / reserve movie: r-m / feed back: f-b / exit >>> ')

    if cmd not in ['n-e', 'n-u', 'add-m', 'a-m', 'r-m', 'f-b','exit']:
        print("Invalid Input")
    
    # add new employee
    if cmd == 'n-e':
        password = '1234'
        emp_pass = input("Enter Password: ")
        if emp_pass == password:
            try:
                name, email, phone, emp_position = input("Enter Employee Info (name | email | phone | position) use ',' to seperate: ").split(',')
                new_emp = Employee()
            except ValueError as e:
                print(e)
                continue
            # phone validation
            new_emp.phone = phone
            # email validation
            new_emp.email = email
            if new_emp.email_isvalid and new_emp.phone_isvalid:    
                if new_emp.phone not in cinema.all_employees:
                    cinema.all_employees[new_emp.phone] = new_emp
                    print("New employee added!")
                else:
                    print("Already Exists!")
        else:
            print("Wrong Password!")
    
    # add new movie
    if cmd == 'add-m':
        print()
        default_movies()
        print()
        password = '1234'
        emp_pass = input("Enter Password: ")
        if emp_pass == password:
            phone = input("Enter Your Phone Number: ")
            for emp_id, employee in cinema.all_employees.items():
                if employee.phone == phone:
                    try:
                        name, year, start_time, end_time, date = input("Enter Name of movie,Year, Start time, End time, Date | use ',' to seperate: ").split(',')
                        year = str(year)
                        msg, new_movie = employee.add_movie(name, year, start_time, end_time, date)
                        # movie found from api
                        if msg:
                            # cheking for repeated movie
                            if new_movie.id_ not in cinema.availabel_movies:
                                #new_movie.
                                cinema.availabel_movies[new_movie.id_] = new_movie
                                print("New Movie Added!")
                            else:
                                print("Movie Exists!")
                        # movie not found from api
                        if not msg:
                            print('movie not found from api')
                    except Exception as e:
                        print(e)
                else:
                    print("phone number not found")
        else:
            print("Wrong Password!")

    # add new user
    if cmd == 'n-u':
        try:
            name, email, phone = input("Enter User Info (name | email | phone) use ',' to seperate: ").split(',')
            new_user = User()
        except ValueError as e:
            print(e)
            continue
        # phone validator
        new_user.phone = phone
        # email validator
        new_user.email = email
        if new_user.email_isvalid and new_user.phone_isvalid:
            if phone not in cinema.all_users:
                cinema.all_users[new_user.phone] = new_user
                print("New User Added!")
            else:
                print("User Exists!")
    
    # reserve movie 
    if cmd == 'r-m':
        phone_num = input('Enter Phone number: ')
        if phone_num in cinema.all_users:
            try:
                movie_id, start_time, date = input("Movie ID, Star time, date: (use ',') : ").split(',')
                if movie_id in cinema.availabel_movies:
                    if cinema.availabel_movies[movie_id].start_time == start_time and cinema.availabel_movies[movie_id].date == date:       
                        seat_number = cinema.seat_number_generator()
                        if seat_number == None:
                            print("No free space!")
                        else:
                            # obj from reserve class
                            new_reserve = Reservation(movie_id, start_time, date, phone_num, seat_number)
                            # finding user based on their phone number
                            for obj in cinema.all_users.values():
                                if obj.phone == phone_num:
                                    obj.reservations[new_reserve.reserve_id] = new_reserve
                                    print("Reservation Done!")
                                    break
                    else:
                        print ('The date and time of the requested movie does not match the show list.')
                else:
                    print ('The name of this movie is not in the cinema screening list')
            except Exception as e:
                print(e)
        else:
            print("Not a user!")
    
    # available movies
    if cmd == 'a-m':
        print()
        for m_id, movie in cinema.availabel_movies.items():
            print(f"{'*' * 20} {movie.title} {'*' * 20}")
            print(movie)
    
    # feedback
    if cmd == 'f-b':
        try:
            movie_id, phone = input ("Enter This Info (movie_id | phone) use ',' to seperate: ").split(',')
            if phone in cinema.all_users and movie_id in cinema.availabel_movies:
                cinemausers = cinema.all_users.items()
                cinemaMovies = cinema.availabel_movies.items()
                new_feedback = Feedback(phone, movie_id, cinemausers, cinemaMovies)
                new_feedback.add_rc()
            else:
                print ('The phone number or movie ID is incorrect.')
        except Exception as e:
            print(e)
    
    # exit
    if cmd == 'exit':
        break   