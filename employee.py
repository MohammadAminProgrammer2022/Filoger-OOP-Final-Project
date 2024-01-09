from person import *


class Employee(Person):
    emp_id = 1000
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


if __name__ == "__main__":
    e1 = Employee('p1')
    print(e1.employee_id)
    
    e2 = Employee('p2')
    print(e2.employee_id)
    
    e3 = Employee('p3')
    print(e3.employee_id)