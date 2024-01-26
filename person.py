from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name=None, email=None, phone=None):
        self.name = name
        self.__email = email
        self.__phone = phone
    
    def __str__(self):
        return f"Name: {self.name}" 
    
    # email
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, new_email):
        if '@' not in new_email or new_email.count('.') != 1 or len(new_email) < 4:
            print("Invalid Email!")
            self.email_isvalid = False
        else:
            self.__email = new_email
            self.email_isvalid = True

    # phone
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, new_phone):
        try:
            new_p = int(new_phone)
            self.__phone = new_phone
            self.phone_isvalid = True
        except ValueError as e:
            print("Invalid Phone number!")
            self.phone_isvalid = False