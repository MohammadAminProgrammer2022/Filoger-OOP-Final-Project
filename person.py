from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, email, phone, username):
        self.name = name
        self.email = email
        self.phone = phone
        self.username = username
    def __str__(self):
        return f"Name: {self.name} | Email: {self.email} | Phone: {self.phone} | User Name: {self.username}" 
        